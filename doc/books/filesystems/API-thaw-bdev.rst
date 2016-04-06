
.. _API-thaw-bdev:

=========
thaw_bdev
=========

*man thaw_bdev(9)*

*4.6.0-rc1*

- unlock filesystem


Synopsis
========

.. c:function:: int thaw_bdev( struct block_device * bdev, struct super_block * sb )

Arguments
=========

``bdev``
    blockdevice to unlock

``sb``
    associated superblock


Description
===========

Unlocks the filesystem and marks it writeable again after ``freeze_bdev``.
