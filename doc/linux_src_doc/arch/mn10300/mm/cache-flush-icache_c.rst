.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mn10300/mm/cache-flush-icache.c

.. _`flush_icache_page`:

flush_icache_page
=================

.. c:function:: void flush_icache_page(struct vm_area_struct *vma, struct page *page)

    Flush a page from the dcache and invalidate the icache

    :param struct vm_area_struct \*vma:
        The VMA the page is part of.

    :param struct page \*page:
        The page to be flushed.

.. _`flush_icache_page.description`:

Description
-----------

Write a page back from the dcache and invalidate the icache so that we can
run code from it that we've just written into it

.. _`flush_icache_page_range`:

flush_icache_page_range
=======================

.. c:function:: void flush_icache_page_range(unsigned long start, unsigned long end)

    Flush dcache and invalidate icache for part of a single page

    :param unsigned long start:
        The starting virtual address of the page part.

    :param unsigned long end:
        The ending virtual address of the page part.

.. _`flush_icache_page_range.description`:

Description
-----------

Flush the dcache and invalidate the icache for part of a single page, as
determined by the virtual addresses given.  The page must be in the paged
area.

.. _`flush_icache_range`:

flush_icache_range
==================

.. c:function:: void flush_icache_range(unsigned long start, unsigned long end)

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

.. This file was automatic generated / don't edit.

