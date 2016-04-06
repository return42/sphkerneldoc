
.. _API-blk-release-queue:

=================
blk_release_queue
=================

*man blk_release_queue(9)*

*4.6.0-rc1*

release a ``struct request_queue`` when it is no longer needed


Synopsis
========

.. c:function:: void blk_release_queue( struct kobject * kobj )

Arguments
=========

``kobj``
    the kobj belonging to the request queue to be released


Description
===========

blk_release_queue is the pair to ``blk_init_queue`` or ``blk_queue_make_request``. It should be called when a request queue is being released; typically when a block device is
being de-registered. Currently, its primary task it to free all the ``struct request`` structures that were allocated to the queue and the queue itself.


Note
====

The low level driver must have finished any outstanding requests first via ``blk_cleanup_queue``.
