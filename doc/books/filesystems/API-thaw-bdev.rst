.. -*- coding: utf-8; mode: rst -*-

.. _API-thaw-bdev:

=========
thaw_bdev
=========

*man thaw_bdev(9)*

*4.6.0-rc5*

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

Unlocks the filesystem and marks it writeable again after
``freeze_bdev``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
