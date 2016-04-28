.. -*- coding: utf-8; mode: rst -*-

.. _API-lookup-bdev:

===========
lookup_bdev
===========

*man lookup_bdev(9)*

*4.6.0-rc5*

lookup a struct block_device by name


Synopsis
========

.. c:function:: struct block_device * lookup_bdev( const char * pathname )

Arguments
=========

``pathname``
    special file representing the block device


Description
===========

Get a reference to the blockdevice at ``pathname`` in the current
namespace if possible and return it. Return ERR_PTR(error) otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
