.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/mempolicy.c

.. _`alloc_pages_vma`:

alloc_pages_vma
===============

.. c:function:: struct page *alloc_pages_vma(gfp_t gfp, int order, struct vm_area_struct *vma, unsigned long addr, int node, bool hugepage)

    Allocate a page for a VMA.

    :param gfp_t gfp:
        %GFP_USER    user allocation.
        \ ``GFP_KERNEL``\   kernel allocations,
        \ ``GFP_HIGHMEM``\  highmem/user allocations,
        \ ``GFP_FS``\       allocation should not call back into a file system.
        \ ``GFP_ATOMIC``\   don't sleep.

    :param int order:
        Order of the GFP allocation.

    :param struct vm_area_struct \*vma:
        Pointer to VMA or NULL if not available.

    :param unsigned long addr:
        Virtual Address of the allocation. Must be inside the VMA.

    :param int node:
        Which node to prefer for allocation (modulo policy).

    :param bool hugepage:
        for hugepages try only the preferred node if possible

.. _`alloc_pages_vma.description`:

Description
-----------

This function allocates a page from the kernel page pool and applies
a NUMA policy associated with the VMA or the current process.
When VMA is not NULL caller must hold down_read on the mmap_sem of the
mm_struct of the VMA to prevent it from going away. Should be used for
all allocations for pages that will be mapped into user space. Returns
NULL when no page can be allocated.

.. _`alloc_pages_current`:

alloc_pages_current
===================

.. c:function:: struct page *alloc_pages_current(gfp_t gfp, unsigned order)

    Allocate pages.

    :param gfp_t gfp:
        %GFP_USER   user allocation,
        \ ``GFP_KERNEL``\  kernel allocation,
        \ ``GFP_HIGHMEM``\  highmem allocation,
        \ ``GFP_FS``\      don't call back into a file system.
        \ ``GFP_ATOMIC``\  don't sleep.

    :param unsigned order:
        Power of two of allocation size in pages. 0 is a single page.

.. _`alloc_pages_current.description`:

Description
-----------

Allocate a page from the kernel page pool.  When not in
interrupt context and apply the current process NUMA policy.
Returns NULL when no page can be allocated.

.. _`mpol_misplaced`:

mpol_misplaced
==============

.. c:function:: int mpol_misplaced(struct page *page, struct vm_area_struct *vma, unsigned long addr)

    check whether current page node is valid in policy

    :param struct page \*page:
        page to be checked

    :param struct vm_area_struct \*vma:
        vm area where page mapped

    :param unsigned long addr:
        virtual address where page mapped

.. _`mpol_misplaced.description`:

Description
-----------

Lookup current policy node id for vma,addr and "compare to" page's
node id.

.. _`mpol_misplaced.return`:

Return
------

-1      - not misplaced, page is in the right node
node    - node id where the page should be

Policy determination "mimics" \ :c:func:`alloc_page_vma`\ .
Called from fault path where we know the vma and faulting address.

.. _`mpol_shared_policy_init`:

mpol_shared_policy_init
=======================

.. c:function:: void mpol_shared_policy_init(struct shared_policy *sp, struct mempolicy *mpol)

    initialize shared policy for inode

    :param struct shared_policy \*sp:
        pointer to inode shared policy

    :param struct mempolicy \*mpol:
        struct mempolicy to install

.. _`mpol_shared_policy_init.description`:

Description
-----------

Install non-NULL \ ``mpol``\  in inode's shared policy rb-tree.
On entry, the current task has a reference on a non-NULL \ ``mpol``\ .
This must be released on exit.
This is called at \ :c:func:`get_inode`\  calls and we can use GFP_KERNEL.

.. _`mpol_parse_str`:

mpol_parse_str
==============

.. c:function:: int mpol_parse_str(char *str, struct mempolicy **mpol)

    parse string to mempolicy, for tmpfs mpol mount option.

    :param char \*str:
        string containing mempolicy to parse

    :param struct mempolicy \*\*mpol:
        pointer to struct mempolicy pointer, returned on success.

.. _`mpol_parse_str.format-of-input`:

Format of input
---------------

<mode>[=<flags>][:<nodelist>]

On success, returns 0, else 1

.. _`mpol_to_str`:

mpol_to_str
===========

.. c:function:: void mpol_to_str(char *buffer, int maxlen, struct mempolicy *pol)

    format a mempolicy structure for printing

    :param char \*buffer:
        to contain formatted mempolicy string

    :param int maxlen:
        length of \ ``buffer``\ 

    :param struct mempolicy \*pol:
        pointer to mempolicy to be formatted

.. _`mpol_to_str.description`:

Description
-----------

Convert \ ``pol``\  into a string.  If \ ``buffer``\  is too short, truncate the string.
Recommend a \ ``maxlen``\  of at least 32 for the longest mode, "interleave", the
longest flag, "relative", and to display at least a few node ids.

.. This file was automatic generated / don't edit.

