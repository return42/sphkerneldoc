
.. _API-disk-flush-events:

=================
disk_flush_events
=================

*man disk_flush_events(9)*

*4.6.0-rc1*

schedule immediate event checking and flushing


Synopsis
========

.. c:function:: void disk_flush_events( struct gendisk * disk, unsigned int mask )

Arguments
=========

``disk``
    disk to check and flush events for

``mask``
    events to flush


Description
===========

Schedule immediate event checking on ``disk`` if not blocked. Events in ``mask`` are scheduled to be cleared from the driver. Note that this doesn't clear the events from
``disk``->ev.


CONTEXT
=======

If ``mask`` is non-zero must be called with bdev->bd_mutex held.
