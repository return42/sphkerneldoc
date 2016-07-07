.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mn10300/include/asm/tlbflush.h

.. _`local_flush_tlb`:

local_flush_tlb
===============

.. c:function:: void local_flush_tlb( void)

    Flush the current MM's entries from the local CPU's TLBs

    :param  void:
        no arguments

.. _`local_flush_tlb_all`:

local_flush_tlb_all
===================

.. c:function:: void local_flush_tlb_all( void)

    Flush all entries from the local CPU's TLBs

    :param  void:
        no arguments

.. _`local_flush_tlb_one`:

local_flush_tlb_one
===================

.. c:function:: void local_flush_tlb_one(unsigned long addr)

    Flush one entry from the local CPU's TLBs

    :param unsigned long addr:
        *undescribed*

.. _`local_flush_tlb_page`:

local_flush_tlb_page
====================

.. c:function:: void local_flush_tlb_page(struct mm_struct *mm, unsigned long addr)

    Flush a page's entry from the local CPU's TLBs

    :param struct mm_struct \*mm:
        The MM to flush for

    :param unsigned long addr:
        The address of the target page in RAM (not its page struct)

.. This file was automatic generated / don't edit.

