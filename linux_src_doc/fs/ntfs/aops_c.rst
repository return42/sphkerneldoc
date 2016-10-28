.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/aops.c

.. _`ntfs_end_buffer_async_read`:

ntfs_end_buffer_async_read
==========================

.. c:function:: void ntfs_end_buffer_async_read(struct buffer_head *bh, int uptodate)

    NTFS kernel address space operations and page cache handling.

    :param struct buffer_head \*bh:
        *undescribed*

    :param int uptodate:
        *undescribed*

.. _`ntfs_end_buffer_async_read.description`:

Description
-----------

Copyright (c) 2001-2014 Anton Altaparmakov and Tuxera Inc.
Copyright (c) 2002 Richard Russon

This program/include file is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as published
by the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program/include file is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program (in the main directory of the Linux-NTFS
distribution in the file COPYING); if not, write to the Free Software
Foundation,Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

.. _`ntfs_read_block`:

ntfs_read_block
===============

.. c:function:: int ntfs_read_block(struct page *page)

    fill a \ ``page``\  of an address space with data

    :param struct page \*page:
        page cache page to fill with data

.. _`ntfs_read_block.description`:

Description
-----------

Fill the page \ ``page``\  of the address space belonging to the \ ``page``\ ->host inode.
We read each buffer asynchronously and when all buffers are read in, our io
completion handler \ :c:func:`ntfs_end_buffer_read_async`\ , if required, automatically
applies the mst fixups to the page before finally marking it uptodate and
unlocking it.

We only enforce allocated_size limit because i_size is checked for in
\ :c:func:`generic_file_read`\ .

Return 0 on success and -errno on error.

Contains an adapted version of fs/buffer.c::\ :c:func:`block_read_full_page`\ .

.. _`ntfs_readpage`:

ntfs_readpage
=============

.. c:function:: int ntfs_readpage(struct file *file, struct page *page)

    fill a \ ``page``\  of a \ ``file``\  with data from the device

    :param struct file \*file:
        open file to which the page \ ``page``\  belongs or NULL

    :param struct page \*page:
        page cache page to fill with data

.. _`ntfs_readpage.description`:

Description
-----------

For non-resident attributes, \ :c:func:`ntfs_readpage`\  fills the \ ``page``\  of the open
file \ ``file``\  by calling the ntfs version of the generic \ :c:func:`block_read_full_page`\ 
function, \ :c:func:`ntfs_read_block`\ , which in turn creates and reads in the buffers
associated with the page asynchronously.

For resident attributes, OTOH, \ :c:func:`ntfs_readpage`\  fills \ ``page``\  by copying the
data from the mft record (which at this stage is most likely in memory) and
fills the remainder with zeroes. Thus, in this case, I/O is synchronous, as
even if the mft record is not cached at this point in time, we need to wait
for it to be read in before we can do the copy.

Return 0 on success and -errno on error.

.. _`ntfs_write_block`:

ntfs_write_block
================

.. c:function:: int ntfs_write_block(struct page *page, struct writeback_control *wbc)

    write a \ ``page``\  to the backing store

    :param struct page \*page:
        page cache page to write out

    :param struct writeback_control \*wbc:
        writeback control structure

.. _`ntfs_write_block.description`:

Description
-----------

This function is for writing pages belonging to non-resident, non-mst
protected attributes to their backing store.

For a page with buffers, map and write the dirty buffers asynchronously
under page writeback. For a page without buffers, create buffers for the
page, then proceed as above.

If a page doesn't have buffers the page dirty state is definitive. If a page
does have buffers, the page dirty state is just a hint, and the buffer dirty
state is definitive. (A hint which has rules: dirty buffers against a clean
page is illegal. Other combinations are legal and need to be handled. In
particular a dirty page containing clean buffers for example.)

Return 0 on success and -errno on error.

Based on \ :c:func:`ntfs_read_block`\  and \\ :c:func:`__block_write_full_page`\ .

.. _`ntfs_write_mst_block`:

ntfs_write_mst_block
====================

.. c:function:: int ntfs_write_mst_block(struct page *page, struct writeback_control *wbc)

    write a \ ``page``\  to the backing store

    :param struct page \*page:
        page cache page to write out

    :param struct writeback_control \*wbc:
        writeback control structure

.. _`ntfs_write_mst_block.description`:

Description
-----------

This function is for writing pages belonging to non-resident, mst protected
attributes to their backing store.  The only supported attributes are index
allocation and \ ``$MFT``\ /\ ``$DATA``\ .  Both directory inodes and index inodes are
supported for the index allocation case.

The page must remain locked for the duration of the write because we apply
the mst fixups, write, and then undo the fixups, so if we were to unlock the
page before undoing the fixups, any other user of the page will see the
page contents as corrupt.

We clear the page uptodate flag for the duration of the function to ensure
exclusion for the \ ``$MFT``\ /\ ``$DATA``\  case against someone mapping an mft record we
are about to apply the mst fixups to.

Return 0 on success and -errno on error.

Based on \ :c:func:`ntfs_write_block`\ , \ :c:func:`ntfs_mft_writepage`\ , and
\ :c:func:`write_mft_record_nolock`\ .

.. _`ntfs_writepage`:

ntfs_writepage
==============

.. c:function:: int ntfs_writepage(struct page *page, struct writeback_control *wbc)

    write a \ ``page``\  to the backing store

    :param struct page \*page:
        page cache page to write out

    :param struct writeback_control \*wbc:
        writeback control structure

.. _`ntfs_writepage.description`:

Description
-----------

This is called from the VM when it wants to have a dirty ntfs page cache
page cleaned.  The VM has already locked the page and marked it clean.

For non-resident attributes, \ :c:func:`ntfs_writepage`\  writes the \ ``page``\  by calling
the ntfs version of the generic \ :c:func:`block_write_full_page`\  function,
\ :c:func:`ntfs_write_block`\ , which in turn if necessary creates and writes the
buffers associated with the page asynchronously.

For resident attributes, OTOH, \ :c:func:`ntfs_writepage`\  writes the \ ``page``\  by copying
the data to the mft record (which at this stage is most likely in memory).
The mft record is then marked dirty and written out asynchronously via the
vfs inode dirty code path for the inode the mft record belongs to or via the
vm page dirty code path for the page the mft record is in.

Based on \ :c:func:`ntfs_readpage`\  and fs/buffer.c::\ :c:func:`block_write_full_page`\ .

Return 0 on success and -errno on error.

.. _`ntfs_bmap`:

ntfs_bmap
=========

.. c:function:: sector_t ntfs_bmap(struct address_space *mapping, sector_t block)

    map logical file block to physical device block

    :param struct address_space \*mapping:
        address space mapping to which the block to be mapped belongs

    :param sector_t block:
        logical block to map to its physical device block

.. _`ntfs_bmap.description`:

Description
-----------

For regular, non-resident files (i.e. not compressed and not encrypted), map
the logical \ ``block``\  belonging to the file described by the address space
mapping \ ``mapping``\  to its physical device block.

The size of the block is equal to the \ ``s_blocksize``\  field of the super block
of the mounted file system which is guaranteed to be smaller than or equal
to the cluster size thus the block is guaranteed to fit entirely inside the
cluster which means we do not need to care how many contiguous bytes are
available after the beginning of the block.

Return the physical device block if the mapping succeeded or 0 if the block
is sparse or there was an error.

.. _`ntfs_bmap.note`:

Note
----

This is a problem if someone tries to run \ :c:func:`bmap`\  on \ ``$Boot``\  system file
as that really is in block zero but there is nothing we can do.  \ :c:func:`bmap`\  is
just broken in that respect (just like it cannot distinguish sparse from
not available or error).

.. _`mark_ntfs_record_dirty`:

mark_ntfs_record_dirty
======================

.. c:function:: void mark_ntfs_record_dirty(struct page *page, const unsigned int ofs)

    mark an ntfs record dirty

    :param struct page \*page:
        page containing the ntfs record to mark dirty

    :param const unsigned int ofs:
        byte offset within \ ``page``\  at which the ntfs record begins

.. _`mark_ntfs_record_dirty.description`:

Description
-----------

Set the buffers and the page in which the ntfs record is located dirty.

The latter also marks the vfs inode the ntfs record belongs to dirty
(I_DIRTY_PAGES only).

If the page does not have buffers, we create them and set them uptodate.
The page may not be locked which is why we need to handle the buffers under
the mapping->private_lock.  Once the buffers are marked dirty we no longer
need the lock since \ :c:func:`try_to_free_buffers`\  does not free dirty buffers.

.. This file was automatic generated / don't edit.

