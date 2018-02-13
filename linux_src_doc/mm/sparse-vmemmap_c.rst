.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/sparse-vmemmap.c

.. _`altmap_alloc_block_buf`:

altmap_alloc_block_buf
======================

.. c:function:: void *altmap_alloc_block_buf(unsigned long size, struct vmem_altmap *altmap)

    allocate pages from the device page map

    :param unsigned long size:
        size (in bytes) of the allocation

    :param struct vmem_altmap \*altmap:
        device page map

.. _`altmap_alloc_block_buf.description`:

Description
-----------

Allocations are aligned to the size of the request.

.. This file was automatic generated / don't edit.

