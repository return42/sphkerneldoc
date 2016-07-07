.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/file.c

.. _`gfs2_llseek`:

gfs2_llseek
===========

.. c:function:: loff_t gfs2_llseek(struct file *file, loff_t offset, int whence)

    seek to a location in a file

    :param struct file \*file:
        the file

    :param loff_t offset:
        the offset

    :param int whence:
        Where to seek from (SEEK_SET, SEEK_CUR, or SEEK_END)

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

    :param struct file \*file:
        The directory to read from

    :param struct dir_context \*ctx:
        What to feed directory entries to

.. _`gfs2_readdir.return`:

Return
------

errno

.. _`fsflags_cvt`:

fsflags_cvt
===========

.. c:function:: u32 fsflags_cvt(const u32 *table, u32 val)

    :param const u32 \*table:
        A table of 32 u32 flags

    :param u32 val:
        a 32 bit value to convert

.. _`fsflags_cvt.description`:

Description
-----------

This function can be used to convert between fsflags values and
GFS2's own flags values.

.. _`fsflags_cvt.return`:

Return
------

the converted flags

.. _`do_gfs2_set_flags`:

do_gfs2_set_flags
=================

.. c:function:: int do_gfs2_set_flags(struct file *filp, u32 reqflags, u32 mask)

    set flags on an inode

    :param struct file \*filp:
        file pointer

    :param u32 reqflags:
        The flags to set

    :param u32 mask:
        Indicates which flags are valid

.. _`gfs2_size_hint`:

gfs2_size_hint
==============

.. c:function:: void gfs2_size_hint(struct file *filep, loff_t offset, size_t size)

    Give a hint to the size of a write request

    :param struct file \*filep:
        The struct file

    :param loff_t offset:
        The file offset of the write

    :param size_t size:
        The length of the write

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

    :param struct page \*page:
        The (locked) page to allocate backing for

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

.. c:function:: int gfs2_page_mkwrite(struct vm_area_struct *vma, struct vm_fault *vmf)

    Make a shared, \ :c:func:`mmap`\ ed, page writable

    :param struct vm_area_struct \*vma:
        The virtual memory area

    :param struct vm_fault \*vmf:
        The virtual memory fault containing the page to become writable

.. _`gfs2_page_mkwrite.description`:

Description
-----------

When the page becomes writable, we need to ensure that we have
blocks allocated on disk to back that page.

.. _`gfs2_mmap`:

gfs2_mmap
=========

.. c:function:: int gfs2_mmap(struct file *file, struct vm_area_struct *vma)

    :param struct file \*file:
        The file to map

    :param struct vm_area_struct \*vma:
        The VMA which described the mapping

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

    :param struct inode \*inode:
        The inode being opened

    :param struct file \*file:
        The file being opened

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

    :param struct inode \*inode:
        the inode to open

    :param struct file \*file:
        the struct file for this opening

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

    :param struct inode \*inode:
        the inode the struct file belongs to

    :param struct file \*file:
        the struct file being closed

.. _`gfs2_release.return`:

Return
------

errno

.. _`gfs2_fsync`:

gfs2_fsync
==========

.. c:function:: int gfs2_fsync(struct file *file, loff_t start, loff_t end, int datasync)

    sync the dirty data for a file (across the cluster)

    :param struct file \*file:
        the file that points to the dentry

    :param loff_t start:
        the start position in the file to sync

    :param loff_t end:
        the end position in the file to sync

    :param int datasync:
        set if we can ignore timestamp changes

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

    :param struct kiocb \*iocb:
        The io context

    :param struct iov_iter \*from:
        *undescribed*

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

    :param struct gfs2_inode \*ip:
        The inode in question.

    :param loff_t \*len:
        Max cap of bytes. What we return in \*len must be <= this.

    :param unsigned int \*data_blocks:
        Compute and return the number of data blocks needed

    :param unsigned int \*ind_blocks:
        Compute and return the number of indirect blocks needed

    :param unsigned int max_blocks:
        The total blocks available to work with.

.. _`calc_max_reserv.return`:

Return
------

void, but \ ``len``\ , \ ``data_blocks``\  and \ ``ind_blocks``\  are filled in.

.. _`gfs2_lock`:

gfs2_lock
=========

.. c:function:: int gfs2_lock(struct file *file, int cmd, struct file_lock *fl)

    acquire/release a posix lock on a file

    :param struct file \*file:
        the file pointer

    :param int cmd:
        either modify or retrieve lock state, possibly wait

    :param struct file_lock \*fl:
        type and range of lock

.. _`gfs2_lock.return`:

Return
------

errno

.. _`gfs2_flock`:

gfs2_flock
==========

.. c:function:: int gfs2_flock(struct file *file, int cmd, struct file_lock *fl)

    acquire/release a flock lock on a file

    :param struct file \*file:
        the file pointer

    :param int cmd:
        either modify or retrieve lock state, possibly wait

    :param struct file_lock \*fl:
        type and range of lock

.. _`gfs2_flock.return`:

Return
------

errno

.. This file was automatic generated / don't edit.

