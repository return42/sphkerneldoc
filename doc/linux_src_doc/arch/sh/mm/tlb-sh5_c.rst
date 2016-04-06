.. -*- coding: utf-8; mode: rst -*-

=========
tlb-sh5.c
=========



.. _xref_sh64_tlb_init:

sh64_tlb_init
=============

.. c:function:: int sh64_tlb_init ( void)

    Perform initial setup for the DTLB and ITLB.

    :param void:
        no arguments




.. _xref_sh64_next_free_dtlb_entry:

sh64_next_free_dtlb_entry
=========================

.. c:function:: unsigned long long sh64_next_free_dtlb_entry ( void)

    Find the next available DTLB entry

    :param void:
        no arguments




.. _xref_sh64_get_wired_dtlb_entry:

sh64_get_wired_dtlb_entry
=========================

.. c:function:: unsigned long long sh64_get_wired_dtlb_entry ( void)

    Allocate a wired (locked-in) entry in the DTLB

    :param void:
        no arguments




.. _xref_sh64_put_wired_dtlb_entry:

sh64_put_wired_dtlb_entry
=========================

.. c:function:: int sh64_put_wired_dtlb_entry (unsigned long long entry)

    Free a wired (locked-in) entry in the DTLB.

    :param unsigned long long entry:
        Address of TLB slot.



Description
-----------

Works like a stack, last one to allocate must be first one to free.




.. _xref_sh64_setup_tlb_slot:

sh64_setup_tlb_slot
===================

.. c:function:: void sh64_setup_tlb_slot (unsigned long long config_addr, unsigned long eaddr, unsigned long asid, unsigned long paddr)

    Load up a translation in a wired slot.

    :param unsigned long long config_addr:
        Address of TLB slot.

    :param unsigned long eaddr:
        Virtual address.

    :param unsigned long asid:
        Address Space Identifier.

    :param unsigned long paddr:
        Physical address.



Description
-----------

Load up a virtual<->physical translation for **eaddr**<->**paddr** in the
pre-allocated TLB slot **config_addr** (see sh64_get_wired_dtlb_entry).




.. _xref_sh64_teardown_tlb_slot:

sh64_teardown_tlb_slot
======================

.. c:function:: void sh64_teardown_tlb_slot (unsigned long long config_addr)

    Teardown a translation.

    :param unsigned long long config_addr:
        Address of TLB slot.



Description
-----------

Teardown any existing mapping in the TLB slot **config_addr**.


