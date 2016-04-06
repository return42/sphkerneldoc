
.. _API-blk-queue-virt-boundary:

=======================
blk_queue_virt_boundary
=======================

*man blk_queue_virt_boundary(9)*

*4.6.0-rc1*

set boundary rules for bio merging


Synopsis
========

.. c:function:: void blk_queue_virt_boundary( struct request_queue * q, unsigned long mask )

Arguments
=========

``q``
    the request queue for the device

``mask``
    the memory boundary mask
