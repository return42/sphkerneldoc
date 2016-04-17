.. -*- coding: utf-8; mode: rst -*-

=============
clocksource.c
=============


.. _`clocks_calc_mult_shift`:

clocks_calc_mult_shift
======================

.. c:function:: void clocks_calc_mult_shift (u32 *mult, u32 *shift, u32 from, u32 to, u32 maxsec)

    calculate mult/shift factors for scaled math of clocks

    :param u32 \*mult:
        pointer to mult variable

    :param u32 \*shift:
        pointer to shift variable

    :param u32 from:
        frequency to convert from

    :param u32 to:
        frequency to convert to

    :param u32 maxsec:
        guaranteed runtime conversion range in seconds



.. _`clocks_calc_mult_shift.description`:

Description
-----------

The function evaluates the shift/mult pair for the scaled math
operations of clocksources and clockevents.

``to`` and ``from`` are frequency values in HZ. For clock sources ``to`` is
NSEC_PER_SEC == 1GHz and ``from`` is the counter frequency. For clock
event ``to`` is the counter frequency and ``from`` is NSEC_PER_SEC.

The ``maxsec`` conversion range argument controls the time frame in
seconds which must be covered by the runtime conversion with the
calculated mult and shift factors. This guarantees that no 64bit
overflow happens when the input value of the conversion is
multiplied with the calculated mult factor. Larger ranges may
reduce the conversion accuracy by chosing smaller mult and shift
factors.



.. _`clocksource_mark_unstable`:

clocksource_mark_unstable
=========================

.. c:function:: void clocksource_mark_unstable (struct clocksource *cs)

    mark clocksource unstable via watchdog

    :param struct clocksource \*cs:
        clocksource to be marked unstable



.. _`clocksource_mark_unstable.description`:

Description
-----------

This function is called instead of clocksource_change_rating from
cpu hotplug code to avoid a deadlock between the clocksource mutex
and the cpu hotplug mutex. It defers the update of the clocksource
to the watchdog thread.



.. _`clocksource_suspend`:

clocksource_suspend
===================

.. c:function:: void clocksource_suspend ( void)

    suspend the clocksource(s)

    :param void:
        no arguments



.. _`clocksource_resume`:

clocksource_resume
==================

.. c:function:: void clocksource_resume ( void)

    resume the clocksource(s)

    :param void:
        no arguments



.. _`clocksource_touch_watchdog`:

clocksource_touch_watchdog
==========================

.. c:function:: void clocksource_touch_watchdog ( void)

    Update watchdog

    :param void:
        no arguments



.. _`clocksource_touch_watchdog.description`:

Description
-----------


Update the watchdog after exception contexts such as kgdb so as not
to incorrectly trip the watchdog. This might fail when the kernel
was stopped in code which holds watchdog_lock.



.. _`clocksource_max_adjustment`:

clocksource_max_adjustment
==========================

.. c:function:: u32 clocksource_max_adjustment (struct clocksource *cs)

    Returns max adjustment amount

    :param struct clocksource \*cs:
        Pointer to clocksource



.. _`clocks_calc_max_nsecs`:

clocks_calc_max_nsecs
=====================

.. c:function:: u64 clocks_calc_max_nsecs (u32 mult, u32 shift, u32 maxadj, u64 mask, u64 *max_cyc)

    Returns maximum nanoseconds that can be converted

    :param u32 mult:
        cycle to nanosecond multiplier

    :param u32 shift:
        cycle to nanosecond divisor (power of two)

    :param u32 maxadj:
        maximum adjustment value to mult (~11%)

    :param u64 mask:
        bitmask for two's complement subtraction of non 64 bit counters

    :param u64 \*max_cyc:
        maximum cycle value before potential overflow (does not include
        any safety margin)



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

.. c:function:: void clocksource_update_max_deferment (struct clocksource *cs)

    Updates the clocksource max_idle_ns & max_cycles

    :param struct clocksource \*cs:
        Pointer to clocksource to be updated



.. _`clocksource_select`:

clocksource_select
==================

.. c:function:: void clocksource_select ( void)

    Select the best clocksource available

    :param void:
        no arguments



.. _`clocksource_select.description`:

Description
-----------


Private function. Must hold clocksource_mutex when called.

Select the clocksource with the best rating, or the clocksource,
which is selected by userspace override.



.. _`__clocksource_update_freq_scale`:

__clocksource_update_freq_scale
===============================

.. c:function:: void __clocksource_update_freq_scale (struct clocksource *cs, u32 scale, u32 freq)

    Used update clocksource with new freq

    :param struct clocksource \*cs:
        clocksource to be registered

    :param u32 scale:
        Scale factor multiplied against freq to get clocksource hz

    :param u32 freq:
        clocksource frequency (cycles per second) divided by scale



.. _`__clocksource_update_freq_scale.description`:

Description
-----------

This should only be called from the clocksource->:c:func:`enable` method.

This \*SHOULD NOT\* be called directly! Please use the
:c:func:`__clocksource_update_freq_hz` or :c:func:`__clocksource_update_freq_khz` helper
functions.



.. _`__clocksource_register_scale`:

__clocksource_register_scale
============================

.. c:function:: int __clocksource_register_scale (struct clocksource *cs, u32 scale, u32 freq)

    Used to install new clocksources

    :param struct clocksource \*cs:
        clocksource to be registered

    :param u32 scale:
        Scale factor multiplied against freq to get clocksource hz

    :param u32 freq:
        clocksource frequency (cycles per second) divided by scale



.. _`__clocksource_register_scale.description`:

Description
-----------

Returns -EBUSY if registration fails, zero otherwise.

This \*SHOULD NOT\* be called directly! Please use the
:c:func:`clocksource_register_hz` or clocksource_register_khz helper functions.



.. _`clocksource_change_rating`:

clocksource_change_rating
=========================

.. c:function:: void clocksource_change_rating (struct clocksource *cs, int rating)

    Change the rating of a registered clocksource

    :param struct clocksource \*cs:
        clocksource to be changed

    :param int rating:
        new rating



.. _`clocksource_unregister`:

clocksource_unregister
======================

.. c:function:: int clocksource_unregister (struct clocksource *cs)

    remove a registered clocksource

    :param struct clocksource \*cs:
        clocksource to be unregistered



.. _`sysfs_show_current_clocksources`:

sysfs_show_current_clocksources
===============================

.. c:function:: ssize_t sysfs_show_current_clocksources (struct device *dev, struct device_attribute *attr, char *buf)

    sysfs interface for current clocksource

    :param struct device \*dev:
        unused

    :param struct device_attribute \*attr:
        unused

    :param char \*buf:
        char buffer to be filled with clocksource list



.. _`sysfs_show_current_clocksources.description`:

Description
-----------

Provides sysfs interface for listing current clocksource.



.. _`sysfs_override_clocksource`:

sysfs_override_clocksource
==========================

.. c:function:: ssize_t sysfs_override_clocksource (struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    interface for manually overriding clocksource

    :param struct device \*dev:
        unused

    :param struct device_attribute \*attr:
        unused

    :param const char \*buf:
        name of override clocksource

    :param size_t count:
        length of buffer



.. _`sysfs_override_clocksource.description`:

Description
-----------

Takes input from sysfs interface for manually overriding the default
clocksource selection.



.. _`sysfs_unbind_clocksource`:

sysfs_unbind_clocksource
========================

.. c:function:: ssize_t sysfs_unbind_clocksource (struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    interface for manually unbinding clocksource

    :param struct device \*dev:
        unused

    :param struct device_attribute \*attr:
        unused

    :param const char \*buf:
        unused

    :param size_t count:
        length of buffer



.. _`sysfs_unbind_clocksource.description`:

Description
-----------

Takes input from sysfs interface for manually unbinding a clocksource.



.. _`sysfs_show_available_clocksources`:

sysfs_show_available_clocksources
=================================

.. c:function:: ssize_t sysfs_show_available_clocksources (struct device *dev, struct device_attribute *attr, char *buf)

    sysfs interface for listing clocksource

    :param struct device \*dev:
        unused

    :param struct device_attribute \*attr:
        unused

    :param char \*buf:
        char buffer to be filled with clocksource list



.. _`sysfs_show_available_clocksources.description`:

Description
-----------

Provides sysfs interface for listing registered clocksources



.. _`boot_override_clocksource`:

boot_override_clocksource
=========================

.. c:function:: int boot_override_clocksource (char *str)

    boot clock override

    :param char \*str:
        override name



.. _`boot_override_clocksource.description`:

Description
-----------

Takes a clocksource= boot argument and uses it
as the clocksource override name.



.. _`boot_override_clock`:

boot_override_clock
===================

.. c:function:: int boot_override_clock (char *str)

    Compatibility layer for deprecated boot option

    :param char \*str:
        override name



.. _`boot_override_clock.description`:

Description
-----------

DEPRECATED! Takes a clock= boot argument and uses it
as the clocksource override name

