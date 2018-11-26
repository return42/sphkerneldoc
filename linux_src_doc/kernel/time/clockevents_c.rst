.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/time/clockevents.c

.. _`clockevent_delta2ns`:

clockevent_delta2ns
===================

.. c:function:: u64 clockevent_delta2ns(unsigned long latch, struct clock_event_device *evt)

    Convert a latch value (device ticks) to nanoseconds

    :param latch:
        value to convert
    :type latch: unsigned long

    :param evt:
        pointer to clock event device descriptor
    :type evt: struct clock_event_device \*

.. _`clockevent_delta2ns.description`:

Description
-----------

Math helper, returns latch value converted to nanoseconds (bound checked)

.. _`clockevents_switch_state`:

clockevents_switch_state
========================

.. c:function:: void clockevents_switch_state(struct clock_event_device *dev, enum clock_event_state state)

    set the operating state of a clock event device

    :param dev:
        device to modify
    :type dev: struct clock_event_device \*

    :param state:
        new state
    :type state: enum clock_event_state

.. _`clockevents_switch_state.description`:

Description
-----------

Must be called with interrupts disabled !

.. _`clockevents_shutdown`:

clockevents_shutdown
====================

.. c:function:: void clockevents_shutdown(struct clock_event_device *dev)

    shutdown the device and clear next_event

    :param dev:
        device to shutdown
    :type dev: struct clock_event_device \*

.. _`clockevents_tick_resume`:

clockevents_tick_resume
=======================

.. c:function:: int clockevents_tick_resume(struct clock_event_device *dev)

    Resume the tick device before using it again

    :param dev:
        device to resume
    :type dev: struct clock_event_device \*

.. _`clockevents_increase_min_delta`:

clockevents_increase_min_delta
==============================

.. c:function:: int clockevents_increase_min_delta(struct clock_event_device *dev)

    raise minimum delta of a clock event device

    :param dev:
        device to increase the minimum delta
    :type dev: struct clock_event_device \*

.. _`clockevents_increase_min_delta.description`:

Description
-----------

Returns 0 on success, -ETIME when the minimum delta reached the limit.

.. _`clockevents_program_min_delta`:

clockevents_program_min_delta
=============================

.. c:function:: int clockevents_program_min_delta(struct clock_event_device *dev)

    Set clock event device to the minimum delay.

    :param dev:
        device to program
    :type dev: struct clock_event_device \*

.. _`clockevents_program_min_delta.description`:

Description
-----------

Returns 0 on success, -ETIME when the retry loop failed.

.. _`clockevents_program_min_delta`:

clockevents_program_min_delta
=============================

.. c:function:: int clockevents_program_min_delta(struct clock_event_device *dev)

    Set clock event device to the minimum delay.

    :param dev:
        device to program
    :type dev: struct clock_event_device \*

.. _`clockevents_program_min_delta.description`:

Description
-----------

Returns 0 on success, -ETIME when the retry loop failed.

.. _`clockevents_program_event`:

clockevents_program_event
=========================

.. c:function:: int clockevents_program_event(struct clock_event_device *dev, ktime_t expires, bool force)

    Reprogram the clock event device.

    :param dev:
        device to program
    :type dev: struct clock_event_device \*

    :param expires:
        absolute expiry time (monotonic clock)
    :type expires: ktime_t

    :param force:
        program minimum delay if expires can not be set
    :type force: bool

.. _`clockevents_program_event.description`:

Description
-----------

Returns 0 on success, -ETIME when the event is in the past.

.. _`clockevents_register_device`:

clockevents_register_device
===========================

.. c:function:: void clockevents_register_device(struct clock_event_device *dev)

    register a clock event device

    :param dev:
        device to register
    :type dev: struct clock_event_device \*

.. _`clockevents_config_and_register`:

clockevents_config_and_register
===============================

.. c:function:: void clockevents_config_and_register(struct clock_event_device *dev, u32 freq, unsigned long min_delta, unsigned long max_delta)

    Configure and register a clock event device

    :param dev:
        device to register
    :type dev: struct clock_event_device \*

    :param freq:
        The clock frequency
    :type freq: u32

    :param min_delta:
        The minimum clock ticks to program in oneshot mode
    :type min_delta: unsigned long

    :param max_delta:
        The maximum clock ticks to program in oneshot mode
    :type max_delta: unsigned long

.. _`clockevents_config_and_register.description`:

Description
-----------

min/max_delta can be 0 for devices which do not support oneshot mode.

.. _`clockevents_update_freq`:

clockevents_update_freq
=======================

.. c:function:: int clockevents_update_freq(struct clock_event_device *dev, u32 freq)

    Update frequency and reprogram a clock event device.

    :param dev:
        device to modify
    :type dev: struct clock_event_device \*

    :param freq:
        new device frequency
    :type freq: u32

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

    :param old:
        device to release (can be NULL)
    :type old: struct clock_event_device \*

    :param new:
        device to request (can be NULL)
    :type new: struct clock_event_device \*

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

    :param void:
        no arguments
    :type void: 

.. _`clockevents_resume`:

clockevents_resume
==================

.. c:function:: void clockevents_resume( void)

    resume clock devices

    :param void:
        no arguments
    :type void: 

.. _`tick_cleanup_dead_cpu`:

tick_cleanup_dead_cpu
=====================

.. c:function:: void tick_cleanup_dead_cpu(int cpu)

    Cleanup the tick and clockevents of a dead cpu

    :param cpu:
        *undescribed*
    :type cpu: int

.. This file was automatic generated / don't edit.

