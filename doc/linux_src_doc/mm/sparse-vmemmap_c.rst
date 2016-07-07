.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/sparse-vmemmap.c

.. _`vmem_altmap_alloc`:

vmem_altmap_alloc
=================

.. c:function:: unsigned long vmem_altmap_alloc(struct vmem_altmap *altmap, unsigned long nr_pfns)

    allocate pages from the vmem_altmap reservation \ ``altmap``\  - reserved page pool for the allocation \ ``nr_pfns``\  - size (in pages) of the allocation

    :param struct vmem_altmap \*altmap:
        *undescribed*

    :param unsigned long nr_pfns:
        *undescribed*

.. _`vmem_altmap_alloc.description`:

Description
-----------

Allocations are aligned to the size of the request

.. This file was automatic generated / don't edit.

