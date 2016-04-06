
.. _API-disk-block-events:

=================
disk_block_events
=================

*man disk_block_events(9)*

*4.6.0-rc1*

block and flush disk event checking


Synopsis
========

.. c:function:: void disk_block_events( struct gendisk * disk )

Arguments
=========

``disk``
    disk to block events for


Description
===========

On return from this function, it is guaranteed that event checking isn't in progress and won't happen until unblocked by ``disk_unblock_events``. Events blocking is counted and the
actual unblocking happens after the matching number of unblocks are done.

Note that this intentionally does not block event checking from ``disk_clear_events``.


CONTEXT
=======

Might sleep.
