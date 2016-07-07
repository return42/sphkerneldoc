.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/codel.h

.. _`codel_params`:

struct codel_params
===================

.. c:type:: struct codel_params

    contains codel parameters

.. _`codel_params.definition`:

Definition
----------

.. code-block:: c

    struct codel_params {
        codel_time_t target;
        codel_time_t ce_threshold;
        codel_time_t interval;
        u32 mtu;
        bool ecn;
    }

.. _`codel_params.members`:

Members
-------

target
    target queue size (in time units)

ce_threshold
    threshold for marking packets with ECN CE

interval
    width of moving time window

mtu
    device mtu, or minimal queue backlog in bytes.

ecn
    is Explicit Congestion Notification enabled

.. _`codel_vars`:

struct codel_vars
=================

.. c:type:: struct codel_vars

    contains codel variables

.. _`codel_vars.definition`:

Definition
----------

.. code-block:: c

    struct codel_vars {
        u32 count;
        u32 lastcount;
        bool dropping;
        u16 rec_inv_sqrt;
        codel_time_t first_above_time;
        codel_time_t drop_next;
        codel_time_t ldelay;
    }

.. _`codel_vars.members`:

Members
-------

count
    how many drops we've done since the last time we
    entered dropping state

lastcount
    count at entry to dropping state

dropping
    set to true if in dropping state

rec_inv_sqrt
    reciprocal value of sqrt(count) >> 1

first_above_time
    when we went (or will go) continuously above target
    for interval

drop_next
    time to drop next packet, or when we dropped last

ldelay
    sojourn time of last dequeued packet

.. _`codel_stats`:

struct codel_stats
==================

.. c:type:: struct codel_stats

    contains codel shared variables and stats

.. _`codel_stats.definition`:

Definition
----------

.. code-block:: c

    struct codel_stats {
        u32 maxpacket;
        u32 drop_count;
        u32 drop_len;
        u32 ecn_mark;
        u32 ce_mark;
    }

.. _`codel_stats.members`:

Members
-------

maxpacket
    largest packet we've seen so far

drop_count
    temp count of dropped packets in \ :c:func:`dequeue`\ 

drop_len
    bytes of dropped packets in \ :c:func:`dequeue`\ 

ecn_mark
    *undescribed*

ce_mark
    *undescribed*

.. _`codel_stats.ecn_mark`:

ecn_mark
--------

number of packets we ECN marked instead of dropping

.. _`codel_stats.ce_mark`:

ce_mark
-------

number of packets CE marked because sojourn time was above ce_threshold

.. This file was automatic generated / don't edit.

