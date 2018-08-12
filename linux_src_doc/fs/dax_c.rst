.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/dax.c

.. _`dax_layout_busy_page`:

dax_layout_busy_page
====================

.. c:function:: struct page *dax_layout_busy_page(struct address_space *mapping)

    find first pinned page in \ ``mapping``\ 

    :param struct address_space \*mapping:
        address space to scan for a page with ref count > 1

.. _`dax_layout_busy_page.description`:

Description
-----------

DAX requires ZONE_DEVICE mapped pages. These pages are never
'onlined' to the page allocator so they are considered idle when
page->count == 1. A filesystem uses this interface to determine if
any page in the mapping is busy, i.e. for DMA, or other
\ :c:func:`get_user_pages`\  usages.

It is expected that the filesystem is holding locks to block the
establishment of new mappings in this address_space. I.e. it expects
to be able to run \ :c:func:`unmap_mapping_range`\  and subsequently not race
\ :c:func:`mapping_mapped`\  becoming true.

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

.. c:function:: vm_fault_t dax_iomap_fault(struct vm_fault *vmf, enum page_entry_size pe_size, pfn_t *pfnp, int *iomap_errp, const struct iomap_ops *ops)

    handle a page fault on a DAX file

    :param struct vm_fault \*vmf:
        The description of the fault

    :param enum page_entry_size pe_size:
        Size of the page to fault in

    :param pfn_t \*pfnp:
        PFN to insert for synchronous faults if fsync is required

    :param int \*iomap_errp:
        Storage for detailed error code in case of error

    :param const struct iomap_ops \*ops:
        Iomap ops passed from the file system

.. _`dax_iomap_fault.description`:

Description
-----------

When a page fault occurs, filesystems may call this helper in
their fault handler for DAX files. \ :c:func:`dax_iomap_fault`\  assumes the caller
has done all the necessary locking for page fault to proceed
successfully.

.. _`dax_insert_pfn_mkwrite`:

dax_insert_pfn_mkwrite
======================

.. c:function:: vm_fault_t dax_insert_pfn_mkwrite(struct vm_fault *vmf, enum page_entry_size pe_size, pfn_t pfn)

    insert PTE or PMD entry into page tables

    :param struct vm_fault \*vmf:
        The description of the fault

    :param enum page_entry_size pe_size:
        Size of entry to be inserted

    :param pfn_t pfn:
        PFN to insert

.. _`dax_insert_pfn_mkwrite.description`:

Description
-----------

This function inserts writeable PTE or PMD entry into page tables for mmaped
DAX file.  It takes care of marking corresponding radix tree entry as dirty
as well.

.. _`dax_finish_sync_fault`:

dax_finish_sync_fault
=====================

.. c:function:: vm_fault_t dax_finish_sync_fault(struct vm_fault *vmf, enum page_entry_size pe_size, pfn_t pfn)

    finish synchronous page fault

    :param struct vm_fault \*vmf:
        The description of the fault

    :param enum page_entry_size pe_size:
        Size of entry to be inserted

    :param pfn_t pfn:
        PFN to insert

.. _`dax_finish_sync_fault.description`:

Description
-----------

This function ensures that the file range touched by the page fault is
stored persistently on the media and handles inserting of appropriate page
table entry.

.. This file was automatic generated / don't edit.

