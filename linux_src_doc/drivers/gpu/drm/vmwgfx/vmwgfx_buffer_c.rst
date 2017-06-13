.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_buffer.c

.. _`__vmw_piter_non_sg_next`:

__vmw_piter_non_sg_next
=======================

.. c:function:: bool __vmw_piter_non_sg_next(struct vmw_piter *viter)

    :param struct vmw_piter \*viter:
        Pointer to the iterator.

.. _`__vmw_piter_non_sg_next.description`:

Description
-----------

These functions return false if past the end of the list,
true otherwise. Functions are selected depending on the current
DMA mapping mode.

.. _`__vmw_piter_non_sg_page`:

__vmw_piter_non_sg_page
=======================

.. c:function:: struct page *__vmw_piter_non_sg_page(struct vmw_piter *viter)

    :param struct vmw_piter \*viter:
        Pointer to the iterator

.. _`__vmw_piter_non_sg_page.description`:

Description
-----------

These functions return a pointer to the page currently
pointed to by \ ``viter``\ . Functions are selected depending on the
current mapping mode.

.. _`__vmw_piter_phys_addr`:

__vmw_piter_phys_addr
=====================

.. c:function:: dma_addr_t __vmw_piter_phys_addr(struct vmw_piter *viter)

    :param struct vmw_piter \*viter:
        Pointer to the iterator

.. _`__vmw_piter_phys_addr.description`:

Description
-----------

These functions return the DMA address of the page currently
pointed to by \ ``viter``\ . Functions are selected depending on the
current mapping mode.

.. _`vmw_piter_start`:

vmw_piter_start
===============

.. c:function:: void vmw_piter_start(struct vmw_piter *viter, const struct vmw_sg_table *vsgt, unsigned long p_offset)

    Initialize a struct vmw_piter.

    :param struct vmw_piter \*viter:
        Pointer to the iterator to initialize

    :param const struct vmw_sg_table \*vsgt:
        Pointer to a struct vmw_sg_table to initialize from

    :param unsigned long p_offset:
        *undescribed*

.. _`vmw_piter_start.description`:

Description
-----------

Note that we're following the convention of \__sg_page_iter_start, so that
the iterator doesn't point to a valid page after initialization; it has
to be advanced one step first.

.. _`vmw_ttm_unmap_from_dma`:

vmw_ttm_unmap_from_dma
======================

.. c:function:: void vmw_ttm_unmap_from_dma(struct vmw_ttm_tt *vmw_tt)

    unmap  device addresses previsouly mapped for TTM pages

    :param struct vmw_ttm_tt \*vmw_tt:
        Pointer to a struct vmw_ttm_backend

.. _`vmw_ttm_unmap_from_dma.description`:

Description
-----------

Used to free dma mappings previously mapped by vmw_ttm_map_for_dma.

.. _`vmw_ttm_map_for_dma`:

vmw_ttm_map_for_dma
===================

.. c:function:: int vmw_ttm_map_for_dma(struct vmw_ttm_tt *vmw_tt)

    map TTM pages to get device addresses

    :param struct vmw_ttm_tt \*vmw_tt:
        Pointer to a struct vmw_ttm_backend

.. _`vmw_ttm_map_for_dma.description`:

Description
-----------

This function is used to get device addresses from the kernel DMA layer.
However, it's violating the DMA API in that when this operation has been
performed, it's illegal for the CPU to write to the pages without first
unmapping the DMA mappings, or calling \ :c:func:`dma_sync_sg_for_cpu`\ . It is
therefore only legal to call this function if we know that the function
\ :c:func:`dma_sync_sg_for_cpu`\  is a NOP, and \ :c:func:`dma_sync_sg_for_device`\  is at most
a CPU write buffer flush.

.. _`vmw_ttm_map_dma`:

vmw_ttm_map_dma
===============

.. c:function:: int vmw_ttm_map_dma(struct vmw_ttm_tt *vmw_tt)

    Make sure TTM pages are visible to the device

    :param struct vmw_ttm_tt \*vmw_tt:
        Pointer to a struct vmw_ttm_tt

.. _`vmw_ttm_map_dma.description`:

Description
-----------

Select the correct function for and make sure the TTM pages are
visible to the device. Allocate storage for the device mappings.
If a mapping has already been performed, indicated by the storage
pointer being non NULL, the function returns success.

.. _`vmw_ttm_unmap_dma`:

vmw_ttm_unmap_dma
=================

.. c:function:: void vmw_ttm_unmap_dma(struct vmw_ttm_tt *vmw_tt)

    Tear down any TTM page device mappings

    :param struct vmw_ttm_tt \*vmw_tt:
        Pointer to a struct vmw_ttm_tt

.. _`vmw_ttm_unmap_dma.description`:

Description
-----------

Tear down any previously set up device DMA mappings and free
any storage space allocated for them. If there are no mappings set up,
this function is a NOP.

.. _`vmw_bo_map_dma`:

vmw_bo_map_dma
==============

.. c:function:: int vmw_bo_map_dma(struct ttm_buffer_object *bo)

    Make sure buffer object pages are visible to the device

    :param struct ttm_buffer_object \*bo:
        Pointer to a struct ttm_buffer_object

.. _`vmw_bo_map_dma.description`:

Description
-----------

Wrapper around vmw_ttm_map_dma, that takes a TTM buffer object pointer
instead of a pointer to a struct vmw_ttm_backend as argument.
Note that the buffer object must be either pinned or reserved before
calling this function.

.. _`vmw_bo_unmap_dma`:

vmw_bo_unmap_dma
================

.. c:function:: void vmw_bo_unmap_dma(struct ttm_buffer_object *bo)

    Make sure buffer object pages are visible to the device

    :param struct ttm_buffer_object \*bo:
        Pointer to a struct ttm_buffer_object

.. _`vmw_bo_unmap_dma.description`:

Description
-----------

Wrapper around vmw_ttm_unmap_dma, that takes a TTM buffer object pointer
instead of a pointer to a struct vmw_ttm_backend as argument.

.. _`vmw_bo_sg_table`:

vmw_bo_sg_table
===============

.. c:function:: const struct vmw_sg_table *vmw_bo_sg_table(struct ttm_buffer_object *bo)

    Return a struct vmw_sg_table object for a TTM buffer object

    :param struct ttm_buffer_object \*bo:
        Pointer to a struct ttm_buffer_object

.. _`vmw_bo_sg_table.description`:

Description
-----------

Returns a pointer to a struct vmw_sg_table object. The object should
not be freed after use.
Note that for the device addresses to be valid, the buffer object must
either be reserved or pinned.

.. _`vmw_move_notify`:

vmw_move_notify
===============

.. c:function:: void vmw_move_notify(struct ttm_buffer_object *bo, bool evict, struct ttm_mem_reg *mem)

    TTM move_notify_callback

    :param struct ttm_buffer_object \*bo:
        The TTM buffer object about to move.

    :param bool evict:
        *undescribed*

    :param struct ttm_mem_reg \*mem:
        The struct ttm_mem_reg indicating to what memory
        region the move is taking place.

.. _`vmw_move_notify.description`:

Description
-----------

Calls move_notify for all subsystems needing it.
(currently only resources).

.. _`vmw_swap_notify`:

vmw_swap_notify
===============

.. c:function:: void vmw_swap_notify(struct ttm_buffer_object *bo)

    TTM move_notify_callback

    :param struct ttm_buffer_object \*bo:
        The TTM buffer object about to be swapped out.

.. This file was automatic generated / don't edit.

