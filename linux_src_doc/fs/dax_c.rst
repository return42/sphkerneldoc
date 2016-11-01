.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/dax.c

.. _`dax_do_io`:

dax_do_io
=========

.. c:function:: ssize_t dax_do_io(struct kiocb *iocb, struct inode *inode, struct iov_iter *iter, get_block_t get_block, dio_iodone_t end_io, int flags)

    Perform I/O to a DAX file

    :param struct kiocb \*iocb:
        The control block for this I/O

    :param struct inode \*inode:
        The file which the I/O is directed at

    :param struct iov_iter \*iter:
        The addresses to do I/O from or to

    :param get_block_t get_block:
        The filesystem method used to translate file offsets to blocks

    :param dio_iodone_t end_io:
        A filesystem callback for I/O completion

    :param int flags:
        See below

.. _`dax_do_io.this-function-uses-the-same-locking-scheme-as-do_blockdev_direct_io`:

This function uses the same locking scheme as do_blockdev_direct_IO
-------------------------------------------------------------------

If \ ``flags``\  has DIO_LOCKING set, we assume that the i_mutex is held by the
caller for writes.  For reads, we take and release the i_mutex ourselves.
If DIO_LOCKING is not set, the filesystem takes care of its own locking.
As with \ :c:func:`do_blockdev_direct_IO`\ , we increment i_dio_count while the I/O
is in progress.

.. _`dax_fault`:

dax_fault
=========

.. c:function:: int dax_fault(struct vm_area_struct *vma, struct vm_fault *vmf, get_block_t get_block)

    handle a page fault on a DAX file

    :param struct vm_area_struct \*vma:
        The virtual memory area where the fault occurred

    :param struct vm_fault \*vmf:
        The description of the fault

    :param get_block_t get_block:
        The filesystem method used to translate file offsets to blocks

.. _`dax_fault.description`:

Description
-----------

When a page fault occurs, filesystems may call this helper in their
fault handler for DAX files. \ :c:func:`dax_fault`\  assumes the caller has done all
the necessary locking for the page fault to proceed successfully.

.. _`dax_pmd_fault`:

dax_pmd_fault
=============

.. c:function:: int dax_pmd_fault(struct vm_area_struct *vma, unsigned long address, pmd_t *pmd, unsigned int flags, get_block_t get_block)

    handle a PMD fault on a DAX file

    :param struct vm_area_struct \*vma:
        The virtual memory area where the fault occurred

    :param unsigned long address:
        *undescribed*

    :param pmd_t \*pmd:
        *undescribed*

    :param unsigned int flags:
        *undescribed*

    :param get_block_t get_block:
        The filesystem method used to translate file offsets to blocks

.. _`dax_pmd_fault.description`:

Description
-----------

When a page fault occurs, filesystems may call this helper in their
pmd_fault handler for DAX files.

.. _`dax_pfn_mkwrite`:

dax_pfn_mkwrite
===============

.. c:function:: int dax_pfn_mkwrite(struct vm_area_struct *vma, struct vm_fault *vmf)

    handle first write to DAX page

    :param struct vm_area_struct \*vma:
        The virtual memory area where the fault occurred

    :param struct vm_fault \*vmf:
        The description of the fault

.. _`dax_zero_page_range`:

dax_zero_page_range
===================

.. c:function:: int dax_zero_page_range(struct inode *inode, loff_t from, unsigned length, get_block_t get_block)

    zero a range within a page of a DAX file

    :param struct inode \*inode:
        The file being truncated

    :param loff_t from:
        The file offset that is being truncated to

    :param unsigned length:
        The number of bytes to zero

    :param get_block_t get_block:
        The filesystem method used to translate file offsets to blocks

.. _`dax_zero_page_range.description`:

Description
-----------

This function can be called by a filesystem when it is zeroing part of a
page in a DAX file.  This is intended for hole-punch operations.  If
you are truncating a file, the helper function \ :c:func:`dax_truncate_page`\  may be
more convenient.

.. _`dax_truncate_page`:

dax_truncate_page
=================

.. c:function:: int dax_truncate_page(struct inode *inode, loff_t from, get_block_t get_block)

    handle a partial page being truncated in a DAX file

    :param struct inode \*inode:
        The file being truncated

    :param loff_t from:
        The file offset that is being truncated to

    :param get_block_t get_block:
        The filesystem method used to translate file offsets to blocks

.. _`dax_truncate_page.description`:

Description
-----------

Similar to \ :c:func:`block_truncate_page`\ , this function can be called by a
filesystem when it is truncating a DAX file to handle the partial page.

.. _`iomap_dax_rw`:

iomap_dax_rw
============

.. c:function:: ssize_t iomap_dax_rw(struct kiocb *iocb, struct iov_iter *iter, struct iomap_ops *ops)

    Perform I/O to a DAX file

    :param struct kiocb \*iocb:
        The control block for this I/O

    :param struct iov_iter \*iter:
        The addresses to do I/O from or to

    :param struct iomap_ops \*ops:
        iomap ops passed from the file system

.. _`iomap_dax_rw.description`:

Description
-----------

This function performs read and write operations to directly mapped
persistent memory.  The callers needs to take care of read/write exclusion
and evicting any page cache pages in the region under I/O.

.. _`iomap_dax_fault`:

iomap_dax_fault
===============

.. c:function:: int iomap_dax_fault(struct vm_area_struct *vma, struct vm_fault *vmf, struct iomap_ops *ops)

    handle a page fault on a DAX file

    :param struct vm_area_struct \*vma:
        The virtual memory area where the fault occurred

    :param struct vm_fault \*vmf:
        The description of the fault

    :param struct iomap_ops \*ops:
        iomap ops passed from the file system

.. _`iomap_dax_fault.description`:

Description
-----------

When a page fault occurs, filesystems may call this helper in their fault
or mkwrite handler for DAX files. Assumes the caller has done all the
necessary locking for the page fault to proceed successfully.

.. This file was automatic generated / don't edit.

