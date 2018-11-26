.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/timecounter.h

.. _`cyclecounter`:

struct cyclecounter
===================

.. c:type:: struct cyclecounter

    hardware abstraction for a free running counter Provides completely state-free accessors to the underlying hardware. Depending on which hardware it reads, the cycle counter may wrap around quickly. Locking rules (if necessary) have to be defined by the implementor and user of specific instances of this API.

.. _`cyclecounter.definition`:

Definition
----------

.. code-block:: c

    struct cyclecounter {
        u64 (*read)(const struct cyclecounter *cc);
        u64 mask;
        u32 mult;
        u32 shift;
    }

.. _`cyclecounter.members`:

Members
-------

read
    returns the current cycle value

mask
    bitmask for two's complement
    subtraction of non 64 bit counters,
    see \ :c:func:`CYCLECOUNTER_MASK`\  helper macro

mult
    cycle to nanosecond multiplier

shift
    cycle to nanosecond divisor (power of two)

.. _`timecounter`:

struct timecounter
==================

.. c:type:: struct timecounter

    layer above a \ ``struct``\  cyclecounter which counts nanoseconds Contains the state needed by \ :c:func:`timecounter_read`\  to detect cycle counter wrap around. Initialize with \ :c:func:`timecounter_init`\ . Also used to convert cycle counts into the corresponding nanosecond counts with \ :c:func:`timecounter_cyc2time`\ . Users of this code are responsible for initializing the underlying cycle counter hardware, locking issues and reading the time more often than the cycle counter wraps around. The nanosecond counter will only wrap around after ~585 years.

.. _`timecounter.definition`:

Definition
----------

.. code-block:: c

    struct timecounter {
        const struct cyclecounter *cc;
        u64 cycle_last;
        u64 nsec;
        u64 mask;
        u64 frac;
    }

.. _`timecounter.members`:

Members
-------

cc
    the cycle counter used by this instance

cycle_last
    most recent cycle counter value seen by
    \ :c:func:`timecounter_read`\ 

nsec
    continuously increasing count

mask
    bit mask for maintaining the 'frac' field

frac
    accumulated fractional nanoseconds

.. _`cyclecounter_cyc2ns`:

cyclecounter_cyc2ns
===================

.. c:function:: u64 cyclecounter_cyc2ns(const struct cyclecounter *cc, u64 cycles, u64 mask, u64 *frac)

    converts cycle counter cycles to nanoseconds

    :param cc:
        Pointer to cycle counter.
    :type cc: const struct cyclecounter \*

    :param cycles:
        Cycles
    :type cycles: u64

    :param mask:
        bit mask for maintaining the 'frac' field
    :type mask: u64

    :param frac:
        pointer to storage for the fractional nanoseconds.
    :type frac: u64 \*

.. _`timecounter_adjtime`:

timecounter_adjtime
===================

.. c:function:: void timecounter_adjtime(struct timecounter *tc, s64 delta)

    Shifts the time of the clock.

    :param tc:
        *undescribed*
    :type tc: struct timecounter \*

    :param delta:
        Desired change in nanoseconds.
    :type delta: s64

.. _`timecounter_init`:

timecounter_init
================

.. c:function:: void timecounter_init(struct timecounter *tc, const struct cyclecounter *cc, u64 start_tstamp)

    initialize a time counter

    :param tc:
        Pointer to time counter which is to be initialized/reset
    :type tc: struct timecounter \*

    :param cc:
        A cycle counter, ready to be used.
    :type cc: const struct cyclecounter \*

    :param start_tstamp:
        Arbitrary initial time stamp.
    :type start_tstamp: u64

.. _`timecounter_init.description`:

Description
-----------

After this call the current cycle register (roughly) corresponds to
the initial time stamp. Every call to \ :c:func:`timecounter_read`\  increments
the time stamp counter by the number of elapsed nanoseconds.

.. _`timecounter_read`:

timecounter_read
================

.. c:function:: u64 timecounter_read(struct timecounter *tc)

    return nanoseconds elapsed since \ :c:func:`timecounter_init`\  plus the initial time stamp

    :param tc:
        Pointer to time counter.
    :type tc: struct timecounter \*

.. _`timecounter_read.description`:

Description
-----------

In other words, keeps track of time since the same epoch as
the function which generated the initial time stamp.

.. _`timecounter_cyc2time`:

timecounter_cyc2time
====================

.. c:function:: u64 timecounter_cyc2time(struct timecounter *tc, u64 cycle_tstamp)

    convert a cycle counter to same time base as values returned by \ :c:func:`timecounter_read`\ 

    :param tc:
        Pointer to time counter.
    :type tc: struct timecounter \*

    :param cycle_tstamp:
        a value returned by tc->cc->read()
    :type cycle_tstamp: u64

.. _`timecounter_cyc2time.description`:

Description
-----------

Cycle counts that are converted correctly as long as they
fall into the interval [-1/2 max cycle count, +1/2 max cycle count],
with "max cycle count" == cs->mask+1.

This allows conversion of cycle counter values which were generated
in the past.

.. This file was automatic generated / don't edit.

