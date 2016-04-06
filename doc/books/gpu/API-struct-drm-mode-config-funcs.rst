
.. _API-struct-drm-mode-config-funcs:

============================
struct drm_mode_config_funcs
============================

*man struct drm_mode_config_funcs(9)*

*4.6.0-rc1*

basic driver provided mode setting functions


Synopsis
========

.. code-block:: c

    struct drm_mode_config_funcs {
      struct drm_framebuffer *(* fb_create) (struct drm_device *dev,struct drm_file *file_priv,const struct drm_mode_fb_cmd2 *mode_cmd);
      void (* output_poll_changed) (struct drm_device *dev);
      int (* atomic_check) (struct drm_device *dev,struct drm_atomic_state *state);
      int (* atomic_commit) (struct drm_device *dev,struct drm_atomic_state *state,bool async);
      struct drm_atomic_state *(* atomic_state_alloc) (struct drm_device *dev);
      void (* atomic_state_clear) (struct drm_atomic_state *state);
      void (* atomic_state_free) (struct drm_atomic_state *state);
    };


Members
=======

fb_create
    Create a new framebuffer object. The core does basic checks on the requested metadata, but most of that is left to the driver. See struct ``drm_mode_fb_cmd2`` for details.

    If the parameters are deemed valid and the backing storage objects in the underlying memory manager all exist, then the driver allocates a new ``drm_framebuffer`` structure,
    subclassed to contain driver-specific information (like the internal native buffer object references). It also needs to fill out all relevant metadata, which should be done by
    calling ``drm_helper_mode_fill_fb_struct``.

    The initialization is finalized by calling ``drm_framebuffer_init``, which registers the framebuffer and makes it accessible to other threads.

    RETURNS:

    A new framebuffer with an initial reference count of 1 or a negative error code encoded with ``ERR_PTR``.

output_poll_changed
    Callback used by helpers to inform the driver of output configuration changes.

    Drivers implementing fbdev emulation with the helpers can call drm_fb_helper_hotplug_changed from this hook to inform the fbdev helper of output changes.

    FIXME:

    Except that there's no vtable for device-level helper callbacks there's no reason this is a core function.

atomic_check
    This is the only hook to validate an atomic modeset update. This function must reject any modeset and state changes which the hardware or driver doesn't support. This includes
    but is of course not limited to:

    - Checking that the modes, framebuffers, scaling and placement requirements and so on are within the limits of the hardware.

    - Checking that any hidden shared resources are not oversubscribed. This can be shared PLLs, shared lanes, overall memory bandwidth, display fifo space (where shared between
    planes or maybe even CRTCs).

    - Checking that virtualized resources exported to userspace are not oversubscribed. For various reasons it can make sense to expose more planes, crtcs or encoders than which
    are physically there. One example is dual-pipe operations (which generally should be hidden from userspace if when lockstepped in hardware, exposed otherwise), where a plane
    might need 1 hardware plane (if it's just on one pipe), 2 hardware planes (when it spans both pipes) or maybe even shared a hardware plane with a 2nd plane (if there's a
    compatible plane requested on the area handled by the other pipe).

    - Check that any transitional state is possible and that if requested, the update can indeed be done in the vblank period without temporarily disabling some functions.

    - Check any other constraints the driver or hardware might have.

    - This callback also needs to correctly fill out the ``drm_crtc_state`` in this update to make sure that ``drm_atomic_crtc_needs_modeset`` reflects the nature of the possible
    update and returns true if and only if the update cannot be applied without tearing within one vblank on that CRTC. The core uses that information to reject updates which
    require a full modeset (i.e. blanking the screen, or at least pausing updates for a substantial amount of time) if userspace has disallowed that in its request.

    - The driver also does not need to repeat basic input validation like done for the corresponding legacy entry points. The core does that before calling this hook.

    See the documentation of ``atomic_commit`` for an exhaustive list of error conditions which don't have to be checked at the ->``atomic_check`` stage?

    See the documentation for struct ``drm_atomic_state`` for how exactly an atomic modeset update is described.

    Drivers using the atomic helpers can implement this hook using ``drm_atomic_helper_check``, or one of the exported sub-functions of it.

    RETURNS:

    0 on success or one of the below negative error codes:

    - -EINVAL, if any of the above constraints are violated.

    - -EDEADLK, when returned from an attempt to acquire an additional ``drm_modeset_lock`` through ``drm_modeset_lock``.

    - -ENOMEM, if allocating additional state sub-structures failed due to lack of memory.

    - -EINTR, -EAGAIN or -ERESTARTSYS, if the IOCTL should be restarted. This can either be due to a pending signal, or because the driver needs to completely bail out to recover
    from an exceptional situation like a GPU hang. From a userspace point all errors are treated equally.

atomic_commit
    This is the only hook to commit an atomic modeset update. The core guarantees that ``atomic_check`` has been called successfully before calling this function, and that nothing
    has been changed in the interim.

    See the documentation for struct ``drm_atomic_state`` for how exactly an atomic modeset update is described.

    Drivers using the atomic helpers can implement this hook using ``drm_atomic_helper_commit``, or one of the exported sub-functions of it.

    Asynchronous commits (as indicated with the async parameter) must do any preparatory work which might result in an unsuccessful commit in the context of this callback. The only
    exceptions are hardware errors resulting in -EIO. But even in that case the driver must ensure that the display pipe is at least running, to avoid compositors crashing when
    pageflips don't work. Anything else, specifically committing the update to the hardware, should be done without blocking the caller. For updates which do not require a modeset
    this must be guaranteed.

    The driver must wait for any pending rendering to the new framebuffers to complete before executing the flip. It should also wait for any pending rendering from other drivers
    if the underlying buffer is a shared dma-buf. Asynchronous commits must not wait for rendering in the context of this callback.

    An application can request to be notified when the atomic commit has completed. These events are per-CRTC and can be distinguished by the CRTC index supplied in ``drm_event``
    to userspace.

    The drm core will supply a struct ``drm_event`` in the event member of each CRTC's ``drm_crtc_state`` structure. This can be handled by the ``drm_crtc_send_vblank_event``
    function, which the driver should call on the provided event upon completion of the atomic commit. Note that if the driver supports vblank signalling and timestamping the
    vblank counters and timestamps must agree with the ones returned from page flip events. With the current vblank helper infrastructure this can be achieved by holding a vblank
    reference while the page flip is pending, acquired through ``drm_crtc_vblank_get`` and released with ``drm_crtc_vblank_put``. Drivers are free to implement their own vblank
    counter and timestamp tracking though, e.g. if they have accurate timestamp registers in hardware.

    NOTE:

    Drivers are not allowed to shut down any display pipe successfully enabled through an atomic commit on their own. Doing so can result in compositors crashing if a page flip is
    suddenly rejected because the pipe is off.

    RETURNS:

    0 on success or one of the below negative error codes:

    - -EBUSY, if an asynchronous updated is requested and there is an earlier updated pending. Drivers are allowed to support a queue of outstanding updates, but currently no
    driver supports that. Note that drivers must wait for preceding updates to complete if a synchronous update is requested, they are not allowed to fail the commit in that case.

    - -ENOMEM, if the driver failed to allocate memory. Specifically this can happen when trying to pin framebuffers, which must only be done when committing the state.

    - -ENOSPC, as a refinement of the more generic -ENOMEM to indicate that the driver has run out of vram, iommu space or similar GPU address space needed for framebuffer.

    - -EIO, if the hardware completely died.

    - -EINTR, -EAGAIN or -ERESTARTSYS, if the IOCTL should be restarted. This can either be due to a pending signal, or because the driver needs to completely bail out to recover
    from an exceptional situation like a GPU hang. From a userspace point of view all errors are treated equally.

    This list is exhaustive. Specifically this hook is not allowed to return -EINVAL (any invalid requests should be caught in ``atomic_check``) or -EDEADLK (this function must not
    acquire additional modeset locks).

atomic_state_alloc
    This optional hook can be used by drivers that want to subclass struct ``drm_atomic_state`` to be able to track their own driver-private global state easily. If this hook is
    implemented, drivers must also implement ``atomic_state_clear`` and ``atomic_state_free``.

    RETURNS:

    A new ``drm_atomic_state`` on success or NULL on failure.

atomic_state_clear
    This hook must clear any driver private state duplicated into the passed-in ``drm_atomic_state``. This hook is called when the caller encountered a ``drm_modeset_lock``
    deadlock and needs to drop all already acquired locks as part of the deadlock avoidance dance implemented in ``drm_modeset_lock_backoff``.

    Any duplicated state must be invalidated since a concurrent atomic update might change it, and the drm atomic interfaces always apply updates as relative changes to the current
    state.

    Drivers that implement this must call ``drm_atomic_state_default_clear`` to clear common state.

atomic_state_free
    This hook needs driver private resources and the ``drm_atomic_state`` itself. Note that the core first calls ``drm_atomic_state_clear`` to avoid code duplicate between the
    clear and free hooks.

    Drivers that implement this must call ``drm_atomic_state_default_free`` to release common resources.


Description
===========

Some global (i.e. not per-CRTC, connector, etc) mode setting functions that involve drivers.
