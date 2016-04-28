.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-queue-io-opt:

================
blk_queue_io_opt
================

*man blk_queue_io_opt(9)*

*4.6.0-rc5*

set optimal request size for the queue


Synopsis
========

.. c:function:: void blk_queue_io_opt( struct request_queue * q, unsigned int opt )

Arguments
=========

``q``
    the request queue for the device

``opt``
    optimal request size in bytes


Description
===========

Storage devices may report an optimal I/O size, which is the device's
preferred unit for sustained I/O. This is rarely reported for disk
drives. For RAID arrays it is usually the stripe width or the internal
track size. A properly aligned multiple of optimal_io_size is the
preferred request size for workloads where sustained throughput is
desired.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
