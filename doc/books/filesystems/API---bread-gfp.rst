
.. _API---bread-gfp:

===========
__bread_gfp
===========

*man __bread_gfp(9)*

*4.6.0-rc1*

reads a specified block and returns the bh


Synopsis
========

.. c:function:: struct buffer_head ⋆ __bread_gfp( struct block_device * bdev, sector_t block, unsigned size, gfp_t gfp )

Arguments
=========

``bdev``
    the block_device to read from

``block``
    number of block

``size``
    size (in bytes) to read

``gfp``
    page allocation flag


Description
===========

Reads a specified block, and returns buffer head that contains it. The page cache can be allocated from non-movable area not to prevent page migration if you set gfp to zero. It
returns NULL if the block was unreadable.
