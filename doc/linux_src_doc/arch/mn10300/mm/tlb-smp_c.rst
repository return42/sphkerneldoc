.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mn10300/mm/tlb-smp.c

.. _`smp_flush_tlb`:

smp_flush_tlb
=============

.. c:function:: void smp_flush_tlb(void *unused)

    Callback to invalidate the TLB.

    :param void \*unused:
        Callback context (ignored).

.. _`flush_tlb_others`:

flush_tlb_others
================

.. c:function:: void flush_tlb_others(cpumask_t cpumask, struct mm_struct *mm, unsigned long va)

    Tell the specified CPUs to invalidate their TLBs

    :param cpumask_t cpumask:
        The list of CPUs to target.

    :param struct mm_struct \*mm:
        The VM context to flush from (if va!=FLUSH_ALL).

    :param unsigned long va:
        Virtual address to flush or FLUSH_ALL to flush everything.

.. _`flush_tlb_mm`:

flush_tlb_mm
============

.. c:function:: void flush_tlb_mm(struct mm_struct *mm)

    Invalidate TLB of specified VM context

    :param struct mm_struct \*mm:
        The VM context to invalidate.

.. _`flush_tlb_current_task`:

flush_tlb_current_task
======================

.. c:function:: void flush_tlb_current_task( void)

    Invalidate TLB of current task

    :param  void:
        no arguments

.. _`flush_tlb_page`:

flush_tlb_page
==============

.. c:function:: void flush_tlb_page(struct vm_area_struct *vma, unsigned long va)

    Invalidate TLB of page

    :param struct vm_area_struct \*vma:
        The VM context to invalidate the page for.

    :param unsigned long va:
        The virtual address of the page to invalidate.

.. _`do_flush_tlb_all`:

do_flush_tlb_all
================

.. c:function:: void do_flush_tlb_all(void *unused)

    Callback to completely invalidate a TLB

    :param void \*unused:
        Callback context (ignored).

.. _`flush_tlb_all`:

flush_tlb_all
=============

.. c:function:: void flush_tlb_all( void)

    Completely invalidate TLBs on all CPUs

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

