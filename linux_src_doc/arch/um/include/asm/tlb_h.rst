.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/um/include/asm/tlb.h

.. _`tlb_remove_tlb_entry`:

tlb_remove_tlb_entry
====================

.. c:function::  tlb_remove_tlb_entry( tlb,  ptep,  address)

    remember a pte unmapping for later tlb invalidation.

    :param tlb:
        *undescribed*
    :type tlb: 

    :param ptep:
        *undescribed*
    :type ptep: 

    :param address:
        *undescribed*
    :type address: 

.. _`tlb_remove_tlb_entry.description`:

Description
-----------

Record the fact that pte's were really umapped in ->need_flush, so we can
later optimise away the tlb invalidate.   This helps when userspace is
unmapping already-unmapped pages, which happens quite a lot.

.. This file was automatic generated / don't edit.

