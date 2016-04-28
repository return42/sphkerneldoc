.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-gnet-stats-queue:

=======================
struct gnet_stats_queue
=======================

*man struct gnet_stats_queue(9)*

*4.6.0-rc5*

queuing statistics


Synopsis
========

.. code-block:: c

    struct gnet_stats_queue {
      __u32 qlen;
      __u32 backlog;
      __u32 drops;
      __u32 requeues;
      __u32 overlimits;
    };


Members
=======

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
