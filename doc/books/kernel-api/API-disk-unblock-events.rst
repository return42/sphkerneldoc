
.. _API-disk-unblock-events:

===================
disk_unblock_events
===================

*man disk_unblock_events(9)*

*4.6.0-rc1*

unblock disk event checking


Synopsis
========

.. c:function:: void disk_unblock_events( struct gendisk * disk )

Arguments
=========

``disk``
    disk to unblock events for


Description
===========

Undo ``disk_block_events``. When the block count reaches zero, it starts events polling if configured.


CONTEXT
=======

Don't care. Safe to call from irq context.
