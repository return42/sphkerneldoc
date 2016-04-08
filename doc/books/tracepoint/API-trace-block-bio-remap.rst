
.. _API-trace-block-bio-remap:

=====================
trace_block_bio_remap
=====================

*man trace_block_bio_remap(9)*

*4.6.0-rc1*

map request for a logical device to the raw device


Synopsis
========

.. c:function:: void trace_block_bio_remap( struct request_queue * q, struct bio * bio, dev_t dev, sector_t from )

Arguments
=========

``q``
    queue holding the operation

``bio``
    revised operation

``dev``
    device for the operation

``from``
    original sector for the operation


Description
===========

An operation for a logical device has been mapped to the raw block device.
