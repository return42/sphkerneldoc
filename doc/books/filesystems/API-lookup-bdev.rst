
.. _API-lookup-bdev:

===========
lookup_bdev
===========

*man lookup_bdev(9)*

*4.6.0-rc1*

lookup a struct block_device by name


Synopsis
========

.. c:function:: struct block_device ⋆ lookup_bdev( const char * pathname )

Arguments
=========

``pathname``
    special file representing the block device


Description
===========

Get a reference to the blockdevice at ``pathname`` in the current namespace if possible and return it. Return ERR_PTR(error) otherwise.
