.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/hexagon/kernel/dma.c

.. _`hexagon_map_page`:

hexagon_map_page
================

.. c:function:: dma_addr_t hexagon_map_page(struct device *dev, struct page *page, unsigned long offset, size_t size, enum dma_data_direction dir, struct dma_attrs *attrs)

    maps an address for device DMA

    :param struct device \*dev:
        pointer to DMA device

    :param struct page \*page:
        pointer to page struct of DMA memory

    :param unsigned long offset:
        offset within page

    :param size_t size:
        size of memory to map

    :param enum dma_data_direction dir:
        transfer direction

    :param struct dma_attrs \*attrs:
        pointer to DMA attrs (not used)

.. _`hexagon_map_page.description`:

Description
-----------

Called to map a memory address to a DMA address prior
to accesses to/from device.

We don't particularly have many hoops to jump through
so far.  Straight translation between phys and virtual.

DMA is not cache coherent so sync is necessary; this
seems to be a convenient place to do it.

.. This file was automatic generated / don't edit.

