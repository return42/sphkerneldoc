.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/power/main.c

.. _`device_pm_sleep_init`:

device_pm_sleep_init
====================

.. c:function:: void device_pm_sleep_init(struct device *dev)

    Initialize system suspend-related device fields.

    :param dev:
        Device object being initialized.
    :type dev: struct device \*

.. _`device_pm_lock`:

device_pm_lock
==============

.. c:function:: void device_pm_lock( void)

    Lock the list of active devices used by the PM core.

    :param void:
        no arguments
    :type void: 

.. _`device_pm_unlock`:

device_pm_unlock
================

.. c:function:: void device_pm_unlock( void)

    Unlock the list of active devices used by the PM core.

    :param void:
        no arguments
    :type void: 

.. _`device_pm_add`:

device_pm_add
=============

.. c:function:: void device_pm_add(struct device *dev)

    Add a device to the PM core's list of active devices.

    :param dev:
        Device to add to the list.
    :type dev: struct device \*

.. _`device_pm_remove`:

device_pm_remove
================

.. c:function:: void device_pm_remove(struct device *dev)

    Remove a device from the PM core's list of active devices.

    :param dev:
        Device to be removed from the list.
    :type dev: struct device \*

.. _`device_pm_move_before`:

device_pm_move_before
=====================

.. c:function:: void device_pm_move_before(struct device *deva, struct device *devb)

    Move device in the PM core's list of active devices.

    :param deva:
        Device to move in dpm_list.
    :type deva: struct device \*

    :param devb:
        Device \ ``deva``\  should come before.
    :type devb: struct device \*

.. _`device_pm_move_after`:

device_pm_move_after
====================

.. c:function:: void device_pm_move_after(struct device *deva, struct device *devb)

    Move device in the PM core's list of active devices.

    :param deva:
        Device to move in dpm_list.
    :type deva: struct device \*

    :param devb:
        Device \ ``deva``\  should come after.
    :type devb: struct device \*

.. _`device_pm_move_last`:

device_pm_move_last
===================

.. c:function:: void device_pm_move_last(struct device *dev)

    Move device to end of the PM core's list of devices.

    :param dev:
        Device to move in dpm_list.
    :type dev: struct device \*

.. _`dpm_wait`:

dpm_wait
========

.. c:function:: void dpm_wait(struct device *dev, bool async)

    Wait for a PM operation to complete.

    :param dev:
        Device to wait for.
    :type dev: struct device \*

    :param async:
        If unset, wait only if the device's power.async_suspend flag is set.
    :type async: bool

.. _`pm_op`:

pm_op
=====

.. c:function:: pm_callback_t pm_op(const struct dev_pm_ops *ops, pm_message_t state)

    Return the PM operation appropriate for given PM event.

    :param ops:
        PM operations to choose from.
    :type ops: const struct dev_pm_ops \*

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

.. _`pm_late_early_op`:

pm_late_early_op
================

.. c:function:: pm_callback_t pm_late_early_op(const struct dev_pm_ops *ops, pm_message_t state)

    Return the PM operation appropriate for given PM event.

    :param ops:
        PM operations to choose from.
    :type ops: const struct dev_pm_ops \*

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

.. _`pm_late_early_op.description`:

Description
-----------

Runtime PM is disabled for \ ``dev``\  while this function is being executed.

.. _`pm_noirq_op`:

pm_noirq_op
===========

.. c:function:: pm_callback_t pm_noirq_op(const struct dev_pm_ops *ops, pm_message_t state)

    Return the PM operation appropriate for given PM event.

    :param ops:
        PM operations to choose from.
    :type ops: const struct dev_pm_ops \*

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

.. _`pm_noirq_op.description`:

Description
-----------

The driver of \ ``dev``\  will not receive interrupts while this function is being
executed.

.. _`dpm_watchdog_handler`:

dpm_watchdog_handler
====================

.. c:function:: void dpm_watchdog_handler(struct timer_list *t)

    Driver suspend / resume watchdog handler.

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`dpm_watchdog_handler.description`:

Description
-----------

Called when a driver has timed out suspending or resuming.
There's not much we can do here to recover so \ :c:func:`panic`\  to
capture a crash-dump in pstore.

.. _`dpm_watchdog_set`:

dpm_watchdog_set
================

.. c:function:: void dpm_watchdog_set(struct dpm_watchdog *wd, struct device *dev)

    Enable pm watchdog for given device.

    :param wd:
        Watchdog. Must be allocated on the stack.
    :type wd: struct dpm_watchdog \*

    :param dev:
        Device to handle.
    :type dev: struct device \*

.. _`dpm_watchdog_clear`:

dpm_watchdog_clear
==================

.. c:function:: void dpm_watchdog_clear(struct dpm_watchdog *wd)

    Disable suspend/resume watchdog.

    :param wd:
        Watchdog to disable.
    :type wd: struct dpm_watchdog \*

.. _`dev_pm_skip_next_resume_phases`:

dev_pm_skip_next_resume_phases
==============================

.. c:function:: void dev_pm_skip_next_resume_phases(struct device *dev)

    Skip next system resume phases for device.

    :param dev:
        Target device.
    :type dev: struct device \*

.. _`dev_pm_skip_next_resume_phases.description`:

Description
-----------

Make the core skip the "early resume" and "resume" phases for \ ``dev``\ .

This function can be called by middle-layer code during the "noirq" phase of
system resume if necessary, but not by device drivers.

.. _`suspend_event`:

suspend_event
=============

.. c:function:: pm_message_t suspend_event(pm_message_t resume_msg)

    Return a "suspend" message for given "resume" one.

    :param resume_msg:
        PM message representing a system-wide resume transition.
    :type resume_msg: pm_message_t

.. _`dev_pm_may_skip_resume`:

dev_pm_may_skip_resume
======================

.. c:function:: bool dev_pm_may_skip_resume(struct device *dev)

    System-wide device resume optimization check.

    :param dev:
        Target device.
    :type dev: struct device \*

.. _`dev_pm_may_skip_resume.description`:

Description
-----------

Checks whether or not the device may be left in suspend after a system-wide
transition to the working state.

.. _`device_resume_noirq`:

device_resume_noirq
===================

.. c:function:: int device_resume_noirq(struct device *dev, pm_message_t state, bool async)

    Execute a "noirq resume" callback for given device.

    :param dev:
        Device to handle.
    :type dev: struct device \*

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

    :param async:
        If true, the device is being resumed asynchronously.
    :type async: bool

.. _`device_resume_noirq.description`:

Description
-----------

The driver of \ ``dev``\  will not receive interrupts while this function is being
executed.

.. _`dpm_resume_noirq`:

dpm_resume_noirq
================

.. c:function:: void dpm_resume_noirq(pm_message_t state)

    Execute "noirq resume" callbacks for all devices.

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

.. _`dpm_resume_noirq.description`:

Description
-----------

Invoke the "noirq" resume callbacks for all devices in dpm_noirq_list and
allow device drivers' interrupt handlers to be called.

.. _`device_resume_early`:

device_resume_early
===================

.. c:function:: int device_resume_early(struct device *dev, pm_message_t state, bool async)

    Execute an "early resume" callback for given device.

    :param dev:
        Device to handle.
    :type dev: struct device \*

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

    :param async:
        If true, the device is being resumed asynchronously.
    :type async: bool

.. _`device_resume_early.description`:

Description
-----------

Runtime PM is disabled for \ ``dev``\  while this function is being executed.

.. _`dpm_resume_early`:

dpm_resume_early
================

.. c:function:: void dpm_resume_early(pm_message_t state)

    Execute "early resume" callbacks for all devices.

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

.. _`dpm_resume_start`:

dpm_resume_start
================

.. c:function:: void dpm_resume_start(pm_message_t state)

    Execute "noirq" and "early" device callbacks.

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

.. _`device_resume`:

device_resume
=============

.. c:function:: int device_resume(struct device *dev, pm_message_t state, bool async)

    Execute "resume" callbacks for given device.

    :param dev:
        Device to handle.
    :type dev: struct device \*

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

    :param async:
        If true, the device is being resumed asynchronously.
    :type async: bool

.. _`dpm_resume`:

dpm_resume
==========

.. c:function:: void dpm_resume(pm_message_t state)

    Execute "resume" callbacks for non-sysdev devices.

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

.. _`dpm_resume.description`:

Description
-----------

Execute the appropriate "resume" callback for all devices whose status
indicates that they are suspended.

.. _`device_complete`:

device_complete
===============

.. c:function:: void device_complete(struct device *dev, pm_message_t state)

    Complete a PM transition for given device.

    :param dev:
        Device to handle.
    :type dev: struct device \*

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

.. _`dpm_complete`:

dpm_complete
============

.. c:function:: void dpm_complete(pm_message_t state)

    Complete a PM transition for all non-sysdev devices.

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

.. _`dpm_complete.description`:

Description
-----------

Execute the ->complete() callbacks for all devices whose PM status is not
DPM_ON (this allows new devices to be registered).

.. _`dpm_resume_end`:

dpm_resume_end
==============

.. c:function:: void dpm_resume_end(pm_message_t state)

    Execute "resume" callbacks and complete system transition.

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

.. _`dpm_resume_end.description`:

Description
-----------

Execute "resume" callbacks for all devices and complete the PM transition of
the system.

.. _`resume_event`:

resume_event
============

.. c:function:: pm_message_t resume_event(pm_message_t sleep_state)

    Return a "resume" message for given "suspend" sleep state.

    :param sleep_state:
        PM message representing a sleep state.
    :type sleep_state: pm_message_t

.. _`resume_event.description`:

Description
-----------

Return a PM message representing the resume event corresponding to given
sleep state.

.. _`__device_suspend_noirq`:

\__device_suspend_noirq
=======================

.. c:function:: int __device_suspend_noirq(struct device *dev, pm_message_t state, bool async)

    Execute a "noirq suspend" callback for given device.

    :param dev:
        Device to handle.
    :type dev: struct device \*

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

    :param async:
        If true, the device is being suspended asynchronously.
    :type async: bool

.. _`__device_suspend_noirq.description`:

Description
-----------

The driver of \ ``dev``\  will not receive interrupts while this function is being
executed.

.. _`dpm_suspend_noirq`:

dpm_suspend_noirq
=================

.. c:function:: int dpm_suspend_noirq(pm_message_t state)

    Execute "noirq suspend" callbacks for all devices.

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

.. _`dpm_suspend_noirq.description`:

Description
-----------

Prevent device drivers' interrupt handlers from being called and invoke
"noirq" suspend callbacks for all non-sysdev devices.

.. _`__device_suspend_late`:

\__device_suspend_late
======================

.. c:function:: int __device_suspend_late(struct device *dev, pm_message_t state, bool async)

    Execute a "late suspend" callback for given device.

    :param dev:
        Device to handle.
    :type dev: struct device \*

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

    :param async:
        If true, the device is being suspended asynchronously.
    :type async: bool

.. _`__device_suspend_late.description`:

Description
-----------

Runtime PM is disabled for \ ``dev``\  while this function is being executed.

.. _`dpm_suspend_late`:

dpm_suspend_late
================

.. c:function:: int dpm_suspend_late(pm_message_t state)

    Execute "late suspend" callbacks for all devices.

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

.. _`dpm_suspend_end`:

dpm_suspend_end
===============

.. c:function:: int dpm_suspend_end(pm_message_t state)

    Execute "late" and "noirq" device suspend callbacks.

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

.. _`legacy_suspend`:

legacy_suspend
==============

.. c:function:: int legacy_suspend(struct device *dev, pm_message_t state, int (*cb)(struct device *dev, pm_message_t state), const char *info)

    Execute a legacy (bus or class) suspend callback for device.

    :param dev:
        Device to suspend.
    :type dev: struct device \*

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

    :param int (\*cb)(struct device \*dev, pm_message_t state):
        Suspend callback to execute.

    :param info:
        string description of caller.
    :type info: const char \*

.. _`__device_suspend`:

\__device_suspend
=================

.. c:function:: int __device_suspend(struct device *dev, pm_message_t state, bool async)

    Execute "suspend" callbacks for given device.

    :param dev:
        Device to handle.
    :type dev: struct device \*

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

    :param async:
        If true, the device is being suspended asynchronously.
    :type async: bool

.. _`dpm_suspend`:

dpm_suspend
===========

.. c:function:: int dpm_suspend(pm_message_t state)

    Execute "suspend" callbacks for all non-sysdev devices.

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

.. _`device_prepare`:

device_prepare
==============

.. c:function:: int device_prepare(struct device *dev, pm_message_t state)

    Prepare a device for system power transition.

    :param dev:
        Device to handle.
    :type dev: struct device \*

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

.. _`device_prepare.description`:

Description
-----------

Execute the ->prepare() callback(s) for given device.  No new children of the
device may be registered after this function has returned.

.. _`dpm_prepare`:

dpm_prepare
===========

.. c:function:: int dpm_prepare(pm_message_t state)

    Prepare all non-sysdev devices for a system PM transition.

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

.. _`dpm_prepare.description`:

Description
-----------

Execute the ->prepare() callback(s) for all devices.

.. _`dpm_suspend_start`:

dpm_suspend_start
=================

.. c:function:: int dpm_suspend_start(pm_message_t state)

    Prepare devices for PM transition and suspend them.

    :param state:
        PM transition of the system being carried out.
    :type state: pm_message_t

.. _`dpm_suspend_start.description`:

Description
-----------

Prepare all non-sysdev devices for system PM transition and execute "suspend"
callbacks for them.

.. _`device_pm_wait_for_dev`:

device_pm_wait_for_dev
======================

.. c:function:: int device_pm_wait_for_dev(struct device *subordinate, struct device *dev)

    Wait for suspend/resume of a device to complete.

    :param subordinate:
        Device that needs to wait for \ ``dev``\ .
    :type subordinate: struct device \*

    :param dev:
        Device to wait for.
    :type dev: struct device \*

.. _`dpm_for_each_dev`:

dpm_for_each_dev
================

.. c:function:: void dpm_for_each_dev(void *data, void (*fn)(struct device *, void *))

    device iterator.

    :param data:
        data for the callback.
    :type data: void \*

    :param void (\*fn)(struct device \*, void \*):
        function to be called for each device.

.. _`dpm_for_each_dev.description`:

Description
-----------

Iterate over devices in dpm_list, and call \ ``fn``\  for each device,
passing it \ ``data``\ .

.. This file was automatic generated / don't edit.

