.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/page_vma_mapped.c

.. _`check_pte`:

check_pte
=========

.. c:function:: bool check_pte(struct page_vma_mapped_walk *pvmw)

    check if \ ``pvmw->page``\  is mapped at the \ ``pvmw->pte``\ 

    :param pvmw:
        *undescribed*
    :type pvmw: struct page_vma_mapped_walk \*

.. _`check_pte.description`:

Description
-----------

\ :c:func:`page_vma_mapped_walk`\  found a place where \ ``pvmw->page``\  is \*potentially\*
mapped. \ :c:func:`check_pte`\  has to validate this.

\ ``pvmw->pte``\  may point to empty PTE, swap PTE or PTE pointing to arbitrary
page.

If PVMW_MIGRATION flag is set, returns true if \ ``pvmw->pte``\  contains migration
entry that points to \ ``pvmw->page``\  or any subpage in case of THP.

If PVMW_MIGRATION flag is not set, returns true if \ ``pvmw->pte``\  points to
\ ``pvmw->page``\  or any subpage in case of THP.

Otherwise, return false.

.. _`page_vma_mapped_walk`:

page_vma_mapped_walk
====================

.. c:function:: bool page_vma_mapped_walk(struct page_vma_mapped_walk *pvmw)

    check if \ ``pvmw->page``\  is mapped in \ ``pvmw->vma``\  at \ ``pvmw->address``\ 

    :param pvmw:
        pointer to struct page_vma_mapped_walk. page, vma, address and flags
        must be set. pmd, pte and ptl must be NULL.
    :type pvmw: struct page_vma_mapped_walk \*

.. _`page_vma_mapped_walk.description`:

Description
-----------

Returns true if the page is mapped in the vma. \ ``pvmw->pmd``\  and \ ``pvmw->pte``\  point
to relevant page table entries. \ ``pvmw->ptl``\  is locked. \ ``pvmw->address``\  is
adjusted if needed (for PTE-mapped THPs).

If \ ``pvmw->pmd``\  is set but \ ``pvmw->pte``\  is not, you have found PMD-mapped page
(usually THP). For PTE-mapped THP, you should run \ :c:func:`page_vma_mapped_walk`\  in
a loop to find all PTEs that map the THP.

For HugeTLB pages, \ ``pvmw->pte``\  is set to the relevant page table entry
regardless of which page table level the page is mapped at. \ ``pvmw->pmd``\  is
NULL.

Retruns false if there are no more page table entries for the page in
the vma. \ ``pvmw->ptl``\  is unlocked and \ ``pvmw->pte``\  is unmapped.

If you need to stop the walk before \ :c:func:`page_vma_mapped_walk`\  returned false,
use \ :c:func:`page_vma_mapped_walk_done`\ . It will do the housekeeping.

.. _`page_mapped_in_vma`:

page_mapped_in_vma
==================

.. c:function:: int page_mapped_in_vma(struct page *page, struct vm_area_struct *vma)

    check whether a page is really mapped in a VMA

    :param page:
        the page to test
    :type page: struct page \*

    :param vma:
        the VMA to test
    :type vma: struct vm_area_struct \*

.. _`page_mapped_in_vma.description`:

Description
-----------

Returns 1 if the page is mapped into the page tables of the VMA, 0
if the page is not mapped into the page tables of this VMA.  Only
valid for normal file or anonymous VMAs.

.. This file was automatic generated / don't edit.

