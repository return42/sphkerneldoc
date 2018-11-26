.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/cpu/mtrr/cleanup.c

.. _`mtrr_trim_uncached_memory`:

mtrr_trim_uncached_memory
=========================

.. c:function:: int mtrr_trim_uncached_memory(unsigned long end_pfn)

    trim RAM not covered by MTRRs

    :param end_pfn:
        ending page frame number
    :type end_pfn: unsigned long

.. _`mtrr_trim_uncached_memory.description`:

Description
-----------

Some buggy BIOSes don't setup the MTRRs properly for systems with certain
memory configurations.  This routine checks that the highest MTRR matches
the end of memory, to make sure the MTRRs having a write back type cover
all of the memory the kernel is intending to use.  If not, it'll trim any
memory off the end by adjusting end_pfn, removing it from the kernel's
allocation pools, warning the user with an obnoxious message.

.. This file was automatic generated / don't edit.

