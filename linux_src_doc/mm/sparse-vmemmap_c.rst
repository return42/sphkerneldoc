.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/sparse-vmemmap.c

.. _`altmap_alloc_block_buf`:

altmap_alloc_block_buf
======================

.. c:function:: void *altmap_alloc_block_buf(unsigned long size, struct vmem_altmap *altmap)

    allocate pages from the device page map

    :param size:
        size (in bytes) of the allocation
    :type size: unsigned long

    :param altmap:
        device page map
    :type altmap: struct vmem_altmap \*

.. _`altmap_alloc_block_buf.description`:

Description
-----------

Allocations are aligned to the size of the request.

.. This file was automatic generated / don't edit.

