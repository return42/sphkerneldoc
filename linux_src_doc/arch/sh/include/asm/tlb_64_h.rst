.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sh/include/asm/tlb_64.h

.. _`for_each_dtlb_entry`:

for_each_dtlb_entry
===================

.. c:function::  for_each_dtlb_entry( tlb)

    Iterate over free (non-wired) DTLB entries

    :param tlb:
        TLB entry
    :type tlb: 

.. _`for_each_itlb_entry`:

for_each_itlb_entry
===================

.. c:function::  for_each_itlb_entry( tlb)

    Iterate over free (non-wired) ITLB entries

    :param tlb:
        TLB entry
    :type tlb: 

.. _`__flush_tlb_slot`:

__flush_tlb_slot
================

.. c:function:: void __flush_tlb_slot(unsigned long long slot)

    Flushes TLB slot \ ``slot``\ .

    :param slot:
        Address of TLB slot.
    :type slot: unsigned long long

.. This file was automatic generated / don't edit.

