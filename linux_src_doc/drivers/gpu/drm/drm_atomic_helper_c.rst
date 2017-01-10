.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_atomic_helper.c

.. _`drm_atomic_helper_check_modeset`:

drm_atomic_helper_check_modeset
===============================

.. c:function:: int drm_atomic_helper_check_modeset(struct drm_device *dev, struct drm_atomic_state *state)

    validate state object for modeset changes

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_atomic_state \*state:
        the driver state object

.. _`drm_atomic_helper_check_modeset.description`:

Description
-----------

Check the state object to see if the requested state is physically possible.
This does all the crtc and connector related computations for an atomic
update and adds any additional connectors needed for full modesets and calls
down into ->mode_fixup functions of the driver backend.

crtc_state->mode_changed is set when the input mode is changed.
crtc_state->connectors_changed is set when a connector is added or
removed from the crtc.
crtc_state->active_changed is set when crtc_state->active changes,
which is used for dpms.
See also: \ :c:func:`drm_atomic_crtc_needs_modeset`\ 

.. _`drm_atomic_helper_check_modeset.important`:

IMPORTANT
---------


Drivers which set ->mode_changed (e.g. in their ->atomic_check hooks if a
plane update can't be done without a full modeset) _must_ call this function
afterwards after that change. It is permitted to call this function multiple
times for the same update, e.g. when the ->atomic_check functions depend upon
the adjusted dotclock for fifo space allocation and watermark computation.

.. _`drm_atomic_helper_check_modeset.return`:

Return
------

Zero for success or -errno

.. _`drm_atomic_helper_check_planes`:

drm_atomic_helper_check_planes
==============================

.. c:function:: int drm_atomic_helper_check_planes(struct drm_device *dev, struct drm_atomic_state *state)

    validate state object for planes changes

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_atomic_state \*state:
        the driver state object

.. _`drm_atomic_helper_check_planes.description`:

Description
-----------

Check the state object to see if the requested state is physically possible.
This does all the plane update related checks using by calling into the
->atomic_check hooks provided by the driver.

It also sets crtc_state->planes_changed to indicate that a crtc has
updated planes.

.. _`drm_atomic_helper_check_planes.return`:

Return
------

Zero for success or -errno

.. _`drm_atomic_helper_check`:

drm_atomic_helper_check
=======================

.. c:function:: int drm_atomic_helper_check(struct drm_device *dev, struct drm_atomic_state *state)

    validate state object

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_atomic_state \*state:
        the driver state object

.. _`drm_atomic_helper_check.description`:

Description
-----------

Check the state object to see if the requested state is physically possible.
Only crtcs and planes have check callbacks, so for any additional (global)
checking that a driver needs it can simply wrap that around this function.
Drivers without such needs can directly use this as their ->atomic_check()
callback.

This just wraps the two parts of the state checking for planes and modeset
state in the default order: First it calls \ :c:func:`drm_atomic_helper_check_modeset`\ 
and then \ :c:func:`drm_atomic_helper_check_planes`\ . The assumption is that the
->atomic_check functions depend upon an updated adjusted_mode.clock to
e.g. properly compute watermarks.

.. _`drm_atomic_helper_check.return`:

Return
------

Zero for success or -errno

.. _`drm_atomic_helper_update_legacy_modeset_state`:

drm_atomic_helper_update_legacy_modeset_state
=============================================

.. c:function:: void drm_atomic_helper_update_legacy_modeset_state(struct drm_device *dev, struct drm_atomic_state *old_state)

    update legacy modeset state

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_atomic_state \*old_state:
        atomic state object with old state structures

.. _`drm_atomic_helper_update_legacy_modeset_state.description`:

Description
-----------

This function updates all the various legacy modeset state pointers in
connectors, encoders and crtcs. It also updates the timestamping constants
used for precise vblank timestamps by calling
\ :c:func:`drm_calc_timestamping_constants`\ .

Drivers can use this for building their own atomic commit if they don't have
a pure helper-based modeset implementation.

.. _`drm_atomic_helper_commit_modeset_disables`:

drm_atomic_helper_commit_modeset_disables
=========================================

.. c:function:: void drm_atomic_helper_commit_modeset_disables(struct drm_device *dev, struct drm_atomic_state *old_state)

    modeset commit to disable outputs

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_atomic_state \*old_state:
        atomic state object with old state structures

.. _`drm_atomic_helper_commit_modeset_disables.description`:

Description
-----------

This function shuts down all the outputs that need to be shut down and
prepares them (if required) with the new mode.

For compatibility with legacy crtc helpers this should be called before
\ :c:func:`drm_atomic_helper_commit_planes`\ , which is what the default commit function
does. But drivers with different needs can group the modeset commits together
and do the plane commits at the end. This is useful for drivers doing runtime
PM since planes updates then only happen when the CRTC is actually enabled.

.. _`drm_atomic_helper_commit_modeset_enables`:

drm_atomic_helper_commit_modeset_enables
========================================

.. c:function:: void drm_atomic_helper_commit_modeset_enables(struct drm_device *dev, struct drm_atomic_state *old_state)

    modeset commit to enable outputs

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_atomic_state \*old_state:
        atomic state object with old state structures

.. _`drm_atomic_helper_commit_modeset_enables.description`:

Description
-----------

This function enables all the outputs with the new configuration which had to
be turned off for the update.

For compatibility with legacy crtc helpers this should be called after
\ :c:func:`drm_atomic_helper_commit_planes`\ , which is what the default commit function
does. But drivers with different needs can group the modeset commits together
and do the plane commits at the end. This is useful for drivers doing runtime
PM since planes updates then only happen when the CRTC is actually enabled.

.. _`drm_atomic_helper_wait_for_fences`:

drm_atomic_helper_wait_for_fences
=================================

.. c:function:: int drm_atomic_helper_wait_for_fences(struct drm_device *dev, struct drm_atomic_state *state, bool pre_swap)

    wait for fences stashed in plane state

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_atomic_state \*state:
        atomic state object with old state structures

    :param bool pre_swap:
        If true, do an interruptible wait, and \ ``state``\  is the new state.
        Otherwise \ ``state``\  is the old state.

.. _`drm_atomic_helper_wait_for_fences.description`:

Description
-----------

For implicit sync, driver should fish the exclusive fence out from the
incoming fb's and stash it in the drm_plane_state.  This is called after
\ :c:func:`drm_atomic_helper_swap_state`\  so it uses the current plane state (and
just uses the atomic state to find the changed planes)

Note that \ ``pre_swap``\  is needed since the point where we block for fences moves
around depending upon whether an atomic commit is blocking or
non-blocking. For async commit all waiting needs to happen after
\ :c:func:`drm_atomic_helper_swap_state`\  is called, but for synchronous commits we want
to wait **before** we do anything that can't be easily rolled back. That is
before we call \ :c:func:`drm_atomic_helper_swap_state`\ .

Returns zero if success or < 0 if \ :c:func:`dma_fence_wait`\  fails.

.. _`drm_atomic_helper_framebuffer_changed`:

drm_atomic_helper_framebuffer_changed
=====================================

.. c:function:: bool drm_atomic_helper_framebuffer_changed(struct drm_device *dev, struct drm_atomic_state *old_state, struct drm_crtc *crtc)

    check if framebuffer has changed

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_atomic_state \*old_state:
        atomic state object with old state structures

    :param struct drm_crtc \*crtc:
        DRM crtc

.. _`drm_atomic_helper_framebuffer_changed.description`:

Description
-----------

Checks whether the framebuffer used for this CRTC changes as a result of
the atomic update.  This is useful for drivers which cannot use
\ :c:func:`drm_atomic_helper_wait_for_vblanks`\  and need to reimplement its
functionality.

.. _`drm_atomic_helper_framebuffer_changed.return`:

Return
------

true if the framebuffer changed.

.. _`drm_atomic_helper_wait_for_vblanks`:

drm_atomic_helper_wait_for_vblanks
==================================

.. c:function:: void drm_atomic_helper_wait_for_vblanks(struct drm_device *dev, struct drm_atomic_state *old_state)

    wait for vblank on crtcs

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_atomic_state \*old_state:
        atomic state object with old state structures

.. _`drm_atomic_helper_wait_for_vblanks.description`:

Description
-----------

Helper to, after atomic commit, wait for vblanks on all effected
crtcs (ie. before cleaning up old framebuffers using
\ :c:func:`drm_atomic_helper_cleanup_planes`\ ). It will only wait on crtcs where the
framebuffers have actually changed to optimize for the legacy cursor and
plane update use-case.

.. _`drm_atomic_helper_commit_tail`:

drm_atomic_helper_commit_tail
=============================

.. c:function:: void drm_atomic_helper_commit_tail(struct drm_atomic_state *old_state)

    commit atomic update to hardware

    :param struct drm_atomic_state \*old_state:
        atomic state object with old state structures

.. _`drm_atomic_helper_commit_tail.description`:

Description
-----------

This is the default implemenation for the ->atomic_commit_tail() hook of the
\ :c:type:`struct drm_mode_config_helper_funcs <drm_mode_config_helper_funcs>`\  vtable.

Note that the default ordering of how the various stages are called is to
match the legacy modeset helper library closest. One peculiarity of that is
that it doesn't mesh well with runtime PM at all.

For drivers supporting runtime PM the recommended sequence is instead ::

    drm_atomic_helper_commit_modeset_disables(dev, old_state);

    drm_atomic_helper_commit_modeset_enables(dev, old_state);

    drm_atomic_helper_commit_planes(dev, old_state,
                                    DRM_PLANE_COMMIT_ACTIVE_ONLY);

for committing the atomic update to hardware.  See the kerneldoc entries for
these three functions for more details.

.. _`drm_atomic_helper_commit`:

drm_atomic_helper_commit
========================

.. c:function:: int drm_atomic_helper_commit(struct drm_device *dev, struct drm_atomic_state *state, bool nonblock)

    commit validated state object

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_atomic_state \*state:
        the driver state object

    :param bool nonblock:
        whether nonblocking behavior is requested.

.. _`drm_atomic_helper_commit.description`:

Description
-----------

This function commits a with \ :c:func:`drm_atomic_helper_check`\  pre-validated state
object. This can still fail when e.g. the framebuffer reservation fails. This
function implements nonblocking commits, using
\ :c:func:`drm_atomic_helper_setup_commit`\  and related functions.

Committing the actual hardware state is done through the
->atomic_commit_tail() callback of the \ :c:type:`struct drm_mode_config_helper_funcs <drm_mode_config_helper_funcs>`\  vtable,
or it's default implementation \ :c:func:`drm_atomic_helper_commit_tail`\ .

.. _`drm_atomic_helper_commit.return`:

Return
------

Zero for success or -errno.

.. _`drm_atomic_helper_setup_commit`:

drm_atomic_helper_setup_commit
==============================

.. c:function:: int drm_atomic_helper_setup_commit(struct drm_atomic_state *state, bool nonblock)

    setup possibly nonblocking commit

    :param struct drm_atomic_state \*state:
        new modeset state to be committed

    :param bool nonblock:
        whether nonblocking behavior is requested.

.. _`drm_atomic_helper_setup_commit.description`:

Description
-----------

This function prepares \ ``state``\  to be used by the atomic helper's support for
nonblocking commits. Drivers using the nonblocking commit infrastructure
should always call this function from their ->atomic_commit hook.

To be able to use this support drivers need to use a few more helper
functions. \ :c:func:`drm_atomic_helper_wait_for_dependencies`\  must be called before
actually committing the hardware state, and for nonblocking commits this call
must be placed in the async worker. See also \ :c:func:`drm_atomic_helper_swap_state`\ 
and it's stall parameter, for when a driver's commit hooks look at the
->state pointers of struct \ :c:type:`struct drm_crtc <drm_crtc>`\ , \ :c:type:`struct drm_plane <drm_plane>`\  or \ :c:type:`struct drm_connector <drm_connector>`\  directly.

Completion of the hardware commit step must be signalled using
\ :c:func:`drm_atomic_helper_commit_hw_done`\ . After this step the driver is not allowed
to read or change any permanent software or hardware modeset state. The only
exception is state protected by other means than \ :c:type:`struct drm_modeset_lock <drm_modeset_lock>`\  locks.
Only the free standing \ ``state``\  with pointers to the old state structures can
be inspected, e.g. to clean up old buffers using
\ :c:func:`drm_atomic_helper_cleanup_planes`\ .

At the very end, before cleaning up \ ``state``\  drivers must call
\ :c:func:`drm_atomic_helper_commit_cleanup_done`\ .

This is all implemented by in \ :c:func:`drm_atomic_helper_commit`\ , giving drivers a
complete and esay-to-use default implementation of the \ :c:func:`atomic_commit`\  hook.

The tracking of asynchronously executed and still pending commits is done
using the core structure \ :c:type:`struct drm_crtc_commit <drm_crtc_commit>`\ .

By default there's no need to clean up resources allocated by this function
explicitly: \ :c:func:`drm_atomic_state_default_clear`\  will take care of that
automatically.

.. _`drm_atomic_helper_setup_commit.return`:

Return
------


0 on success. -EBUSY when userspace schedules nonblocking commits too fast,
-ENOMEM on allocation failures and -EINTR when a signal is pending.

.. _`drm_atomic_helper_wait_for_dependencies`:

drm_atomic_helper_wait_for_dependencies
=======================================

.. c:function:: void drm_atomic_helper_wait_for_dependencies(struct drm_atomic_state *old_state)

    wait for required preceeding commits

    :param struct drm_atomic_state \*old_state:
        atomic state object with old state structures

.. _`drm_atomic_helper_wait_for_dependencies.description`:

Description
-----------

This function waits for all preceeding commits that touch the same CRTC as
\ ``old_state``\  to both be committed to the hardware (as signalled by
drm_atomic_helper_commit_hw_done) and executed by the hardware (as signalled
by calling drm_crtc_vblank_send_event on the event member of
\ :c:type:`struct drm_crtc_state <drm_crtc_state>`\ ).

This is part of the atomic helper support for nonblocking commits, see
\ :c:func:`drm_atomic_helper_setup_commit`\  for an overview.

.. _`drm_atomic_helper_commit_hw_done`:

drm_atomic_helper_commit_hw_done
================================

.. c:function:: void drm_atomic_helper_commit_hw_done(struct drm_atomic_state *old_state)

    setup possible nonblocking commit

    :param struct drm_atomic_state \*old_state:
        atomic state object with old state structures

.. _`drm_atomic_helper_commit_hw_done.description`:

Description
-----------

This function is used to signal completion of the hardware commit step. After
this step the driver is not allowed to read or change any permanent software
or hardware modeset state. The only exception is state protected by other
means than \ :c:type:`struct drm_modeset_lock <drm_modeset_lock>`\  locks.

Drivers should try to postpone any expensive or delayed cleanup work after
this function is called.

This is part of the atomic helper support for nonblocking commits, see
\ :c:func:`drm_atomic_helper_setup_commit`\  for an overview.

.. _`drm_atomic_helper_commit_cleanup_done`:

drm_atomic_helper_commit_cleanup_done
=====================================

.. c:function:: void drm_atomic_helper_commit_cleanup_done(struct drm_atomic_state *old_state)

    signal completion of commit

    :param struct drm_atomic_state \*old_state:
        atomic state object with old state structures

.. _`drm_atomic_helper_commit_cleanup_done.description`:

Description
-----------

This signals completion of the atomic update \ ``old_state``\ , including any
cleanup work. If used, it must be called right before calling
\ :c:func:`drm_atomic_state_put`\ .

This is part of the atomic helper support for nonblocking commits, see
\ :c:func:`drm_atomic_helper_setup_commit`\  for an overview.

.. _`drm_atomic_helper_prepare_planes`:

drm_atomic_helper_prepare_planes
================================

.. c:function:: int drm_atomic_helper_prepare_planes(struct drm_device *dev, struct drm_atomic_state *state)

    prepare plane resources before commit

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_atomic_state \*state:
        atomic state object with new state structures

.. _`drm_atomic_helper_prepare_planes.description`:

Description
-----------

This function prepares plane state, specifically framebuffers, for the new
configuration. If any failure is encountered this function will call
->cleanup_fb on any already successfully prepared framebuffer.

.. _`drm_atomic_helper_prepare_planes.return`:

Return
------

0 on success, negative error code on failure.

.. _`drm_atomic_helper_commit_planes`:

drm_atomic_helper_commit_planes
===============================

.. c:function:: void drm_atomic_helper_commit_planes(struct drm_device *dev, struct drm_atomic_state *old_state, uint32_t flags)

    commit plane state

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_atomic_state \*old_state:
        atomic state object with old state structures

    :param uint32_t flags:
        flags for committing plane state

.. _`drm_atomic_helper_commit_planes.description`:

Description
-----------

This function commits the new plane state using the plane and atomic helper
functions for planes and crtcs. It assumes that the atomic state has already
been pushed into the relevant object state pointers, since this step can no
longer fail.

It still requires the global state object \ ``old_state``\  to know which planes and
crtcs need to be updated though.

Note that this function does all plane updates across all CRTCs in one step.
If the hardware can't support this approach look at
\ :c:func:`drm_atomic_helper_commit_planes_on_crtc`\  instead.

Plane parameters can be updated by applications while the associated CRTC is
disabled. The DRM/KMS core will store the parameters in the plane state,
which will be available to the driver when the CRTC is turned on. As a result
most drivers don't need to be immediately notified of plane updates for a
disabled CRTC.

Unless otherwise needed, drivers are advised to set the ACTIVE_ONLY flag in
\ ``flags``\  in order not to receive plane update notifications related to a
disabled CRTC. This avoids the need to manually ignore plane updates in
driver code when the driver and/or hardware can't or just don't need to deal
with updates on disabled CRTCs, for example when supporting runtime PM.

Drivers may set the NO_DISABLE_AFTER_MODESET flag in \ ``flags``\  if the relevant
display controllers require to disable a CRTC's planes when the CRTC is
disabled. This function would skip the ->atomic_disable call for a plane if
the CRTC of the old plane state needs a modesetting operation. Of course,
the drivers need to disable the planes in their CRTC disable callbacks
since no one else would do that.

The \ :c:func:`drm_atomic_helper_commit`\  default implementation doesn't set the
ACTIVE_ONLY flag to most closely match the behaviour of the legacy helpers.
This should not be copied blindly by drivers.

.. _`drm_atomic_helper_commit_planes_on_crtc`:

drm_atomic_helper_commit_planes_on_crtc
=======================================

.. c:function:: void drm_atomic_helper_commit_planes_on_crtc(struct drm_crtc_state *old_crtc_state)

    commit plane state for a crtc

    :param struct drm_crtc_state \*old_crtc_state:
        atomic state object with the old crtc state

.. _`drm_atomic_helper_commit_planes_on_crtc.description`:

Description
-----------

This function commits the new plane state using the plane and atomic helper
functions for planes on the specific crtc. It assumes that the atomic state
has already been pushed into the relevant object state pointers, since this
step can no longer fail.

This function is useful when plane updates should be done crtc-by-crtc
instead of one global step like \ :c:func:`drm_atomic_helper_commit_planes`\  does.

This function can only be savely used when planes are not allowed to move
between different CRTCs because this function doesn't handle inter-CRTC
depencies. Callers need to ensure that either no such depencies exist,
resolve them through ordering of commit calls or through some other means.

.. _`drm_atomic_helper_disable_planes_on_crtc`:

drm_atomic_helper_disable_planes_on_crtc
========================================

.. c:function:: void drm_atomic_helper_disable_planes_on_crtc(struct drm_crtc_state *old_crtc_state, bool atomic)

    helper to disable CRTC's planes

    :param struct drm_crtc_state \*old_crtc_state:
        atomic state object with the old CRTC state

    :param bool atomic:
        if set, synchronize with CRTC's atomic_begin/flush hooks

.. _`drm_atomic_helper_disable_planes_on_crtc.description`:

Description
-----------

Disables all planes associated with the given CRTC. This can be
used for instance in the CRTC helper atomic_disable callback to disable
all planes.

If the atomic-parameter is set the function calls the CRTC's
atomic_begin hook before and atomic_flush hook after disabling the
planes.

It is a bug to call this function without having implemented the
->atomic_disable() plane hook.

.. _`drm_atomic_helper_cleanup_planes`:

drm_atomic_helper_cleanup_planes
================================

.. c:function:: void drm_atomic_helper_cleanup_planes(struct drm_device *dev, struct drm_atomic_state *old_state)

    cleanup plane resources after commit

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_atomic_state \*old_state:
        atomic state object with old state structures

.. _`drm_atomic_helper_cleanup_planes.description`:

Description
-----------

This function cleans up plane state, specifically framebuffers, from the old
configuration. Hence the old configuration must be perserved in \ ``old_state``\  to
be able to call this function.

This function must also be called on the new state when the atomic update
fails at any point after calling \ :c:func:`drm_atomic_helper_prepare_planes`\ .

.. _`drm_atomic_helper_swap_state`:

drm_atomic_helper_swap_state
============================

.. c:function:: void drm_atomic_helper_swap_state(struct drm_atomic_state *state, bool stall)

    store atomic state into current sw state

    :param struct drm_atomic_state \*state:
        atomic state

    :param bool stall:
        stall for proceeding commits

.. _`drm_atomic_helper_swap_state.description`:

Description
-----------

This function stores the atomic state into the current state pointers in all
driver objects. It should be called after all failing steps have been done
and succeeded, but before the actual hardware state is committed.

For cleanup and error recovery the current state for all changed objects will
be swaped into \ ``state``\ .

With that sequence it fits perfectly into the plane prepare/cleanup sequence:

1. Call \ :c:func:`drm_atomic_helper_prepare_planes`\  with the staged atomic state.

2. Do any other steps that might fail.

3. Put the staged state into the current state pointers with this function.

4. Actually commit the hardware state.

5. Call \ :c:func:`drm_atomic_helper_cleanup_planes`\  with \ ``state``\ , which since step 3
contains the old state. Also do any other cleanup required with that state.

\ ``stall``\  must be set when nonblocking commits for this driver directly access
the ->state pointer of \ :c:type:`struct drm_plane <drm_plane>`\ , \ :c:type:`struct drm_crtc <drm_crtc>`\  or \ :c:type:`struct drm_connector <drm_connector>`\ . With the
current atomic helpers this is almost always the case, since the helpers
don't pass the right state structures to the callbacks.

.. _`drm_atomic_helper_update_plane`:

drm_atomic_helper_update_plane
==============================

.. c:function:: int drm_atomic_helper_update_plane(struct drm_plane *plane, struct drm_crtc *crtc, struct drm_framebuffer *fb, int crtc_x, int crtc_y, unsigned int crtc_w, unsigned int crtc_h, uint32_t src_x, uint32_t src_y, uint32_t src_w, uint32_t src_h)

    Helper for primary plane update using atomic

    :param struct drm_plane \*plane:
        plane object to update

    :param struct drm_crtc \*crtc:
        owning CRTC of owning plane

    :param struct drm_framebuffer \*fb:
        framebuffer to flip onto plane

    :param int crtc_x:
        x offset of primary plane on crtc

    :param int crtc_y:
        y offset of primary plane on crtc

    :param unsigned int crtc_w:
        width of primary plane rectangle on crtc

    :param unsigned int crtc_h:
        height of primary plane rectangle on crtc

    :param uint32_t src_x:
        x offset of \ ``fb``\  for panning

    :param uint32_t src_y:
        y offset of \ ``fb``\  for panning

    :param uint32_t src_w:
        width of source rectangle in \ ``fb``\ 

    :param uint32_t src_h:
        height of source rectangle in \ ``fb``\ 

.. _`drm_atomic_helper_update_plane.description`:

Description
-----------

Provides a default plane update handler using the atomic driver interface.

.. _`drm_atomic_helper_update_plane.return`:

Return
------

Zero on success, error code on failure

.. _`drm_atomic_helper_disable_plane`:

drm_atomic_helper_disable_plane
===============================

.. c:function:: int drm_atomic_helper_disable_plane(struct drm_plane *plane)

    Helper for primary plane disable using * atomic

    :param struct drm_plane \*plane:
        plane to disable

.. _`drm_atomic_helper_disable_plane.description`:

Description
-----------

Provides a default plane disable handler using the atomic driver interface.

.. _`drm_atomic_helper_disable_plane.return`:

Return
------

Zero on success, error code on failure

.. _`drm_atomic_helper_set_config`:

drm_atomic_helper_set_config
============================

.. c:function:: int drm_atomic_helper_set_config(struct drm_mode_set *set)

    set a new config from userspace

    :param struct drm_mode_set \*set:
        mode set configuration

.. _`drm_atomic_helper_set_config.description`:

Description
-----------

Provides a default crtc set_config handler using the atomic driver interface.

.. _`drm_atomic_helper_set_config.return`:

Return
------

Returns 0 on success, negative errno numbers on failure.

.. _`drm_atomic_helper_disable_all`:

drm_atomic_helper_disable_all
=============================

.. c:function:: int drm_atomic_helper_disable_all(struct drm_device *dev, struct drm_modeset_acquire_ctx *ctx)

    disable all currently active outputs

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_modeset_acquire_ctx \*ctx:
        lock acquisition context

.. _`drm_atomic_helper_disable_all.description`:

Description
-----------

Loops through all connectors, finding those that aren't turned off and then
turns them off by setting their DPMS mode to OFF and deactivating the CRTC
that they are connected to.

This is used for example in suspend/resume to disable all currently active
functions when suspending.

Note that if callers haven't already acquired all modeset locks this might
return -EDEADLK, which must be handled by calling \ :c:func:`drm_modeset_backoff`\ .

.. _`drm_atomic_helper_disable_all.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_atomic_helper_disable_all.see-also`:

See also
--------

drm_atomic_helper_suspend(), \ :c:func:`drm_atomic_helper_resume`\ 

.. _`drm_atomic_helper_suspend`:

drm_atomic_helper_suspend
=========================

.. c:function:: struct drm_atomic_state *drm_atomic_helper_suspend(struct drm_device *dev)

    subsystem-level suspend helper

    :param struct drm_device \*dev:
        DRM device

.. _`drm_atomic_helper_suspend.description`:

Description
-----------

Duplicates the current atomic state, disables all active outputs and then
returns a pointer to the original atomic state to the caller. Drivers can
pass this pointer to the \ :c:func:`drm_atomic_helper_resume`\  helper upon resume to
restore the output configuration that was active at the time the system
entered suspend.

Note that it is potentially unsafe to use this. The atomic state object
returned by this function is assumed to be persistent. Drivers must ensure
that this holds true. Before calling this function, drivers must make sure
to suspend fbdev emulation so that nothing can be using the device.

.. _`drm_atomic_helper_suspend.return`:

Return
------

A pointer to a copy of the state before suspend on success or an \ :c:func:`ERR_PTR`\ -
encoded error code on failure. Drivers should store the returned atomic
state object and pass it to the \ :c:func:`drm_atomic_helper_resume`\  helper upon
resume.

.. _`drm_atomic_helper_suspend.see-also`:

See also
--------

drm_atomic_helper_duplicate_state(), \ :c:func:`drm_atomic_helper_disable_all`\ ,
\ :c:func:`drm_atomic_helper_resume`\ 

.. _`drm_atomic_helper_resume`:

drm_atomic_helper_resume
========================

.. c:function:: int drm_atomic_helper_resume(struct drm_device *dev, struct drm_atomic_state *state)

    subsystem-level resume helper

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_atomic_state \*state:
        atomic state to resume to

.. _`drm_atomic_helper_resume.description`:

Description
-----------

Calls \ :c:func:`drm_mode_config_reset`\  to synchronize hardware and software states,
grabs all modeset locks and commits the atomic state object. This can be
used in conjunction with the \ :c:func:`drm_atomic_helper_suspend`\  helper to
implement suspend/resume for drivers that support atomic mode-setting.

.. _`drm_atomic_helper_resume.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_atomic_helper_resume.see-also`:

See also
--------

drm_atomic_helper_suspend()

.. _`drm_atomic_helper_crtc_set_property`:

drm_atomic_helper_crtc_set_property
===================================

.. c:function:: int drm_atomic_helper_crtc_set_property(struct drm_crtc *crtc, struct drm_property *property, uint64_t val)

    helper for crtc properties

    :param struct drm_crtc \*crtc:
        DRM crtc

    :param struct drm_property \*property:
        DRM property

    :param uint64_t val:
        value of property

.. _`drm_atomic_helper_crtc_set_property.description`:

Description
-----------

Provides a default crtc set_property handler using the atomic driver
interface.

.. _`drm_atomic_helper_crtc_set_property.return`:

Return
------

Zero on success, error code on failure

.. _`drm_atomic_helper_plane_set_property`:

drm_atomic_helper_plane_set_property
====================================

.. c:function:: int drm_atomic_helper_plane_set_property(struct drm_plane *plane, struct drm_property *property, uint64_t val)

    helper for plane properties

    :param struct drm_plane \*plane:
        DRM plane

    :param struct drm_property \*property:
        DRM property

    :param uint64_t val:
        value of property

.. _`drm_atomic_helper_plane_set_property.description`:

Description
-----------

Provides a default plane set_property handler using the atomic driver
interface.

.. _`drm_atomic_helper_plane_set_property.return`:

Return
------

Zero on success, error code on failure

.. _`drm_atomic_helper_connector_set_property`:

drm_atomic_helper_connector_set_property
========================================

.. c:function:: int drm_atomic_helper_connector_set_property(struct drm_connector *connector, struct drm_property *property, uint64_t val)

    helper for connector properties

    :param struct drm_connector \*connector:
        DRM connector

    :param struct drm_property \*property:
        DRM property

    :param uint64_t val:
        value of property

.. _`drm_atomic_helper_connector_set_property.description`:

Description
-----------

Provides a default connector set_property handler using the atomic driver
interface.

.. _`drm_atomic_helper_connector_set_property.return`:

Return
------

Zero on success, error code on failure

.. _`drm_atomic_helper_page_flip`:

drm_atomic_helper_page_flip
===========================

.. c:function:: int drm_atomic_helper_page_flip(struct drm_crtc *crtc, struct drm_framebuffer *fb, struct drm_pending_vblank_event *event, uint32_t flags)

    execute a legacy page flip

    :param struct drm_crtc \*crtc:
        DRM crtc

    :param struct drm_framebuffer \*fb:
        DRM framebuffer

    :param struct drm_pending_vblank_event \*event:
        optional DRM event to signal upon completion

    :param uint32_t flags:
        flip flags for non-vblank sync'ed updates

.. _`drm_atomic_helper_page_flip.description`:

Description
-----------

Provides a default page flip implementation using the atomic driver interface.

Note that for now so called async page flips (i.e. updates which are not
synchronized to vblank) are not supported, since the atomic interfaces have
no provisions for this yet.

.. _`drm_atomic_helper_page_flip.return`:

Return
------

Returns 0 on success, negative errno numbers on failure.

.. _`drm_atomic_helper_connector_dpms`:

drm_atomic_helper_connector_dpms
================================

.. c:function:: int drm_atomic_helper_connector_dpms(struct drm_connector *connector, int mode)

    connector dpms helper implementation

    :param struct drm_connector \*connector:
        affected connector

    :param int mode:
        DPMS mode

.. _`drm_atomic_helper_connector_dpms.description`:

Description
-----------

This is the main helper function provided by the atomic helper framework for
implementing the legacy DPMS connector interface. It computes the new desired
->active state for the corresponding CRTC (if the connector is enabled) and
updates it.

.. _`drm_atomic_helper_connector_dpms.return`:

Return
------

Returns 0 on success, negative errno numbers on failure.

.. _`drm_atomic_helper_best_encoder`:

drm_atomic_helper_best_encoder
==============================

.. c:function:: struct drm_encoder *drm_atomic_helper_best_encoder(struct drm_connector *connector)

    Helper for \ :c:type:`struct drm_connector_helper_funcs <drm_connector_helper_funcs>`\  ->best_encoder callback

    :param struct drm_connector \*connector:
        Connector control structure

.. _`drm_atomic_helper_best_encoder.description`:

Description
-----------

This is a \ :c:type:`struct drm_connector_helper_funcs <drm_connector_helper_funcs>`\  ->best_encoder callback helper for
connectors that support exactly 1 encoder, statically determined at driver
init time.

.. _`drm_atomic_helper_crtc_reset`:

drm_atomic_helper_crtc_reset
============================

.. c:function:: void drm_atomic_helper_crtc_reset(struct drm_crtc *crtc)

    default ->reset hook for CRTCs

    :param struct drm_crtc \*crtc:
        drm CRTC

.. _`drm_atomic_helper_crtc_reset.description`:

Description
-----------

Resets the atomic state for \ ``crtc``\  by freeing the state pointer (which might
be NULL, e.g. at driver load time) and allocating a new empty state object.

.. _`__drm_atomic_helper_crtc_duplicate_state`:

__drm_atomic_helper_crtc_duplicate_state
========================================

.. c:function:: void __drm_atomic_helper_crtc_duplicate_state(struct drm_crtc *crtc, struct drm_crtc_state *state)

    copy atomic CRTC state

    :param struct drm_crtc \*crtc:
        CRTC object

    :param struct drm_crtc_state \*state:
        atomic CRTC state

.. _`__drm_atomic_helper_crtc_duplicate_state.description`:

Description
-----------

Copies atomic state from a CRTC's current state and resets inferred values.
This is useful for drivers that subclass the CRTC state.

.. _`drm_atomic_helper_crtc_duplicate_state`:

drm_atomic_helper_crtc_duplicate_state
======================================

.. c:function:: struct drm_crtc_state *drm_atomic_helper_crtc_duplicate_state(struct drm_crtc *crtc)

    default state duplicate hook

    :param struct drm_crtc \*crtc:
        drm CRTC

.. _`drm_atomic_helper_crtc_duplicate_state.description`:

Description
-----------

Default CRTC state duplicate hook for drivers which don't have their own
subclassed CRTC state structure.

.. _`__drm_atomic_helper_crtc_destroy_state`:

__drm_atomic_helper_crtc_destroy_state
======================================

.. c:function:: void __drm_atomic_helper_crtc_destroy_state(struct drm_crtc_state *state)

    release CRTC state

    :param struct drm_crtc_state \*state:
        CRTC state object to release

.. _`__drm_atomic_helper_crtc_destroy_state.description`:

Description
-----------

Releases all resources stored in the CRTC state without actually freeing
the memory of the CRTC state. This is useful for drivers that subclass the
CRTC state.

.. _`drm_atomic_helper_crtc_destroy_state`:

drm_atomic_helper_crtc_destroy_state
====================================

.. c:function:: void drm_atomic_helper_crtc_destroy_state(struct drm_crtc *crtc, struct drm_crtc_state *state)

    default state destroy hook

    :param struct drm_crtc \*crtc:
        drm CRTC

    :param struct drm_crtc_state \*state:
        CRTC state object to release

.. _`drm_atomic_helper_crtc_destroy_state.description`:

Description
-----------

Default CRTC state destroy hook for drivers which don't have their own
subclassed CRTC state structure.

.. _`drm_atomic_helper_plane_reset`:

drm_atomic_helper_plane_reset
=============================

.. c:function:: void drm_atomic_helper_plane_reset(struct drm_plane *plane)

    default ->reset hook for planes

    :param struct drm_plane \*plane:
        drm plane

.. _`drm_atomic_helper_plane_reset.description`:

Description
-----------

Resets the atomic state for \ ``plane``\  by freeing the state pointer (which might
be NULL, e.g. at driver load time) and allocating a new empty state object.

.. _`__drm_atomic_helper_plane_duplicate_state`:

__drm_atomic_helper_plane_duplicate_state
=========================================

.. c:function:: void __drm_atomic_helper_plane_duplicate_state(struct drm_plane *plane, struct drm_plane_state *state)

    copy atomic plane state

    :param struct drm_plane \*plane:
        plane object

    :param struct drm_plane_state \*state:
        atomic plane state

.. _`__drm_atomic_helper_plane_duplicate_state.description`:

Description
-----------

Copies atomic state from a plane's current state. This is useful for
drivers that subclass the plane state.

.. _`drm_atomic_helper_plane_duplicate_state`:

drm_atomic_helper_plane_duplicate_state
=======================================

.. c:function:: struct drm_plane_state *drm_atomic_helper_plane_duplicate_state(struct drm_plane *plane)

    default state duplicate hook

    :param struct drm_plane \*plane:
        drm plane

.. _`drm_atomic_helper_plane_duplicate_state.description`:

Description
-----------

Default plane state duplicate hook for drivers which don't have their own
subclassed plane state structure.

.. _`__drm_atomic_helper_plane_destroy_state`:

__drm_atomic_helper_plane_destroy_state
=======================================

.. c:function:: void __drm_atomic_helper_plane_destroy_state(struct drm_plane_state *state)

    release plane state

    :param struct drm_plane_state \*state:
        plane state object to release

.. _`__drm_atomic_helper_plane_destroy_state.description`:

Description
-----------

Releases all resources stored in the plane state without actually freeing
the memory of the plane state. This is useful for drivers that subclass the
plane state.

.. _`drm_atomic_helper_plane_destroy_state`:

drm_atomic_helper_plane_destroy_state
=====================================

.. c:function:: void drm_atomic_helper_plane_destroy_state(struct drm_plane *plane, struct drm_plane_state *state)

    default state destroy hook

    :param struct drm_plane \*plane:
        drm plane

    :param struct drm_plane_state \*state:
        plane state object to release

.. _`drm_atomic_helper_plane_destroy_state.description`:

Description
-----------

Default plane state destroy hook for drivers which don't have their own
subclassed plane state structure.

.. _`__drm_atomic_helper_connector_reset`:

__drm_atomic_helper_connector_reset
===================================

.. c:function:: void __drm_atomic_helper_connector_reset(struct drm_connector *connector, struct drm_connector_state *conn_state)

    reset state on connector

    :param struct drm_connector \*connector:
        drm connector

    :param struct drm_connector_state \*conn_state:
        connector state to assign

.. _`__drm_atomic_helper_connector_reset.description`:

Description
-----------

Initializes the newly allocated \ ``conn_state``\  and assigns it to
#connector ->state, usually required when initializing the drivers
or when called from the ->reset hook.

This is useful for drivers that subclass the connector state.

.. _`drm_atomic_helper_connector_reset`:

drm_atomic_helper_connector_reset
=================================

.. c:function:: void drm_atomic_helper_connector_reset(struct drm_connector *connector)

    default ->reset hook for connectors

    :param struct drm_connector \*connector:
        drm connector

.. _`drm_atomic_helper_connector_reset.description`:

Description
-----------

Resets the atomic state for \ ``connector``\  by freeing the state pointer (which
might be NULL, e.g. at driver load time) and allocating a new empty state
object.

.. _`__drm_atomic_helper_connector_duplicate_state`:

__drm_atomic_helper_connector_duplicate_state
=============================================

.. c:function:: void __drm_atomic_helper_connector_duplicate_state(struct drm_connector *connector, struct drm_connector_state *state)

    copy atomic connector state

    :param struct drm_connector \*connector:
        connector object

    :param struct drm_connector_state \*state:
        atomic connector state

.. _`__drm_atomic_helper_connector_duplicate_state.description`:

Description
-----------

Copies atomic state from a connector's current state. This is useful for
drivers that subclass the connector state.

.. _`drm_atomic_helper_connector_duplicate_state`:

drm_atomic_helper_connector_duplicate_state
===========================================

.. c:function:: struct drm_connector_state *drm_atomic_helper_connector_duplicate_state(struct drm_connector *connector)

    default state duplicate hook

    :param struct drm_connector \*connector:
        drm connector

.. _`drm_atomic_helper_connector_duplicate_state.description`:

Description
-----------

Default connector state duplicate hook for drivers which don't have their own
subclassed connector state structure.

.. _`drm_atomic_helper_duplicate_state`:

drm_atomic_helper_duplicate_state
=================================

.. c:function:: struct drm_atomic_state *drm_atomic_helper_duplicate_state(struct drm_device *dev, struct drm_modeset_acquire_ctx *ctx)

    duplicate an atomic state object

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_modeset_acquire_ctx \*ctx:
        lock acquisition context

.. _`drm_atomic_helper_duplicate_state.description`:

Description
-----------

Makes a copy of the current atomic state by looping over all objects and
duplicating their respective states. This is used for example by suspend/
resume support code to save the state prior to suspend such that it can
be restored upon resume.

Note that this treats atomic state as persistent between save and restore.
Drivers must make sure that this is possible and won't result in confusion
or erroneous behaviour.

Note that if callers haven't already acquired all modeset locks this might
return -EDEADLK, which must be handled by calling \ :c:func:`drm_modeset_backoff`\ .

.. _`drm_atomic_helper_duplicate_state.return`:

Return
------

A pointer to the copy of the atomic state object on success or an
\ :c:func:`ERR_PTR`\ -encoded error code on failure.

.. _`drm_atomic_helper_duplicate_state.see-also`:

See also
--------

drm_atomic_helper_suspend(), \ :c:func:`drm_atomic_helper_resume`\ 

.. _`__drm_atomic_helper_connector_destroy_state`:

__drm_atomic_helper_connector_destroy_state
===========================================

.. c:function:: void __drm_atomic_helper_connector_destroy_state(struct drm_connector_state *state)

    release connector state

    :param struct drm_connector_state \*state:
        connector state object to release

.. _`__drm_atomic_helper_connector_destroy_state.description`:

Description
-----------

Releases all resources stored in the connector state without actually
freeing the memory of the connector state. This is useful for drivers that
subclass the connector state.

.. _`drm_atomic_helper_connector_destroy_state`:

drm_atomic_helper_connector_destroy_state
=========================================

.. c:function:: void drm_atomic_helper_connector_destroy_state(struct drm_connector *connector, struct drm_connector_state *state)

    default state destroy hook

    :param struct drm_connector \*connector:
        drm connector

    :param struct drm_connector_state \*state:
        connector state object to release

.. _`drm_atomic_helper_connector_destroy_state.description`:

Description
-----------

Default connector state destroy hook for drivers which don't have their own
subclassed connector state structure.

.. _`drm_atomic_helper_legacy_gamma_set`:

drm_atomic_helper_legacy_gamma_set
==================================

.. c:function:: int drm_atomic_helper_legacy_gamma_set(struct drm_crtc *crtc, u16 *red, u16 *green, u16 *blue, uint32_t size)

    set the legacy gamma correction table

    :param struct drm_crtc \*crtc:
        CRTC object

    :param u16 \*red:
        red correction table

    :param u16 \*green:
        green correction table

    :param u16 \*blue:
        green correction table

    :param uint32_t size:
        size of the tables

.. _`drm_atomic_helper_legacy_gamma_set.description`:

Description
-----------

Implements support for legacy gamma correction table for drivers
that support color management through the DEGAMMA_LUT/GAMMA_LUT
properties.

.. This file was automatic generated / don't edit.

