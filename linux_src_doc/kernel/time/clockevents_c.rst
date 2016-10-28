.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/time/clockevents.c

.. _`clockevent_delta2ns`:

clockevent_delta2ns
===================

.. c:function:: u64 clockevent_delta2ns(unsigned long latch, struct clock_event_device *evt)

    Convert a latch value (device ticks) to nanoseconds

    :param unsigned long latch:
        value to convert

    :param struct clock_event_device \*evt:
        pointer to clock event device descriptor

.. _`clockevent_delta2ns.description`:

Description
-----------

Math helper, returns latch value converted to nanoseconds (bound checked)

.. _`clockevents_switch_state`:

clockevents_switch_state
========================

.. c:function:: void clockevents_switch_state(struct clock_event_device *dev, enum clock_event_state state)

    set the operating state of a clock event device

    :param struct clock_event_device \*dev:
        device to modify

    :param enum clock_event_state state:
        new state

.. _`clockevents_switch_state.description`:

Description
-----------

Must be called with interrupts disabled !

.. _`clockevents_shutdown`:

clockevents_shutdown
====================

.. c:function:: void clockevents_shutdown(struct clock_event_device *dev)

    shutdown the device and clear next_event

    :param struct clock_event_device \*dev:
        device to shutdown

.. _`clockevents_tick_resume`:

clockevents_tick_resume
=======================

.. c:function:: int clockevents_tick_resume(struct clock_event_device *dev)

    Resume the tick device before using it again

    :param struct clock_event_device \*dev:
        device to resume

.. _`clockevents_increase_min_delta`:

clockevents_increase_min_delta
==============================

.. c:function:: int clockevents_increase_min_delta(struct clock_event_device *dev)

    raise minimum delta of a clock event device

    :param struct clock_event_device \*dev:
        device to increase the minimum delta

.. _`clockevents_increase_min_delta.description`:

Description
-----------

Returns 0 on success, -ETIME when the minimum delta reached the limit.

.. _`clockevents_program_min_delta`:

clockevents_program_min_delta
=============================

.. c:function:: int clockevents_program_min_delta(struct clock_event_device *dev)

    Set clock event device to the minimum delay.

    :param struct clock_event_device \*dev:
        device to program

.. _`clockevents_program_min_delta.description`:

Description
-----------

Returns 0 on success, -ETIME when the retry loop failed.

.. _`clockevents_program_min_delta`:

clockevents_program_min_delta
=============================

.. c:function:: int clockevents_program_min_delta(struct clock_event_device *dev)

    Set clock event device to the minimum delay.

    :param struct clock_event_device \*dev:
        device to program

.. _`clockevents_program_min_delta.description`:

Description
-----------

Returns 0 on success, -ETIME when the retry loop failed.

.. _`clockevents_program_event`:

clockevents_program_event
=========================

.. c:function:: int clockevents_program_event(struct clock_event_device *dev, ktime_t expires, bool force)

    Reprogram the clock event device.

    :param struct clock_event_device \*dev:
        device to program

    :param ktime_t expires:
        absolute expiry time (monotonic clock)

    :param bool force:
        program minimum delay if expires can not be set

.. _`clockevents_program_event.description`:

Description
-----------

Returns 0 on success, -ETIME when the event is in the past.

.. _`clockevents_register_device`:

clockevents_register_device
===========================

.. c:function:: void clockevents_register_device(struct clock_event_device *dev)

    register a clock event device

    :param struct clock_event_device \*dev:
        device to register

.. _`clockevents_config_and_register`:

clockevents_config_and_register
===============================

.. c:function:: void clockevents_config_and_register(struct clock_event_device *dev, u32 freq, unsigned long min_delta, unsigned long max_delta)

    Configure and register a clock event device

    :param struct clock_event_device \*dev:
        device to register

    :param u32 freq:
        The clock frequency

    :param unsigned long min_delta:
        The minimum clock ticks to program in oneshot mode

    :param unsigned long max_delta:
        The maximum clock ticks to program in oneshot mode

.. _`clockevents_config_and_register.description`:

Description
-----------

min/max_delta can be 0 for devices which do not support oneshot mode.

.. _`clockevents_update_freq`:

clockevents_update_freq
=======================

.. c:function:: int clockevents_update_freq(struct clock_event_device *dev, u32 freq)

    Update frequency and reprogram a clock event device.

    :param struct clock_event_device \*dev:
        device to modify

    :param u32 freq:
        new device frequency

.. _`clockevents_update_freq.description`:

Description
-----------

Reconfigure and reprogram a clock event device in oneshot
mode. Must be called on the cpu for which the device delivers per
cpu timer events. If called for the broadcast device the core takes
care of serialization.

Returns 0 on success, -ETIME when the event is in the past.

.. _`clockevents_exchange_device`:

clockevents_exchange_device
===========================

.. c:function:: void clockevents_exchange_device(struct clock_event_device *old, struct clock_event_device *new)

    release and request clock devices

    :param struct clock_event_device \*old:
        device to release (can be NULL)

    :param struct clock_event_device \*new:
        device to request (can be NULL)

.. _`clockevents_exchange_device.description`:

Description
-----------

Called from various tick functions with clockevents_lock held and
interrupts disabled.

.. _`clockevents_suspend`:

clockevents_suspend
===================

.. c:function:: void clockevents_suspend( void)

    suspend clock devices

    :param  void:
        no arguments

.. _`clockevents_resume`:

clockevents_resume
==================

.. c:function:: void clockevents_resume( void)

    resume clock devices

    :param  void:
        no arguments

.. _`tick_cleanup_dead_cpu`:

tick_cleanup_dead_cpu
=====================

.. c:function:: void tick_cleanup_dead_cpu(int cpu)

    Cleanup the tick and clockevents of a dead cpu

    :param int cpu:
        *undescribed*

.. This file was automatic generated / don't edit.

