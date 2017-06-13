.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/time/sched_clock.c

.. _`clock_read_data`:

struct clock_read_data
======================

.. c:type:: struct clock_read_data

    data required to read from \ :c:func:`sched_clock`\ 

.. _`clock_read_data.definition`:

Definition
----------

.. code-block:: c

    struct clock_read_data {
        u64 epoch_ns;
        u64 epoch_cyc;
        u64 sched_clock_mask;
        u64 (*read_sched_clock)(void);
        u32 mult;
        u32 shift;
    }

.. _`clock_read_data.members`:

Members
-------

epoch_ns
    sched_clock() value at last update

epoch_cyc
    Clock cycle value at last update.

sched_clock_mask
    Bitmask for two's complement subtraction of non 64bit
    clocks.

read_sched_clock
    Current clock source (or dummy source when suspended).

mult
    Multipler for scaled math conversion.

shift
    Shift value for scaled math conversion.

.. _`clock_read_data.description`:

Description
-----------

Care must be taken when updating this structure; it is read by
some very hot code paths. It occupies <=40 bytes and, when combined
with the seqcount used to synchronize access, comfortably fits into
a 64 byte cache line.

.. _`clock_data`:

struct clock_data
=================

.. c:type:: struct clock_data

    all data needed for \ :c:func:`sched_clock`\  (including registration of a new clock source)

.. _`clock_data.definition`:

Definition
----------

.. code-block:: c

    struct clock_data {
        seqcount_t seq;
        struct clock_read_data read_data;
        ktime_t wrap_kt;
        unsigned long rate;
        u64 (*actual_read_sched_clock)(void);
    }

.. _`clock_data.members`:

Members
-------

seq
    Sequence counter for protecting updates. The lowest
    bit is the index for \ ``read_data``\ .

read_data
    Data required to read from sched_clock.

wrap_kt
    Duration for which clock can run before wrapping.

rate
    Tick rate of the registered clock.

actual_read_sched_clock
    Registered hardware level clock read function.

.. _`clock_data.description`:

Description
-----------

The ordering of this structure has been chosen to optimize cache
performance. In particular 'seq' and 'read_data[0]' (combined) should fit
into a single 64-byte cache line.

.. This file was automatic generated / don't edit.

