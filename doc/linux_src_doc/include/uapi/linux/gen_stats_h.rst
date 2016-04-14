.. -*- coding: utf-8; mode: rst -*-

===========
gen_stats.h
===========

.. _`gnet_stats_basic`:

struct gnet_stats_basic
=======================

.. c:type:: struct gnet_stats_basic

    byte/packet throughput statistics



Definition
----------

.. code-block:: c

  struct gnet_stats_basic {
    __u64 bytes;
    __u32 packets;
  };



Members
-------

:``bytes``:
    number of seen bytes

:``packets``:
    number of seen packets



.. _`gnet_stats_rate_est`:

struct gnet_stats_rate_est
==========================

.. c:type:: struct gnet_stats_rate_est

    rate estimator



Definition
----------

.. code-block:: c

  struct gnet_stats_rate_est {
    __u32 bps;
    __u32 pps;
  };



Members
-------

:``bps``:
    current byte rate

:``pps``:
    current packet rate



.. _`gnet_stats_rate_est64`:

struct gnet_stats_rate_est64
============================

.. c:type:: struct gnet_stats_rate_est64

    rate estimator



Definition
----------

.. code-block:: c

  struct gnet_stats_rate_est64 {
    __u64 bps;
    __u64 pps;
  };



Members
-------

:``bps``:
    current byte rate

:``pps``:
    current packet rate



.. _`gnet_stats_queue`:

struct gnet_stats_queue
=======================

.. c:type:: struct gnet_stats_queue

    queuing statistics



Definition
----------

.. code-block:: c

  struct gnet_stats_queue {
    __u32 qlen;
    __u32 backlog;
    __u32 drops;
    __u32 requeues;
    __u32 overlimits;
  };



Members
-------

:``qlen``:
    queue length

:``backlog``:
    backlog size of queue

:``drops``:
    number of dropped packets

:``requeues``:
    number of requeues

:``overlimits``:
    number of enqueues over the limit



.. _`gnet_estimator`:

struct gnet_estimator
=====================

.. c:type:: struct gnet_estimator

    rate estimator configuration



Definition
----------

.. code-block:: c

  struct gnet_estimator {
    signed char interval;
    unsigned char ewma_log;
  };



Members
-------

:``interval``:
    sampling period

:``ewma_log``:
    the log of measurement window weight


