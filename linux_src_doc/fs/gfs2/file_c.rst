.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/file.c

.. _`gfs2_llseek`:

gfs2_llseek
===========

.. c:function:: loff_t gfs2_llseek(struct file *file, loff_t offset, int whence)

    seek to a location in a file

    :param file:
        the file
    :type file: struct file \*

    :param offset:
        the offset
    :type offset: loff_t

    :param whence:
        Where to seek from (SEEK_SET, SEEK_CUR, or SEEK_END)
    :type whence: int

.. _`gfs2_llseek.description`:

Description
-----------

SEEK_END requires the glock for the file because it references the
file's size.

.. _`gfs2_llseek.return`:

Return
------

The new offset, or errno

.. _`gfs2_readdir`:

gfs2_readdir
============

.. c:function:: int gfs2_readdir(struct file *file, struct dir_context *ctx)

    Iterator for a directory

    :param file:
        The directory to read from
    :type file: struct file \*

    :param ctx:
        What to feed directory entries to
    :type ctx: struct dir_context \*

.. _`gfs2_readdir.return`:

Return
------

errno

.. _`do_gfs2_set_flags`:

do_gfs2_set_flags
=================

.. c:function:: int do_gfs2_set_flags(struct file *filp, u32 reqflags, u32 mask)

    set flags on an inode

    :param filp:
        file pointer
    :type filp: struct file \*

    :param reqflags:
        The flags to set
    :type reqflags: u32

    :param mask:
        Indicates which flags are valid
    :type mask: u32

.. _`gfs2_size_hint`:

gfs2_size_hint
==============

.. c:function:: void gfs2_size_hint(struct file *filep, loff_t offset, size_t size)

    Give a hint to the size of a write request

    :param filep:
        The struct file
    :type filep: struct file \*

    :param offset:
        The file offset of the write
    :type offset: loff_t

    :param size:
        The length of the write
    :type size: size_t

.. _`gfs2_size_hint.description`:

Description
-----------

When we are about to do a write, this function records the total
write size in order to provide a suitable hint to the lower layers
about how many blocks will be required.

.. _`gfs2_allocate_page_backing`:

gfs2_allocate_page_backing
==========================

.. c:function:: int gfs2_allocate_page_backing(struct page *page)

    Use bmap to allocate blocks

    :param page:
        The (locked) page to allocate backing for
    :type page: struct page \*

.. _`gfs2_allocate_page_backing.description`:

Description
-----------

We try to allocate all the blocks required for the page in
one go. This might fail for various reasons, so we keep
trying until all the blocks to back this page are allocated.
If some of the blocks are already allocated, thats ok too.

.. _`gfs2_page_mkwrite`:

gfs2_page_mkwrite
=================

.. c:function:: vm_fault_t gfs2_page_mkwrite(struct vm_fault *vmf)

    Make a shared, \ :c:func:`mmap`\ ed, page writable

    :param vmf:
        The virtual memory fault containing the page to become writable
    :type vmf: struct vm_fault \*

.. _`gfs2_page_mkwrite.description`:

Description
-----------

When the page becomes writable, we need to ensure that we have
blocks allocated on disk to back that page.

.. _`gfs2_mmap`:

gfs2_mmap
=========

.. c:function:: int gfs2_mmap(struct file *file, struct vm_area_struct *vma)

    :param file:
        The file to map
    :type file: struct file \*

    :param vma:
        The VMA which described the mapping
    :type vma: struct vm_area_struct \*

.. _`gfs2_mmap.description`:

Description
-----------

There is no need to get a lock here unless we should be updating
atime. We ignore any locking errors since the only consequence is
a missed atime update (which will just be deferred until later).

.. _`gfs2_mmap.return`:

Return
------

0

.. _`gfs2_open_common`:

gfs2_open_common
================

.. c:function:: int gfs2_open_common(struct inode *inode, struct file *file)

    This is common to open and atomic_open

    :param inode:
        The inode being opened
    :type inode: struct inode \*

    :param file:
        The file being opened
    :type file: struct file \*

.. _`gfs2_open_common.description`:

Description
-----------

This maybe called under a glock or not depending upon how it has
been called. We must always be called under a glock for regular
files, however. For other file types, it does not matter whether
we hold the glock or not.

.. _`gfs2_open_common.return`:

Return
------

Error code or 0 for success

.. _`gfs2_open`:

gfs2_open
=========

.. c:function:: int gfs2_open(struct inode *inode, struct file *file)

    open a file

    :param inode:
        the inode to open
    :type inode: struct inode \*

    :param file:
        the struct file for this opening
    :type file: struct file \*

.. _`gfs2_open.description`:

Description
-----------

After atomic_open, this function is only used for opening files
which are already cached. We must still get the glock for regular
files to ensure that we have the file size uptodate for the large
file check which is in the common code. That is only an issue for
regular files though.

.. _`gfs2_open.return`:

Return
------

errno

.. _`gfs2_release`:

gfs2_release
============

.. c:function:: int gfs2_release(struct inode *inode, struct file *file)

    called to close a struct file

    :param inode:
        the inode the struct file belongs to
    :type inode: struct inode \*

    :param file:
        the struct file being closed
    :type file: struct file \*

.. _`gfs2_release.return`:

Return
------

errno

.. _`gfs2_fsync`:

gfs2_fsync
==========

.. c:function:: int gfs2_fsync(struct file *file, loff_t start, loff_t end, int datasync)

    sync the dirty data for a file (across the cluster)

    :param file:
        the file that points to the dentry
    :type file: struct file \*

    :param start:
        the start position in the file to sync
    :type start: loff_t

    :param end:
        the end position in the file to sync
    :type end: loff_t

    :param datasync:
        set if we can ignore timestamp changes
    :type datasync: int

.. _`gfs2_fsync.description`:

Description
-----------

We split the data flushing here so that we don't wait for the data
until after we've also sent the metadata to disk. Note that for
data=ordered, we will write & wait for the data at the log flush
stage anyway, so this is unlikely to make much of a difference
except in the data=writeback case.

If the fdatawrite fails due to any reason except -EIO, we will
continue the remainder of the fsync, although we'll still report
the error at the end. This is to match \ :c:func:`filemap_write_and_wait_range`\ 
behaviour.

.. _`gfs2_fsync.return`:

Return
------

errno

.. _`gfs2_file_write_iter`:

gfs2_file_write_iter
====================

.. c:function:: ssize_t gfs2_file_write_iter(struct kiocb *iocb, struct iov_iter *from)

    Perform a write to a file

    :param iocb:
        The io context
    :type iocb: struct kiocb \*

    :param from:
        The data to write
    :type from: struct iov_iter \*

.. _`gfs2_file_write_iter.description`:

Description
-----------

We have to do a lock/unlock here to refresh the inode size for
O_APPEND writes, otherwise we can land up writing at the wrong
offset. There is still a race, but provided the app is using its
own file locking, this will make O_APPEND work as expected.

.. _`calc_max_reserv`:

calc_max_reserv
===============

.. c:function:: void calc_max_reserv(struct gfs2_inode *ip, loff_t *len, unsigned int *data_blocks, unsigned int *ind_blocks, unsigned int max_blocks)

    Reverse of write_calc_reserv. Given a number of blocks, determine how many bytes can be written.

    :param ip:
        The inode in question.
    :type ip: struct gfs2_inode \*

    :param len:
        Max cap of bytes. What we return in \*len must be <= this.
    :type len: loff_t \*

    :param data_blocks:
        Compute and return the number of data blocks needed
    :type data_blocks: unsigned int \*

    :param ind_blocks:
        Compute and return the number of indirect blocks needed
    :type ind_blocks: unsigned int \*

    :param max_blocks:
        The total blocks available to work with.
    :type max_blocks: unsigned int

.. _`calc_max_reserv.return`:

Return
------

void, but \ ``len``\ , \ ``data_blocks``\  and \ ``ind_blocks``\  are filled in.

.. _`gfs2_lock`:

gfs2_lock
=========

.. c:function:: int gfs2_lock(struct file *file, int cmd, struct file_lock *fl)

    acquire/release a posix lock on a file

    :param file:
        the file pointer
    :type file: struct file \*

    :param cmd:
        either modify or retrieve lock state, possibly wait
    :type cmd: int

    :param fl:
        type and range of lock
    :type fl: struct file_lock \*

.. _`gfs2_lock.return`:

Return
------

errno

.. _`gfs2_flock`:

gfs2_flock
==========

.. c:function:: int gfs2_flock(struct file *file, int cmd, struct file_lock *fl)

    acquire/release a flock lock on a file

    :param file:
        the file pointer
    :type file: struct file \*

    :param cmd:
        either modify or retrieve lock state, possibly wait
    :type cmd: int

    :param fl:
        type and range of lock
    :type fl: struct file_lock \*

.. _`gfs2_flock.return`:

Return
------

errno

.. This file was automatic generated / don't edit.

