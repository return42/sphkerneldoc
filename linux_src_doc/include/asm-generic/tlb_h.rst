.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/asm-generic/tlb.h

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

Record the fact that pte's were really unmapped by updating the range,
so we can later optimise away the tlb invalidate.   This helps when
userspace is unmapping already-unmapped pages, which happens quite a lot.

.. _`__tlb_remove_pmd_tlb_entry`:

\__tlb_remove_pmd_tlb_entry
===========================

.. c:function::  __tlb_remove_pmd_tlb_entry( tlb,  pmdp,  address)

    remember a pmd mapping for later tlb invalidation This is a nop so far, because only x86 needs it.

    :param tlb:
        *undescribed*
    :type tlb: 

    :param pmdp:
        *undescribed*
    :type pmdp: 

    :param address:
        *undescribed*
    :type address: 

.. _`__tlb_remove_pud_tlb_entry`:

\__tlb_remove_pud_tlb_entry
===========================

.. c:function::  __tlb_remove_pud_tlb_entry( tlb,  pudp,  address)

    remember a pud mapping for later tlb invalidation. This is a nop so far, because only x86 needs it.

    :param tlb:
        *undescribed*
    :type tlb: 

    :param pudp:
        *undescribed*
    :type pudp: 

    :param address:
        *undescribed*
    :type address: 

.. This file was automatic generated / don't edit.

