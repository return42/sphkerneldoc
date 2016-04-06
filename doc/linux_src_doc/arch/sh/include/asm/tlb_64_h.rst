.. -*- coding: utf-8; mode: rst -*-

========
tlb_64.h
========



.. _xref_for_each_dtlb_entry:

for_each_dtlb_entry
===================

.. c:function:: for_each_dtlb_entry ( tlb)

    Iterate over free (non-wired) DTLB entries

    :param tlb:
        TLB entry




.. _xref_for_each_itlb_entry:

for_each_itlb_entry
===================

.. c:function:: for_each_itlb_entry ( tlb)

    Iterate over free (non-wired) ITLB entries

    :param tlb:
        TLB entry




.. _xref___flush_tlb_slot:

__flush_tlb_slot
================

.. c:function:: void __flush_tlb_slot (unsigned long long slot)

    Flushes TLB slot @slot.

    :param unsigned long long slot:
        Address of TLB slot.


