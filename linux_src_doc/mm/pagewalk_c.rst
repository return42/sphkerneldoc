.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/pagewalk.c

.. _`walk_page_range`:

walk_page_range
===============

.. c:function:: int walk_page_range(unsigned long start, unsigned long end, struct mm_walk *walk)

    walk page table with caller specific callbacks

    :param unsigned long start:
        start address of the virtual address range

    :param unsigned long end:
        end address of the virtual address range

    :param struct mm_walk \*walk:
        mm_walk structure defining the callbacks and the target address space

.. _`walk_page_range.description`:

Description
-----------

Recursively walk the page table tree of the process represented by \ ``walk``\ ->mm
within the virtual address range [@start, \ ``end``\ ). During walking, we can do
some caller-specific works for each entry, by setting up \ :c:func:`pmd_entry`\ ,
\ :c:func:`pte_entry`\ , and/or \ :c:func:`hugetlb_entry`\ . If you don't set up for some of these
callbacks, the associated entries/pages are just ignored.

.. _`walk_page_range.the-return-values-of-these-callbacks-are-commonly-defined-like-below`:

The return values of these callbacks are commonly defined like below
--------------------------------------------------------------------


- 0  : succeeded to handle the current entry, and if you don't reach the
end address yet, continue to walk.
- >0 : succeeded to handle the current entry, and return to the caller
with caller specific value.
- <0 : failed to handle the current entry, and return to the caller
with error code.

Before starting to walk page table, some callers want to check whether
they really want to walk over the current vma, typically by checking
its vm_flags. \ :c:func:`walk_page_test`\  and \ ``walk``\ ->test_walk() are used for this
purpose.

struct mm_walk keeps current values of some common data like vma and pmd,
which are useful for the access from callbacks. If you want to pass some
caller-specific data to callbacks, \ ``walk``\ ->private should be helpful.

.. _`walk_page_range.locking`:

Locking
-------

Callers of \ :c:func:`walk_page_range`\  and \ :c:func:`walk_page_vma`\  should hold
\ ``walk``\ ->mm->mmap_sem, because these function traverse vma list and/or
access to vma's data.

.. This file was automatic generated / don't edit.

