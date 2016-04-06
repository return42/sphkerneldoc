
.. _API-get-super:

=========
get_super
=========

*man get_super(9)*

*4.6.0-rc1*

get the superblock of a device


Synopsis
========

.. c:function:: struct super_block ⋆ get_super( struct block_device * bdev )

Arguments
=========

``bdev``
    device to get the superblock for

    Scans the superblock list and finds the superblock of the file system mounted on the device given. ``NULL`` is returned if no match is found.
