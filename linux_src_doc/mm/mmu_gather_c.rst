.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/mmu_gather.c

.. _`tlb_gather_mmu`:

tlb_gather_mmu
==============

.. c:function:: void tlb_gather_mmu(struct mmu_gather *tlb, struct mm_struct *mm, unsigned long start, unsigned long end)

    initialize an mmu_gather structure for page-table tear-down

    :param tlb:
        the mmu_gather structure to initialize
    :type tlb: struct mmu_gather \*

    :param mm:
        the mm_struct of the target address space
    :type mm: struct mm_struct \*

    :param start:
        start of the region that will be removed from the page-table
    :type start: unsigned long

    :param end:
        end of the region that will be removed from the page-table
    :type end: unsigned long

.. _`tlb_gather_mmu.description`:

Description
-----------

Called to initialize an (on-stack) mmu_gather structure for page-table
tear-down from \ ``mm``\ . The \ ``start``\  and \ ``end``\  are set to 0 and -1
respectively when \ ``mm``\  is without users and we're going to destroy
the full address space (exit/execve).

.. This file was automatic generated / don't edit.

