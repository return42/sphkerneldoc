.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iommu/of_iommu.c

.. _`of_get_dma_window`:

of_get_dma_window
=================

.. c:function:: int of_get_dma_window(struct device_node *dn, const char *prefix, int index, unsigned long *busno, dma_addr_t *addr, size_t *size)

    Parse \*dma-window property and returns 0 if found.

    :param struct device_node \*dn:
        device node

    :param const char \*prefix:
        prefix for property name if any

    :param int index:
        index to start to parse

    :param unsigned long \*busno:
        Returns busno if supported. Otherwise pass NULL

    :param dma_addr_t \*addr:
        Returns address that DMA starts

    :param size_t \*size:
        Returns the range that DMA can handle

.. _`of_get_dma_window.description`:

Description
-----------

This supports different formats flexibly. "prefix" can be
configured if any. "busno" and "index" are optionally
specified. Set 0(or NULL) if not used.

.. This file was automatic generated / don't edit.

