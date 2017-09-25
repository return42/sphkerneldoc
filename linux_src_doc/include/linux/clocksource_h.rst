.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/clocksource.h

.. _`clocksource`:

struct clocksource
==================

.. c:type:: struct clocksource

    hardware abstraction for a free running counter Provides mostly state-free accessors to the underlying hardware. This is the structure used for system time.

.. _`clocksource.definition`:

Definition
----------

.. code-block:: c

    struct clocksource {
        u64 (*read)(struct clocksource *cs);
        u64 mask;
        u32 mult;
        u32 shift;
        u64 max_idle_ns;
        u32 maxadj;
    #ifdef CONFIG_ARCH_CLOCKSOURCE_DATA
        struct arch_clocksource_data archdata;
    #endif
        u64 max_cycles;
        const char *name;
        struct list_head list;
        int rating;
        int (*enable)(struct clocksource *cs);
        void (*disable)(struct clocksource *cs);
        unsigned long flags;
        void (*suspend)(struct clocksource *cs);
        void (*resume)(struct clocksource *cs);
        void (*mark_unstable)(struct clocksource *cs);
        void (*tick_stable)(struct clocksource *cs);
    #ifdef CONFIG_CLOCKSOURCE_WATCHDOG
        struct list_head wd_list;
        u64 cs_last;
        u64 wd_last;
    #endif
        struct module *owner;
    }

.. _`clocksource.members`:

Members
-------

read
    returns a cycle value, passes clocksource as argument

mask
    bitmask for two's complement
    subtraction of non 64 bit counters

mult
    cycle to nanosecond multiplier

shift
    cycle to nanosecond divisor (power of two)

max_idle_ns
    max idle time permitted by the clocksource (nsecs)

maxadj
    maximum adjustment value to mult (~11%)

archdata
    arch-specific data

max_cycles
    maximum safe cycle value which won't overflow on multiplication

name
    ptr to clocksource name

list
    list head for registration

rating
    rating value for selection (higher is better)
    To avoid rating inflation the following
    list should give you a guide as to how
    to assign your clocksource a rating
    1-99: Unfit for real use
    Only available for bootup and testing purposes.
    100-199: Base level usability.
    Functional for real use, but not desired.
    200-299: Good.
    A correct and usable clocksource.
    300-399: Desired.
    A reasonably fast and accurate clocksource.
    400-499: Perfect
    The ideal clocksource. A must-use where
    available.

enable
    optional function to enable the clocksource

disable
    optional function to disable the clocksource

flags
    flags describing special properties

suspend
    suspend function for the clocksource, if necessary

resume
    resume function for the clocksource, if necessary

mark_unstable
    Optional function to inform the clocksource driver that
    the watchdog marked the clocksource unstable

tick_stable
    *undescribed*

wd_list
    *undescribed*

cs_last
    *undescribed*

wd_last
    *undescribed*

owner
    module reference, must be set by clocksource in modules

.. _`clocksource.note`:

Note
----

This struct is not used in hotpathes of the timekeeping code
because the timekeeper caches the hot path fields in its own data
structure, so no line cache alignment is required,

The pointer to the clocksource itself is handed to the read
callback. If you need extra information there you can wrap struct
clocksource into your own struct. Depending on the amount of
information you need you should consider to cache line align that
structure.

.. _`clocksource_khz2mult`:

clocksource_khz2mult
====================

.. c:function:: u32 clocksource_khz2mult(u32 khz, u32 shift_constant)

    calculates mult from khz and shift

    :param u32 khz:
        Clocksource frequency in KHz

    :param u32 shift_constant:
        Clocksource shift factor

.. _`clocksource_khz2mult.description`:

Description
-----------

Helper functions that converts a khz counter frequency to a timsource
multiplier, given the clocksource shift value

.. _`clocksource_hz2mult`:

clocksource_hz2mult
===================

.. c:function:: u32 clocksource_hz2mult(u32 hz, u32 shift_constant)

    calculates mult from hz and shift

    :param u32 hz:
        Clocksource frequency in Hz

    :param u32 shift_constant:
        Clocksource shift factor

.. _`clocksource_hz2mult.description`:

Description
-----------

Helper functions that converts a hz counter
frequency to a timsource multiplier, given the
clocksource shift value

.. _`clocksource_cyc2ns`:

clocksource_cyc2ns
==================

.. c:function:: s64 clocksource_cyc2ns(u64 cycles, u32 mult, u32 shift)

    converts clocksource cycles to nanoseconds

    :param u64 cycles:
        cycles

    :param u32 mult:
        cycle to nanosecond multiplier

    :param u32 shift:
        cycle to nanosecond divisor (power of two)

.. _`clocksource_cyc2ns.description`:

Description
-----------

Converts clocksource cycles to nanoseconds, using the given \ ``mult``\  and \ ``shift``\ .
The code is optimized for performance and is not intended to work
with absolute clocksource cycles (as those will easily overflow),
but is only intended to be used with relative (delta) clocksource cycles.

XXX - This could use some \ :c:func:`mult_lxl_ll`\  asm optimization

.. This file was automatic generated / don't edit.

