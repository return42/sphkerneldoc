
.. _API-blk-limits-io-opt:

=================
blk_limits_io_opt
=================

*man blk_limits_io_opt(9)*

*4.6.0-rc1*

set optimal request size for a device


Synopsis
========

.. c:function:: void blk_limits_io_opt( struct queue_limits * limits, unsigned int opt )

Arguments
=========

``limits``
    the queue limits

``opt``
    smallest I/O size in bytes


Description
===========

Storage devices may report an optimal I/O size, which is the device's preferred unit for sustained I/O. This is rarely reported for disk drives. For RAID arrays it is usually the
stripe width or the internal track size. A properly aligned multiple of optimal_io_size is the preferred request size for workloads where sustained throughput is desired.
