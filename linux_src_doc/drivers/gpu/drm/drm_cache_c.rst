.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_cache.c

.. _`drm_clflush_pages`:

drm_clflush_pages
=================

.. c:function:: void drm_clflush_pages(struct page  *pages, unsigned long num_pages)

    Flush dcache lines of a set of pages.

    :param pages:
        List of pages to be flushed.
    :type pages: struct page  \*

    :param num_pages:
        Number of pages in the array.
    :type num_pages: unsigned long

.. _`drm_clflush_pages.description`:

Description
-----------

Flush every data cache line entry that points to an address belonging
to a page in the array.

.. _`drm_clflush_sg`:

drm_clflush_sg
==============

.. c:function:: void drm_clflush_sg(struct sg_table *st)

    Flush dcache lines pointing to a scather-gather.

    :param st:
        struct sg_table.
    :type st: struct sg_table \*

.. _`drm_clflush_sg.description`:

Description
-----------

Flush every data cache line entry that points to an address in the
sg.

.. _`drm_clflush_virt_range`:

drm_clflush_virt_range
======================

.. c:function:: void drm_clflush_virt_range(void *addr, unsigned long length)

    Flush dcache lines of a region

    :param addr:
        Initial kernel memory address.
    :type addr: void \*

    :param length:
        Region size.
    :type length: unsigned long

.. _`drm_clflush_virt_range.description`:

Description
-----------

Flush every data cache line entry that points to an address in the
region requested.

.. This file was automatic generated / don't edit.

