.. -*- coding: utf-8; mode: rst -*-

.. _API-disk-clear-events:

=================
disk_clear_events
=================

*man disk_clear_events(9)*

*4.6.0-rc5*

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

Disk events are synchronously checked and pending events in ``mask`` are
cleared and returned. This ignores the block count.


CONTEXT
=======

Might sleep.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
