.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/dax.c

.. _`dax_pfn_mkwrite`:

dax_pfn_mkwrite
===============

.. c:function:: int dax_pfn_mkwrite(struct vm_fault *vmf)

    handle first write to DAX page

    :param struct vm_fault \*vmf:
        The description of the fault

.. _`dax_iomap_rw`:

dax_iomap_rw
============

.. c:function:: ssize_t dax_iomap_rw(struct kiocb *iocb, struct iov_iter *iter, const struct iomap_ops *ops)

    Perform I/O to a DAX file

    :param struct kiocb \*iocb:
        The control block for this I/O

    :param struct iov_iter \*iter:
        The addresses to do I/O from or to

    :param const struct iomap_ops \*ops:
        iomap ops passed from the file system

.. _`dax_iomap_rw.description`:

Description
-----------

This function performs read and write operations to directly mapped
persistent memory.  The callers needs to take care of read/write exclusion
and evicting any page cache pages in the region under I/O.

.. _`dax_iomap_fault`:

dax_iomap_fault
===============

.. c:function:: int dax_iomap_fault(struct vm_fault *vmf, enum page_entry_size pe_size, const struct iomap_ops *ops)

    handle a page fault on a DAX file

    :param struct vm_fault \*vmf:
        The description of the fault

    :param enum page_entry_size pe_size:
        *undescribed*

    :param const struct iomap_ops \*ops:
        iomap ops passed from the file system

.. _`dax_iomap_fault.description`:

Description
-----------

When a page fault occurs, filesystems may call this helper in
their fault handler for DAX files. \ :c:func:`dax_iomap_fault`\  assumes the caller
has done all the necessary locking for page fault to proceed
successfully.

.. This file was automatic generated / don't edit.

