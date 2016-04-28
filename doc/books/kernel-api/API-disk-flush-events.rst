.. -*- coding: utf-8; mode: rst -*-

.. _API-disk-flush-events:

=================
disk_flush_events
=================

*man disk_flush_events(9)*

*4.6.0-rc5*

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

Schedule immediate event checking on ``disk`` if not blocked. Events in
``mask`` are scheduled to be cleared from the driver. Note that this
doesn't clear the events from ``disk``->ev.


CONTEXT
=======

If ``mask`` is non-zero must be called with bdev->bd_mutex held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
