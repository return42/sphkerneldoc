.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-queue-alignment-offset:

==========================
blk_queue_alignment_offset
==========================

*man blk_queue_alignment_offset(9)*

*4.6.0-rc5*

set physical block alignment offset


Synopsis
========

.. c:function:: void blk_queue_alignment_offset( struct request_queue * q, unsigned int offset )

Arguments
=========

``q``
    the request queue for the device

``offset``
    alignment offset in bytes


Description
===========

Some devices are naturally misaligned to compensate for things like the
legacy DOS partition table 63-sector offset. Low-level drivers should
call this function for devices whose first sector is not naturally
aligned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
