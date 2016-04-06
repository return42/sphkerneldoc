
.. _API-blk-queue-alignment-offset:

==========================
blk_queue_alignment_offset
==========================

*man blk_queue_alignment_offset(9)*

*4.6.0-rc1*

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

Some devices are naturally misaligned to compensate for things like the legacy DOS partition table 63-sector offset. Low-level drivers should call this function for devices whose
first sector is not naturally aligned.
