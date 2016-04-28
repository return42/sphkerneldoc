.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-queue-max-hw-sectors:

========================
blk_queue_max_hw_sectors
========================

*man blk_queue_max_hw_sectors(9)*

*4.6.0-rc5*

set max sectors for a request for this queue


Synopsis
========

.. c:function:: void blk_queue_max_hw_sectors( struct request_queue * q, unsigned int max_hw_sectors )

Arguments
=========

``q``
    the request queue for the device

``max_hw_sectors``
    max hardware sectors in the usual 512b unit


Description
===========

Enables a low level driver to set a hard upper limit, max_hw_sectors,
on the size of requests. max_hw_sectors is set by the device driver
based upon the capabilities of the I/O controller.

max_dev_sectors is a hard limit imposed by the storage device for
READ/WRITE requests. It is set by the disk driver.

max_sectors is a soft limit imposed by the block layer for filesystem
type requests. This value can be overridden on a per-device basis in
/sys/block/<device>/queue/max_sectors_kb. The soft limit can not
exceed max_hw_sectors.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
