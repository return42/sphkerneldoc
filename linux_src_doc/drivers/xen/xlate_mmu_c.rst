.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/xen/xlate_mmu.c

.. _`xen_xlate_map_ballooned_pages`:

xen_xlate_map_ballooned_pages
=============================

.. c:function:: int xen_xlate_map_ballooned_pages(xen_pfn_t **gfns, void **virt, unsigned long nr_grant_frames)

    map a new set of ballooned pages

    :param xen_pfn_t \*\*gfns:
        returns the array of corresponding GFNs

    :param void \*\*virt:
        returns the virtual address of the mapped region

    :param unsigned long nr_grant_frames:
        number of GFNs
        \ ``return``\  0 on success, error otherwise

.. _`xen_xlate_map_ballooned_pages.description`:

Description
-----------

This allocates a set of ballooned pages and maps them into the
kernel's address space.

.. This file was automatic generated / don't edit.

