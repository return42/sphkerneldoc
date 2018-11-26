.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/mm/tlb_hash64.c

.. _`__flush_hash_table_range`:

\__flush_hash_table_range
=========================

.. c:function:: void __flush_hash_table_range(struct mm_struct *mm, unsigned long start, unsigned long end)

    Flush all HPTEs for a given address range from the hash table (and the TLB). But keeps the linux PTEs intact.

    :param mm:
        mm_struct of the target address space (generally init_mm)
    :type mm: struct mm_struct \*

    :param start:
        starting address
    :type start: unsigned long

    :param end:
        ending address (not included in the flush)
    :type end: unsigned long

.. _`__flush_hash_table_range.description`:

Description
-----------

This function is mostly to be used by some IO hotplug code in order
to remove all hash entries from a given address range used to map IO
space on a removed PCI-PCI bidge without tearing down the full mapping
since 64K pages may overlap with other bridges when using 64K pages
with 4K HW pages on IO space.

Because of that usage pattern, it is implemented for small size rather
than speed.

.. This file was automatic generated / don't edit.

