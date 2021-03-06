.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/power/runtime.c

.. _`update_pm_runtime_accounting`:

update_pm_runtime_accounting
============================

.. c:function:: void update_pm_runtime_accounting(struct device *dev)

    Update the time accounting of power states

    :param dev:
        Device to update the accounting for
    :type dev: struct device \*

.. _`update_pm_runtime_accounting.description`:

Description
-----------

In order to be able to have time accounting of the various power states
(as used by programs such as PowerTOP to show the effectiveness of runtime
PM), we need to track the time spent in each state.
update_pm_runtime_accounting must be called each time before the
runtime_status field is updated, to account the time in the old state
correctly.

.. _`pm_runtime_deactivate_timer`:

pm_runtime_deactivate_timer
===========================

.. c:function:: void pm_runtime_deactivate_timer(struct device *dev)

    Deactivate given device's suspend timer.

    :param dev:
        Device to handle.
    :type dev: struct device \*

.. _`pm_runtime_cancel_pending`:

pm_runtime_cancel_pending
=========================

.. c:function:: void pm_runtime_cancel_pending(struct device *dev)

    Deactivate suspend timer and cancel requests.

    :param dev:
        Device to handle.
    :type dev: struct device \*

.. _`rpm_check_suspend_allowed`:

rpm_check_suspend_allowed
=========================

.. c:function:: int rpm_check_suspend_allowed(struct device *dev)

    Test whether a device may be suspended.

    :param dev:
        Device to test.
    :type dev: struct device \*

.. _`__rpm_callback`:

\__rpm_callback
===============

.. c:function:: int __rpm_callback(int (*cb)(struct device *), struct device *dev) __releases(&dev->power.lock) __acquires&dev->power.lock)

    Run a given runtime PM callback for a given device.

    :param int (\*cb)(struct device \*):
        Runtime PM callback to run.

.. _`rpm_idle`:

rpm_idle
========

.. c:function:: int rpm_idle(struct device *dev, int rpmflags)

    Notify device bus type if the device can be suspended.

    :param dev:
        Device to notify the bus type about.
    :type dev: struct device \*

    :param rpmflags:
        Flag bits.
    :type rpmflags: int

.. _`rpm_idle.description`:

Description
-----------

Check if the device's runtime PM status allows it to be suspended.  If
another idle notification has been started earlier, return immediately.  If
the RPM_ASYNC flag is set then queue an idle-notification request; otherwise
run the ->runtime_idle() callback directly. If the ->runtime_idle callback
doesn't exist or if it returns 0, call rpm_suspend with the RPM_AUTO flag.

This function must be called under dev->power.lock with interrupts disabled.

.. _`rpm_callback`:

rpm_callback
============

.. c:function:: int rpm_callback(int (*cb)(struct device *), struct device *dev)

    Run a given runtime PM callback for a given device.

    :param int (\*cb)(struct device \*):
        Runtime PM callback to run.

    :param dev:
        Device to run the callback for.
    :type dev: struct device \*

.. _`rpm_suspend`:

rpm_suspend
===========

.. c:function:: int rpm_suspend(struct device *dev, int rpmflags)

    Carry out runtime suspend of given device.

    :param dev:
        Device to suspend.
    :type dev: struct device \*

    :param rpmflags:
        Flag bits.
    :type rpmflags: int

.. _`rpm_suspend.description`:

Description
-----------

Check if the device's runtime PM status allows it to be suspended.
Cancel a pending idle notification, autosuspend or suspend. If
another suspend has been started earlier, either return immediately
or wait for it to finish, depending on the RPM_NOWAIT and RPM_ASYNC
flags. If the RPM_ASYNC flag is set then queue a suspend request;
otherwise run the ->runtime_suspend() callback directly. When
->runtime_suspend succeeded, if a deferred resume was requested while
the callback was running then carry it out, otherwise send an idle
notification for its parent (if the suspend succeeded and both
ignore_children of parent->power and irq_safe of dev->power are not set).
If ->runtime_suspend failed with -EAGAIN or -EBUSY, and if the RPM_AUTO
flag is set and the next autosuspend-delay expiration time is in the
future, schedule another autosuspend attempt.

This function must be called under dev->power.lock with interrupts disabled.

.. _`rpm_resume`:

rpm_resume
==========

.. c:function:: int rpm_resume(struct device *dev, int rpmflags)

    Carry out runtime resume of given device.

    :param dev:
        Device to resume.
    :type dev: struct device \*

    :param rpmflags:
        Flag bits.
    :type rpmflags: int

.. _`rpm_resume.description`:

Description
-----------

Check if the device's runtime PM status allows it to be resumed.  Cancel
any scheduled or pending requests.  If another resume has been started
earlier, either return immediately or wait for it to finish, depending on the
RPM_NOWAIT and RPM_ASYNC flags.  Similarly, if there's a suspend running in
parallel with this function, either tell the other process to resume after
suspending (deferred_resume) or wait for it to finish.  If the RPM_ASYNC
flag is set then queue a resume request; otherwise run the
->runtime_resume() callback directly.  Queue an idle notification for the
device if the resume succeeded.

This function must be called under dev->power.lock with interrupts disabled.

.. _`pm_runtime_work`:

pm_runtime_work
===============

.. c:function:: void pm_runtime_work(struct work_struct *work)

    Universal runtime PM work function.

    :param work:
        Work structure used for scheduling the execution of this function.
    :type work: struct work_struct \*

.. _`pm_runtime_work.description`:

Description
-----------

Use \ ``work``\  to get the device object the work is to be done for, determine what
is to be done and execute the appropriate runtime PM function.

.. _`pm_suspend_timer_fn`:

pm_suspend_timer_fn
===================

.. c:function:: void pm_suspend_timer_fn(struct timer_list *t)

    Timer function for \ :c:func:`pm_schedule_suspend`\ .

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`pm_suspend_timer_fn.description`:

Description
-----------

Check if the time is right and queue a suspend request.

.. _`pm_schedule_suspend`:

pm_schedule_suspend
===================

.. c:function:: int pm_schedule_suspend(struct device *dev, unsigned int delay)

    Set up a timer to submit a suspend request in future.

    :param dev:
        Device to suspend.
    :type dev: struct device \*

    :param delay:
        Time to wait before submitting a suspend request, in milliseconds.
    :type delay: unsigned int

.. _`__pm_runtime_idle`:

\__pm_runtime_idle
==================

.. c:function:: int __pm_runtime_idle(struct device *dev, int rpmflags)

    Entry point for runtime idle operations.

    :param dev:
        Device to send idle notification for.
    :type dev: struct device \*

    :param rpmflags:
        Flag bits.
    :type rpmflags: int

.. _`__pm_runtime_idle.description`:

Description
-----------

If the RPM_GET_PUT flag is set, decrement the device's usage count and
return immediately if it is larger than zero.  Then carry out an idle
notification, either synchronous or asynchronous.

This routine may be called in atomic context if the RPM_ASYNC flag is set,
or if \ :c:func:`pm_runtime_irq_safe`\  has been called.

.. _`__pm_runtime_suspend`:

\__pm_runtime_suspend
=====================

.. c:function:: int __pm_runtime_suspend(struct device *dev, int rpmflags)

    Entry point for runtime put/suspend operations.

    :param dev:
        Device to suspend.
    :type dev: struct device \*

    :param rpmflags:
        Flag bits.
    :type rpmflags: int

.. _`__pm_runtime_suspend.description`:

Description
-----------

If the RPM_GET_PUT flag is set, decrement the device's usage count and
return immediately if it is larger than zero.  Then carry out a suspend,
either synchronous or asynchronous.

This routine may be called in atomic context if the RPM_ASYNC flag is set,
or if \ :c:func:`pm_runtime_irq_safe`\  has been called.

.. _`__pm_runtime_resume`:

\__pm_runtime_resume
====================

.. c:function:: int __pm_runtime_resume(struct device *dev, int rpmflags)

    Entry point for runtime resume operations.

    :param dev:
        Device to resume.
    :type dev: struct device \*

    :param rpmflags:
        Flag bits.
    :type rpmflags: int

.. _`__pm_runtime_resume.description`:

Description
-----------

If the RPM_GET_PUT flag is set, increment the device's usage count.  Then
carry out a resume, either synchronous or asynchronous.

This routine may be called in atomic context if the RPM_ASYNC flag is set,
or if \ :c:func:`pm_runtime_irq_safe`\  has been called.

.. _`pm_runtime_get_if_in_use`:

pm_runtime_get_if_in_use
========================

.. c:function:: int pm_runtime_get_if_in_use(struct device *dev)

    Conditionally bump up the device's usage counter.

    :param dev:
        Device to handle.
    :type dev: struct device \*

.. _`pm_runtime_get_if_in_use.description`:

Description
-----------

Return -EINVAL if runtime PM is disabled for the device.

If that's not the case and if the device's runtime PM status is RPM_ACTIVE
and the runtime PM usage counter is nonzero, increment the counter and
return 1.  Otherwise return 0 without changing the counter.

.. _`__pm_runtime_set_status`:

\__pm_runtime_set_status
========================

.. c:function:: int __pm_runtime_set_status(struct device *dev, unsigned int status)

    Set runtime PM status of a device.

    :param dev:
        Device to handle.
    :type dev: struct device \*

    :param status:
        New runtime PM status of the device.
    :type status: unsigned int

.. _`__pm_runtime_set_status.description`:

Description
-----------

If runtime PM of the device is disabled or its power.runtime_error field is
different from zero, the status may be changed either to RPM_ACTIVE, or to
RPM_SUSPENDED, as long as that reflects the actual state of the device.
However, if the device has a parent and the parent is not active, and the
parent's power.ignore_children flag is unset, the device's status cannot be
set to RPM_ACTIVE, so -EBUSY is returned in that case.

If successful, \__pm_runtime_set_status() clears the power.runtime_error field
and the device parent's counter of unsuspended children is modified to
reflect the new status.  If the new status is RPM_SUSPENDED, an idle
notification request for the parent is submitted.

.. _`__pm_runtime_barrier`:

\__pm_runtime_barrier
=====================

.. c:function:: void __pm_runtime_barrier(struct device *dev)

    Cancel pending requests and wait for completions.

    :param dev:
        Device to handle.
    :type dev: struct device \*

.. _`__pm_runtime_barrier.description`:

Description
-----------

Flush all pending requests for the device from pm_wq and wait for all
runtime PM operations involving the device in progress to complete.

Should be called under dev->power.lock with interrupts disabled.

.. _`pm_runtime_barrier`:

pm_runtime_barrier
==================

.. c:function:: int pm_runtime_barrier(struct device *dev)

    Flush pending requests and wait for completions.

    :param dev:
        Device to handle.
    :type dev: struct device \*

.. _`pm_runtime_barrier.description`:

Description
-----------

Prevent the device from being suspended by incrementing its usage counter and
if there's a pending resume request for the device, wake the device up.
Next, make sure that all pending requests for the device have been flushed
from pm_wq and wait for all runtime PM operations involving the device in
progress to complete.

.. _`pm_runtime_barrier.return-value`:

Return value
------------

1, if there was a resume request pending and the device had to be woken up,
0, otherwise

.. _`__pm_runtime_disable`:

\__pm_runtime_disable
=====================

.. c:function:: void __pm_runtime_disable(struct device *dev, bool check_resume)

    Disable runtime PM of a device.

    :param dev:
        Device to handle.
    :type dev: struct device \*

    :param check_resume:
        If set, check if there's a resume request for the device.
    :type check_resume: bool

.. _`__pm_runtime_disable.description`:

Description
-----------

Increment power.disable_depth for the device and if it was zero previously,
cancel all pending runtime PM requests for the device and wait for all
operations in progress to complete.  The device can be either active or
suspended after its runtime PM has been disabled.

If \ ``check_resume``\  is set and there's a resume request pending when
\__pm_runtime_disable() is called and power.disable_depth is zero, the
function will wake up the device before disabling its runtime PM.

.. _`pm_runtime_enable`:

pm_runtime_enable
=================

.. c:function:: void pm_runtime_enable(struct device *dev)

    Enable runtime PM of a device.

    :param dev:
        Device to handle.
    :type dev: struct device \*

.. _`pm_runtime_forbid`:

pm_runtime_forbid
=================

.. c:function:: void pm_runtime_forbid(struct device *dev)

    Block runtime PM of a device.

    :param dev:
        Device to handle.
    :type dev: struct device \*

.. _`pm_runtime_forbid.description`:

Description
-----------

Increase the device's usage count and clear its power.runtime_auto flag,
so that it cannot be suspended at run time until \ :c:func:`pm_runtime_allow`\  is called
for it.

.. _`pm_runtime_allow`:

pm_runtime_allow
================

.. c:function:: void pm_runtime_allow(struct device *dev)

    Unblock runtime PM of a device.

    :param dev:
        Device to handle.
    :type dev: struct device \*

.. _`pm_runtime_allow.description`:

Description
-----------

Decrease the device's usage count and set its power.runtime_auto flag.

.. _`pm_runtime_no_callbacks`:

pm_runtime_no_callbacks
=======================

.. c:function:: void pm_runtime_no_callbacks(struct device *dev)

    Ignore runtime PM callbacks for a device.

    :param dev:
        Device to handle.
    :type dev: struct device \*

.. _`pm_runtime_no_callbacks.description`:

Description
-----------

Set the power.no_callbacks flag, which tells the PM core that this
device is power-managed through its parent and has no runtime PM
callbacks of its own.  The runtime sysfs attributes will be removed.

.. _`pm_runtime_irq_safe`:

pm_runtime_irq_safe
===================

.. c:function:: void pm_runtime_irq_safe(struct device *dev)

    Leave interrupts disabled during callbacks.

    :param dev:
        Device to handle
    :type dev: struct device \*

.. _`pm_runtime_irq_safe.description`:

Description
-----------

Set the power.irq_safe flag, which tells the PM core that the
->runtime_suspend() and ->runtime_resume() callbacks for this device should
always be invoked with the spinlock held and interrupts disabled.  It also
causes the parent's usage counter to be permanently incremented, preventing
the parent from runtime suspending -- otherwise an irq-safe child might have
to wait for a non-irq-safe parent.

.. _`update_autosuspend`:

update_autosuspend
==================

.. c:function:: void update_autosuspend(struct device *dev, int old_delay, int old_use)

    Handle a change to a device's autosuspend settings.

    :param dev:
        Device to handle.
    :type dev: struct device \*

    :param old_delay:
        The former autosuspend_delay value.
    :type old_delay: int

    :param old_use:
        The former use_autosuspend value.
    :type old_use: int

.. _`update_autosuspend.description`:

Description
-----------

Prevent runtime suspend if the new delay is negative and use_autosuspend is
set; otherwise allow it.  Send an idle notification if suspends are allowed.

This function must be called under dev->power.lock with interrupts disabled.

.. _`pm_runtime_set_autosuspend_delay`:

pm_runtime_set_autosuspend_delay
================================

.. c:function:: void pm_runtime_set_autosuspend_delay(struct device *dev, int delay)

    Set a device's autosuspend_delay value.

    :param dev:
        Device to handle.
    :type dev: struct device \*

    :param delay:
        Value of the new delay in milliseconds.
    :type delay: int

.. _`pm_runtime_set_autosuspend_delay.description`:

Description
-----------

Set the device's power.autosuspend_delay value.  If it changes to negative
and the power.use_autosuspend flag is set, prevent runtime suspends.  If it
changes the other way, allow runtime suspends.

.. _`__pm_runtime_use_autosuspend`:

\__pm_runtime_use_autosuspend
=============================

.. c:function:: void __pm_runtime_use_autosuspend(struct device *dev, bool use)

    Set a device's use_autosuspend flag.

    :param dev:
        Device to handle.
    :type dev: struct device \*

    :param use:
        New value for use_autosuspend.
    :type use: bool

.. _`__pm_runtime_use_autosuspend.description`:

Description
-----------

Set the device's power.use_autosuspend flag, and allow or prevent runtime
suspends as needed.

.. _`pm_runtime_init`:

pm_runtime_init
===============

.. c:function:: void pm_runtime_init(struct device *dev)

    Initialize runtime PM fields in given device object.

    :param dev:
        Device object to initialize.
    :type dev: struct device \*

.. _`pm_runtime_reinit`:

pm_runtime_reinit
=================

.. c:function:: void pm_runtime_reinit(struct device *dev)

    Re-initialize runtime PM fields in given device object.

    :param dev:
        Device object to re-initialize.
    :type dev: struct device \*

.. _`pm_runtime_remove`:

pm_runtime_remove
=================

.. c:function:: void pm_runtime_remove(struct device *dev)

    Prepare for removing a device from device hierarchy.

    :param dev:
        Device object being removed from device hierarchy.
    :type dev: struct device \*

.. _`pm_runtime_clean_up_links`:

pm_runtime_clean_up_links
=========================

.. c:function:: void pm_runtime_clean_up_links(struct device *dev)

    Prepare links to consumers for driver removal.

    :param dev:
        Device whose driver is going to be removed.
    :type dev: struct device \*

.. _`pm_runtime_clean_up_links.description`:

Description
-----------

Check links from this device to any consumers and if any of them have active
runtime PM references to the device, drop the usage counter of the device
(once per link).

Links with the DL_FLAG_STATELESS flag set are ignored.

Since the device is guaranteed to be runtime-active at the point this is
called, nothing else needs to be done here.

Moreover, this is called after \ :c:func:`device_links_busy`\  has returned 'false', so
the status of each link is guaranteed to be DL_STATE_SUPPLIER_UNBIND and
therefore rpm_active can't be manipulated concurrently.

.. _`pm_runtime_get_suppliers`:

pm_runtime_get_suppliers
========================

.. c:function:: void pm_runtime_get_suppliers(struct device *dev)

    Resume and reference-count supplier devices.

    :param dev:
        Consumer device.
    :type dev: struct device \*

.. _`pm_runtime_put_suppliers`:

pm_runtime_put_suppliers
========================

.. c:function:: void pm_runtime_put_suppliers(struct device *dev)

    Drop references to supplier devices.

    :param dev:
        Consumer device.
    :type dev: struct device \*

.. _`pm_runtime_force_suspend`:

pm_runtime_force_suspend
========================

.. c:function:: int pm_runtime_force_suspend(struct device *dev)

    Force a device into suspend state if needed.

    :param dev:
        Device to suspend.
    :type dev: struct device \*

.. _`pm_runtime_force_suspend.description`:

Description
-----------

Disable runtime PM so we safely can check the device's runtime PM status and
if it is active, invoke its ->runtime_suspend callback to suspend it and
change its runtime PM status field to RPM_SUSPENDED.  Also, if the device's
usage and children counters don't indicate that the device was in use before
the system-wide transition under way, decrement its parent's children counter
(if there is a parent).  Keep runtime PM disabled to preserve the state
unless we encounter errors.

Typically this function may be invoked from a system suspend callback to make
sure the device is put into low power state and it should only be used during
system-wide PM transitions to sleep states.  It assumes that the analogous
\ :c:func:`pm_runtime_force_resume`\  will be used to resume the device.

.. _`pm_runtime_force_resume`:

pm_runtime_force_resume
=======================

.. c:function:: int pm_runtime_force_resume(struct device *dev)

    Force a device into resume state if needed.

    :param dev:
        Device to resume.
    :type dev: struct device \*

.. _`pm_runtime_force_resume.description`:

Description
-----------

Prior invoking this function we expect the user to have brought the device
into low power state by a call to \ :c:func:`pm_runtime_force_suspend`\ . Here we reverse
those actions and bring the device into full power, if it is expected to be
used on system resume.  In the other case, we defer the resume to be managed
via runtime PM.

Typically this function may be invoked from a system resume callback.

.. This file was automatic generated / don't edit.

