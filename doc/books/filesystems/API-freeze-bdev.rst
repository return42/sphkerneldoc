.. -*- coding: utf-8; mode: rst -*-

.. _API-freeze-bdev:

===========
freeze_bdev
===========

*man freeze_bdev(9)*

*4.6.0-rc5*

- lock a filesystem and force it into a consistent state


Synopsis
========

.. c:function:: struct super_block * freeze_bdev( struct block_device * bdev )

Arguments
=========

``bdev``
    blockdevice to lock


Description
===========

If a superblock is found on this device, we take the s_umount semaphore
on it to make sure nobody unmounts until the snapshot creation is done.
The reference counter (bd_fsfreeze_count) guarantees that only the
last unfreeze process can unfreeze the frozen filesystem actually when
multiple freeze requests arrive simultaneously. It counts up in
``freeze_bdev`` and count down in ``thaw_bdev``. When it becomes 0,
``thaw_bdev`` will unfreeze actually.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
