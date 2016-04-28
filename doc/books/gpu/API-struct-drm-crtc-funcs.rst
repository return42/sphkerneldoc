.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-drm-crtc-funcs:

=====================
struct drm_crtc_funcs
=====================

*man struct drm_crtc_funcs(9)*

*4.6.0-rc5*

control CRTCs for a given device


Synopsis
========

.. code-block:: c

    struct drm_crtc_funcs {
      void (* reset) (struct drm_crtc *crtc);
      int (* cursor_set) (struct drm_crtc *crtc, struct drm_file *file_priv,uint32_t handle, uint32_t width, uint32_t height);
      int (* cursor_set2) (struct drm_crtc *crtc, struct drm_file *file_priv,uint32_t handle, uint32_t width, uint32_t height,int32_t hot_x, int32_t hot_y);
      int (* cursor_move) (struct drm_crtc *crtc, int x, int y);
      void (* gamma_set) (struct drm_crtc *crtc, u16 *r, u16 *g, u16 *b,uint32_t start, uint32_t size);
      void (* destroy) (struct drm_crtc *crtc);
      int (* set_config) (struct drm_mode_set *set);
      int (* page_flip) (struct drm_crtc *crtc,struct drm_framebuffer *fb,struct drm_pending_vblank_event *event,uint32_t flags);
      int (* set_property) (struct drm_crtc *crtc,struct drm_property *property, uint64_t val);
      struct drm_crtc_state *(* atomic_duplicate_state) (struct drm_crtc *crtc);
      void (* atomic_destroy_state) (struct drm_crtc *crtc,struct drm_crtc_state *state);
      int (* atomic_set_property) (struct drm_crtc *crtc,struct drm_crtc_state *state,struct drm_property *property,uint64_t val);
      int (* atomic_get_property) (struct drm_crtc *crtc,const struct drm_crtc_state *state,struct drm_property *property,uint64_t *val);
    };


Members
=======

reset
    Reset CRTC hardware and software state to off. This function isn't
    called by the core directly, only through ``drm_mode_config_reset``.
    It's not a helper hook only for historical reasons.

    Atomic drivers can use ``drm_atomic_helper_crtc_reset`` to reset
    atomic state using this hook.

cursor_set
    Update the cursor image. The cursor position is relative to the CRTC
    and can be partially or fully outside of the visible area.

    Note that contrary to all other KMS functions the legacy cursor
    entry points don't take a framebuffer object, but instead take
    directly a raw buffer object id from the driver's buffer manager
    (which is either GEM or TTM for current drivers).

    This entry point is deprecated, drivers should instead implement
    universal plane support and register a proper cursor plane using
    ``drm_crtc_init_with_planes``.

    This callback is optional

    RETURNS:

    0 on success or a negative error code on failure.

cursor_set2
    Update the cursor image, including hotspot information. The hotspot
    must not affect the cursor position in CRTC coordinates, but is only
    meant as a hint for virtualized display hardware to coordinate the
    guests and hosts cursor position. The cursor hotspot is relative to
    the cursor image. Otherwise this works exactly like ``cursor_set``.

    This entry point is deprecated, drivers should instead implement
    universal plane support and register a proper cursor plane using
    ``drm_crtc_init_with_planes``.

    This callback is optional.

    RETURNS:

    0 on success or a negative error code on failure.

cursor_move
    Update the cursor position. The cursor does not need to be visible
    when this hook is called.

    This entry point is deprecated, drivers should instead implement
    universal plane support and register a proper cursor plane using
    ``drm_crtc_init_with_planes``.

    This callback is optional.

    RETURNS:

    0 on success or a negative error code on failure.

gamma_set
    Set gamma on the CRTC.

    This callback is optional.

    NOTE:

    Drivers that support gamma tables and also fbdev emulation through
    the provided helper library need to take care to fill out the gamma
    hooks for both. Currently there's a bit an unfortunate duplication
    going on, which should eventually be unified to just one set of
    hooks.

destroy
    Clean up plane resources. This is only called at driver unload time
    through ``drm_mode_config_cleanup`` since a CRTC cannot be
    hotplugged in DRM.

set_config
    This is the main legacy entry point to change the modeset state on a
    CRTC. All the details of the desired configuration are passed in a
    struct ``drm_mode_set`` - see there for details.

    Drivers implementing atomic modeset should use
    ``drm_atomic_helper_set_config`` to implement this hook.

    RETURNS:

    0 on success or a negative error code on failure.

page_flip
    Legacy entry point to schedule a flip to the given framebuffer.

    Page flipping is a synchronization mechanism that replaces the frame
    buffer being scanned out by the CRTC with a new frame buffer during
    vertical blanking, avoiding tearing (except when requested otherwise
    through the DRM_MODE_PAGE_FLIP_ASYNC flag). When an application
    requests a page flip the DRM core verifies that the new frame buffer
    is large enough to be scanned out by the CRTC in the currently
    configured mode and then calls the CRTC ->``page_flip`` operation
    with a pointer to the new frame buffer.

    The driver must wait for any pending rendering to the new
    framebuffer to complete before executing the flip. It should also
    wait for any pending rendering from other drivers if the underlying
    buffer is a shared dma-buf.

    An application can request to be notified when the page flip has
    completed. The drm core will supply a struct ``drm_event`` in the
    event parameter in this case. This can be handled by the
    ``drm_crtc_send_vblank_event`` function, which the driver should
    call on the provided event upon completion of the flip. Note that if
    the driver supports vblank signalling and timestamping the vblank
    counters and timestamps must agree with the ones returned from page
    flip events. With the current vblank helper infrastructure this can
    be achieved by holding a vblank reference while the page flip is
    pending, acquired through ``drm_crtc_vblank_get`` and released with
    ``drm_crtc_vblank_put``. Drivers are free to implement their own
    vblank counter and timestamp tracking though, e.g. if they have
    accurate timestamp registers in hardware.

    FIXME:

    Up to that point drivers need to manage events themselves and can
    use even->base.list freely for that. Specifically they need to
    ensure that they don't send out page flip (or vblank) events for
    which the corresponding drm file has been closed already. The drm
    core unfortunately does not (yet) take care of that. Therefore
    drivers currently must clean up and release pending events in their
    ->preclose driver function.

    This callback is optional.

    NOTE:

    Very early versions of the KMS ABI mandated that the driver must
    block (but not reject) any rendering to the old framebuffer until
    the flip operation has completed and the old framebuffer is no
    longer visible. This requirement has been lifted, and userspace is
    instead expected to request delivery of an event and wait with
    recycling old buffers until such has been received.

    RETURNS:

    0 on success or a negative error code on failure. Note that if a
    ->``page_flip`` operation is already pending the callback should
    return -EBUSY. Pageflips on a disabled CRTC (either by setting a
    NULL mode or just runtime disabled through DPMS respectively the new
    atomic “ACTIVE” state) should result in an -EINVAL error code. Note
    that ``drm_atomic_helper_page_flip`` checks this already for atomic
    drivers.

set_property
    This is the legacy entry point to update a property attached to the
    CRTC.

    Drivers implementing atomic modeset should use
    ``drm_atomic_helper_crtc_set_property`` to implement this hook.

    This callback is optional if the driver does not support any legacy
    driver-private properties.

    RETURNS:

    0 on success or a negative error code on failure.

atomic_duplicate_state
    Duplicate the current atomic state for this CRTC and return it. The
    core and helpers gurantee that any atomic state duplicated with this
    hook and still owned by the caller (i.e. not transferred to the
    driver by calling ->``atomic_commit`` from struct
    ``drm_mode_config_funcs``) will be cleaned up by calling the
    ``atomic_destroy_state`` hook in this structure.

    Atomic drivers which don't subclass struct ``drm_crtc`` should use
    ``drm_atomic_helper_crtc_duplicate_state``. Drivers that subclass
    the state structure to extend it with driver-private state should
    use ``__drm_atomic_helper_crtc_duplicate_state`` to make sure shared
    state is duplicated in a consistent fashion across drivers.

    It is an error to call this hook before crtc->state has been
    initialized correctly.

    NOTE:

    If the duplicate state references refcounted resources this hook
    must acquire a reference for each of them. The driver must release
    these references again in ``atomic_destroy_state``.

    RETURNS:

    Duplicated atomic state or NULL when the allocation failed.

atomic_destroy_state
    Destroy a state duplicated with ``atomic_duplicate_state`` and
    release or unreference all resources it references

atomic_set_property
    Decode a driver-private property value and store the decoded value
    into the passed-in state structure. Since the atomic core decodes
    all standardized properties (even for extensions beyond the core set
    of properties which might not be implemented by all drivers) this
    requires drivers to subclass the state structure.

    Such driver-private properties should really only be implemented for
    truly hardware/vendor specific state. Instead it is preferred to
    standardize atomic extension and decode the properties used to
    expose such an extension in the core.

    Do not call this function directly, use
    ``drm_atomic_crtc_set_property`` instead.

    This callback is optional if the driver does not support any
    driver-private atomic properties.

    NOTE:

    This function is called in the state assembly phase of atomic
    modesets, which can be aborted for any reason (including on
    userspace's request to just check whether a configuration would be
    possible). Drivers MUST NOT touch any persistent state (hardware or
    software) or data structures except the passed in ``state``
    parameter.

    Also since userspace controls in which order properties are set this
    function must not do any input validation (since the state update is
    incomplete and hence likely inconsistent). Instead any such input
    validation must be done in the various atomic_check callbacks.

    RETURNS:

    0 if the property has been found, -EINVAL if the property isn't
    implemented by the driver (which should never happen, the core only
    asks for properties attached to this CRTC). No other validation is
    allowed by the driver. The core already checks that the property
    value is within the range (integer, valid enum value, ...) the
    driver set when registering the property.

atomic_get_property
    Reads out the decoded driver-private property. This is used to
    implement the GETCRTC IOCTL.

    Do not call this function directly, use
    ``drm_atomic_crtc_get_property`` instead.

    This callback is optional if the driver does not support any
    driver-private atomic properties.

    RETURNS:

    0 on success, -EINVAL if the property isn't implemented by the
    driver (which should never happen, the core only asks for properties
    attached to this CRTC).


Description
===========

The drm_crtc_funcs structure is the central CRTC management structure
in the DRM. Each CRTC controls one or more connectors (note that the
name CRTC is simply historical, a CRTC may control LVDS, VGA, DVI, TV
out, etc. connectors, not just CRTs).

Each driver is responsible for filling out this structure at startup
time, in addition to providing other modesetting features, like i2c and
DDC bus accessors.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
