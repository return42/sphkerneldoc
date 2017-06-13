.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/power/wakeup.c

.. _`wakeup_source_prepare`:

wakeup_source_prepare
=====================

.. c:function:: void wakeup_source_prepare(struct wakeup_source *ws, const char *name)

    Prepare a new wakeup source for initialization.

    :param struct wakeup_source \*ws:
        Wakeup source to prepare.

    :param const char \*name:
        Pointer to the name of the new wakeup source.

.. _`wakeup_source_prepare.description`:

Description
-----------

Callers must ensure that the \ ``name``\  string won't be freed when \ ``ws``\  is still in
use.

.. _`wakeup_source_create`:

wakeup_source_create
====================

.. c:function:: struct wakeup_source *wakeup_source_create(const char *name)

    Create a struct wakeup_source object.

    :param const char \*name:
        Name of the new wakeup source.

.. _`wakeup_source_drop`:

wakeup_source_drop
==================

.. c:function:: void wakeup_source_drop(struct wakeup_source *ws)

    Prepare a struct wakeup_source object for destruction.

    :param struct wakeup_source \*ws:
        Wakeup source to prepare for destruction.

.. _`wakeup_source_drop.description`:

Description
-----------

Callers must ensure that \__pm_stay_awake() or \__pm_wakeup_event() will never
be run in parallel with this function for the same wakeup source object.

.. _`wakeup_source_destroy`:

wakeup_source_destroy
=====================

.. c:function:: void wakeup_source_destroy(struct wakeup_source *ws)

    Destroy a struct wakeup_source object.

    :param struct wakeup_source \*ws:
        Wakeup source to destroy.

.. _`wakeup_source_destroy.description`:

Description
-----------

Use only for wakeup source objects created with \ :c:func:`wakeup_source_create`\ .

.. _`wakeup_source_add`:

wakeup_source_add
=================

.. c:function:: void wakeup_source_add(struct wakeup_source *ws)

    Add given object to the list of wakeup sources.

    :param struct wakeup_source \*ws:
        Wakeup source object to add to the list.

.. _`wakeup_source_remove`:

wakeup_source_remove
====================

.. c:function:: void wakeup_source_remove(struct wakeup_source *ws)

    Remove given object from the wakeup sources list.

    :param struct wakeup_source \*ws:
        Wakeup source object to remove from the list.

.. _`wakeup_source_register`:

wakeup_source_register
======================

.. c:function:: struct wakeup_source *wakeup_source_register(const char *name)

    Create wakeup source and add it to the list.

    :param const char \*name:
        Name of the wakeup source to register.

.. _`wakeup_source_unregister`:

wakeup_source_unregister
========================

.. c:function:: void wakeup_source_unregister(struct wakeup_source *ws)

    Remove wakeup source from the list and remove it.

    :param struct wakeup_source \*ws:
        Wakeup source object to unregister.

.. _`device_wakeup_attach`:

device_wakeup_attach
====================

.. c:function:: int device_wakeup_attach(struct device *dev, struct wakeup_source *ws)

    Attach a wakeup source object to a device object.

    :param struct device \*dev:
        Device to handle.

    :param struct wakeup_source \*ws:
        Wakeup source object to attach to \ ``dev``\ .

.. _`device_wakeup_attach.description`:

Description
-----------

This causes \ ``dev``\  to be treated as a wakeup device.

.. _`device_wakeup_enable`:

device_wakeup_enable
====================

.. c:function:: int device_wakeup_enable(struct device *dev)

    Enable given device to be a wakeup source.

    :param struct device \*dev:
        Device to handle.

.. _`device_wakeup_enable.description`:

Description
-----------

Create a wakeup source object, register it and attach it to \ ``dev``\ .

.. _`device_wakeup_attach_irq`:

device_wakeup_attach_irq
========================

.. c:function:: int device_wakeup_attach_irq(struct device *dev, struct wake_irq *wakeirq)

    Attach a wakeirq to a wakeup source

    :param struct device \*dev:
        Device to handle

    :param struct wake_irq \*wakeirq:
        Device specific wakeirq entry

.. _`device_wakeup_attach_irq.description`:

Description
-----------

Attach a device wakeirq to the wakeup source so the device
wake IRQ can be configured automatically for suspend and
resume.

Call under the device's power.lock lock.

.. _`device_wakeup_detach_irq`:

device_wakeup_detach_irq
========================

.. c:function:: void device_wakeup_detach_irq(struct device *dev)

    Detach a wakeirq from a wakeup source

    :param struct device \*dev:
        Device to handle

.. _`device_wakeup_detach_irq.description`:

Description
-----------

Removes a device wakeirq from the wakeup source.

Call under the device's power.lock lock.

.. _`device_wakeup_arm_wake_irqs`:

device_wakeup_arm_wake_irqs
===========================

.. c:function:: void device_wakeup_arm_wake_irqs( void)

    :param  void:
        no arguments

.. _`device_wakeup_arm_wake_irqs.description`:

Description
-----------

Itereates over the list of device wakeirqs to arm them.

.. _`device_wakeup_disarm_wake_irqs`:

device_wakeup_disarm_wake_irqs
==============================

.. c:function:: void device_wakeup_disarm_wake_irqs( void)

    :param  void:
        no arguments

.. _`device_wakeup_disarm_wake_irqs.description`:

Description
-----------

Itereates over the list of device wakeirqs to disarm them.

.. _`device_wakeup_detach`:

device_wakeup_detach
====================

.. c:function:: struct wakeup_source *device_wakeup_detach(struct device *dev)

    Detach a device's wakeup source object from it.

    :param struct device \*dev:
        Device to detach the wakeup source object from.

.. _`device_wakeup_detach.description`:

Description
-----------

After it returns, \ ``dev``\  will not be treated as a wakeup device any more.

.. _`device_wakeup_disable`:

device_wakeup_disable
=====================

.. c:function:: int device_wakeup_disable(struct device *dev)

    Do not regard a device as a wakeup source any more.

    :param struct device \*dev:
        Device to handle.

.. _`device_wakeup_disable.description`:

Description
-----------

Detach the \ ``dev``\ 's wakeup source object from it, unregister this wakeup source
object and destroy it.

.. _`device_set_wakeup_capable`:

device_set_wakeup_capable
=========================

.. c:function:: void device_set_wakeup_capable(struct device *dev, bool capable)

    Set/reset device wakeup capability flag.

    :param struct device \*dev:
        Device to handle.

    :param bool capable:
        Whether or not \ ``dev``\  is capable of waking up the system from sleep.

.. _`device_set_wakeup_capable.description`:

Description
-----------

If \ ``capable``\  is set, set the \ ``dev``\ 's power.can_wakeup flag and add its
wakeup-related attributes to sysfs.  Otherwise, unset the \ ``dev``\ 's
power.can_wakeup flag and remove its wakeup-related attributes from sysfs.

This function may sleep and it can't be called from any context where
sleeping is not allowed.

.. _`device_init_wakeup`:

device_init_wakeup
==================

.. c:function:: int device_init_wakeup(struct device *dev, bool enable)

    Device wakeup initialization.

    :param struct device \*dev:
        Device to handle.

    :param bool enable:
        Whether or not to enable \ ``dev``\  as a wakeup device.

.. _`device_init_wakeup.description`:

Description
-----------

By default, most devices should leave wakeup disabled.  The exceptions are

.. _`device_init_wakeup.devices-that-everyone-expects-to-be-wakeup-sources`:

devices that everyone expects to be wakeup sources
--------------------------------------------------

keyboards, power buttons,
possibly network interfaces, etc.  Also, devices that don't generate their
own wakeup requests but merely forward requests from one bus to another
(like PCI bridges) should have wakeup enabled by default.

.. _`device_set_wakeup_enable`:

device_set_wakeup_enable
========================

.. c:function:: int device_set_wakeup_enable(struct device *dev, bool enable)

    Enable or disable a device to wake up the system.

    :param struct device \*dev:
        Device to handle.

    :param bool enable:
        *undescribed*

.. _`wakeup_source_not_registered`:

wakeup_source_not_registered
============================

.. c:function:: bool wakeup_source_not_registered(struct wakeup_source *ws)

    validate the given wakeup source.

    :param struct wakeup_source \*ws:
        Wakeup source to be validated.

.. _`wakeup_source_activate`:

wakeup_source_activate
======================

.. c:function:: void wakeup_source_activate(struct wakeup_source *ws, bool hard)

    Mark given wakeup source as active.

    :param struct wakeup_source \*ws:
        Wakeup source to handle.

    :param bool hard:
        If set, abort suspends in progress and wake up from suspend-to-idle.

.. _`wakeup_source_activate.description`:

Description
-----------

Update the \ ``ws``\ ' statistics and, if \ ``ws``\  has just been activated, notify the PM
core of the event by incrementing the counter of of wakeup events being
processed.

.. _`wakeup_source_report_event`:

wakeup_source_report_event
==========================

.. c:function:: void wakeup_source_report_event(struct wakeup_source *ws, bool hard)

    Report wakeup event using the given source.

    :param struct wakeup_source \*ws:
        Wakeup source to report the event for.

    :param bool hard:
        If set, abort suspends in progress and wake up from suspend-to-idle.

.. _`__pm_stay_awake`:

__pm_stay_awake
===============

.. c:function:: void __pm_stay_awake(struct wakeup_source *ws)

    Notify the PM core of a wakeup event.

    :param struct wakeup_source \*ws:
        Wakeup source object associated with the source of the event.

.. _`__pm_stay_awake.description`:

Description
-----------

It is safe to call this function from interrupt context.

.. _`pm_stay_awake`:

pm_stay_awake
=============

.. c:function:: void pm_stay_awake(struct device *dev)

    Notify the PM core that a wakeup event is being processed.

    :param struct device \*dev:
        Device the wakeup event is related to.

.. _`pm_stay_awake.description`:

Description
-----------

Notify the PM core of a wakeup event (signaled by \ ``dev``\ ) by calling
\__pm_stay_awake for the \ ``dev``\ 's wakeup source object.

Call this function after detecting of a wakeup event if \ :c:func:`pm_relax`\  is going
to be called directly after processing the event (and possibly passing it to
user space for further processing).

.. _`wakeup_source_deactivate`:

wakeup_source_deactivate
========================

.. c:function:: void wakeup_source_deactivate(struct wakeup_source *ws)

    Mark given wakeup source as inactive.

    :param struct wakeup_source \*ws:
        Wakeup source to handle.

.. _`wakeup_source_deactivate.description`:

Description
-----------

Update the \ ``ws``\ ' statistics and notify the PM core that the wakeup source has
become inactive by decrementing the counter of wakeup events being processed
and incrementing the counter of registered wakeup events.

.. _`__pm_relax`:

__pm_relax
==========

.. c:function:: void __pm_relax(struct wakeup_source *ws)

    Notify the PM core that processing of a wakeup event has ended.

    :param struct wakeup_source \*ws:
        Wakeup source object associated with the source of the event.

.. _`__pm_relax.description`:

Description
-----------

Call this function for wakeup events whose processing started with calling
\__pm_stay_awake().

It is safe to call it from interrupt context.

.. _`pm_relax`:

pm_relax
========

.. c:function:: void pm_relax(struct device *dev)

    Notify the PM core that processing of a wakeup event has ended.

    :param struct device \*dev:
        Device that signaled the event.

.. _`pm_relax.description`:

Description
-----------

Execute \__pm_relax() for the \ ``dev``\ 's wakeup source object.

.. _`pm_wakeup_timer_fn`:

pm_wakeup_timer_fn
==================

.. c:function:: void pm_wakeup_timer_fn(unsigned long data)

    Delayed finalization of a wakeup event.

    :param unsigned long data:
        Address of the wakeup source object associated with the event source.

.. _`pm_wakeup_timer_fn.description`:

Description
-----------

Call \ :c:func:`wakeup_source_deactivate`\  for the wakeup source whose address is stored
in \ ``data``\  if it is currently active and its timer has not been canceled and
the expiration time of the timer is not in future.

.. _`pm_wakeup_ws_event`:

pm_wakeup_ws_event
==================

.. c:function:: void pm_wakeup_ws_event(struct wakeup_source *ws, unsigned int msec, bool hard)

    Notify the PM core of a wakeup event.

    :param struct wakeup_source \*ws:
        Wakeup source object associated with the event source.

    :param unsigned int msec:
        Anticipated event processing time (in milliseconds).

    :param bool hard:
        If set, abort suspends in progress and wake up from suspend-to-idle.

.. _`pm_wakeup_ws_event.description`:

Description
-----------

Notify the PM core of a wakeup event whose source is \ ``ws``\  that will take
approximately \ ``msec``\  milliseconds to be processed by the kernel.  If \ ``ws``\  is
not active, activate it.  If \ ``msec``\  is nonzero, set up the \ ``ws``\ ' timer to
execute \ :c:func:`pm_wakeup_timer_fn`\  in future.

It is safe to call this function from interrupt context.

.. _`pm_wakeup_dev_event`:

pm_wakeup_dev_event
===================

.. c:function:: void pm_wakeup_dev_event(struct device *dev, unsigned int msec, bool hard)

    Notify the PM core of a wakeup event.

    :param struct device \*dev:
        Device the wakeup event is related to.

    :param unsigned int msec:
        Anticipated event processing time (in milliseconds).

    :param bool hard:
        If set, abort suspends in progress and wake up from suspend-to-idle.

.. _`pm_wakeup_dev_event.description`:

Description
-----------

Call \ :c:func:`pm_wakeup_ws_event`\  for the \ ``dev``\ 's wakeup source object.

.. _`pm_wakeup_pending`:

pm_wakeup_pending
=================

.. c:function:: bool pm_wakeup_pending( void)

    Check if power transition in progress should be aborted.

    :param  void:
        no arguments

.. _`pm_wakeup_pending.description`:

Description
-----------

Compare the current number of registered wakeup events with its preserved
value from the past and return true if new wakeup events have been registered
since the old value was stored.  Also return true if the current number of
wakeup events being processed is different from zero.

.. _`pm_get_wakeup_count`:

pm_get_wakeup_count
===================

.. c:function:: bool pm_get_wakeup_count(unsigned int *count, bool block)

    Read the number of registered wakeup events.

    :param unsigned int \*count:
        Address to store the value at.

    :param bool block:
        Whether or not to block.

.. _`pm_get_wakeup_count.description`:

Description
-----------

Store the number of registered wakeup events at the address in \ ``count``\ .  If
\ ``block``\  is set, block until the current number of wakeup events being
processed is zero.

Return 'false' if the current number of wakeup events being processed is
nonzero.  Otherwise return 'true'.

.. _`pm_save_wakeup_count`:

pm_save_wakeup_count
====================

.. c:function:: bool pm_save_wakeup_count(unsigned int count)

    Save the current number of registered wakeup events.

    :param unsigned int count:
        Value to compare with the current number of registered wakeup events.

.. _`pm_save_wakeup_count.description`:

Description
-----------

If \ ``count``\  is equal to the current number of registered wakeup events and the
current number of wakeup events being processed is zero, store \ ``count``\  as the
old number of registered wakeup events for \ :c:func:`pm_check_wakeup_events`\ , enable
wakeup events detection and return 'true'.  Otherwise disable wakeup events
detection and return 'false'.

.. _`pm_wakep_autosleep_enabled`:

pm_wakep_autosleep_enabled
==========================

.. c:function:: void pm_wakep_autosleep_enabled(bool set)

    Modify autosleep_enabled for all wakeup sources.

    :param bool set:
        *undescribed*

.. _`print_wakeup_source_stats`:

print_wakeup_source_stats
=========================

.. c:function:: int print_wakeup_source_stats(struct seq_file *m, struct wakeup_source *ws)

    Print wakeup source statistics information.

    :param struct seq_file \*m:
        seq_file to print the statistics into.

    :param struct wakeup_source \*ws:
        Wakeup source object to print the statistics for.

.. _`wakeup_sources_stats_show`:

wakeup_sources_stats_show
=========================

.. c:function:: int wakeup_sources_stats_show(struct seq_file *m, void *unused)

    Print wakeup sources statistics information.

    :param struct seq_file \*m:
        seq_file to print the statistics into.

    :param void \*unused:
        *undescribed*

.. This file was automatic generated / don't edit.

