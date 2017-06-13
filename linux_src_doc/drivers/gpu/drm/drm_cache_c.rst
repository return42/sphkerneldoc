.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_cache.c

.. _`drm_clflush_pages`:

drm_clflush_pages
=================

.. c:function:: void drm_clflush_pages(struct page  *pages[], unsigned long num_pages)

    Flush dcache lines of a set of pages.

    :param struct page  \*pages:
        List of pages to be flushed.

    :param unsigned long num_pages:
        Number of pages in the array.

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

    :param struct sg_table \*st:
        struct sg_table.

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

    :param void \*addr:
        Initial kernel memory address.

    :param unsigned long length:
        Region size.

.. _`drm_clflush_virt_range.description`:

Description
-----------

Flush every data cache line entry that points to an address in the
region requested.

.. This file was automatic generated / don't edit.

