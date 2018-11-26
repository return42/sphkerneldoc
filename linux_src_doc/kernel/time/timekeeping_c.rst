.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/time/timekeeping.c

.. _`tk_fast`:

struct tk_fast
==============

.. c:type:: struct tk_fast

    NMI safe timekeeper

.. _`tk_fast.definition`:

Definition
----------

.. code-block:: c

    struct tk_fast {
        seqcount_t seq;
        struct tk_read_base base[2];
    }

.. _`tk_fast.members`:

Members
-------

seq
    Sequence counter for protecting updates. The lowest bit
    is the index for the tk_read_base array

base
    tk_read_base array. Access is indexed by the lowest bit of
    \ ``seq``\ .

.. _`tk_fast.description`:

Description
-----------

See \ ``update_fast_timekeeper``\ () below.

.. _`tk_setup_internals`:

tk_setup_internals
==================

.. c:function:: void tk_setup_internals(struct timekeeper *tk, struct clocksource *clock)

    Set up internals to use clocksource clock.

    :param tk:
        The target timekeeper to setup.
    :type tk: struct timekeeper \*

    :param clock:
        Pointer to clocksource.
    :type clock: struct clocksource \*

.. _`tk_setup_internals.description`:

Description
-----------

Calculates a fixed cycle/nsec interval for a given clocksource/adjustment
pair and interval request.

Unless you're the timekeeping code, you should not be using this!

.. _`update_fast_timekeeper`:

update_fast_timekeeper
======================

.. c:function:: void update_fast_timekeeper(const struct tk_read_base *tkr, struct tk_fast *tkf)

    Update the fast and NMI safe monotonic timekeeper.

    :param tkr:
        Timekeeping readout base from which we take the update
    :type tkr: const struct tk_read_base \*

    :param tkf:
        *undescribed*
    :type tkf: struct tk_fast \*

.. _`update_fast_timekeeper.description`:

Description
-----------

We want to use this from any context including NMI and tracing /
instrumenting the timekeeping code itself.

Employ the latch technique; see \ ``raw_write_seqcount_latch``\ .

So if a NMI hits the update of base[0] then it will use base[1]
which is still consistent. In the worst case this can result is a
slightly wrong timestamp (a few nanoseconds). See
\ ``ktime_get_mono_fast_ns``\ .

.. _`__ktime_get_fast_ns`:

\__ktime_get_fast_ns
====================

.. c:function:: u64 __ktime_get_fast_ns(struct tk_fast *tkf)

    Fast NMI safe access to clock monotonic

    :param tkf:
        *undescribed*
    :type tkf: struct tk_fast \*

.. _`__ktime_get_fast_ns.description`:

Description
-----------

This timestamp is not guaranteed to be monotonic across an update.

.. _`__ktime_get_fast_ns.the-timestamp-is-calculated-by`:

The timestamp is calculated by
------------------------------


now = base_mono + clock_delta \* slope

So if the update lowers the slope, readers who are forced to the
not yet updated second array are still using the old steeper slope.

tmono
^
\|    o  n
\|   o n
\|  u
\| o
\|o
\|12345678---> reader order

o = old slope
u = update
n = new slope

So reader 6 will observe time going backwards versus reader 5.

While other CPUs are likely to be able observe that, the only way
for a CPU local observation is when an NMI hits in the middle of
the update. Timestamps taken from that NMI context might be ahead
of the following timestamps. Callers need to be aware of that and
deal with it.

.. _`ktime_get_boot_fast_ns`:

ktime_get_boot_fast_ns
======================

.. c:function:: u64 notrace ktime_get_boot_fast_ns( void)

    NMI safe and fast access to boot clock.

    :param void:
        no arguments
    :type void: 

.. _`ktime_get_boot_fast_ns.description`:

Description
-----------

To keep it NMI safe since we're accessing from tracing, we're not using a
separate timekeeper with updates to monotonic clock and boot offset
protected with seqlocks. This has the following minor side effects:

(1) Its possible that a timestamp be taken after the boot offset is updated
but before the timekeeper is updated. If this happens, the new boot offset
is added to the old timekeeping making the clock appear to update slightly

.. _`ktime_get_boot_fast_ns.earlier`:

earlier
-------

CPU 0                                        CPU 1
\ :c:func:`timekeeping_inject_sleeptime64`\ 
\__timekeeping_inject_sleeptime(tk, delta);
\ :c:func:`timestamp`\ ;
timekeeping_update(tk, TK_CLEAR_NTP...);

(2) On 32-bit systems, the 64-bit boot offset (tk->offs_boot) may be
partially updated.  Since the tk->offs_boot update is a rare event, this
should be a rare occurrence which postprocessing should be able to handle.

.. _`ktime_get_real_fast_ns`:

ktime_get_real_fast_ns
======================

.. c:function:: u64 ktime_get_real_fast_ns( void)

    - NMI safe and fast access to clock realtime.

    :param void:
        no arguments
    :type void: 

.. _`halt_fast_timekeeper`:

halt_fast_timekeeper
====================

.. c:function:: void halt_fast_timekeeper(const struct timekeeper *tk)

    Prevent fast timekeeper from accessing clocksource.

    :param tk:
        Timekeeper to snapshot.
    :type tk: const struct timekeeper \*

.. _`halt_fast_timekeeper.description`:

Description
-----------

It generally is unsafe to access the clocksource after timekeeping has been
suspended, so take a snapshot of the readout base of \ ``tk``\  and use it as the
fast timekeeper's readout base while suspended.  It will return the same
number of cycles every time until timekeeping is resumed at which time the
proper readout base for the fast timekeeper will be restored automatically.

.. _`pvclock_gtod_register_notifier`:

pvclock_gtod_register_notifier
==============================

.. c:function:: int pvclock_gtod_register_notifier(struct notifier_block *nb)

    register a pvclock timedata update listener

    :param nb:
        *undescribed*
    :type nb: struct notifier_block \*

.. _`pvclock_gtod_unregister_notifier`:

pvclock_gtod_unregister_notifier
================================

.. c:function:: int pvclock_gtod_unregister_notifier(struct notifier_block *nb)

    unregister a pvclock timedata update listener

    :param nb:
        *undescribed*
    :type nb: struct notifier_block \*

.. _`timekeeping_forward_now`:

timekeeping_forward_now
=======================

.. c:function:: void timekeeping_forward_now(struct timekeeper *tk)

    update clock to the current time

    :param tk:
        *undescribed*
    :type tk: struct timekeeper \*

.. _`timekeeping_forward_now.description`:

Description
-----------

Forward the current clock to update its state since the last call to
\ :c:func:`update_wall_time`\ . This is useful before significant clock changes,
as it avoids having to deal with this time offset explicitly.

.. _`ktime_get_real_ts64`:

ktime_get_real_ts64
===================

.. c:function:: void ktime_get_real_ts64(struct timespec64 *ts)

    Returns the time of day in a timespec64.

    :param ts:
        pointer to the timespec to be set
    :type ts: struct timespec64 \*

.. _`ktime_get_real_ts64.description`:

Description
-----------

Returns the time of day in a timespec64 (WARN if suspended).

.. _`ktime_mono_to_any`:

ktime_mono_to_any
=================

.. c:function:: ktime_t ktime_mono_to_any(ktime_t tmono, enum tk_offsets offs)

    convert mononotic time to any other time

    :param tmono:
        time to convert.
    :type tmono: ktime_t

    :param offs:
        which offset to use
    :type offs: enum tk_offsets

.. _`ktime_get_raw`:

ktime_get_raw
=============

.. c:function:: ktime_t ktime_get_raw( void)

    Returns the raw monotonic time in ktime_t format

    :param void:
        no arguments
    :type void: 

.. _`ktime_get_ts64`:

ktime_get_ts64
==============

.. c:function:: void ktime_get_ts64(struct timespec64 *ts)

    get the monotonic clock in timespec64 format

    :param ts:
        pointer to timespec variable
    :type ts: struct timespec64 \*

.. _`ktime_get_ts64.description`:

Description
-----------

The function calculates the monotonic clock from the realtime
clock and the wall_to_monotonic offset and stores the result
in normalized timespec64 format in the variable pointed to by \ ``ts``\ .

.. _`ktime_get_seconds`:

ktime_get_seconds
=================

.. c:function:: time64_t ktime_get_seconds( void)

    Get the seconds portion of CLOCK_MONOTONIC

    :param void:
        no arguments
    :type void: 

.. _`ktime_get_seconds.description`:

Description
-----------

Returns the seconds portion of CLOCK_MONOTONIC with a single non
serialized read. tk->ktime_sec is of type 'unsigned long' so this
works on both 32 and 64 bit systems. On 32 bit systems the readout
covers ~136 years of uptime which should be enough to prevent
premature wrap arounds.

.. _`ktime_get_real_seconds`:

ktime_get_real_seconds
======================

.. c:function:: time64_t ktime_get_real_seconds( void)

    Get the seconds portion of CLOCK_REALTIME

    :param void:
        no arguments
    :type void: 

.. _`ktime_get_real_seconds.description`:

Description
-----------

Returns the wall clock seconds since 1970. This replaces the
\ :c:func:`get_seconds`\  interface which is not y2038 safe on 32bit systems.

For 64bit systems the fast access to tk->xtime_sec is preserved. On
32bit systems the access must be protected with the sequence
counter to provide "atomic" access to the 64bit tk->xtime_sec
value.

.. _`__ktime_get_real_seconds`:

\__ktime_get_real_seconds
=========================

.. c:function:: time64_t __ktime_get_real_seconds( void)

    The same as ktime_get_real_seconds but without the sequence counter protect. This internal function is called just when timekeeping lock is already held.

    :param void:
        no arguments
    :type void: 

.. _`ktime_get_snapshot`:

ktime_get_snapshot
==================

.. c:function:: void ktime_get_snapshot(struct system_time_snapshot *systime_snapshot)

    snapshots the realtime/monotonic raw clocks with counter

    :param systime_snapshot:
        pointer to struct receiving the system time snapshot
    :type systime_snapshot: struct system_time_snapshot \*

.. _`adjust_historical_crosststamp`:

adjust_historical_crosststamp
=============================

.. c:function:: int adjust_historical_crosststamp(struct system_time_snapshot *history, u64 partial_history_cycles, u64 total_history_cycles, bool discontinuity, struct system_device_crosststamp *ts)

    adjust crosstimestamp previous to current interval

    :param history:
        Snapshot representing start of history
    :type history: struct system_time_snapshot \*

    :param partial_history_cycles:
        Cycle offset into history (fractional part)
    :type partial_history_cycles: u64

    :param total_history_cycles:
        Total history length in cycles
    :type total_history_cycles: u64

    :param discontinuity:
        True indicates clock was set on history period
    :type discontinuity: bool

    :param ts:
        Cross timestamp that should be adjusted using
        partial/total ratio
    :type ts: struct system_device_crosststamp \*

.. _`adjust_historical_crosststamp.description`:

Description
-----------

Helper function used by \ :c:func:`get_device_system_crosststamp`\  to correct the
crosstimestamp corresponding to the start of the current interval to the
system counter value (timestamp point) provided by the driver. The
total_history\_\* quantities are the total history starting at the provided
reference point and ending at the start of the current interval. The cycle
count between the driver timestamp point and the start of the current
interval is partial_history_cycles.

.. _`get_device_system_crosststamp`:

get_device_system_crosststamp
=============================

.. c:function:: int get_device_system_crosststamp(int (*get_time_fn)(ktime_t *device_time, struct system_counterval_t *sys_counterval, void *ctx), void *ctx, struct system_time_snapshot *history_begin, struct system_device_crosststamp *xtstamp)

    Synchronously capture system/device timestamp

    :param int (\*get_time_fn)(ktime_t \*device_time, struct system_counterval_t \*sys_counterval, void \*ctx):
        Callback to get simultaneous device time and
        system counter from the device driver

    :param ctx:
        Context passed to \ :c:func:`get_time_fn`\ 
    :type ctx: void \*

    :param history_begin:
        Historical reference point used to interpolate system
        time when counter provided by the driver is before the current interval
    :type history_begin: struct system_time_snapshot \*

    :param xtstamp:
        Receives simultaneously captured system and device time
    :type xtstamp: struct system_device_crosststamp \*

.. _`get_device_system_crosststamp.description`:

Description
-----------

Reads a timestamp from a device and correlates it to system time

.. _`do_settimeofday64`:

do_settimeofday64
=================

.. c:function:: int do_settimeofday64(const struct timespec64 *ts)

    Sets the time of day.

    :param ts:
        pointer to the timespec64 variable containing the new time
    :type ts: const struct timespec64 \*

.. _`do_settimeofday64.description`:

Description
-----------

Sets the time of day to the new time and update NTP and notify hrtimers

.. _`timekeeping_inject_offset`:

timekeeping_inject_offset
=========================

.. c:function:: int timekeeping_inject_offset(const struct timespec64 *ts)

    Adds or subtracts from the current time.

    :param ts:
        *undescribed*
    :type ts: const struct timespec64 \*

.. _`timekeeping_inject_offset.description`:

Description
-----------

Adds or subtracts an offset value from the current time.

.. _`__timekeeping_set_tai_offset`:

\__timekeeping_set_tai_offset
=============================

.. c:function:: void __timekeeping_set_tai_offset(struct timekeeper *tk, s32 tai_offset)

    Sets the TAI offset from UTC and monotonic

    :param tk:
        *undescribed*
    :type tk: struct timekeeper \*

    :param tai_offset:
        *undescribed*
    :type tai_offset: s32

.. _`change_clocksource`:

change_clocksource
==================

.. c:function:: int change_clocksource(void *data)

    Swaps clocksources if a new one is available

    :param data:
        *undescribed*
    :type data: void \*

.. _`change_clocksource.description`:

Description
-----------

Accumulates current time interval and initializes new clocksource

.. _`timekeeping_notify`:

timekeeping_notify
==================

.. c:function:: int timekeeping_notify(struct clocksource *clock)

    Install a new clock source

    :param clock:
        pointer to the clock source
    :type clock: struct clocksource \*

.. _`timekeeping_notify.description`:

Description
-----------

This function is called from clocksource.c after a new, better clock
source has been registered. The caller holds the clocksource_mutex.

.. _`ktime_get_raw_ts64`:

ktime_get_raw_ts64
==================

.. c:function:: void ktime_get_raw_ts64(struct timespec64 *ts)

    Returns the raw monotonic time in a timespec

    :param ts:
        pointer to the timespec64 to be set
    :type ts: struct timespec64 \*

.. _`ktime_get_raw_ts64.description`:

Description
-----------

Returns the raw monotonic time (completely un-modified by ntp)

.. _`timekeeping_valid_for_hres`:

timekeeping_valid_for_hres
==========================

.. c:function:: int timekeeping_valid_for_hres( void)

    Check if timekeeping is suitable for hres

    :param void:
        no arguments
    :type void: 

.. _`timekeeping_max_deferment`:

timekeeping_max_deferment
=========================

.. c:function:: u64 timekeeping_max_deferment( void)

    Returns max time the clocksource can be deferred

    :param void:
        no arguments
    :type void: 

.. _`read_persistent_clock`:

read_persistent_clock
=====================

.. c:function:: void read_persistent_clock(struct timespec *ts)

    Return time from the persistent clock.

    :param ts:
        *undescribed*
    :type ts: struct timespec \*

.. _`read_persistent_clock.description`:

Description
-----------

Weak dummy function for arches that do not yet support it.
Reads the time from the battery backed persistent clock.
Returns a timespec with tv_sec=0 and tv_nsec=0 if unsupported.

XXX - Do be sure to remove it once all arches implement it.

.. _`read_persistent_wall_and_boot_offset`:

read_persistent_wall_and_boot_offset
====================================

.. c:function:: void read_persistent_wall_and_boot_offset(struct timespec64 *wall_time, struct timespec64 *boot_offset)

    Read persistent clock, and also offset from the boot.

    :param wall_time:
        *undescribed*
    :type wall_time: struct timespec64 \*

    :param boot_offset:
        *undescribed*
    :type boot_offset: struct timespec64 \*

.. _`read_persistent_wall_and_boot_offset.description`:

Description
-----------

Weak dummy function for arches that do not yet support it.
wall_time    - current time as returned by persistent clock
boot_offset  - offset that is defined as wall_time - boot_time
The default function calculates offset based on the current value of
\ :c:func:`local_clock`\ . This way architectures that support \ :c:func:`sched_clock`\  but don't
support dedicated boot time clock will provide the best estimate of the
boot time.

.. _`__timekeeping_inject_sleeptime`:

\__timekeeping_inject_sleeptime
===============================

.. c:function:: void __timekeeping_inject_sleeptime(struct timekeeper *tk, const struct timespec64 *delta)

    Internal function to add sleep interval

    :param tk:
        *undescribed*
    :type tk: struct timekeeper \*

    :param delta:
        pointer to a timespec delta value
    :type delta: const struct timespec64 \*

.. _`__timekeeping_inject_sleeptime.description`:

Description
-----------

Takes a timespec offset measuring a suspend interval and properly
adds the sleep offset to the timekeeping variables.

.. _`timekeeping_rtc_skipresume`:

timekeeping_rtc_skipresume
==========================

.. c:function:: bool timekeeping_rtc_skipresume( void)

    injection, the preference order is: 1) non-stop clocksource 2) persistent clock (ie: RTC accessible when irqs are off) 3) RTC

    :param void:
        no arguments
    :type void: 

.. _`timekeeping_rtc_skipresume.description`:

Description
-----------

1) and 2) are used by timekeeping, 3) by RTC subsystem.
If system has neither 1) nor 2), 3) will be used finally.


If timekeeping has injected sleeptime via either 1) or 2),
3) becomes needless, so in this case we don't need to call
\ :c:func:`rtc_resume`\ , and this is what \ :c:func:`timekeeping_rtc_skipresume`\ 
means.

.. _`timekeeping_rtc_skipsuspend`:

timekeeping_rtc_skipsuspend
===========================

.. c:function:: bool timekeeping_rtc_skipsuspend( void)

    \ :c:func:`timekeeping_resume`\  which is invoked after \ :c:func:`rtc_suspend`\ , so we can't skip \ :c:func:`rtc_suspend`\  surely if system has 1).

    :param void:
        no arguments
    :type void: 

.. _`timekeeping_rtc_skipsuspend.description`:

Description
-----------

But if system has 2), 2) will definitely be used, so in this
case we don't need to call \ :c:func:`rtc_suspend`\ , and this is what
\ :c:func:`timekeeping_rtc_skipsuspend`\  means.

.. _`timekeeping_inject_sleeptime64`:

timekeeping_inject_sleeptime64
==============================

.. c:function:: void timekeeping_inject_sleeptime64(const struct timespec64 *delta)

    Adds suspend interval to timeekeeping values

    :param delta:
        pointer to a timespec64 delta value
    :type delta: const struct timespec64 \*

.. _`timekeeping_inject_sleeptime64.description`:

Description
-----------

This hook is for architectures that cannot support read_persistent_clock64
because their RTC/persistent clock is only accessible when irqs are enabled.
and also don't have an effective nonstop clocksource.

This function should only be called by \ :c:func:`rtc_resume`\ , and allows
a suspend offset to be injected into the timekeeping values.

.. _`timekeeping_resume`:

timekeeping_resume
==================

.. c:function:: void timekeeping_resume( void)

    Resumes the generic timekeeping subsystem.

    :param void:
        no arguments
    :type void: 

.. _`accumulate_nsecs_to_secs`:

accumulate_nsecs_to_secs
========================

.. c:function:: unsigned int accumulate_nsecs_to_secs(struct timekeeper *tk)

    Accumulates nsecs into secs

    :param tk:
        *undescribed*
    :type tk: struct timekeeper \*

.. _`accumulate_nsecs_to_secs.description`:

Description
-----------

Helper function that accumulates the nsecs greater than a second
from the xtime_nsec field to the xtime_secs field.
It also calls into the NTP code to handle leapsecond processing.

.. _`logarithmic_accumulation`:

logarithmic_accumulation
========================

.. c:function:: u64 logarithmic_accumulation(struct timekeeper *tk, u64 offset, u32 shift, unsigned int *clock_set)

    shifted accumulation of cycles

    :param tk:
        *undescribed*
    :type tk: struct timekeeper \*

    :param offset:
        *undescribed*
    :type offset: u64

    :param shift:
        *undescribed*
    :type shift: u32

    :param clock_set:
        *undescribed*
    :type clock_set: unsigned int \*

.. _`logarithmic_accumulation.description`:

Description
-----------

This functions accumulates a shifted interval of cycles into
into a shifted interval nanoseconds. Allows for O(log) accumulation
loop.

Returns the unconsumed cycles.

.. _`update_wall_time`:

update_wall_time
================

.. c:function:: void update_wall_time( void)

    Uses the current clocksource to increment the wall time

    :param void:
        no arguments
    :type void: 

.. _`getboottime64`:

getboottime64
=============

.. c:function:: void getboottime64(struct timespec64 *ts)

    Return the real time of system boot.

    :param ts:
        pointer to the timespec64 to be set
    :type ts: struct timespec64 \*

.. _`getboottime64.description`:

Description
-----------

Returns the wall-time of boot in a timespec64.

This is based on the wall_to_monotonic offset and the total suspend
time. Calls to settimeofday will affect the value returned (which
basically means that however wrong your real time clock is at boot time,
you get the right time here).

.. _`ktime_get_update_offsets_now`:

ktime_get_update_offsets_now
============================

.. c:function:: ktime_t ktime_get_update_offsets_now(unsigned int *cwsseq, ktime_t *offs_real, ktime_t *offs_boot, ktime_t *offs_tai)

    hrtimer helper

    :param cwsseq:
        pointer to check and store the clock was set sequence number
    :type cwsseq: unsigned int \*

    :param offs_real:
        pointer to storage for monotonic -> realtime offset
    :type offs_real: ktime_t \*

    :param offs_boot:
        pointer to storage for monotonic -> boottime offset
    :type offs_boot: ktime_t \*

    :param offs_tai:
        pointer to storage for monotonic -> clock tai offset
    :type offs_tai: ktime_t \*

.. _`ktime_get_update_offsets_now.description`:

Description
-----------

Returns current monotonic time and updates the offsets if the
sequence number in \ ``cwsseq``\  and timekeeper.clock_was_set_seq are
different.

Called from \ :c:func:`hrtimer_interrupt`\  or \ :c:func:`retrigger_next_event`\ 

.. _`timekeeping_validate_timex`:

timekeeping_validate_timex
==========================

.. c:function:: int timekeeping_validate_timex(const struct timex *txc)

    Ensures the timex is ok for use in do_adjtimex

    :param txc:
        *undescribed*
    :type txc: const struct timex \*

.. _`do_adjtimex`:

do_adjtimex
===========

.. c:function:: int do_adjtimex(struct timex *txc)

    Accessor function to NTP \__do_adjtimex function

    :param txc:
        *undescribed*
    :type txc: struct timex \*

.. _`hardpps`:

hardpps
=======

.. c:function:: void hardpps(const struct timespec64 *phase_ts, const struct timespec64 *raw_ts)

    Accessor function to NTP \__hardpps function

    :param phase_ts:
        *undescribed*
    :type phase_ts: const struct timespec64 \*

    :param raw_ts:
        *undescribed*
    :type raw_ts: const struct timespec64 \*

.. _`xtime_update`:

xtime_update
============

.. c:function:: void xtime_update(unsigned long ticks)

    advances the timekeeping infrastructure

    :param ticks:
        number of ticks, that have elapsed since the last call.
    :type ticks: unsigned long

.. _`xtime_update.description`:

Description
-----------

Must be called with interrupts disabled.

.. This file was automatic generated / don't edit.

