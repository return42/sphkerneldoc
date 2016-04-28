.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-block-bio-remap:

=====================
trace_block_bio_remap
=====================

*man trace_block_bio_remap(9)*

*4.6.0-rc5*

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

An operation for a logical device has been mapped to the raw block
device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
