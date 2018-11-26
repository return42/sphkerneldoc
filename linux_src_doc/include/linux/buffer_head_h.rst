.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/buffer_head.h

.. _`__bread`:

\__bread
========

.. c:function:: struct buffer_head *__bread(struct block_device *bdev, sector_t block, unsigned size)

    reads a specified block and returns the bh

    :param bdev:
        the block_device to read from
    :type bdev: struct block_device \*

    :param block:
        number of block
    :type block: sector_t

    :param size:
        size (in bytes) to read
    :type size: unsigned

.. _`__bread.description`:

Description
-----------

Reads a specified block, and returns buffer head that contains it.
The page cache is allocated from movable area so that it can be migrated.
It returns NULL if the block was unreadable.

.. This file was automatic generated / don't edit.

