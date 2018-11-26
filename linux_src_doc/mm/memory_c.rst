.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/memory.c

.. _`unmap_vmas`:

unmap_vmas
==========

.. c:function:: void unmap_vmas(struct mmu_gather *tlb, struct vm_area_struct *vma, unsigned long start_addr, unsigned long end_addr)

    unmap a range of memory covered by a list of vma's

    :param tlb:
        address of the caller's struct mmu_gather
    :type tlb: struct mmu_gather \*

    :param vma:
        the starting vma
    :type vma: struct vm_area_struct \*

    :param start_addr:
        virtual address at which to start unmapping
    :type start_addr: unsigned long

    :param end_addr:
        virtual address at which to end unmapping
    :type end_addr: unsigned long

.. _`unmap_vmas.description`:

Description
-----------

Unmap all pages in the vma list.

Only addresses between `start' and `end' will be unmapped.

The VMA list must be sorted in ascending virtual address order.

\ :c:func:`unmap_vmas`\  assumes that the caller will flush the whole unmapped address
range after \ :c:func:`unmap_vmas`\  returns.  So the only responsibility here is to
ensure that any thus-far unmapped pages are flushed before \ :c:func:`unmap_vmas`\ 
drops the lock and schedules.

.. _`zap_page_range`:

zap_page_range
==============

.. c:function:: void zap_page_range(struct vm_area_struct *vma, unsigned long start, unsigned long size)

    remove user pages in a given range

    :param vma:
        vm_area_struct holding the applicable pages
    :type vma: struct vm_area_struct \*

    :param start:
        starting address of pages to zap
    :type start: unsigned long

    :param size:
        number of bytes to zap
    :type size: unsigned long

.. _`zap_page_range.description`:

Description
-----------

Caller must protect the VMA list

.. _`zap_page_range_single`:

zap_page_range_single
=====================

.. c:function:: void zap_page_range_single(struct vm_area_struct *vma, unsigned long address, unsigned long size, struct zap_details *details)

    remove user pages in a given range

    :param vma:
        vm_area_struct holding the applicable pages
    :type vma: struct vm_area_struct \*

    :param address:
        starting address of pages to zap
    :type address: unsigned long

    :param size:
        number of bytes to zap
    :type size: unsigned long

    :param details:
        details of shared cache invalidation
    :type details: struct zap_details \*

.. _`zap_page_range_single.description`:

Description
-----------

The range must fit into one VMA.

.. _`zap_vma_ptes`:

zap_vma_ptes
============

.. c:function:: void zap_vma_ptes(struct vm_area_struct *vma, unsigned long address, unsigned long size)

    remove ptes mapping the vma

    :param vma:
        vm_area_struct holding ptes to be zapped
    :type vma: struct vm_area_struct \*

    :param address:
        starting address of pages to zap
    :type address: unsigned long

    :param size:
        number of bytes to zap
    :type size: unsigned long

.. _`zap_vma_ptes.description`:

Description
-----------

This function only unmaps ptes assigned to VM_PFNMAP vmas.

The entire address range must be fully contained within the vma.

.. _`vm_insert_page`:

vm_insert_page
==============

.. c:function:: int vm_insert_page(struct vm_area_struct *vma, unsigned long addr, struct page *page)

    insert single page into user vma

    :param vma:
        user vma to map to
    :type vma: struct vm_area_struct \*

    :param addr:
        target user address of this page
    :type addr: unsigned long

    :param page:
        source kernel page
    :type page: struct page \*

.. _`vm_insert_page.description`:

Description
-----------

This allows drivers to insert individual pages they've allocated
into a user vma.

The page has to be a nice clean _individual_ kernel allocation.
If you allocate a compound page, you need to have marked it as
such (__GFP_COMP), or manually just split the page up yourself
(see \ :c:func:`split_page`\ ).

NOTE! Traditionally this was done with "remap_pfn_range()" which
took an arbitrary page protection parameter. This doesn't allow
that. Your vma protection will have to be set up correctly, which
means that if you want a shared writable mapping, you'd better
ask for a shared writable mapping!

The page does not need to be reserved.

Usually this function is called from f_op->mmap() handler
under mm->mmap_sem write-lock, so it can change vma->vm_flags.
Caller must set VM_MIXEDMAP on vma if it wants to call this
function from other places, for example from page-fault handler.

.. _`vmf_insert_pfn_prot`:

vmf_insert_pfn_prot
===================

.. c:function:: vm_fault_t vmf_insert_pfn_prot(struct vm_area_struct *vma, unsigned long addr, unsigned long pfn, pgprot_t pgprot)

    insert single pfn into user vma with specified pgprot

    :param vma:
        user vma to map to
    :type vma: struct vm_area_struct \*

    :param addr:
        target user address of this page
    :type addr: unsigned long

    :param pfn:
        source kernel pfn
    :type pfn: unsigned long

    :param pgprot:
        pgprot flags for the inserted page
    :type pgprot: pgprot_t

.. _`vmf_insert_pfn_prot.description`:

Description
-----------

This is exactly like \ :c:func:`vmf_insert_pfn`\ , except that it allows drivers to
to override pgprot on a per-page basis.

This only makes sense for IO mappings, and it makes no sense for
COW mappings.  In general, using multiple vmas is preferable;
vmf_insert_pfn_prot should only be used if using multiple VMAs is
impractical.

.. _`vmf_insert_pfn_prot.context`:

Context
-------

Process context.  May allocate using \ ``GFP_KERNEL``\ .

.. _`vmf_insert_pfn_prot.return`:

Return
------

vm_fault_t value.

.. _`vmf_insert_pfn`:

vmf_insert_pfn
==============

.. c:function:: vm_fault_t vmf_insert_pfn(struct vm_area_struct *vma, unsigned long addr, unsigned long pfn)

    insert single pfn into user vma

    :param vma:
        user vma to map to
    :type vma: struct vm_area_struct \*

    :param addr:
        target user address of this page
    :type addr: unsigned long

    :param pfn:
        source kernel pfn
    :type pfn: unsigned long

.. _`vmf_insert_pfn.description`:

Description
-----------

Similar to vm_insert_page, this allows drivers to insert individual pages
they've allocated into a user vma. Same comments apply.

This function should only be called from a vm_ops->fault handler, and
in that case the handler should return the result of this function.

vma cannot be a COW mapping.

As this is called only for pages that do not currently exist, we
do not need to flush old virtual caches or the TLB.

.. _`vmf_insert_pfn.context`:

Context
-------

Process context.  May allocate using \ ``GFP_KERNEL``\ .

.. _`vmf_insert_pfn.return`:

Return
------

vm_fault_t value.

.. _`remap_pfn_range`:

remap_pfn_range
===============

.. c:function:: int remap_pfn_range(struct vm_area_struct *vma, unsigned long addr, unsigned long pfn, unsigned long size, pgprot_t prot)

    remap kernel memory to userspace

    :param vma:
        user vma to map to
    :type vma: struct vm_area_struct \*

    :param addr:
        target user address to start at
    :type addr: unsigned long

    :param pfn:
        physical address of kernel memory
    :type pfn: unsigned long

    :param size:
        size of map area
    :type size: unsigned long

    :param prot:
        page protection flags for this mapping
    :type prot: pgprot_t

.. _`remap_pfn_range.note`:

Note
----

this is only safe if the mm semaphore is held when called.

.. _`vm_iomap_memory`:

vm_iomap_memory
===============

.. c:function:: int vm_iomap_memory(struct vm_area_struct *vma, phys_addr_t start, unsigned long len)

    remap memory to userspace

    :param vma:
        user vma to map to
    :type vma: struct vm_area_struct \*

    :param start:
        start of area
    :type start: phys_addr_t

    :param len:
        size of area
    :type len: unsigned long

.. _`vm_iomap_memory.description`:

Description
-----------

This is a simplified \ :c:func:`io_remap_pfn_range`\  for common driver use. The
driver just needs to give us the physical memory range to be mapped,
we'll figure out the rest from the vma information.

NOTE! Some drivers might want to tweak vma->vm_page_prot first to get
whatever write-combining details or similar.

.. _`finish_mkwrite_fault`:

finish_mkwrite_fault
====================

.. c:function:: vm_fault_t finish_mkwrite_fault(struct vm_fault *vmf)

    finish page fault for a shared mapping, making PTE writeable once the page is prepared

    :param vmf:
        structure describing the fault
    :type vmf: struct vm_fault \*

.. _`finish_mkwrite_fault.description`:

Description
-----------

This function handles all that is needed to finish a write page fault in a
shared mapping due to PTE being read-only once the mapped page is prepared.
It handles locking of PTE and modifying it. The function returns
VM_FAULT_WRITE on success, 0 when PTE got changed before we acquired PTE
lock.

The function expects the page to be locked or other protection against
concurrent faults / writeback (such as DAX radix tree locks).

.. _`unmap_mapping_pages`:

unmap_mapping_pages
===================

.. c:function:: void unmap_mapping_pages(struct address_space *mapping, pgoff_t start, pgoff_t nr, bool even_cows)

    Unmap pages from processes.

    :param mapping:
        The address space containing pages to be unmapped.
    :type mapping: struct address_space \*

    :param start:
        Index of first page to be unmapped.
    :type start: pgoff_t

    :param nr:
        Number of pages to be unmapped.  0 to unmap to end of file.
    :type nr: pgoff_t

    :param even_cows:
        Whether to unmap even private COWed pages.
    :type even_cows: bool

.. _`unmap_mapping_pages.description`:

Description
-----------

Unmap the pages in this address space from any userspace process which
has them mmaped.  Generally, you want to remove COWed pages as well when
a file is being truncated, but not when invalidating pages from the page
cache.

.. _`unmap_mapping_range`:

unmap_mapping_range
===================

.. c:function:: void unmap_mapping_range(struct address_space *mapping, loff_t const holebegin, loff_t const holelen, int even_cows)

    unmap the portion of all mmaps in the specified address_space corresponding to the specified byte range in the underlying file.

    :param mapping:
        the address space containing mmaps to be unmapped.
    :type mapping: struct address_space \*

    :param holebegin:
        byte in first page to unmap, relative to the start of
        the underlying file.  This will be rounded down to a PAGE_SIZE
        boundary.  Note that this is different from \ :c:func:`truncate_pagecache`\ , which
        must keep the partial page.  In contrast, we must get rid of
        partial pages.
    :type holebegin: loff_t const

    :param holelen:
        size of prospective hole in bytes.  This will be rounded
        up to a PAGE_SIZE boundary.  A holelen of zero truncates to the
        end of the file.
    :type holelen: loff_t const

    :param even_cows:
        1 when truncating a file, unmap even private COWed pages;
        but 0 when invalidating pagecache, don't throw away private data.
    :type even_cows: int

.. _`alloc_set_pte`:

alloc_set_pte
=============

.. c:function:: vm_fault_t alloc_set_pte(struct vm_fault *vmf, struct mem_cgroup *memcg, struct page *page)

    setup new PTE entry for given page and add reverse page mapping. If needed, the fucntion allocates page table or use pre-allocated.

    :param vmf:
        fault environment
    :type vmf: struct vm_fault \*

    :param memcg:
        memcg to charge page (only for private mappings)
    :type memcg: struct mem_cgroup \*

    :param page:
        page to map
    :type page: struct page \*

.. _`alloc_set_pte.description`:

Description
-----------

Caller must take care of unlocking vmf->ptl, if vmf->pte is non-NULL on
return.

Target users are page handler itself and implementations of
vm_ops->map_pages.

.. _`finish_fault`:

finish_fault
============

.. c:function:: vm_fault_t finish_fault(struct vm_fault *vmf)

    finish page fault once we have prepared the page to fault

    :param vmf:
        structure describing the fault
    :type vmf: struct vm_fault \*

.. _`finish_fault.description`:

Description
-----------

This function handles all that is needed to finish a page fault once the
page to fault in is prepared. It handles locking of PTEs, inserts PTE for
given page, adds reverse page mapping, handles memcg charges and LRU
addition. The function returns 0 on success, VM_FAULT_ code in case of
error.

The function expects the page to be locked and on success it consumes a
reference of a page being mapped (for the PTE which maps it).

.. _`follow_pfn`:

follow_pfn
==========

.. c:function:: int follow_pfn(struct vm_area_struct *vma, unsigned long address, unsigned long *pfn)

    look up PFN at a user virtual address

    :param vma:
        memory mapping
    :type vma: struct vm_area_struct \*

    :param address:
        user virtual address
    :type address: unsigned long

    :param pfn:
        location to store found PFN
    :type pfn: unsigned long \*

.. _`follow_pfn.description`:

Description
-----------

Only IO mappings and raw PFN mappings are allowed.

Returns zero and the pfn at \ ``pfn``\  on success, -ve otherwise.

.. _`access_remote_vm`:

access_remote_vm
================

.. c:function:: int access_remote_vm(struct mm_struct *mm, unsigned long addr, void *buf, int len, unsigned int gup_flags)

    access another process' address space

    :param mm:
        the mm_struct of the target address space
    :type mm: struct mm_struct \*

    :param addr:
        start address to access
    :type addr: unsigned long

    :param buf:
        source or destination buffer
    :type buf: void \*

    :param len:
        number of bytes to transfer
    :type len: int

    :param gup_flags:
        flags modifying lookup behaviour
    :type gup_flags: unsigned int

.. _`access_remote_vm.description`:

Description
-----------

The caller must hold a reference on \ ``mm``\ .

.. This file was automatic generated / don't edit.

