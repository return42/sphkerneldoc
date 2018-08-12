.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_vblank.c

.. _`vblank-handling`:

vblank handling
===============

Vertical blanking plays a major role in graphics rendering. To achieve
tear-free display, users must synchronize page flips and/or rendering to
vertical blanking. The DRM API offers ioctls to perform page flips
synchronized to vertical blanking and wait for vertical blanking.

The DRM core handles most of the vertical blanking management logic, which
involves filtering out spurious interrupts, keeping race-free blanking
counters, coping with counter wrap-around and resets and keeping use counts.
It relies on the driver to generate vertical blanking interrupts and
optionally provide a hardware vertical blanking counter.

Drivers must initialize the vertical blanking handling core with a call to
\ :c:func:`drm_vblank_init`\ . Minimally, a driver needs to implement
\ :c:type:`drm_crtc_funcs.enable_vblank <drm_crtc_funcs>`\  and \ :c:type:`drm_crtc_funcs.disable_vblank <drm_crtc_funcs>`\  plus call
\ :c:func:`drm_crtc_handle_vblank`\  in it's vblank interrupt handler for working vblank
support.

Vertical blanking interrupts can be enabled by the DRM core or by drivers
themselves (for instance to handle page flipping operations).  The DRM core
maintains a vertical blanking use count to ensure that the interrupts are not
disabled while a user still needs them. To increment the use count, drivers
call \ :c:func:`drm_crtc_vblank_get`\  and release the vblank reference again with
\ :c:func:`drm_crtc_vblank_put`\ . In between these two calls vblank interrupts are
guaranteed to be enabled.

On many hardware disabling the vblank interrupt cannot be done in a race-free
manner, see \ :c:type:`drm_driver.vblank_disable_immediate <drm_driver>`\  and
\ :c:type:`drm_driver.max_vblank_count <drm_driver>`\ . In that case the vblank core only disables the
vblanks after a timer has expired, which can be configured through the
``vblankoffdelay`` module parameter.

.. _`drm_crtc_accurate_vblank_count`:

drm_crtc_accurate_vblank_count
==============================

.. c:function:: u64 drm_crtc_accurate_vblank_count(struct drm_crtc *crtc)

    retrieve the master vblank counter

    :param struct drm_crtc \*crtc:
        which counter to retrieve

.. _`drm_crtc_accurate_vblank_count.description`:

Description
-----------

This function is similar to \ :c:func:`drm_crtc_vblank_count`\  but this function
interpolates to handle a race with vblank interrupts using the high precision
timestamping support.

This is mostly useful for hardware that can obtain the scanout position, but
doesn't have a hardware frame counter.

.. _`drm_vblank_init`:

drm_vblank_init
===============

.. c:function:: int drm_vblank_init(struct drm_device *dev, unsigned int num_crtcs)

    initialize vblank support

    :param struct drm_device \*dev:
        DRM device

    :param unsigned int num_crtcs:
        number of CRTCs supported by \ ``dev``\ 

.. _`drm_vblank_init.description`:

Description
-----------

This function initializes vblank support for \ ``num_crtcs``\  display pipelines.
Cleanup is handled by the DRM core, or through calling \ :c:func:`drm_dev_fini`\  for
drivers with a \ :c:type:`drm_driver.release <drm_driver>`\  callback.

.. _`drm_vblank_init.return`:

Return
------

Zero on success or a negative error code on failure.

.. _`drm_crtc_vblank_waitqueue`:

drm_crtc_vblank_waitqueue
=========================

.. c:function:: wait_queue_head_t *drm_crtc_vblank_waitqueue(struct drm_crtc *crtc)

    get vblank waitqueue for the CRTC

    :param struct drm_crtc \*crtc:
        which CRTC's vblank waitqueue to retrieve

.. _`drm_crtc_vblank_waitqueue.description`:

Description
-----------

This function returns a pointer to the vblank waitqueue for the CRTC.
Drivers can use this to implement vblank waits using \ :c:func:`wait_event`\  and related
functions.

.. _`drm_calc_timestamping_constants`:

drm_calc_timestamping_constants
===============================

.. c:function:: void drm_calc_timestamping_constants(struct drm_crtc *crtc, const struct drm_display_mode *mode)

    calculate vblank timestamp constants

    :param struct drm_crtc \*crtc:
        drm_crtc whose timestamp constants should be updated.

    :param const struct drm_display_mode \*mode:
        display mode containing the scanout timings

.. _`drm_calc_timestamping_constants.description`:

Description
-----------

Calculate and store various constants which are later needed by vblank and
swap-completion timestamping, e.g, by
\ :c:func:`drm_calc_vbltimestamp_from_scanoutpos`\ . They are derived from CRTC's true
scanout timing, so they take things like panel scaling or other adjustments
into account.

.. _`drm_calc_vbltimestamp_from_scanoutpos`:

drm_calc_vbltimestamp_from_scanoutpos
=====================================

.. c:function:: bool drm_calc_vbltimestamp_from_scanoutpos(struct drm_device *dev, unsigned int pipe, int *max_error, ktime_t *vblank_time, bool in_vblank_irq)

    precise vblank timestamp helper

    :param struct drm_device \*dev:
        DRM device

    :param unsigned int pipe:
        index of CRTC whose vblank timestamp to retrieve

    :param int \*max_error:
        Desired maximum allowable error in timestamps (nanosecs)
        On return contains true maximum error of timestamp

    :param ktime_t \*vblank_time:
        Pointer to time which should receive the timestamp

    :param bool in_vblank_irq:
        True when called from \ :c:func:`drm_crtc_handle_vblank`\ .  Some drivers
        need to apply some workarounds for gpu-specific vblank irq quirks
        if flag is set.

.. _`drm_calc_vbltimestamp_from_scanoutpos.description`:

Description
-----------

Implements calculation of exact vblank timestamps from given drm_display_mode
timings and current video scanout position of a CRTC. This can be directly
used as the \ :c:type:`drm_driver.get_vblank_timestamp <drm_driver>`\  implementation of a kms driver
if \ :c:type:`drm_driver.get_scanout_position <drm_driver>`\  is implemented.

The current implementation only handles standard video modes. For double scan
and interlaced modes the driver is supposed to adjust the hardware mode
(taken from \ :c:type:`drm_crtc_state.adjusted <drm_crtc_state>`\  mode for atomic modeset drivers) to
match the scanout position reported.

Note that atomic drivers must call \ :c:func:`drm_calc_timestamping_constants`\  before
enabling a CRTC. The atomic helpers already take care of that in
\ :c:func:`drm_atomic_helper_update_legacy_modeset_state`\ .

.. _`drm_calc_vbltimestamp_from_scanoutpos.return`:

Return
------


Returns true on success, and false on failure, i.e. when no accurate
timestamp could be acquired.

.. _`drm_get_last_vbltimestamp`:

drm_get_last_vbltimestamp
=========================

.. c:function:: bool drm_get_last_vbltimestamp(struct drm_device *dev, unsigned int pipe, ktime_t *tvblank, bool in_vblank_irq)

    retrieve raw timestamp for the most recent vblank interval

    :param struct drm_device \*dev:
        DRM device

    :param unsigned int pipe:
        index of CRTC whose vblank timestamp to retrieve

    :param ktime_t \*tvblank:
        Pointer to target time which should receive the timestamp

    :param bool in_vblank_irq:
        True when called from \ :c:func:`drm_crtc_handle_vblank`\ .  Some drivers
        need to apply some workarounds for gpu-specific vblank irq quirks
        if flag is set.

.. _`drm_get_last_vbltimestamp.description`:

Description
-----------

Fetches the system timestamp corresponding to the time of the most recent
vblank interval on specified CRTC. May call into kms-driver to
compute the timestamp with a high-precision GPU specific method.

Returns zero if timestamp originates from uncorrected \ :c:func:`do_gettimeofday`\ 
call, i.e., it isn't very precisely locked to the true vblank.

.. _`drm_get_last_vbltimestamp.return`:

Return
------

True if timestamp is considered to be very precise, false otherwise.

.. _`drm_crtc_vblank_count`:

drm_crtc_vblank_count
=====================

.. c:function:: u64 drm_crtc_vblank_count(struct drm_crtc *crtc)

    retrieve "cooked" vblank counter value

    :param struct drm_crtc \*crtc:
        which counter to retrieve

.. _`drm_crtc_vblank_count.description`:

Description
-----------

Fetches the "cooked" vblank count value that represents the number of
vblank events since the system was booted, including lost events due to
modesetting activity. Note that this timer isn't correct against a racing
vblank interrupt (since it only reports the software vblank counter), see
\ :c:func:`drm_crtc_accurate_vblank_count`\  for such use-cases.

.. _`drm_crtc_vblank_count.return`:

Return
------

The software vblank counter.

.. _`drm_vblank_count_and_time`:

drm_vblank_count_and_time
=========================

.. c:function:: u64 drm_vblank_count_and_time(struct drm_device *dev, unsigned int pipe, ktime_t *vblanktime)

    retrieve "cooked" vblank counter value and the system timestamp corresponding to that vblank counter value.

    :param struct drm_device \*dev:
        DRM device

    :param unsigned int pipe:
        index of CRTC whose counter to retrieve

    :param ktime_t \*vblanktime:
        Pointer to ktime_t to receive the vblank timestamp.

.. _`drm_vblank_count_and_time.description`:

Description
-----------

Fetches the "cooked" vblank count value that represents the number of
vblank events since the system was booted, including lost events due to
modesetting activity. Returns corresponding system timestamp of the time
of the vblank interval that corresponds to the current vblank counter value.

This is the legacy version of \ :c:func:`drm_crtc_vblank_count_and_time`\ .

.. _`drm_crtc_vblank_count_and_time`:

drm_crtc_vblank_count_and_time
==============================

.. c:function:: u64 drm_crtc_vblank_count_and_time(struct drm_crtc *crtc, ktime_t *vblanktime)

    retrieve "cooked" vblank counter value and the system timestamp corresponding to that vblank counter value

    :param struct drm_crtc \*crtc:
        which counter to retrieve

    :param ktime_t \*vblanktime:
        Pointer to time to receive the vblank timestamp.

.. _`drm_crtc_vblank_count_and_time.description`:

Description
-----------

Fetches the "cooked" vblank count value that represents the number of
vblank events since the system was booted, including lost events due to
modesetting activity. Returns corresponding system timestamp of the time
of the vblank interval that corresponds to the current vblank counter value.

.. _`drm_crtc_arm_vblank_event`:

drm_crtc_arm_vblank_event
=========================

.. c:function:: void drm_crtc_arm_vblank_event(struct drm_crtc *crtc, struct drm_pending_vblank_event *e)

    arm vblank event after pageflip

    :param struct drm_crtc \*crtc:
        the source CRTC of the vblank event

    :param struct drm_pending_vblank_event \*e:
        the event to send

.. _`drm_crtc_arm_vblank_event.description`:

Description
-----------

A lot of drivers need to generate vblank events for the very next vblank
interrupt. For example when the page flip interrupt happens when the page
flip gets armed, but not when it actually executes within the next vblank
period. This helper function implements exactly the required vblank arming
behaviour.

.. _`drm_crtc_arm_vblank_event.note`:

NOTE
----

Drivers using this to send out the \ :c:type:`drm_crtc_state.event <drm_crtc_state>`\  as part of an
atomic commit must ensure that the next vblank happens at exactly the same
time as the atomic commit is committed to the hardware. This function itself
does **not** protect against the next vblank interrupt racing with either this
function call or the atomic commit operation. A possible sequence could be:

1. Driver commits new hardware state into vblank-synchronized registers.
2. A vblank happens, committing the hardware state. Also the corresponding
   vblank interrupt is fired off and fully processed by the interrupt
   handler.
3. The atomic commit operation proceeds to call \ :c:func:`drm_crtc_arm_vblank_event`\ .
4. The event is only send out for the next vblank, which is wrong.

An equivalent race can happen when the driver calls
\ :c:func:`drm_crtc_arm_vblank_event`\  before writing out the new hardware state.

The only way to make this work safely is to prevent the vblank from firing
(and the hardware from committing anything else) until the entire atomic
commit sequence has run to completion. If the hardware does not have such a
feature (e.g. using a "go" bit), then it is unsafe to use this functions.
Instead drivers need to manually send out the event from their interrupt
handler by calling \ :c:func:`drm_crtc_send_vblank_event`\  and make sure that there's no
possible race with the hardware committing the atomic update.

Caller must hold a vblank reference for the event \ ``e``\ , which will be dropped
when the next vblank arrives.

.. _`drm_crtc_send_vblank_event`:

drm_crtc_send_vblank_event
==========================

.. c:function:: void drm_crtc_send_vblank_event(struct drm_crtc *crtc, struct drm_pending_vblank_event *e)

    helper to send vblank event after pageflip

    :param struct drm_crtc \*crtc:
        the source CRTC of the vblank event

    :param struct drm_pending_vblank_event \*e:
        the event to send

.. _`drm_crtc_send_vblank_event.description`:

Description
-----------

Updates sequence # and timestamp on event for the most recently processed
vblank, and sends it to userspace.  Caller must hold event lock.

See \ :c:func:`drm_crtc_arm_vblank_event`\  for a helper which can be used in certain
situation, especially to send out events for atomic commit operations.

.. _`drm_crtc_vblank_get`:

drm_crtc_vblank_get
===================

.. c:function:: int drm_crtc_vblank_get(struct drm_crtc *crtc)

    get a reference count on vblank events

    :param struct drm_crtc \*crtc:
        which CRTC to own

.. _`drm_crtc_vblank_get.description`:

Description
-----------

Acquire a reference count on vblank events to avoid having them disabled
while in use.

.. _`drm_crtc_vblank_get.return`:

Return
------

Zero on success or a negative error code on failure.

.. _`drm_crtc_vblank_put`:

drm_crtc_vblank_put
===================

.. c:function:: void drm_crtc_vblank_put(struct drm_crtc *crtc)

    give up ownership of vblank events

    :param struct drm_crtc \*crtc:
        which counter to give up

.. _`drm_crtc_vblank_put.description`:

Description
-----------

Release ownership of a given vblank counter, turning off interrupts
if possible. Disable interrupts after drm_vblank_offdelay milliseconds.

.. _`drm_wait_one_vblank`:

drm_wait_one_vblank
===================

.. c:function:: void drm_wait_one_vblank(struct drm_device *dev, unsigned int pipe)

    wait for one vblank

    :param struct drm_device \*dev:
        DRM device

    :param unsigned int pipe:
        CRTC index

.. _`drm_wait_one_vblank.description`:

Description
-----------

This waits for one vblank to pass on \ ``pipe``\ , using the irq driver interfaces.
It is a failure to call this when the vblank irq for \ ``pipe``\  is disabled, e.g.
due to lack of driver support or because the crtc is off.

This is the legacy version of \ :c:func:`drm_crtc_wait_one_vblank`\ .

.. _`drm_crtc_wait_one_vblank`:

drm_crtc_wait_one_vblank
========================

.. c:function:: void drm_crtc_wait_one_vblank(struct drm_crtc *crtc)

    wait for one vblank

    :param struct drm_crtc \*crtc:
        DRM crtc

.. _`drm_crtc_wait_one_vblank.description`:

Description
-----------

This waits for one vblank to pass on \ ``crtc``\ , using the irq driver interfaces.
It is a failure to call this when the vblank irq for \ ``crtc``\  is disabled, e.g.
due to lack of driver support or because the crtc is off.

.. _`drm_crtc_vblank_off`:

drm_crtc_vblank_off
===================

.. c:function:: void drm_crtc_vblank_off(struct drm_crtc *crtc)

    disable vblank events on a CRTC

    :param struct drm_crtc \*crtc:
        CRTC in question

.. _`drm_crtc_vblank_off.description`:

Description
-----------

Drivers can use this function to shut down the vblank interrupt handling when
disabling a crtc. This function ensures that the latest vblank frame count is
stored so that drm_vblank_on can restore it again.

Drivers must use this function when the hardware vblank counter can get
reset, e.g. when suspending or disabling the \ ``crtc``\  in general.

.. _`drm_crtc_vblank_reset`:

drm_crtc_vblank_reset
=====================

.. c:function:: void drm_crtc_vblank_reset(struct drm_crtc *crtc)

    reset vblank state to off on a CRTC

    :param struct drm_crtc \*crtc:
        CRTC in question

.. _`drm_crtc_vblank_reset.description`:

Description
-----------

Drivers can use this function to reset the vblank state to off at load time.
Drivers should use this together with the \ :c:func:`drm_crtc_vblank_off`\  and
\ :c:func:`drm_crtc_vblank_on`\  functions. The difference compared to
\ :c:func:`drm_crtc_vblank_off`\  is that this function doesn't save the vblank counter
and hence doesn't need to call any driver hooks.

This is useful for recovering driver state e.g. on driver load, or on resume.

.. _`drm_crtc_vblank_on`:

drm_crtc_vblank_on
==================

.. c:function:: void drm_crtc_vblank_on(struct drm_crtc *crtc)

    enable vblank events on a CRTC

    :param struct drm_crtc \*crtc:
        CRTC in question

.. _`drm_crtc_vblank_on.description`:

Description
-----------

This functions restores the vblank interrupt state captured with
\ :c:func:`drm_crtc_vblank_off`\  again and is generally called when enabling \ ``crtc``\ . Note
that calls to \ :c:func:`drm_crtc_vblank_on`\  and \ :c:func:`drm_crtc_vblank_off`\  can be
unbalanced and so can also be unconditionally called in driver load code to
reflect the current hardware state of the crtc.

.. _`drm_vblank_restore`:

drm_vblank_restore
==================

.. c:function:: void drm_vblank_restore(struct drm_device *dev, unsigned int pipe)

    estimate missed vblanks and update vblank count.

    :param struct drm_device \*dev:
        DRM device

    :param unsigned int pipe:
        CRTC index

.. _`drm_vblank_restore.description`:

Description
-----------

Power manamement features can cause frame counter resets between vblank
disable and enable. Drivers can use this function in their
\ :c:type:`drm_crtc_funcs.enable_vblank <drm_crtc_funcs>`\  implementation to estimate missed vblanks since
the last \ :c:type:`drm_crtc_funcs.disable_vblank <drm_crtc_funcs>`\  using timestamps and update the
vblank counter.

This function is the legacy version of \ :c:func:`drm_crtc_vblank_restore`\ .

.. _`drm_crtc_vblank_restore`:

drm_crtc_vblank_restore
=======================

.. c:function:: void drm_crtc_vblank_restore(struct drm_crtc *crtc)

    estimate missed vblanks and update vblank count.

    :param struct drm_crtc \*crtc:
        CRTC in question

.. _`drm_crtc_vblank_restore.description`:

Description
-----------

Power manamement features can cause frame counter resets between vblank
disable and enable. Drivers can use this function in their
\ :c:type:`drm_crtc_funcs.enable_vblank <drm_crtc_funcs>`\  implementation to estimate missed vblanks since
the last \ :c:type:`drm_crtc_funcs.disable_vblank <drm_crtc_funcs>`\  using timestamps and update the
vblank counter.

.. _`drm_handle_vblank`:

drm_handle_vblank
=================

.. c:function:: bool drm_handle_vblank(struct drm_device *dev, unsigned int pipe)

    handle a vblank event

    :param struct drm_device \*dev:
        DRM device

    :param unsigned int pipe:
        index of CRTC where this event occurred

.. _`drm_handle_vblank.description`:

Description
-----------

Drivers should call this routine in their vblank interrupt handlers to
update the vblank counter and send any signals that may be pending.

This is the legacy version of \ :c:func:`drm_crtc_handle_vblank`\ .

.. _`drm_crtc_handle_vblank`:

drm_crtc_handle_vblank
======================

.. c:function:: bool drm_crtc_handle_vblank(struct drm_crtc *crtc)

    handle a vblank event

    :param struct drm_crtc \*crtc:
        where this event occurred

.. _`drm_crtc_handle_vblank.description`:

Description
-----------

Drivers should call this routine in their vblank interrupt handlers to
update the vblank counter and send any signals that may be pending.

This is the native KMS version of \ :c:func:`drm_handle_vblank`\ .

.. _`drm_crtc_handle_vblank.return`:

Return
------

True if the event was successfully handled, false on failure.

.. This file was automatic generated / don't edit.

