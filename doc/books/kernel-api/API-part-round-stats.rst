.. -*- coding: utf-8; mode: rst -*-

.. _API-part-round-stats:

================
part_round_stats
================

*man part_round_stats(9)*

*4.6.0-rc5*

Round off the performance stats on a struct disk_stats.


Synopsis
========

.. c:function:: void part_round_stats( int cpu, struct hd_struct * part )

Arguments
=========

``cpu``
    cpu number for stats access

``part``
    target partition


Description
===========

The average IO queue length and utilisation statistics are maintained by
observing the current state of the queue length and the amount of time
it has been in this state for.

Normally, that accounting is done on IO completion, but that can result
in more than a second's worth of IO being accounted for within any one
second, leading to >100% utilisation. To deal with that, we call this
function to do a round-off before returning the results when reading
/proc/diskstats. This accounts immediately for all queue usage up to the
current jiffies and restarts the counters again.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
