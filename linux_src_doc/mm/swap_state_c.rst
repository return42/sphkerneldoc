.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/swap_state.c

.. _`add_to_swap`:

add_to_swap
===========

.. c:function:: int add_to_swap(struct page *page)

    allocate swap space for a page

    :param page:
        page we want to move to swap
    :type page: struct page \*

.. _`add_to_swap.description`:

Description
-----------

Allocate swap space for the page and add the page to the
swap cache.  Caller needs to hold the page lock.

.. _`swap_cluster_readahead`:

swap_cluster_readahead
======================

.. c:function:: struct page *swap_cluster_readahead(swp_entry_t entry, gfp_t gfp_mask, struct vm_fault *vmf)

    swap in pages in hope we need them soon

    :param entry:
        swap entry of this memory
    :type entry: swp_entry_t

    :param gfp_mask:
        memory allocation flags
    :type gfp_mask: gfp_t

    :param vmf:
        fault information
    :type vmf: struct vm_fault \*

.. _`swap_cluster_readahead.description`:

Description
-----------

Returns the struct page for entry and addr, after queueing swapin.

Primitive swap readahead code. We simply read an aligned block of
(1 << page_cluster) entries in the swap area. This method is chosen
because it doesn't cost us any seek time.  We also make sure to queue
the 'original' request together with the readahead ones...

This has been extended to use the NUMA policies from the mm triggering
the readahead.

Caller must hold down_read on the vma->vm_mm if vmf->vma is not NULL.

.. _`swapin_readahead`:

swapin_readahead
================

.. c:function:: struct page *swapin_readahead(swp_entry_t entry, gfp_t gfp_mask, struct vm_fault *vmf)

    swap in pages in hope we need them soon

    :param entry:
        swap entry of this memory
    :type entry: swp_entry_t

    :param gfp_mask:
        memory allocation flags
    :type gfp_mask: gfp_t

    :param vmf:
        fault information
    :type vmf: struct vm_fault \*

.. _`swapin_readahead.description`:

Description
-----------

Returns the struct page for entry and addr, after queueing swapin.

It's a main entry function for swap readahead. By the configuration,
it will read ahead blocks by cluster-based(ie, physical disk based)
or vma-based(ie, virtual address based on faulty address) readahead.

.. This file was automatic generated / don't edit.

