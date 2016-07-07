.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/gen_stats.h

.. _`gnet_stats_basic`:

struct gnet_stats_basic
=======================

.. c:type:: struct gnet_stats_basic

    byte/packet throughput statistics

.. _`gnet_stats_basic.definition`:

Definition
----------

.. code-block:: c

    struct gnet_stats_basic {
        __u64 bytes;
        __u32 packets;
    }

.. _`gnet_stats_basic.members`:

Members
-------

bytes
    number of seen bytes

packets
    number of seen packets

.. _`gnet_stats_rate_est`:

struct gnet_stats_rate_est
==========================

.. c:type:: struct gnet_stats_rate_est

    rate estimator

.. _`gnet_stats_rate_est.definition`:

Definition
----------

.. code-block:: c

    struct gnet_stats_rate_est {
        __u32 bps;
        __u32 pps;
    }

.. _`gnet_stats_rate_est.members`:

Members
-------

bps
    current byte rate

pps
    current packet rate

.. _`gnet_stats_rate_est64`:

struct gnet_stats_rate_est64
============================

.. c:type:: struct gnet_stats_rate_est64

    rate estimator

.. _`gnet_stats_rate_est64.definition`:

Definition
----------

.. code-block:: c

    struct gnet_stats_rate_est64 {
        __u64 bps;
        __u64 pps;
    }

.. _`gnet_stats_rate_est64.members`:

Members
-------

bps
    current byte rate

pps
    current packet rate

.. _`gnet_stats_queue`:

struct gnet_stats_queue
=======================

.. c:type:: struct gnet_stats_queue

    queuing statistics

.. _`gnet_stats_queue.definition`:

Definition
----------

.. code-block:: c

    struct gnet_stats_queue {
        __u32 qlen;
        __u32 backlog;
        __u32 drops;
        __u32 requeues;
        __u32 overlimits;
    }

.. _`gnet_stats_queue.members`:

Members
-------

qlen
    queue length

backlog
    backlog size of queue

drops
    number of dropped packets

requeues
    number of requeues

overlimits
    number of enqueues over the limit

.. _`gnet_estimator`:

struct gnet_estimator
=====================

.. c:type:: struct gnet_estimator

    rate estimator configuration

.. _`gnet_estimator.definition`:

Definition
----------

.. code-block:: c

    struct gnet_estimator {
        signed char interval;
        unsigned char ewma_log;
    }

.. _`gnet_estimator.members`:

Members
-------

interval
    sampling period

ewma_log
    the log of measurement window weight

.. This file was automatic generated / don't edit.

