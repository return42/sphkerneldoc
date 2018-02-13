.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sh/mm/cache-sh4.c

.. _`__flush_cache_one`:

\__flush_cache_one
==================

.. c:function:: void __flush_cache_one(unsigned long addr, unsigned long phys, unsigned long exec_offset)

    :param unsigned long addr:
        address in memory mapped cache array

    :param unsigned long phys:
        P1 address to flush (has to match tags if addr has 'A' bit
        set i.e. associative write)

    :param unsigned long exec_offset:
        set to 0x20000000 if flush has to be executed from P2
        region else 0x0

.. _`__flush_cache_one.description`:

Description
-----------

The offset into the cache array implied by 'addr' selects the
'colour' of the virtual address range that will be flushed.  The
operation (purge/write-back) is selected by the lower 2 bits of
'phys'.

.. This file was automatic generated / don't edit.

