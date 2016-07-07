.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/swap_state.c

.. _`add_to_swap`:

add_to_swap
===========

.. c:function:: int add_to_swap(struct page *page, struct list_head *list)

    allocate swap space for a page

    :param struct page \*page:
        page we want to move to swap

    :param struct list_head \*list:
        *undescribed*

.. _`add_to_swap.description`:

Description
-----------

Allocate swap space for the page and add the page to the
swap cache.  Caller needs to hold the page lock.

.. _`swapin_readahead`:

swapin_readahead
================

.. c:function:: struct page *swapin_readahead(swp_entry_t entry, gfp_t gfp_mask, struct vm_area_struct *vma, unsigned long addr)

    swap in pages in hope we need them soon

    :param swp_entry_t entry:
        swap entry of this memory

    :param gfp_t gfp_mask:
        memory allocation flags

    :param struct vm_area_struct \*vma:
        user vma this address belongs to

    :param unsigned long addr:
        target address for mempolicy

.. _`swapin_readahead.description`:

Description
-----------

Returns the struct page for entry and addr, after queueing swapin.

Primitive swap readahead code. We simply read an aligned block of
(1 << page_cluster) entries in the swap area. This method is chosen
because it doesn't cost us any seek time.  We also make sure to queue
the 'original' request together with the readahead ones...

This has been extended to use the NUMA policies from the mm triggering
the readahead.

Caller must hold down_read on the vma->vm_mm if vma is not NULL.

.. This file was automatic generated / don't edit.

