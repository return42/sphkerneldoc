.. -*- coding: utf-8; mode: rst -*-

==================
cache-inv-icache.c
==================


.. _`flush_icache_page_range`:

flush_icache_page_range
=======================

.. c:function:: void flush_icache_page_range (unsigned long start, unsigned long end)

    Flush dcache and invalidate icache for part of a single page

    :param unsigned long start:
        The starting virtual address of the page part.

    :param unsigned long end:
        The ending virtual address of the page part.



.. _`flush_icache_page_range.description`:

Description
-----------

Invalidate the icache for part of a single page, as determined by the
virtual addresses given.  The page must be in the paged area.  The dcache is
not flushed as the cache must be in write-through mode to get here.



.. _`flush_icache_range`:

flush_icache_range
==================

.. c:function:: void flush_icache_range (unsigned long start, unsigned long end)

    Globally flush dcache and invalidate icache for region

    :param unsigned long start:
        The starting virtual address of the region.

    :param unsigned long end:
        The ending virtual address of the region.



.. _`flush_icache_range.description`:

Description
-----------

This is used by the kernel to globally flush some code it has just written
from the dcache back to RAM and then to globally invalidate the icache over
that region so that that code can be run on all CPUs in the system.

