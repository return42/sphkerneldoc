.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_irq.c

.. _`drm_accurate_vblank_count`:

drm_accurate_vblank_count
=========================

.. c:function:: u32 drm_accurate_vblank_count(struct drm_crtc *crtc)

    retrieve the master vblank counter

    :param struct drm_crtc \*crtc:
        which counter to retrieve

.. _`drm_accurate_vblank_count.description`:

Description
-----------

This function is similar to \ ``drm_crtc_vblank_count``\  but this
function interpolates to handle a race with vblank irq's.

This is mostly useful for hardware that can obtain the scanout
position, but doesn't have a frame counter.

.. _`drm_vblank_cleanup`:

drm_vblank_cleanup
==================

.. c:function:: void drm_vblank_cleanup(struct drm_device *dev)

    cleanup vblank support

    :param struct drm_device \*dev:
        DRM device

.. _`drm_vblank_cleanup.description`:

Description
-----------

This function cleans up any resources allocated in drm_vblank_init.

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

.. _`drm_vblank_init.return`:

Return
------

Zero on success or a negative error code on failure.

.. _`drm_irq_install`:

drm_irq_install
===============

.. c:function:: int drm_irq_install(struct drm_device *dev, int irq)

    install IRQ handler

    :param struct drm_device \*dev:
        DRM device

    :param int irq:
        IRQ number to install the handler for

.. _`drm_irq_install.description`:

Description
-----------

Initializes the IRQ related data. Installs the handler, calling the driver
\ :c:func:`irq_preinstall`\  and \ :c:func:`irq_postinstall`\  functions before and after the
installation.

This is the simplified helper interface provided for drivers with no special
needs. Drivers which need to install interrupt handlers for multiple
interrupts must instead set \ :c:type:`drm_device.irq_enabled <drm_device>`\  to signal the DRM core
that vblank interrupts are available.

.. _`drm_irq_install.return`:

Return
------

Zero on success or a negative error code on failure.

.. _`drm_irq_uninstall`:

drm_irq_uninstall
=================

.. c:function:: int drm_irq_uninstall(struct drm_device *dev)

    uninstall the IRQ handler

    :param struct drm_device \*dev:
        DRM device

.. _`drm_irq_uninstall.description`:

Description
-----------

Calls the driver's \ :c:func:`irq_uninstall`\  function and unregisters the IRQ handler.
This should only be called by drivers which used \ :c:func:`drm_irq_install`\  to set up
their interrupt handler. Other drivers must only reset
\ :c:type:`drm_device.irq_enabled <drm_device>`\  to false.

Note that for kernel modesetting drivers it is a bug if this function fails.
The sanity checks are only to catch buggy user modesetting drivers which call
the same function through an ioctl.

.. _`drm_irq_uninstall.return`:

Return
------

Zero on success or a negative error code on failure.

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

Calculate and store various constants which are later
needed by vblank and swap-completion timestamping, e.g,
by \ :c:func:`drm_calc_vbltimestamp_from_scanoutpos`\ . They are
derived from CRTC's true scanout timing, so they take
things like panel scaling or other adjustments into account.

.. _`drm_calc_vbltimestamp_from_scanoutpos`:

drm_calc_vbltimestamp_from_scanoutpos
=====================================

.. c:function:: int drm_calc_vbltimestamp_from_scanoutpos(struct drm_device *dev, unsigned int pipe, int *max_error, struct timeval *vblank_time, unsigned flags, const struct drm_display_mode *mode)

    precise vblank timestamp helper

    :param struct drm_device \*dev:
        DRM device

    :param unsigned int pipe:
        index of CRTC whose vblank timestamp to retrieve

    :param int \*max_error:
        Desired maximum allowable error in timestamps (nanosecs)
        On return contains true maximum error of timestamp

    :param struct timeval \*vblank_time:
        Pointer to struct timeval which should receive the timestamp

    :param unsigned flags:
        Flags to pass to driver:
        0 = Default,
        DRM_CALLED_FROM_VBLIRQ = If function is called from vbl IRQ handler

    :param const struct drm_display_mode \*mode:
        mode which defines the scanout timings

.. _`drm_calc_vbltimestamp_from_scanoutpos.description`:

Description
-----------

Implements calculation of exact vblank timestamps from given drm_display_mode
timings and current video scanout position of a CRTC. This can be called from
within \ :c:func:`get_vblank_timestamp`\  implementation of a kms driver to implement the
actual timestamping.

Should return timestamps conforming to the OML_sync_control OpenML
extension specification. The timestamp corresponds to the end of
the vblank interval, aka start of scanout of topmost-leftmost display
pixel in the following video frame.

Requires support for optional dev->driver->get_scanout_position()
in kms driver, plus a bit of setup code to provide a drm_display_mode
that corresponds to the true scanout timing.

The current implementation only handles standard video modes. It
returns as no operation if a doublescan or interlaced video mode is
active. Higher level code is expected to handle this.

.. _`drm_calc_vbltimestamp_from_scanoutpos.return`:

Return
------

Negative value on error, failure or if not supported in current

.. _`drm_calc_vbltimestamp_from_scanoutpos.video-mode`:

video mode
----------


-EINVAL    Invalid CRTC.
-EAGAIN    Temporary unavailable, e.g., called before initial modeset.
-ENOTSUPP  Function not supported in current display mode.
-EIO       Failed, e.g., due to failed scanout position query.

Returns or'ed positive status flags on success:

DRM_VBLANKTIME_SCANOUTPOS_METHOD - Signal this method used for timestamping.
DRM_VBLANKTIME_INVBL - Timestamp taken while scanout was in vblank interval.

.. _`drm_get_last_vbltimestamp`:

drm_get_last_vbltimestamp
=========================

.. c:function:: bool drm_get_last_vbltimestamp(struct drm_device *dev, unsigned int pipe, struct timeval *tvblank, unsigned flags)

    retrieve raw timestamp for the most recent vblank interval

    :param struct drm_device \*dev:
        DRM device

    :param unsigned int pipe:
        index of CRTC whose vblank timestamp to retrieve

    :param struct timeval \*tvblank:
        Pointer to target struct timeval which should receive the timestamp

    :param unsigned flags:
        Flags to pass to driver:
        0 = Default,
        DRM_CALLED_FROM_VBLIRQ = If function is called from vbl IRQ handler

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

.. c:function:: u32 drm_crtc_vblank_count(struct drm_crtc *crtc)

    retrieve "cooked" vblank counter value

    :param struct drm_crtc \*crtc:
        which counter to retrieve

.. _`drm_crtc_vblank_count.description`:

Description
-----------

Fetches the "cooked" vblank count value that represents the number of
vblank events since the system was booted, including lost events due to
modesetting activity.

.. _`drm_crtc_vblank_count.return`:

Return
------

The software vblank counter.

.. _`drm_vblank_count_and_time`:

drm_vblank_count_and_time
=========================

.. c:function:: u32 drm_vblank_count_and_time(struct drm_device *dev, unsigned int pipe, struct timeval *vblanktime)

    retrieve "cooked" vblank counter value and the system timestamp corresponding to that vblank counter value.

    :param struct drm_device \*dev:
        DRM device

    :param unsigned int pipe:
        index of CRTC whose counter to retrieve

    :param struct timeval \*vblanktime:
        Pointer to struct timeval to receive the vblank timestamp.

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

.. c:function:: u32 drm_crtc_vblank_count_and_time(struct drm_crtc *crtc, struct timeval *vblanktime)

    retrieve "cooked" vblank counter value and the system timestamp corresponding to that vblank counter value

    :param struct drm_crtc \*crtc:
        which counter to retrieve

    :param struct timeval \*vblanktime:
        Pointer to struct timeval to receive the vblank timestamp.

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
does **not** protect again the next vblank interrupt racing with either this
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

Caller must hold event lock. Caller must also hold a vblank reference for
the event \ ``e``\ , which will be dropped when the next vblank arrives.

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

.. _`drm_vblank_enable`:

drm_vblank_enable
=================

.. c:function:: int drm_vblank_enable(struct drm_device *dev, unsigned int pipe)

    enable the vblank interrupt on a CRTC

    :param struct drm_device \*dev:
        DRM device

    :param unsigned int pipe:
        CRTC index

.. _`drm_vblank_enable.return`:

Return
------

Zero on success or a negative error code on failure.

.. _`drm_vblank_get`:

drm_vblank_get
==============

.. c:function:: int drm_vblank_get(struct drm_device *dev, unsigned int pipe)

    get a reference count on vblank events

    :param struct drm_device \*dev:
        DRM device

    :param unsigned int pipe:
        index of CRTC to own

.. _`drm_vblank_get.description`:

Description
-----------

Acquire a reference count on vblank events to avoid having them disabled
while in use.

This is the legacy version of \ :c:func:`drm_crtc_vblank_get`\ .

.. _`drm_vblank_get.return`:

Return
------

Zero on success or a negative error code on failure.

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

.. _`drm_vblank_put`:

drm_vblank_put
==============

.. c:function:: void drm_vblank_put(struct drm_device *dev, unsigned int pipe)

    release ownership of vblank events

    :param struct drm_device \*dev:
        DRM device

    :param unsigned int pipe:
        index of CRTC to release

.. _`drm_vblank_put.description`:

Description
-----------

Release ownership of a given vblank counter, turning off interrupts
if possible. Disable interrupts after drm_vblank_offdelay milliseconds.

This is the legacy version of \ :c:func:`drm_crtc_vblank_put`\ .

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
reset, e.g. when suspending.

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
\ :c:func:`drm_crtc_vblank_off`\  again. Note that calls to \ :c:func:`drm_crtc_vblank_on`\  and
\ :c:func:`drm_crtc_vblank_off`\  can be unbalanced and so can also be unconditionally called
in driver load code to reflect the current hardware state of the crtc.

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

