.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/file.c

.. _`ntfs_file_open`:

ntfs_file_open
==============

.. c:function:: int ntfs_file_open(struct inode *vi, struct file *filp)

    called when an inode is about to be opened

    :param vi:
        inode to be opened
    :type vi: struct inode \*

    :param filp:
        file structure describing the inode
    :type filp: struct file \*

.. _`ntfs_file_open.description`:

Description
-----------

Limit file size to the page cache limit on architectures where unsigned long
is 32-bits. This is the most we can do for now without overflowing the page
cache page index. Doing it this way means we don't run into problems because
of existing too large files. It would be better to allow the user to read
the beginning of the file but I doubt very much anyone is going to hit this
check on a 32-bit architecture, so there is no point in adding the extra
complexity required to support this.

On 64-bit architectures, the check is hopefully optimized away by the
compiler.

After the check passes, just call \ :c:func:`generic_file_open`\  to do its work.

.. _`ntfs_attr_extend_initialized`:

ntfs_attr_extend_initialized
============================

.. c:function:: int ntfs_attr_extend_initialized(ntfs_inode *ni, const s64 new_init_size)

    extend the initialized size of an attribute

    :param ni:
        ntfs inode of the attribute to extend
    :type ni: ntfs_inode \*

    :param new_init_size:
        requested new initialized size in bytes
    :type new_init_size: const s64

.. _`ntfs_attr_extend_initialized.description`:

Description
-----------

Extend the initialized size of an attribute described by the ntfs inode \ ``ni``\ 
to \ ``new_init_size``\  bytes.  This involves zeroing any non-sparse space between
the old initialized size and \ ``new_init_size``\  both in the page cache and on
disk (if relevant complete pages are already uptodate in the page cache then
these are simply marked dirty).

As a side-effect, the file size (vfs inode->i_size) may be incremented as,
in the resident attribute case, it is tied to the initialized size and, in
the non-resident attribute case, it may not fall below the initialized size.

Note that if the attribute is resident, we do not need to touch the page
cache at all.  This is because if the page cache page is not uptodate we
bring it uptodate later, when doing the write to the mft record since we
then already have the page mapped.  And if the page is uptodate, the
non-initialized region will already have been zeroed when the page was
brought uptodate and the region may in fact already have been overwritten
with new data via \ :c:func:`mmap`\  based writes, so we cannot just zero it.  And since
POSIX specifies that the behaviour of resizing a file whilst it is \ :c:func:`mmap`\ ped
is unspecified, we choose not to do zeroing and thus we do not need to touch
the page at all.  For a more detailed explanation see \ :c:func:`ntfs_truncate`\  in
fs/ntfs/inode.c.

Return 0 on success and -errno on error.  In the case that an error is
encountered it is possible that the initialized size will already have been
incremented some way towards \ ``new_init_size``\  but it is guaranteed that if
this is the case, the necessary zeroing will also have happened and that all
metadata is self-consistent.

.. _`ntfs_attr_extend_initialized.locking`:

Locking
-------

i_mutex on the vfs inode corrseponsind to the ntfs inode \ ``ni``\  must be
held by the caller.

.. _`__ntfs_grab_cache_pages`:

\__ntfs_grab_cache_pages
========================

.. c:function:: int __ntfs_grab_cache_pages(struct address_space *mapping, pgoff_t index, const unsigned nr_pages, struct page **pages, struct page **cached_page)

    obtain a number of locked pages

    :param mapping:
        address space mapping from which to obtain page cache pages
    :type mapping: struct address_space \*

    :param index:
        starting index in \ ``mapping``\  at which to begin obtaining pages
    :type index: pgoff_t

    :param nr_pages:
        number of page cache pages to obtain
    :type nr_pages: const unsigned

    :param pages:
        array of pages in which to return the obtained page cache pages
    :type pages: struct page \*\*

    :param cached_page:
        allocated but as yet unused page
    :type cached_page: struct page \*\*

.. _`__ntfs_grab_cache_pages.description`:

Description
-----------

Obtain \ ``nr_pages``\  locked page cache pages from the mapping \ ``mapping``\  and
starting at index \ ``index``\ .

If a page is newly created, add it to lru list

Note, the page locks are obtained in ascending page index order.

.. _`ntfs_prepare_pages_for_non_resident_write`:

ntfs_prepare_pages_for_non_resident_write
=========================================

.. c:function:: int ntfs_prepare_pages_for_non_resident_write(struct page **pages, unsigned nr_pages, s64 pos, size_t bytes)

    prepare pages for receiving data

    :param pages:
        array of destination pages
    :type pages: struct page \*\*

    :param nr_pages:
        number of pages in \ ``pages``\ 
    :type nr_pages: unsigned

    :param pos:
        byte position in file at which the write begins
    :type pos: s64

    :param bytes:
        number of bytes to be written
    :type bytes: size_t

.. _`ntfs_prepare_pages_for_non_resident_write.description`:

Description
-----------

This is called for non-resident attributes from \ :c:func:`ntfs_file_buffered_write`\ 
with i_mutex held on the inode (@pages[0]->mapping->host).  There are
\ ``nr_pages``\  pages in \ ``pages``\  which are locked but not \ :c:func:`kmap`\ ped.  The source
data has not yet been copied into the \ ``pages``\ .

Need to fill any holes with actual clusters, allocate buffers if necessary,
ensure all the buffers are mapped, and bring uptodate any buffers that are
only partially being written to.

If \ ``nr_pages``\  is greater than one, we are guaranteed that the cluster size is
greater than PAGE_SIZE, that all pages in \ ``pages``\  are entirely inside
the same cluster and that they are the entirety of that cluster, and that
the cluster is sparse, i.e. we need to allocate a cluster to fill the hole.

i_size is not to be modified yet.

Return 0 on success or -errno on error.

.. _`ntfs_commit_pages_after_non_resident_write`:

ntfs_commit_pages_after_non_resident_write
==========================================

.. c:function:: int ntfs_commit_pages_after_non_resident_write(struct page **pages, const unsigned nr_pages, s64 pos, size_t bytes)

    commit the received data

    :param pages:
        array of destination pages
    :type pages: struct page \*\*

    :param nr_pages:
        number of pages in \ ``pages``\ 
    :type nr_pages: const unsigned

    :param pos:
        byte position in file at which the write begins
    :type pos: s64

    :param bytes:
        number of bytes to be written
    :type bytes: size_t

.. _`ntfs_commit_pages_after_non_resident_write.description`:

Description
-----------

See description of \ :c:func:`ntfs_commit_pages_after_write`\ , below.

.. _`ntfs_commit_pages_after_write`:

ntfs_commit_pages_after_write
=============================

.. c:function:: int ntfs_commit_pages_after_write(struct page **pages, const unsigned nr_pages, s64 pos, size_t bytes)

    commit the received data

    :param pages:
        array of destination pages
    :type pages: struct page \*\*

    :param nr_pages:
        number of pages in \ ``pages``\ 
    :type nr_pages: const unsigned

    :param pos:
        byte position in file at which the write begins
    :type pos: s64

    :param bytes:
        number of bytes to be written
    :type bytes: size_t

.. _`ntfs_commit_pages_after_write.description`:

Description
-----------

This is called from \ :c:func:`ntfs_file_buffered_write`\  with i_mutex held on the inode
(@pages[0]->mapping->host).  There are \ ``nr_pages``\  pages in \ ``pages``\  which are
locked but not \ :c:func:`kmap`\ ped.  The source data has already been copied into the
\ ``page``\ .  \ :c:func:`ntfs_prepare_pages_for_non_resident_write`\  has been called before
the data was copied (for non-resident attributes only) and it returned
success.

Need to set uptodate and mark dirty all buffers within the boundary of the
write.  If all buffers in a page are uptodate we set the page uptodate, too.

Setting the buffers dirty ensures that they get written out later when
\ :c:func:`ntfs_writepage`\  is invoked by the VM.

Finally, we need to update i_size and initialized_size as appropriate both
in the inode and the mft record.

This is modelled after fs/buffer.c::generic_commit_write(), which marks
buffers uptodate and dirty, sets the page uptodate if all buffers in the
page are uptodate, and updates i_size if the end of io is beyond i_size.  In
that case, it also marks the inode dirty.

If things have gone as outlined in
\ :c:func:`ntfs_prepare_pages_for_non_resident_write`\ , we do not need to do any page
content modifications here for non-resident attributes.  For resident
attributes we need to do the uptodate bringing here which we combine with
the copying into the mft record which means we save one atomic kmap.

Return 0 on success or -errno on error.

.. _`ntfs_perform_write`:

ntfs_perform_write
==================

.. c:function:: ssize_t ntfs_perform_write(struct file *file, struct iov_iter *i, loff_t pos)

    perform buffered write to a file

    :param file:
        file to write to
    :type file: struct file \*

    :param i:
        iov_iter with data to write
    :type i: struct iov_iter \*

    :param pos:
        byte offset in file at which to begin writing to
    :type pos: loff_t

.. _`ntfs_file_write_iter`:

ntfs_file_write_iter
====================

.. c:function:: ssize_t ntfs_file_write_iter(struct kiocb *iocb, struct iov_iter *from)

    simple wrapper for \ :c:func:`ntfs_file_write_iter_nolock`\ 

    :param iocb:
        IO state structure
    :type iocb: struct kiocb \*

    :param from:
        iov_iter with data to write
    :type from: struct iov_iter \*

.. _`ntfs_file_write_iter.description`:

Description
-----------

Basically the same as \ :c:func:`generic_file_write_iter`\  except that it ends up
up calling \ :c:func:`ntfs_perform_write`\  instead of \ :c:func:`generic_perform_write`\  and that
O_DIRECT is not implemented.

.. _`ntfs_file_fsync`:

ntfs_file_fsync
===============

.. c:function:: int ntfs_file_fsync(struct file *filp, loff_t start, loff_t end, int datasync)

    sync a file to disk

    :param filp:
        file to be synced
    :type filp: struct file \*

    :param start:
        *undescribed*
    :type start: loff_t

    :param end:
        *undescribed*
    :type end: loff_t

    :param datasync:
        if non-zero only flush user data and not metadata
    :type datasync: int

.. _`ntfs_file_fsync.description`:

Description
-----------

Data integrity sync of a file to disk.  Used for fsync, fdatasync, and msync
system calls.  This function is inspired by fs/buffer.c::file_fsync().

If \ ``datasync``\  is false, write the mft record and all associated extent mft
records as well as the \ ``$DATA``\  attribute and then sync the block device.

If \ ``datasync``\  is true and the attribute is non-resident, we skip the writing
of the mft record and all associated extent mft records (this might still
happen due to the \ :c:func:`write_inode_now`\  call).

Also, if \ ``datasync``\  is true, we do not wait on the inode to be written out
but we always wait on the page cache pages to be written out.

.. _`ntfs_file_fsync.locking`:

Locking
-------

Caller must hold i_mutex on the inode.

.. _`ntfs_file_fsync.todo`:

TODO
----

We should probably also write all attribute/index inodes associated
with this inode but since we have no simple way of getting to them we ignore
this problem for now.

.. This file was automatic generated / don't edit.

