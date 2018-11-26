.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/time/clocksource.c

.. _`clocks_calc_mult_shift`:

clocks_calc_mult_shift
======================

.. c:function:: void clocks_calc_mult_shift(u32 *mult, u32 *shift, u32 from, u32 to, u32 maxsec)

    calculate mult/shift factors for scaled math of clocks

    :param mult:
        pointer to mult variable
    :type mult: u32 \*

    :param shift:
        pointer to shift variable
    :type shift: u32 \*

    :param from:
        frequency to convert from
    :type from: u32

    :param to:
        frequency to convert to
    :type to: u32

    :param maxsec:
        guaranteed runtime conversion range in seconds
    :type maxsec: u32

.. _`clocks_calc_mult_shift.description`:

Description
-----------

The function evaluates the shift/mult pair for the scaled math
operations of clocksources and clockevents.

\ ``to``\  and \ ``from``\  are frequency values in HZ. For clock sources \ ``to``\  is
NSEC_PER_SEC == 1GHz and \ ``from``\  is the counter frequency. For clock
event \ ``to``\  is the counter frequency and \ ``from``\  is NSEC_PER_SEC.

The \ ``maxsec``\  conversion range argument controls the time frame in
seconds which must be covered by the runtime conversion with the
calculated mult and shift factors. This guarantees that no 64bit
overflow happens when the input value of the conversion is
multiplied with the calculated mult factor. Larger ranges may
reduce the conversion accuracy by chosing smaller mult and shift
factors.

.. _`clocksource_mark_unstable`:

clocksource_mark_unstable
=========================

.. c:function:: void clocksource_mark_unstable(struct clocksource *cs)

    mark clocksource unstable via watchdog

    :param cs:
        clocksource to be marked unstable
    :type cs: struct clocksource \*

.. _`clocksource_mark_unstable.description`:

Description
-----------

This function is called by the x86 TSC code to mark clocksources as unstable;
it defers demotion and re-selection to a kthread.

.. _`clocksource_suspend_select`:

clocksource_suspend_select
==========================

.. c:function:: void clocksource_suspend_select(bool fallback)

    Select the best clocksource for suspend timing

    :param fallback:
        if select a fallback clocksource
    :type fallback: bool

.. _`clocksource_start_suspend_timing`:

clocksource_start_suspend_timing
================================

.. c:function:: void clocksource_start_suspend_timing(struct clocksource *cs, u64 start_cycles)

    Start measuring the suspend timing

    :param cs:
        current clocksource from timekeeping
    :type cs: struct clocksource \*

    :param start_cycles:
        current cycles from timekeeping
    :type start_cycles: u64

.. _`clocksource_start_suspend_timing.description`:

Description
-----------

This function will save the start cycle values of suspend timer to calculate
the suspend time when resuming system.

This function is called late in the suspend process from \ :c:func:`timekeeping_suspend`\ ,
that means processes are freezed, non-boot cpus and interrupts are disabled
now. It is therefore possible to start the suspend timer without taking the
clocksource mutex.

.. _`clocksource_stop_suspend_timing`:

clocksource_stop_suspend_timing
===============================

.. c:function:: u64 clocksource_stop_suspend_timing(struct clocksource *cs, u64 cycle_now)

    Stop measuring the suspend timing

    :param cs:
        current clocksource from timekeeping
    :type cs: struct clocksource \*

    :param cycle_now:
        current cycles from timekeeping
    :type cycle_now: u64

.. _`clocksource_stop_suspend_timing.description`:

Description
-----------

This function will calculate the suspend time from suspend timer.

Returns nanoseconds since suspend started, 0 if no usable suspend clocksource.

This function is called early in the resume process from \ :c:func:`timekeeping_resume`\ ,
that means there is only one cpu, no processes are running and the interrupts
are disabled. It is therefore possible to stop the suspend timer without
taking the clocksource mutex.

.. _`clocksource_suspend`:

clocksource_suspend
===================

.. c:function:: void clocksource_suspend( void)

    suspend the clocksource(s)

    :param void:
        no arguments
    :type void: 

.. _`clocksource_resume`:

clocksource_resume
==================

.. c:function:: void clocksource_resume( void)

    resume the clocksource(s)

    :param void:
        no arguments
    :type void: 

.. _`clocksource_touch_watchdog`:

clocksource_touch_watchdog
==========================

.. c:function:: void clocksource_touch_watchdog( void)

    Update watchdog

    :param void:
        no arguments
    :type void: 

.. _`clocksource_touch_watchdog.description`:

Description
-----------

Update the watchdog after exception contexts such as kgdb so as not
to incorrectly trip the watchdog. This might fail when the kernel
was stopped in code which holds watchdog_lock.

.. _`clocksource_max_adjustment`:

clocksource_max_adjustment
==========================

.. c:function:: u32 clocksource_max_adjustment(struct clocksource *cs)

    Returns max adjustment amount

    :param cs:
        Pointer to clocksource
    :type cs: struct clocksource \*

.. _`clocks_calc_max_nsecs`:

clocks_calc_max_nsecs
=====================

.. c:function:: u64 clocks_calc_max_nsecs(u32 mult, u32 shift, u32 maxadj, u64 mask, u64 *max_cyc)

    Returns maximum nanoseconds that can be converted

    :param mult:
        cycle to nanosecond multiplier
    :type mult: u32

    :param shift:
        cycle to nanosecond divisor (power of two)
    :type shift: u32

    :param maxadj:
        maximum adjustment value to mult (~11%)
    :type maxadj: u32

    :param mask:
        bitmask for two's complement subtraction of non 64 bit counters
    :type mask: u64

    :param max_cyc:
        maximum cycle value before potential overflow (does not include
        any safety margin)
    :type max_cyc: u64 \*

.. _`clocks_calc_max_nsecs.note`:

NOTE
----

This function includes a safety margin of 50%, in other words, we
return half the number of nanoseconds the hardware counter can technically
cover. This is done so that we can potentially detect problems caused by
delayed timers or bad hardware, which might result in time intervals that
are larger than what the math used can handle without overflows.

.. _`clocksource_update_max_deferment`:

clocksource_update_max_deferment
================================

.. c:function:: void clocksource_update_max_deferment(struct clocksource *cs)

    Updates the clocksource max_idle_ns & max_cycles

    :param cs:
        Pointer to clocksource to be updated
    :type cs: struct clocksource \*

.. _`clocksource_select`:

clocksource_select
==================

.. c:function:: void clocksource_select( void)

    Select the best clocksource available

    :param void:
        no arguments
    :type void: 

.. _`clocksource_select.description`:

Description
-----------

Private function. Must hold clocksource_mutex when called.

Select the clocksource with the best rating, or the clocksource,
which is selected by userspace override.

.. _`__clocksource_update_freq_scale`:

\__clocksource_update_freq_scale
================================

.. c:function:: void __clocksource_update_freq_scale(struct clocksource *cs, u32 scale, u32 freq)

    Used update clocksource with new freq

    :param cs:
        clocksource to be registered
    :type cs: struct clocksource \*

    :param scale:
        Scale factor multiplied against freq to get clocksource hz
    :type scale: u32

    :param freq:
        clocksource frequency (cycles per second) divided by scale
    :type freq: u32

.. _`__clocksource_update_freq_scale.description`:

Description
-----------

This should only be called from the clocksource->enable() method.

This \*SHOULD NOT\* be called directly! Please use the
\__clocksource_update_freq_hz() or \__clocksource_update_freq_khz() helper
functions.

.. _`__clocksource_register_scale`:

\__clocksource_register_scale
=============================

.. c:function:: int __clocksource_register_scale(struct clocksource *cs, u32 scale, u32 freq)

    Used to install new clocksources

    :param cs:
        clocksource to be registered
    :type cs: struct clocksource \*

    :param scale:
        Scale factor multiplied against freq to get clocksource hz
    :type scale: u32

    :param freq:
        clocksource frequency (cycles per second) divided by scale
    :type freq: u32

.. _`__clocksource_register_scale.description`:

Description
-----------

Returns -EBUSY if registration fails, zero otherwise.

This \*SHOULD NOT\* be called directly! Please use the
\ :c:func:`clocksource_register_hz`\  or clocksource_register_khz helper functions.

.. _`clocksource_change_rating`:

clocksource_change_rating
=========================

.. c:function:: void clocksource_change_rating(struct clocksource *cs, int rating)

    Change the rating of a registered clocksource

    :param cs:
        clocksource to be changed
    :type cs: struct clocksource \*

    :param rating:
        new rating
    :type rating: int

.. _`clocksource_unregister`:

clocksource_unregister
======================

.. c:function:: int clocksource_unregister(struct clocksource *cs)

    remove a registered clocksource

    :param cs:
        clocksource to be unregistered
    :type cs: struct clocksource \*

.. _`current_clocksource_show`:

current_clocksource_show
========================

.. c:function:: ssize_t current_clocksource_show(struct device *dev, struct device_attribute *attr, char *buf)

    sysfs interface for current clocksource

    :param dev:
        unused
    :type dev: struct device \*

    :param attr:
        unused
    :type attr: struct device_attribute \*

    :param buf:
        char buffer to be filled with clocksource list
    :type buf: char \*

.. _`current_clocksource_show.description`:

Description
-----------

Provides sysfs interface for listing current clocksource.

.. _`current_clocksource_store`:

current_clocksource_store
=========================

.. c:function:: ssize_t current_clocksource_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    interface for manually overriding clocksource

    :param dev:
        unused
    :type dev: struct device \*

    :param attr:
        unused
    :type attr: struct device_attribute \*

    :param buf:
        name of override clocksource
    :type buf: const char \*

    :param count:
        length of buffer
    :type count: size_t

.. _`current_clocksource_store.description`:

Description
-----------

Takes input from sysfs interface for manually overriding the default
clocksource selection.

.. _`unbind_clocksource_store`:

unbind_clocksource_store
========================

.. c:function:: ssize_t unbind_clocksource_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    interface for manually unbinding clocksource

    :param dev:
        unused
    :type dev: struct device \*

    :param attr:
        unused
    :type attr: struct device_attribute \*

    :param buf:
        unused
    :type buf: const char \*

    :param count:
        length of buffer
    :type count: size_t

.. _`unbind_clocksource_store.description`:

Description
-----------

Takes input from sysfs interface for manually unbinding a clocksource.

.. _`available_clocksource_show`:

available_clocksource_show
==========================

.. c:function:: ssize_t available_clocksource_show(struct device *dev, struct device_attribute *attr, char *buf)

    sysfs interface for listing clocksource

    :param dev:
        unused
    :type dev: struct device \*

    :param attr:
        unused
    :type attr: struct device_attribute \*

    :param buf:
        char buffer to be filled with clocksource list
    :type buf: char \*

.. _`available_clocksource_show.description`:

Description
-----------

Provides sysfs interface for listing registered clocksources

.. _`boot_override_clocksource`:

boot_override_clocksource
=========================

.. c:function:: int boot_override_clocksource(char* str)

    boot clock override

    :param str:
        override name
    :type str: char\*

.. _`boot_override_clocksource.description`:

Description
-----------

Takes a clocksource= boot argument and uses it
as the clocksource override name.

.. _`boot_override_clock`:

boot_override_clock
===================

.. c:function:: int boot_override_clock(char* str)

    Compatibility layer for deprecated boot option

    :param str:
        override name
    :type str: char\*

.. _`boot_override_clock.description`:

Description
-----------

DEPRECATED! Takes a clock= boot argument and uses it
as the clocksource override name

.. This file was automatic generated / don't edit.

