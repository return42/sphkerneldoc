.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/rmap.c

.. _`__anon_vma_prepare`:

\__anon_vma_prepare
===================

.. c:function:: int __anon_vma_prepare(struct vm_area_struct *vma)

    attach an anon_vma to a memory region

    :param struct vm_area_struct \*vma:
        the memory region in question

.. _`__anon_vma_prepare.description`:

Description
-----------

This makes sure the memory mapping described by 'vma' has
an 'anon_vma' attached to it, so that we can associate the
anonymous pages mapped into it with that anon_vma.

The common case will be that we already have one, which
is handled inline by \ :c:func:`anon_vma_prepare`\ . But if
not we either need to find an adjacent mapping that we
can re-use the anon_vma from (very common when the only
reason for splitting a vma has been \ :c:func:`mprotect`\ ), or we
allocate a new one.

Anon-vma allocations are very subtle, because we may have
optimistically looked up an anon_vma in \ :c:func:`page_lock_anon_vma_read`\ 
and that may actually touch the spinlock even in the newly
allocated vma (it depends on RCU to make sure that the
anon_vma isn't actually destroyed).

As a result, we need to do proper anon_vma locking even
for the new allocation. At the same time, we do not want
to do any locking for the common case of already having
an anon_vma.

This must be called with the mmap_sem held for reading.

.. _`page_referenced`:

page_referenced
===============

.. c:function:: int page_referenced(struct page *page, int is_locked, struct mem_cgroup *memcg, unsigned long *vm_flags)

    test if the page was referenced

    :param struct page \*page:
        the page to test

    :param int is_locked:
        caller holds lock on the page

    :param struct mem_cgroup \*memcg:
        target memory cgroup

    :param unsigned long \*vm_flags:
        collect encountered vma->vm_flags who actually referenced the page

.. _`page_referenced.description`:

Description
-----------

Quick test_and_clear_referenced for all mappings to a page,
returns the number of ptes which referenced the page.

.. _`page_move_anon_rmap`:

page_move_anon_rmap
===================

.. c:function:: void page_move_anon_rmap(struct page *page, struct vm_area_struct *vma)

    move a page to our anon_vma

    :param struct page \*page:
        the page to move to our anon_vma

    :param struct vm_area_struct \*vma:
        the vma the page belongs to

.. _`page_move_anon_rmap.description`:

Description
-----------

When a page belongs exclusively to one process after a COW event,
that page can be moved into the anon_vma that belongs to just that
process, so the rmap code will not search the parent or sibling
processes.

.. _`__page_set_anon_rmap`:

\__page_set_anon_rmap
=====================

.. c:function:: void __page_set_anon_rmap(struct page *page, struct vm_area_struct *vma, unsigned long address, int exclusive)

    set up new anonymous rmap

    :param struct page \*page:
        Page to add to rmap

    :param struct vm_area_struct \*vma:
        VM area to add page to.

    :param unsigned long address:
        User virtual address of the mapping

    :param int exclusive:
        the page is exclusively owned by the current process

.. _`__page_check_anon_rmap`:

\__page_check_anon_rmap
=======================

.. c:function:: void __page_check_anon_rmap(struct page *page, struct vm_area_struct *vma, unsigned long address)

    sanity check anonymous rmap addition

    :param struct page \*page:
        the page to add the mapping to

    :param struct vm_area_struct \*vma:
        the vm area in which the mapping is added

    :param unsigned long address:
        the user virtual address mapped

.. _`page_add_anon_rmap`:

page_add_anon_rmap
==================

.. c:function:: void page_add_anon_rmap(struct page *page, struct vm_area_struct *vma, unsigned long address, bool compound)

    add pte mapping to an anonymous page

    :param struct page \*page:
        the page to add the mapping to

    :param struct vm_area_struct \*vma:
        the vm area in which the mapping is added

    :param unsigned long address:
        the user virtual address mapped

    :param bool compound:
        charge the page as compound or small page

.. _`page_add_anon_rmap.description`:

Description
-----------

The caller needs to hold the pte lock, and the page must be locked in

.. _`page_add_anon_rmap.the-anon_vma-case`:

the anon_vma case
-----------------

to serialize mapping,index checking after setting,
and to ensure that PageAnon is not being upgraded racily to PageKsm
(but PageKsm is never downgraded to PageAnon).

.. _`page_add_new_anon_rmap`:

page_add_new_anon_rmap
======================

.. c:function:: void page_add_new_anon_rmap(struct page *page, struct vm_area_struct *vma, unsigned long address, bool compound)

    add pte mapping to a new anonymous page

    :param struct page \*page:
        the page to add the mapping to

    :param struct vm_area_struct \*vma:
        the vm area in which the mapping is added

    :param unsigned long address:
        the user virtual address mapped

    :param bool compound:
        charge the page as compound or small page

.. _`page_add_new_anon_rmap.description`:

Description
-----------

Same as page_add_anon_rmap but must only be called on \*new\* pages.
This means the inc-and-test can be bypassed.
Page does not have to be locked.

.. _`page_add_file_rmap`:

page_add_file_rmap
==================

.. c:function:: void page_add_file_rmap(struct page *page, bool compound)

    add pte mapping to a file page

    :param struct page \*page:
        the page to add the mapping to

    :param bool compound:
        charge the page as compound or small page

.. _`page_add_file_rmap.description`:

Description
-----------

The caller needs to hold the pte lock.

.. _`page_remove_rmap`:

page_remove_rmap
================

.. c:function:: void page_remove_rmap(struct page *page, bool compound)

    take down pte mapping from a page

    :param struct page \*page:
        page to remove mapping from

    :param bool compound:
        uncharge the page as compound or small page

.. _`page_remove_rmap.description`:

Description
-----------

The caller needs to hold the pte lock.

.. _`try_to_unmap`:

try_to_unmap
============

.. c:function:: bool try_to_unmap(struct page *page, enum ttu_flags flags)

    try to remove all page table mappings to a page

    :param struct page \*page:
        the page to get unmapped

    :param enum ttu_flags flags:
        action and flags

.. _`try_to_unmap.description`:

Description
-----------

Tries to remove all the page table entries which are mapping this
page, used in the pageout path.  Caller must hold the page lock.

If unmap is successful, return true. Otherwise, false.

.. _`try_to_munlock`:

try_to_munlock
==============

.. c:function:: void try_to_munlock(struct page *page)

    try to munlock a page

    :param struct page \*page:
        the page to be munlocked

.. _`try_to_munlock.description`:

Description
-----------

Called from munlock code.  Checks all of the VMAs mapping the page
to make sure nobody else has this page mlocked. The page will be
returned with PG_mlocked cleared if no other vmas have it mlocked.

.. This file was automatic generated / don't edit.

