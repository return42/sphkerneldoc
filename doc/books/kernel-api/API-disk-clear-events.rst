
.. _API-disk-clear-events:

=================
disk_clear_events
=================

*man disk_clear_events(9)*

*4.6.0-rc1*

synchronously check, clear and return pending events


Synopsis
========

.. c:function:: unsigned int disk_clear_events( struct gendisk * disk, unsigned int mask )

Arguments
=========

``disk``
    disk to fetch and clear events from

``mask``
    mask of events to be fetched and cleared


Description
===========

Disk events are synchronously checked and pending events in ``mask`` are cleared and returned. This ignores the block count.


CONTEXT
=======

Might sleep.
