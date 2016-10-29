.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/buffer.c

.. _`emergency_thaw_all`:

emergency_thaw_all
==================

.. c:function:: void emergency_thaw_all( void)

    - forcibly thaw every frozen filesystem

    :param  void:
        no arguments

.. _`emergency_thaw_all.description`:

Description
-----------

Used for emergency unfreeze of all filesystems via SysRq

.. _`sync_mapping_buffers`:

sync_mapping_buffers
====================

.. c:function:: int sync_mapping_buffers(struct address_space *mapping)

    write out & wait upon a mapping's "associated" buffers

    :param struct address_space \*mapping:
        the mapping which wants those buffers written

.. _`sync_mapping_buffers.description`:

Description
-----------

Starts I/O against the buffers at mapping->private_list, and waits upon
that I/O.

Basically, this is a convenience function for \ :c:func:`fsync`\ .
\ ``mapping``\  is a file or directory which needs those buffers to be written for
a successful \ :c:func:`fsync`\ .

.. _`mark_buffer_dirty`:

mark_buffer_dirty
=================

.. c:function:: void mark_buffer_dirty(struct buffer_head *bh)

    mark a buffer_head as needing writeout

    :param struct buffer_head \*bh:
        the buffer_head to mark dirty

.. _`mark_buffer_dirty.description`:

Description
-----------

\ :c:func:`mark_buffer_dirty`\  will set the dirty bit against the buffer, then set its
backing page dirty, then tag the page as dirty in its address_space's radix
tree and then attach the address_space's inode to its superblock's dirty
inode list.

\ :c:func:`mark_buffer_dirty`\  is atomic.  It takes bh->b_page->mapping->private_lock,
mapping->tree_lock and mapping->host->i_lock.

.. _`__bread_gfp`:

__bread_gfp
===========

.. c:function:: struct buffer_head *__bread_gfp(struct block_device *bdev, sector_t block, unsigned size, gfp_t gfp)

    reads a specified block and returns the bh

    :param struct block_device \*bdev:
        the block_device to read from

    :param sector_t block:
        number of block

    :param unsigned size:
        size (in bytes) to read

    :param gfp_t gfp:
        page allocation flag

.. _`__bread_gfp.description`:

Description
-----------

Reads a specified block, and returns buffer head that contains it.
The page cache can be allocated from non-movable area
not to prevent page migration if you set gfp to zero.
It returns NULL if the block was unreadable.

.. _`block_invalidatepage`:

block_invalidatepage
====================

.. c:function:: void block_invalidatepage(struct page *page, unsigned int offset, unsigned int length)

    invalidate part or all of a buffer-backed page

    :param struct page \*page:
        the page which is affected

    :param unsigned int offset:
        start of the range to invalidate

    :param unsigned int length:
        length of the range to invalidate

.. _`block_invalidatepage.description`:

Description
-----------

\ :c:func:`block_invalidatepage`\  is called when all or part of the page has become
invalidated by a truncate operation.

\ :c:func:`block_invalidatepage`\  does not have to release all buffers, but it must
ensure that no dirty buffer is left outside \ ``offset``\  and that no I/O
is underway against any of the blocks which are outside the truncation
point.  Because the caller is about to free (and possibly reuse) those
blocks on-disk.

.. _`ll_rw_block`:

ll_rw_block
===========

.. c:function:: void ll_rw_block(int rw, int nr, struct buffer_head  *bhs[])

    low-level access to block devices (DEPRECATED)

    :param int rw:
        whether to \ ``READ``\  or \ ``WRITE``\  or maybe \ ``READA``\  (readahead)

    :param int nr:
        number of \ :c:type:`struct buffer_heads <buffer_heads>`\  in the array

    :param struct buffer_head  \*bhs:
        array of pointers to \ :c:type:`struct buffer_head <buffer_head>`\ 

.. _`ll_rw_block.description`:

Description
-----------

\ :c:func:`ll_rw_block`\  takes an array of pointers to \ :c:type:`struct buffer_heads <buffer_heads>`\ , and
requests an I/O operation on them, either a \ ``READ``\  or a \ ``WRITE``\ .  The third
\ ``READA``\  option is described in the documentation for \ :c:func:`generic_make_request`\ 
which \ :c:func:`ll_rw_block`\  calls.

This function drops any buffer that it cannot get a lock on (with the
BH_Lock state bit), any buffer that appears to be clean when doing a write
request, and any buffer that appears to be up-to-date when doing read
request.  Further it marks as clean buffers that are processed for
writing (the buffer cache won't assume that they are actually clean
until the buffer gets unlocked).

ll_rw_block sets b_end_io to simple completion handler that marks
the buffer up-to-date (if appropriate), unlocks the buffer and wakes
any waiters.

All of the buffers must be for the same device, and must also be a
multiple of the current approved size for the device.

.. _`bh_uptodate_or_lock`:

bh_uptodate_or_lock
===================

.. c:function:: int bh_uptodate_or_lock(struct buffer_head *bh)

    Test whether the buffer is uptodate

    :param struct buffer_head \*bh:
        struct buffer_head

.. _`bh_uptodate_or_lock.description`:

Description
-----------

Return true if the buffer is up-to-date and false,
with the buffer locked, if not.

.. _`bh_submit_read`:

bh_submit_read
==============

.. c:function:: int bh_submit_read(struct buffer_head *bh)

    Submit a locked buffer for reading

    :param struct buffer_head \*bh:
        struct buffer_head

.. _`bh_submit_read.description`:

Description
-----------

Returns zero on success and -EIO on error.

.. This file was automatic generated / don't edit.
