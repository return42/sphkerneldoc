.. -*- coding: utf-8; mode: rst -*-

===================
drm_atomic_helper.c
===================



.. _xref_drm_atomic_helper_check_modeset:

drm_atomic_helper_check_modeset
===============================

.. c:function:: int drm_atomic_helper_check_modeset (struct drm_device * dev, struct drm_atomic_state * state)

    validate state object for modeset changes

    :param struct drm_device * dev:
        DRM device

    :param struct drm_atomic_state * state:
        the driver state object



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



IMPORTANT
---------



Drivers which update ->mode_changed (e.g. in their ->atomic_check hooks if a
plane update can't be done without a full modeset) _must_ call this function
afterwards after that change. It is permitted to call this function multiple
times for the same update, e.g. when the ->atomic_check functions depend upon
the adjusted dotclock for fifo space allocation and watermark computation.


RETURNS
Zero for success or -errno




.. _xref_drm_atomic_helper_check_planes:

drm_atomic_helper_check_planes
==============================

.. c:function:: int drm_atomic_helper_check_planes (struct drm_device * dev, struct drm_atomic_state * state)

    validate state object for planes changes

    :param struct drm_device * dev:
        DRM device

    :param struct drm_atomic_state * state:
        the driver state object



Description
-----------

Check the state object to see if the requested state is physically possible.
This does all the plane update related checks using by calling into the
->atomic_check hooks provided by the driver.


It also sets crtc_state->planes_changed to indicate that a crtc has
updated planes.


RETURNS
Zero for success or -errno




.. _xref_drm_atomic_helper_check:

drm_atomic_helper_check
=======================

.. c:function:: int drm_atomic_helper_check (struct drm_device * dev, struct drm_atomic_state * state)

    validate state object

    :param struct drm_device * dev:
        DRM device

    :param struct drm_atomic_state * state:
        the driver state object



Description
-----------

Check the state object to see if the requested state is physically possible.
Only crtcs and planes have check callbacks, so for any additional (global)
checking that a driver needs it can simply wrap that around this function.
Drivers without such needs can directly use this as their ->:c:func:`atomic_check`
callback.


This just wraps the two parts of the state checking for planes and modeset



state in the default order
--------------------------

First it calls :c:func:`drm_atomic_helper_check_modeset`
and then :c:func:`drm_atomic_helper_check_planes`. The assumption is that the
->atomic_check functions depend upon an updated adjusted_mode.clock to
e.g. properly compute watermarks.


RETURNS
Zero for success or -errno




.. _xref_drm_atomic_helper_update_legacy_modeset_state:

drm_atomic_helper_update_legacy_modeset_state
=============================================

.. c:function:: void drm_atomic_helper_update_legacy_modeset_state (struct drm_device * dev, struct drm_atomic_state * old_state)

    update legacy modeset state

    :param struct drm_device * dev:
        DRM device

    :param struct drm_atomic_state * old_state:
        atomic state object with old state structures



Description
-----------

This function updates all the various legacy modeset state pointers in
connectors, encoders and crtcs. It also updates the timestamping constants
used for precise vblank timestamps by calling
:c:func:`drm_calc_timestamping_constants`.


Drivers can use this for building their own atomic commit if they don't have
a pure helper-based modeset implementation.




.. _xref_drm_atomic_helper_commit_modeset_disables:

drm_atomic_helper_commit_modeset_disables
=========================================

.. c:function:: void drm_atomic_helper_commit_modeset_disables (struct drm_device * dev, struct drm_atomic_state * old_state)

    modeset commit to disable outputs

    :param struct drm_device * dev:
        DRM device

    :param struct drm_atomic_state * old_state:
        atomic state object with old state structures



Description
-----------

This function shuts down all the outputs that need to be shut down and
prepares them (if required) with the new mode.


For compatibility with legacy crtc helpers this should be called before
:c:func:`drm_atomic_helper_commit_planes`, which is what the default commit function
does. But drivers with different needs can group the modeset commits together
and do the plane commits at the end. This is useful for drivers doing runtime
PM since planes updates then only happen when the CRTC is actually enabled.




.. _xref_drm_atomic_helper_commit_modeset_enables:

drm_atomic_helper_commit_modeset_enables
========================================

.. c:function:: void drm_atomic_helper_commit_modeset_enables (struct drm_device * dev, struct drm_atomic_state * old_state)

    modeset commit to enable outputs

    :param struct drm_device * dev:
        DRM device

    :param struct drm_atomic_state * old_state:
        atomic state object with old state structures



Description
-----------

This function enables all the outputs with the new configuration which had to
be turned off for the update.


For compatibility with legacy crtc helpers this should be called after
:c:func:`drm_atomic_helper_commit_planes`, which is what the default commit function
does. But drivers with different needs can group the modeset commits together
and do the plane commits at the end. This is useful for drivers doing runtime
PM since planes updates then only happen when the CRTC is actually enabled.




.. _xref_drm_atomic_helper_framebuffer_changed:

drm_atomic_helper_framebuffer_changed
=====================================

.. c:function:: bool drm_atomic_helper_framebuffer_changed (struct drm_device * dev, struct drm_atomic_state * old_state, struct drm_crtc * crtc)

    check if framebuffer has changed

    :param struct drm_device * dev:
        DRM device

    :param struct drm_atomic_state * old_state:
        atomic state object with old state structures

    :param struct drm_crtc * crtc:
        DRM crtc



Description
-----------

Checks whether the framebuffer used for this CRTC changes as a result of
the atomic update.  This is useful for drivers which cannot use
:c:func:`drm_atomic_helper_wait_for_vblanks` and need to reimplement its
functionality.



Returns
-------

true if the framebuffer changed.




.. _xref_drm_atomic_helper_wait_for_vblanks:

drm_atomic_helper_wait_for_vblanks
==================================

.. c:function:: void drm_atomic_helper_wait_for_vblanks (struct drm_device * dev, struct drm_atomic_state * old_state)

    wait for vblank on crtcs

    :param struct drm_device * dev:
        DRM device

    :param struct drm_atomic_state * old_state:
        atomic state object with old state structures



Description
-----------

Helper to, after atomic commit, wait for vblanks on all effected
crtcs (ie. before cleaning up old framebuffers using
:c:func:`drm_atomic_helper_cleanup_planes`). It will only wait on crtcs where the
framebuffers have actually changed to optimize for the legacy cursor and
plane update use-case.




.. _xref_drm_atomic_helper_commit:

drm_atomic_helper_commit
========================

.. c:function:: int drm_atomic_helper_commit (struct drm_device * dev, struct drm_atomic_state * state, bool async)

    commit validated state object

    :param struct drm_device * dev:
        DRM device

    :param struct drm_atomic_state * state:
        the driver state object

    :param bool async:
        asynchronous commit



Description
-----------

This function commits a with :c:func:`drm_atomic_helper_check` pre-validated state
object. This can still fail when e.g. the framebuffer reservation fails. For
now this doesn't implement asynchronous commits.


Note that right now this function does not support async commits, and hence
driver writers must implement their own version for now. Also note that the
default ordering of how the various stages are called is to match the legacy
modeset helper library closest. One peculiarity of that is that it doesn't
mesh well with runtime PM at all.


For drivers supporting runtime PM the recommended sequence is


    drm_atomic_helper_commit_modeset_disables(dev, state);


    drm_atomic_helper_commit_modeset_enables(dev, state);


    drm_atomic_helper_commit_planes(dev, state, true);


See the kerneldoc entries for these three functions for more details.


RETURNS
Zero for success or -errno.




.. _xref_drm_atomic_helper_prepare_planes:

drm_atomic_helper_prepare_planes
================================

.. c:function:: int drm_atomic_helper_prepare_planes (struct drm_device * dev, struct drm_atomic_state * state)

    prepare plane resources before commit

    :param struct drm_device * dev:
        DRM device

    :param struct drm_atomic_state * state:
        atomic state object with new state structures



Description
-----------

This function prepares plane state, specifically framebuffers, for the new
configuration. If any failure is encountered this function will call
->cleanup_fb on any already successfully prepared framebuffer.



Returns
-------

0 on success, negative error code on failure.




.. _xref_drm_atomic_helper_commit_planes:

drm_atomic_helper_commit_planes
===============================

.. c:function:: void drm_atomic_helper_commit_planes (struct drm_device * dev, struct drm_atomic_state * old_state, bool active_only)

    commit plane state

    :param struct drm_device * dev:
        DRM device

    :param struct drm_atomic_state * old_state:
        atomic state object with old state structures

    :param bool active_only:
        Only commit on active CRTC if set



Description
-----------

This function commits the new plane state using the plane and atomic helper
functions for planes and crtcs. It assumes that the atomic state has already
been pushed into the relevant object state pointers, since this step can no
longer fail.


It still requires the global state object **old_state** to know which planes and
crtcs need to be updated though.


Note that this function does all plane updates across all CRTCs in one step.
If the hardware can't support this approach look at
:c:func:`drm_atomic_helper_commit_planes_on_crtc` instead.


Plane parameters can be updated by applications while the associated CRTC is
disabled. The DRM/KMS core will store the parameters in the plane state,
which will be available to the driver when the CRTC is turned on. As a result
most drivers don't need to be immediately notified of plane updates for a
disabled CRTC.


Unless otherwise needed, drivers are advised to set the **active_only**
parameters to true in order not to receive plane update notifications related
to a disabled CRTC. This avoids the need to manually ignore plane updates in
driver code when the driver and/or hardware can't or just don't need to deal
with updates on disabled CRTCs, for example when supporting runtime PM.


The :c:func:`drm_atomic_helper_commit` default implementation only sets **active_only**
to false to most closely match the behaviour of the legacy helpers. This should
not be copied blindly by drivers.




.. _xref_drm_atomic_helper_commit_planes_on_crtc:

drm_atomic_helper_commit_planes_on_crtc
=======================================

.. c:function:: void drm_atomic_helper_commit_planes_on_crtc (struct drm_crtc_state * old_crtc_state)

    commit plane state for a crtc

    :param struct drm_crtc_state * old_crtc_state:
        atomic state object with the old crtc state



Description
-----------

This function commits the new plane state using the plane and atomic helper
functions for planes on the specific crtc. It assumes that the atomic state
has already been pushed into the relevant object state pointers, since this
step can no longer fail.


This function is useful when plane updates should be done crtc-by-crtc
instead of one global step like :c:func:`drm_atomic_helper_commit_planes` does.


This function can only be savely used when planes are not allowed to move
between different CRTCs because this function doesn't handle inter-CRTC
depencies. Callers need to ensure that either no such depencies exist,
resolve them through ordering of commit calls or through some other means.




.. _xref_drm_atomic_helper_disable_planes_on_crtc:

drm_atomic_helper_disable_planes_on_crtc
========================================

.. c:function:: void drm_atomic_helper_disable_planes_on_crtc (struct drm_crtc * crtc, bool atomic)

    helper to disable CRTC's planes

    :param struct drm_crtc * crtc:
        CRTC

    :param bool atomic:
        if set, synchronize with CRTC's atomic_begin/flush hooks



Description
-----------

Disables all planes associated with the given CRTC. This can be
used for instance in the CRTC helper disable callback to disable
all planes before shutting down the display pipeline.


If the atomic-parameter is set the function calls the CRTC's
atomic_begin hook before and atomic_flush hook after disabling the
planes.


It is a bug to call this function without having implemented the
->:c:func:`atomic_disable` plane hook.




.. _xref_drm_atomic_helper_cleanup_planes:

drm_atomic_helper_cleanup_planes
================================

.. c:function:: void drm_atomic_helper_cleanup_planes (struct drm_device * dev, struct drm_atomic_state * old_state)

    cleanup plane resources after commit

    :param struct drm_device * dev:
        DRM device

    :param struct drm_atomic_state * old_state:
        atomic state object with old state structures



Description
-----------

This function cleans up plane state, specifically framebuffers, from the old
configuration. Hence the old configuration must be perserved in **old_state** to
be able to call this function.


This function must also be called on the new state when the atomic update
fails at any point after calling :c:func:`drm_atomic_helper_prepare_planes`.




.. _xref_drm_atomic_helper_swap_state:

drm_atomic_helper_swap_state
============================

.. c:function:: void drm_atomic_helper_swap_state (struct drm_device * dev, struct drm_atomic_state * state)

    store atomic state into current sw state

    :param struct drm_device * dev:
        DRM device

    :param struct drm_atomic_state * state:
        atomic state



Description
-----------

This function stores the atomic state into the current state pointers in all
driver objects. It should be called after all failing steps have been done
and succeeded, but before the actual hardware state is committed.


For cleanup and error recovery the current state for all changed objects will
be swaped into **state**.


With that sequence it fits perfectly into the plane prepare/cleanup sequence:


1. Call :c:func:`drm_atomic_helper_prepare_planes` with the staged atomic state.


2. Do any other steps that might fail.


3. Put the staged state into the current state pointers with this function.


4. Actually commit the hardware state.


5. Call :c:func:`drm_atomic_helper_cleanup_planes` with **state**, which since step 3
contains the old state. Also do any other cleanup required with that state.




.. _xref_drm_atomic_helper_update_plane:

drm_atomic_helper_update_plane
==============================

.. c:function:: int drm_atomic_helper_update_plane (struct drm_plane * plane, struct drm_crtc * crtc, struct drm_framebuffer * fb, int crtc_x, int crtc_y, unsigned int crtc_w, unsigned int crtc_h, uint32_t src_x, uint32_t src_y, uint32_t src_w, uint32_t src_h)

    Helper for primary plane update using atomic

    :param struct drm_plane * plane:
        plane object to update

    :param struct drm_crtc * crtc:
        owning CRTC of owning plane

    :param struct drm_framebuffer * fb:
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
        x offset of **fb** for panning

    :param uint32_t src_y:
        y offset of **fb** for panning

    :param uint32_t src_w:
        width of source rectangle in **fb**

    :param uint32_t src_h:
        height of source rectangle in **fb**



Description
-----------

Provides a default plane update handler using the atomic driver interface.



RETURNS
-------

Zero on success, error code on failure




.. _xref_drm_atomic_helper_disable_plane:

drm_atomic_helper_disable_plane
===============================

.. c:function:: int drm_atomic_helper_disable_plane (struct drm_plane * plane)

    Helper for primary plane disable using * atomic

    :param struct drm_plane * plane:
        plane to disable



Description
-----------

Provides a default plane disable handler using the atomic driver interface.



RETURNS
-------

Zero on success, error code on failure




.. _xref_drm_atomic_helper_set_config:

drm_atomic_helper_set_config
============================

.. c:function:: int drm_atomic_helper_set_config (struct drm_mode_set * set)

    set a new config from userspace

    :param struct drm_mode_set * set:
        mode set configuration



Description
-----------

Provides a default crtc set_config handler using the atomic driver interface.



Returns
-------

Returns 0 on success, negative errno numbers on failure.




.. _xref_drm_atomic_helper_disable_all:

drm_atomic_helper_disable_all
=============================

.. c:function:: int drm_atomic_helper_disable_all (struct drm_device * dev, struct drm_modeset_acquire_ctx * ctx)

    disable all currently active outputs

    :param struct drm_device * dev:
        DRM device

    :param struct drm_modeset_acquire_ctx * ctx:
        lock acquisition context



Description
-----------

Loops through all connectors, finding those that aren't turned off and then
turns them off by setting their DPMS mode to OFF and deactivating the CRTC
that they are connected to.


This is used for example in suspend/resume to disable all currently active
functions when suspending.


Note that if callers haven't already acquired all modeset locks this might
return -EDEADLK, which must be handled by calling :c:func:`drm_modeset_backoff`.



Returns
-------

0 on success or a negative error code on failure.



See also
--------

:c:func:`drm_atomic_helper_suspend`, :c:func:`drm_atomic_helper_resume`




.. _xref_drm_atomic_helper_suspend:

drm_atomic_helper_suspend
=========================

.. c:function:: struct drm_atomic_state * drm_atomic_helper_suspend (struct drm_device * dev)

    subsystem-level suspend helper

    :param struct drm_device * dev:
        DRM device



Description
-----------

Duplicates the current atomic state, disables all active outputs and then
returns a pointer to the original atomic state to the caller. Drivers can
pass this pointer to the :c:func:`drm_atomic_helper_resume` helper upon resume to
restore the output configuration that was active at the time the system
entered suspend.


Note that it is potentially unsafe to use this. The atomic state object
returned by this function is assumed to be persistent. Drivers must ensure
that this holds true. Before calling this function, drivers must make sure
to suspend fbdev emulation so that nothing can be using the device.



Returns
-------

A pointer to a copy of the state before suspend on success or an :c:func:`ERR_PTR`-
encoded error code on failure. Drivers should store the returned atomic
state object and pass it to the :c:func:`drm_atomic_helper_resume` helper upon
resume.



See also
--------

:c:func:`drm_atomic_helper_duplicate_state`, :c:func:`drm_atomic_helper_disable_all`,
:c:func:`drm_atomic_helper_resume`




.. _xref_drm_atomic_helper_resume:

drm_atomic_helper_resume
========================

.. c:function:: int drm_atomic_helper_resume (struct drm_device * dev, struct drm_atomic_state * state)

    subsystem-level resume helper

    :param struct drm_device * dev:
        DRM device

    :param struct drm_atomic_state * state:
        atomic state to resume to



Description
-----------

Calls :c:func:`drm_mode_config_reset` to synchronize hardware and software states,
grabs all modeset locks and commits the atomic state object. This can be
used in conjunction with the :c:func:`drm_atomic_helper_suspend` helper to
implement suspend/resume for drivers that support atomic mode-setting.



Returns
-------

0 on success or a negative error code on failure.



See also
--------

:c:func:`drm_atomic_helper_suspend`




.. _xref_drm_atomic_helper_crtc_set_property:

drm_atomic_helper_crtc_set_property
===================================

.. c:function:: int drm_atomic_helper_crtc_set_property (struct drm_crtc * crtc, struct drm_property * property, uint64_t val)

    helper for crtc properties

    :param struct drm_crtc * crtc:
        DRM crtc

    :param struct drm_property * property:
        DRM property

    :param uint64_t val:
        value of property



Description
-----------

Provides a default crtc set_property handler using the atomic driver
interface.



RETURNS
-------

Zero on success, error code on failure




.. _xref_drm_atomic_helper_plane_set_property:

drm_atomic_helper_plane_set_property
====================================

.. c:function:: int drm_atomic_helper_plane_set_property (struct drm_plane * plane, struct drm_property * property, uint64_t val)

    helper for plane properties

    :param struct drm_plane * plane:
        DRM plane

    :param struct drm_property * property:
        DRM property

    :param uint64_t val:
        value of property



Description
-----------

Provides a default plane set_property handler using the atomic driver
interface.



RETURNS
-------

Zero on success, error code on failure




.. _xref_drm_atomic_helper_connector_set_property:

drm_atomic_helper_connector_set_property
========================================

.. c:function:: int drm_atomic_helper_connector_set_property (struct drm_connector * connector, struct drm_property * property, uint64_t val)

    helper for connector properties

    :param struct drm_connector * connector:
        DRM connector

    :param struct drm_property * property:
        DRM property

    :param uint64_t val:
        value of property



Description
-----------

Provides a default connector set_property handler using the atomic driver
interface.



RETURNS
-------

Zero on success, error code on failure




.. _xref_drm_atomic_helper_page_flip:

drm_atomic_helper_page_flip
===========================

.. c:function:: int drm_atomic_helper_page_flip (struct drm_crtc * crtc, struct drm_framebuffer * fb, struct drm_pending_vblank_event * event, uint32_t flags)

    execute a legacy page flip

    :param struct drm_crtc * crtc:
        DRM crtc

    :param struct drm_framebuffer * fb:
        DRM framebuffer

    :param struct drm_pending_vblank_event * event:
        optional DRM event to signal upon completion

    :param uint32_t flags:
        flip flags for non-vblank sync'ed updates



Description
-----------

Provides a default page flip implementation using the atomic driver interface.


Note that for now so called async page flips (i.e. updates which are not
synchronized to vblank) are not supported, since the atomic interfaces have
no provisions for this yet.



Returns
-------

Returns 0 on success, negative errno numbers on failure.




.. _xref_drm_atomic_helper_connector_dpms:

drm_atomic_helper_connector_dpms
================================

.. c:function:: int drm_atomic_helper_connector_dpms (struct drm_connector * connector, int mode)

    connector dpms helper implementation

    :param struct drm_connector * connector:
        affected connector

    :param int mode:
        DPMS mode



Description
-----------

This is the main helper function provided by the atomic helper framework for
implementing the legacy DPMS connector interface. It computes the new desired
->active state for the corresponding CRTC (if the connector is enabled) and
 updates it.



Returns
-------

Returns 0 on success, negative errno numbers on failure.




.. _xref_drm_atomic_helper_crtc_reset:

drm_atomic_helper_crtc_reset
============================

.. c:function:: void drm_atomic_helper_crtc_reset (struct drm_crtc * crtc)

    default -\\\gt;reset hook for CRTCs

    :param struct drm_crtc * crtc:
        drm CRTC



Description
-----------

Resets the atomic state for **crtc** by freeing the state pointer (which might
be NULL, e.g. at driver load time) and allocating a new empty state object.




.. _xref___drm_atomic_helper_crtc_duplicate_state:

__drm_atomic_helper_crtc_duplicate_state
========================================

.. c:function:: void __drm_atomic_helper_crtc_duplicate_state (struct drm_crtc * crtc, struct drm_crtc_state * state)

    copy atomic CRTC state

    :param struct drm_crtc * crtc:
        CRTC object

    :param struct drm_crtc_state * state:
        atomic CRTC state



Description
-----------

Copies atomic state from a CRTC's current state and resets inferred values.
This is useful for drivers that subclass the CRTC state.




.. _xref_drm_atomic_helper_crtc_duplicate_state:

drm_atomic_helper_crtc_duplicate_state
======================================

.. c:function:: struct drm_crtc_state * drm_atomic_helper_crtc_duplicate_state (struct drm_crtc * crtc)

    default state duplicate hook

    :param struct drm_crtc * crtc:
        drm CRTC



Description
-----------

Default CRTC state duplicate hook for drivers which don't have their own
subclassed CRTC state structure.




.. _xref___drm_atomic_helper_crtc_destroy_state:

__drm_atomic_helper_crtc_destroy_state
======================================

.. c:function:: void __drm_atomic_helper_crtc_destroy_state (struct drm_crtc * crtc, struct drm_crtc_state * state)

    release CRTC state

    :param struct drm_crtc * crtc:
        CRTC object

    :param struct drm_crtc_state * state:
        CRTC state object to release



Description
-----------

Releases all resources stored in the CRTC state without actually freeing
the memory of the CRTC state. This is useful for drivers that subclass the
CRTC state.




.. _xref_drm_atomic_helper_crtc_destroy_state:

drm_atomic_helper_crtc_destroy_state
====================================

.. c:function:: void drm_atomic_helper_crtc_destroy_state (struct drm_crtc * crtc, struct drm_crtc_state * state)

    default state destroy hook

    :param struct drm_crtc * crtc:
        drm CRTC

    :param struct drm_crtc_state * state:
        CRTC state object to release



Description
-----------

Default CRTC state destroy hook for drivers which don't have their own
subclassed CRTC state structure.




.. _xref_drm_atomic_helper_plane_reset:

drm_atomic_helper_plane_reset
=============================

.. c:function:: void drm_atomic_helper_plane_reset (struct drm_plane * plane)

    default -\\\gt;reset hook for planes

    :param struct drm_plane * plane:
        drm plane



Description
-----------

Resets the atomic state for **plane** by freeing the state pointer (which might
be NULL, e.g. at driver load time) and allocating a new empty state object.




.. _xref___drm_atomic_helper_plane_duplicate_state:

__drm_atomic_helper_plane_duplicate_state
=========================================

.. c:function:: void __drm_atomic_helper_plane_duplicate_state (struct drm_plane * plane, struct drm_plane_state * state)

    copy atomic plane state

    :param struct drm_plane * plane:
        plane object

    :param struct drm_plane_state * state:
        atomic plane state



Description
-----------

Copies atomic state from a plane's current state. This is useful for
drivers that subclass the plane state.




.. _xref_drm_atomic_helper_plane_duplicate_state:

drm_atomic_helper_plane_duplicate_state
=======================================

.. c:function:: struct drm_plane_state * drm_atomic_helper_plane_duplicate_state (struct drm_plane * plane)

    default state duplicate hook

    :param struct drm_plane * plane:
        drm plane



Description
-----------

Default plane state duplicate hook for drivers which don't have their own
subclassed plane state structure.




.. _xref___drm_atomic_helper_plane_destroy_state:

__drm_atomic_helper_plane_destroy_state
=======================================

.. c:function:: void __drm_atomic_helper_plane_destroy_state (struct drm_plane * plane, struct drm_plane_state * state)

    release plane state

    :param struct drm_plane * plane:
        plane object

    :param struct drm_plane_state * state:
        plane state object to release



Description
-----------

Releases all resources stored in the plane state without actually freeing
the memory of the plane state. This is useful for drivers that subclass the
plane state.




.. _xref_drm_atomic_helper_plane_destroy_state:

drm_atomic_helper_plane_destroy_state
=====================================

.. c:function:: void drm_atomic_helper_plane_destroy_state (struct drm_plane * plane, struct drm_plane_state * state)

    default state destroy hook

    :param struct drm_plane * plane:
        drm plane

    :param struct drm_plane_state * state:
        plane state object to release



Description
-----------

Default plane state destroy hook for drivers which don't have their own
subclassed plane state structure.




.. _xref___drm_atomic_helper_connector_reset:

__drm_atomic_helper_connector_reset
===================================

.. c:function:: void __drm_atomic_helper_connector_reset (struct drm_connector * connector, struct drm_connector_state * conn_state)

    reset state on connector

    :param struct drm_connector * connector:
        drm connector

    :param struct drm_connector_state * conn_state:
        connector state to assign



Description
-----------

Initializes the newly allocated **conn_state** and assigns it to
#connector ->state, usually required when initializing the drivers
or when called from the ->reset hook.


This is useful for drivers that subclass the connector state.




.. _xref_drm_atomic_helper_connector_reset:

drm_atomic_helper_connector_reset
=================================

.. c:function:: void drm_atomic_helper_connector_reset (struct drm_connector * connector)

    default -\\\gt;reset hook for connectors

    :param struct drm_connector * connector:
        drm connector



Description
-----------

Resets the atomic state for **connector** by freeing the state pointer (which
might be NULL, e.g. at driver load time) and allocating a new empty state
object.




.. _xref___drm_atomic_helper_connector_duplicate_state:

__drm_atomic_helper_connector_duplicate_state
=============================================

.. c:function:: void __drm_atomic_helper_connector_duplicate_state (struct drm_connector * connector, struct drm_connector_state * state)

    copy atomic connector state

    :param struct drm_connector * connector:
        connector object

    :param struct drm_connector_state * state:
        atomic connector state



Description
-----------

Copies atomic state from a connector's current state. This is useful for
drivers that subclass the connector state.




.. _xref_drm_atomic_helper_connector_duplicate_state:

drm_atomic_helper_connector_duplicate_state
===========================================

.. c:function:: struct drm_connector_state * drm_atomic_helper_connector_duplicate_state (struct drm_connector * connector)

    default state duplicate hook

    :param struct drm_connector * connector:
        drm connector



Description
-----------

Default connector state duplicate hook for drivers which don't have their own
subclassed connector state structure.




.. _xref_drm_atomic_helper_duplicate_state:

drm_atomic_helper_duplicate_state
=================================

.. c:function:: struct drm_atomic_state * drm_atomic_helper_duplicate_state (struct drm_device * dev, struct drm_modeset_acquire_ctx * ctx)

    duplicate an atomic state object

    :param struct drm_device * dev:
        DRM device

    :param struct drm_modeset_acquire_ctx * ctx:
        lock acquisition context



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
return -EDEADLK, which must be handled by calling :c:func:`drm_modeset_backoff`.



Returns
-------

A pointer to the copy of the atomic state object on success or an
:c:func:`ERR_PTR`-encoded error code on failure.



See also
--------

:c:func:`drm_atomic_helper_suspend`, :c:func:`drm_atomic_helper_resume`




.. _xref___drm_atomic_helper_connector_destroy_state:

__drm_atomic_helper_connector_destroy_state
===========================================

.. c:function:: void __drm_atomic_helper_connector_destroy_state (struct drm_connector * connector, struct drm_connector_state * state)

    release connector state

    :param struct drm_connector * connector:
        connector object

    :param struct drm_connector_state * state:
        connector state object to release



Description
-----------

Releases all resources stored in the connector state without actually
freeing the memory of the connector state. This is useful for drivers that
subclass the connector state.




.. _xref_drm_atomic_helper_connector_destroy_state:

drm_atomic_helper_connector_destroy_state
=========================================

.. c:function:: void drm_atomic_helper_connector_destroy_state (struct drm_connector * connector, struct drm_connector_state * state)

    default state destroy hook

    :param struct drm_connector * connector:
        drm connector

    :param struct drm_connector_state * state:
        connector state object to release



Description
-----------

Default connector state destroy hook for drivers which don't have their own
subclassed connector state structure.




.. _xref_drm_atomic_helper_legacy_gamma_set:

drm_atomic_helper_legacy_gamma_set
==================================

.. c:function:: void drm_atomic_helper_legacy_gamma_set (struct drm_crtc * crtc, u16 * red, u16 * green, u16 * blue, uint32_t start, uint32_t size)

    set the legacy gamma correction table

    :param struct drm_crtc * crtc:
        CRTC object

    :param u16 * red:
        red correction table

    :param u16 * green:
        green correction table

    :param u16 * blue:
        green correction table

    :param uint32_t start:

        _undescribed_

    :param uint32_t size:
        size of the tables



Description
-----------

Implements support for legacy gamma correction table for drivers
that support color management through the DEGAMMA_LUT/GAMMA_LUT
properties.


