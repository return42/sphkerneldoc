.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/ia64/include/asm/sn/tioca_provider.h

.. _`tioca_paddr_to_gart`:

tioca_paddr_to_gart
===================

.. c:function:: u64 tioca_paddr_to_gart(unsigned long paddr)

    Convert an SGI coretalk address to a CA GART entry

    :param unsigned long paddr:
        page address to convert

.. _`tioca_paddr_to_gart.description`:

Description
-----------

Convert a system [coretalk] address to a GART entry.  GART entries are

.. _`tioca_paddr_to_gart.formed-using-the-following`:

formed using the following
--------------------------


data = ( (1<<63) \|  ( (REMAP_NODE_ID << 40) \| (MD_CHIPLET_ID << 38) \|
(REMAP_SYS_ADDR) ) >> 12 )

DATA written to 1 GART TABLE Entry in system memory is remapped system
addr for 1 page

The data is for coretalk address format right shifted 12 bits with a
valid bit.

GART_TABLE_ENTRY [ 25:0 ]  -- REMAP_SYS_ADDRESS[37:12].
GART_TABLE_ENTRY [ 27:26 ] -- SHUB MD chiplet id.
GART_TABLE_ENTRY [ 41:28 ] -- REMAP_NODE_ID.
GART_TABLE_ENTRY [ 63 ]    -- Valid Bit

.. _`tioca_physpage_to_gart`:

tioca_physpage_to_gart
======================

.. c:function:: unsigned long tioca_physpage_to_gart(u64 page_addr)

    Map a host physical page for SGI CA based DMA

    :param u64 page_addr:
        system page address to map

.. _`tioca_tlbflush`:

tioca_tlbflush
==============

.. c:function:: void tioca_tlbflush(struct tioca_kernel *tioca_kernel)

    invalidate cached SGI CA GART TLB entries

    :param struct tioca_kernel \*tioca_kernel:
        CA context

.. _`tioca_tlbflush.description`:

Description
-----------

Invalidate tlb entries for a given CA GART.  Main complexity is to account
for revA bug.

.. This file was automatic generated / don't edit.

