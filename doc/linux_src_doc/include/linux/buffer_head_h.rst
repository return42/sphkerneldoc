.. -*- coding: utf-8; mode: rst -*-

=============
buffer_head.h
=============


.. _`__bread`:

__bread
=======

.. c:function:: struct buffer_head *__bread (struct block_device *bdev, sector_t block, unsigned size)

    reads a specified block and returns the bh

    :param struct block_device \*bdev:
        the block_device to read from

    :param sector_t block:
        number of block

    :param unsigned size:
        size (in bytes) to read



.. _`__bread.description`:

Description
-----------

Reads a specified block, and returns buffer head that contains it.
The page cache is allocated from movable area so that it can be migrated.
It returns NULL if the block was unreadable.

