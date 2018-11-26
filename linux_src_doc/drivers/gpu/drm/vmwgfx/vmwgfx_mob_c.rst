.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_mob.c

.. _`vmw_mob_assign_ppn`:

vmw_mob_assign_ppn
==================

.. c:function:: void vmw_mob_assign_ppn(u32 **addr, dma_addr_t val)

    Assign a value to a page table entry

    :param addr:
        Pointer to pointer to page table entry.
    :type addr: u32 \*\*

    :param val:
        The page table entry
    :type val: dma_addr_t

.. _`vmw_mob_assign_ppn.description`:

Description
-----------

Assigns a value to a page table entry pointed to by \*@addr and increments
\*@addr according to the page table entry size.

.. This file was automatic generated / don't edit.

