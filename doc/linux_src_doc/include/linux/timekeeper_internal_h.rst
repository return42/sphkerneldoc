.. -*- coding: utf-8; mode: rst -*-

=====================
timekeeper_internal.h
=====================


.. _`tk_read_base`:

struct tk_read_base
===================

.. c:type:: tk_read_base

    base structure for timekeeping readout


.. _`tk_read_base.definition`:

Definition
----------

.. code-block:: c

  struct tk_read_base {
    struct clocksource * clock;
    cycle_t (* read) (struct clocksource *cs);
    cycle_t mask;
    cycle_t cycle_last;
    u32 mult;
    u32 shift;
    u64 xtime_nsec;
    ktime_t base;
  };


.. _`tk_read_base.members`:

Members
-------

:``clock``:
    Current clocksource used for timekeeping.

:``read``:
    Read function of ``clock``

:``mask``:
    Bitmask for two's complement subtraction of non 64bit clocks

:``cycle_last``:
    ``clock`` cycle value at last update

:``mult``:
    (NTP adjusted) multiplier for scaled math conversion

:``shift``:
    Shift value for scaled math conversion

:``xtime_nsec``:
    Shifted (fractional) nano seconds offset for readout

:``base``:
    ktime_t (nanoseconds) base time for readout




.. _`tk_read_base.description`:

Description
-----------

This struct has size 56 byte on 64 bit. Together with a seqcount it
occupies a single 64byte cache line.

The struct is separate from struct timekeeper as it is also used
for a fast NMI safe accessors.



.. _`timekeeper`:

struct timekeeper
=================

.. c:type:: timekeeper

    Structure holding internal timekeeping values.


.. _`timekeeper.definition`:

Definition
----------

.. code-block:: c

  struct timekeeper {
    struct tk_read_base tkr_mono;
    struct tk_read_base tkr_raw;
    u64 xtime_sec;
    unsigned long ktime_sec;
    struct timespec64 wall_to_monotonic;
    ktime_t offs_real;
    ktime_t offs_boot;
    ktime_t offs_tai;
    s32 tai_offset;
    unsigned int clock_was_set_seq;
    u8 cs_was_changed_seq;
    ktime_t next_leap_ktime;
    struct timespec64 raw_time;
    cycle_t cycle_interval;
    u64 xtime_interval;
    s64 xtime_remainder;
    u32 raw_interval;
    s64 ntp_error;
    u32 ntp_error_shift;
    #ifdef CONFIG_DEBUG_TIMEKEEPING
    long last_warning;
    int underflow_seen;
    int overflow_seen;
    #endif
  };


.. _`timekeeper.members`:

Members
-------

:``tkr_mono``:
    The readout base structure for CLOCK_MONOTONIC

:``tkr_raw``:
    The readout base structure for CLOCK_MONOTONIC_RAW

:``xtime_sec``:
    Current CLOCK_REALTIME time in seconds

:``ktime_sec``:
    Current CLOCK_MONOTONIC time in seconds

:``wall_to_monotonic``:
    CLOCK_REALTIME to CLOCK_MONOTONIC offset

:``offs_real``:
    Offset clock monotonic -> clock realtime

:``offs_boot``:
    Offset clock monotonic -> clock boottime

:``offs_tai``:
    Offset clock monotonic -> clock tai

:``tai_offset``:
    The current UTC to TAI offset in seconds

:``clock_was_set_seq``:
    The sequence number of clock was set events

:``cs_was_changed_seq``:
    The sequence number of clocksource change events

:``next_leap_ktime``:
    CLOCK_MONOTONIC time value of a pending leap-second

:``raw_time``:
    Monotonic raw base time in timespec64 format

:``cycle_interval``:
    Number of clock cycles in one NTP interval

:``xtime_interval``:
    Number of clock shifted nano seconds in one NTP
    interval.

:``xtime_remainder``:
    Shifted nano seconds left over when rounding
    ``cycle_interval``

:``raw_interval``:
    Raw nano seconds accumulated per NTP interval.

:``ntp_error``:
    Difference between accumulated time and NTP time in ntp
    shifted nano seconds.

:``ntp_error_shift``:
    Shift conversion between clock shifted nano seconds and
    ntp shifted nano seconds.

:``last_warning``:
    Warning ratelimiter (DEBUG_TIMEKEEPING)

:``underflow_seen``:
    Underflow warning flag (DEBUG_TIMEKEEPING)

:``overflow_seen``:
    Overflow warning flag (DEBUG_TIMEKEEPING)




.. _`timekeeper.note`:

Note
----

For timespec(64) based interfaces wall_to_monotonic is what
we need to add to xtime (or xtime corrected for sub jiffie times)
to get to monotonic time.  Monotonic is pegged at zero at system
boot time, so wall_to_monotonic will be negative, however, we will
ALWAYS keep the tv_nsec part positive so we can use the usual
normalization.

wall_to_monotonic is moved after resume from suspend for the
monotonic time not to jump. We need to add total_sleep_time to
wall_to_monotonic to get the real boot based time offset.

wall_to_monotonic is no longer the boot time, getboottime must be
used instead.

