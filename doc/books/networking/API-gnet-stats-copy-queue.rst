.. -*- coding: utf-8; mode: rst -*-

.. _API-gnet-stats-copy-queue:

=====================
gnet_stats_copy_queue
=====================

*man gnet_stats_copy_queue(9)*

*4.6.0-rc5*

copy queue statistics into statistics TLV


Synopsis
========

.. c:function:: int gnet_stats_copy_queue( struct gnet_dump * d, struct gnet_stats_queue __percpu * cpu_q, struct gnet_stats_queue * q, __u32 qlen )

Arguments
=========

``d``
    dumping handle

``cpu_q``
    per cpu queue statistics

``q``
    queue statistics

``qlen``
    queue length statistics


Description
===========

Appends the queue statistics to the top level TLV created by
``gnet_stats_start_copy``. Using per cpu queue statistics if they are
available.

Returns 0 on success or -1 with the statistic lock released if the room
in the socket buffer was not sufficient.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
