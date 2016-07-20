.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/memory.c

.. _`unmap_vmas`:

unmap_vmas
==========

.. c:function:: void unmap_vmas(struct mmu_gather *tlb, struct vm_area_struct *vma, unsigned long start_addr, unsigned long end_addr)

    unmap a range of memory covered by a list of vma's

    :param struct mmu_gather \*tlb:
        address of the caller's struct mmu_gather

    :param struct vm_area_struct \*vma:
        the starting vma

    :param unsigned long start_addr:
        virtual address at which to start unmapping

    :param unsigned long end_addr:
        virtual address at which to end unmapping

.. _`unmap_vmas.description`:

Description
-----------

Unmap all pages in the vma list.

Only addresses between \`start' and \`end' will be unmapped.

The VMA list must be sorted in ascending virtual address order.

\ :c:func:`unmap_vmas`\  assumes that the caller will flush the whole unmapped address
range after \ :c:func:`unmap_vmas`\  returns.  So the only responsibility here is to
ensure that any thus-far unmapped pages are flushed before \ :c:func:`unmap_vmas`\ 
drops the lock and schedules.

.. _`zap_page_range`:

zap_page_range
==============

.. c:function:: void zap_page_range(struct vm_area_struct *vma, unsigned long start, unsigned long size, struct zap_details *details)

    remove user pages in a given range

    :param struct vm_area_struct \*vma:
        vm_area_struct holding the applicable pages

    :param unsigned long start:
        starting address of pages to zap

    :param unsigned long size:
        number of bytes to zap

    :param struct zap_details \*details:
        details of shared cache invalidation

.. _`zap_page_range.description`:

Description
-----------

Caller must protect the VMA list

.. _`zap_page_range_single`:

zap_page_range_single
=====================

.. c:function:: void zap_page_range_single(struct vm_area_struct *vma, unsigned long address, unsigned long size, struct zap_details *details)

    remove user pages in a given range

    :param struct vm_area_struct \*vma:
        vm_area_struct holding the applicable pages

    :param unsigned long address:
        starting address of pages to zap

    :param unsigned long size:
        number of bytes to zap

    :param struct zap_details \*details:
        details of shared cache invalidation

.. _`zap_page_range_single.description`:

Description
-----------

The range must fit into one VMA.

.. _`zap_vma_ptes`:

zap_vma_ptes
============

.. c:function:: int zap_vma_ptes(struct vm_area_struct *vma, unsigned long address, unsigned long size)

    remove ptes mapping the vma

    :param struct vm_area_struct \*vma:
        vm_area_struct holding ptes to be zapped

    :param unsigned long address:
        starting address of pages to zap

    :param unsigned long size:
        number of bytes to zap

.. _`zap_vma_ptes.description`:

Description
-----------

This function only unmaps ptes assigned to VM_PFNMAP vmas.

The entire address range must be fully contained within the vma.

Returns 0 if successful.

.. _`vm_insert_page`:

vm_insert_page
==============

.. c:function:: int vm_insert_page(struct vm_area_struct *vma, unsigned long addr, struct page *page)

    insert single page into user vma

    :param struct vm_area_struct \*vma:
        user vma to map to

    :param unsigned long addr:
        target user address of this page

    :param struct page \*page:
        source kernel page

.. _`vm_insert_page.description`:

Description
-----------

This allows drivers to insert individual pages they've allocated
into a user vma.

The page has to be a nice clean \_individual\_ kernel allocation.
If you allocate a compound page, you need to have marked it as
such (__GFP_COMP), or manually just split the page up yourself
(see \ :c:func:`split_page`\ ).

NOTE! Traditionally this was done with "\ :c:func:`remap_pfn_range`\ " which
took an arbitrary page protection parameter. This doesn't allow
that. Your vma protection will have to be set up correctly, which
means that if you want a shared writable mapping, you'd better
ask for a shared writable mapping!

The page does not need to be reserved.

Usually this function is called from f_op->\ :c:func:`mmap`\  handler
under mm->mmap_sem write-lock, so it can change vma->vm_flags.
Caller must set VM_MIXEDMAP on vma if it wants to call this
function from other places, for example from page-fault handler.

.. _`vm_insert_pfn`:

vm_insert_pfn
=============

.. c:function:: int vm_insert_pfn(struct vm_area_struct *vma, unsigned long addr, unsigned long pfn)

    insert single pfn into user vma

    :param struct vm_area_struct \*vma:
        user vma to map to

    :param unsigned long addr:
        target user address of this page

    :param unsigned long pfn:
        source kernel pfn

.. _`vm_insert_pfn.description`:

Description
-----------

Similar to vm_insert_page, this allows drivers to insert individual pages
they've allocated into a user vma. Same comments apply.

This function should only be called from a vm_ops->fault handler, and
in that case the handler should return NULL.

vma cannot be a COW mapping.

As this is called only for pages that do not currently exist, we
do not need to flush old virtual caches or the TLB.

.. _`vm_insert_pfn_prot`:

vm_insert_pfn_prot
==================

.. c:function:: int vm_insert_pfn_prot(struct vm_area_struct *vma, unsigned long addr, unsigned long pfn, pgprot_t pgprot)

    insert single pfn into user vma with specified pgprot

    :param struct vm_area_struct \*vma:
        user vma to map to

    :param unsigned long addr:
        target user address of this page

    :param unsigned long pfn:
        source kernel pfn

    :param pgprot_t pgprot:
        pgprot flags for the inserted page

.. _`vm_insert_pfn_prot.description`:

Description
-----------

This is exactly like vm_insert_pfn, except that it allows drivers to
to override pgprot on a per-page basis.

This only makes sense for IO mappings, and it makes no sense for
cow mappings.  In general, using multiple vmas is preferable;
vm_insert_pfn_prot should only be used if using multiple VMAs is
impractical.

.. _`remap_pfn_range`:

remap_pfn_range
===============

.. c:function:: int remap_pfn_range(struct vm_area_struct *vma, unsigned long addr, unsigned long pfn, unsigned long size, pgprot_t prot)

    remap kernel memory to userspace

    :param struct vm_area_struct \*vma:
        user vma to map to

    :param unsigned long addr:
        target user address to start at

    :param unsigned long pfn:
        physical address of kernel memory

    :param unsigned long size:
        size of map area

    :param pgprot_t prot:
        page protection flags for this mapping

.. _`remap_pfn_range.note`:

Note
----

this is only safe if the mm semaphore is held when called.

.. _`vm_iomap_memory`:

vm_iomap_memory
===============

.. c:function:: int vm_iomap_memory(struct vm_area_struct *vma, phys_addr_t start, unsigned long len)

    remap memory to userspace

    :param struct vm_area_struct \*vma:
        user vma to map to

    :param phys_addr_t start:
        start of area

    :param unsigned long len:
        size of area

.. _`vm_iomap_memory.description`:

Description
-----------

This is a simplified \ :c:func:`io_remap_pfn_range`\  for common driver use. The
driver just needs to give us the physical memory range to be mapped,
we'll figure out the rest from the vma information.

NOTE! Some drivers might want to tweak vma->vm_page_prot first to get
whatever write-combining details or similar.

.. _`unmap_mapping_range`:

unmap_mapping_range
===================

.. c:function:: void unmap_mapping_range(struct address_space *mapping, loff_t const holebegin, loff_t const holelen, int even_cows)

    unmap the portion of all mmaps in the specified address_space corresponding to the specified page range in the underlying file.

    :param struct address_space \*mapping:
        the address space containing mmaps to be unmapped.

    :param loff_t const holebegin:
        byte in first page to unmap, relative to the start of
        the underlying file.  This will be rounded down to a PAGE_SIZE
        boundary.  Note that this is different from \ :c:func:`truncate_pagecache`\ , which
        must keep the partial page.  In contrast, we must get rid of
        partial pages.

    :param loff_t const holelen:
        size of prospective hole in bytes.  This will be rounded
        up to a PAGE_SIZE boundary.  A holelen of zero truncates to the
        end of the file.

    :param int even_cows:
        1 when truncating a file, unmap even private COWed pages;
        but 0 when invalidating pagecache, don't throw away private data.

.. _`do_set_pte`:

do_set_pte
==========

.. c:function:: void do_set_pte(struct vm_area_struct *vma, unsigned long address, struct page *page, pte_t *pte, bool write, bool anon)

    setup new PTE entry for given page and add reverse page mapping.

    :param struct vm_area_struct \*vma:
        virtual memory area

    :param unsigned long address:
        user virtual address

    :param struct page \*page:
        page to map

    :param pte_t \*pte:
        pointer to target page table entry

    :param bool write:
        true, if new entry is writable

    :param bool anon:
        true, if it's anonymous page

.. _`do_set_pte.description`:

Description
-----------

Caller must hold page table lock relevant for \ ``pte``\ .

Target users are page handler itself and implementations of
vm_ops->map_pages.

.. _`follow_pfn`:

follow_pfn
==========

.. c:function:: int follow_pfn(struct vm_area_struct *vma, unsigned long address, unsigned long *pfn)

    look up PFN at a user virtual address

    :param struct vm_area_struct \*vma:
        memory mapping

    :param unsigned long address:
        user virtual address

    :param unsigned long \*pfn:
        location to store found PFN

.. _`follow_pfn.description`:

Description
-----------

Only IO mappings and raw PFN mappings are allowed.

Returns zero and the pfn at \ ``pfn``\  on success, -ve otherwise.

.. _`access_remote_vm`:

access_remote_vm
================

.. c:function:: int access_remote_vm(struct mm_struct *mm, unsigned long addr, void *buf, int len, int write)

    access another process' address space

    :param struct mm_struct \*mm:
        the mm_struct of the target address space

    :param unsigned long addr:
        start address to access

    :param void \*buf:
        source or destination buffer

    :param int len:
        number of bytes to transfer

    :param int write:
        whether the access is a write

.. _`access_remote_vm.description`:

Description
-----------

The caller must hold a reference on \ ``mm``\ .

.. This file was automatic generated / don't edit.

