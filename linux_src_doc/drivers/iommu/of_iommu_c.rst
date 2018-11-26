.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iommu/of_iommu.c

.. _`of_get_dma_window`:

of_get_dma_window
=================

.. c:function:: int of_get_dma_window(struct device_node *dn, const char *prefix, int index, unsigned long *busno, dma_addr_t *addr, size_t *size)

    Parse \*dma-window property and returns 0 if found.

    :param dn:
        device node
    :type dn: struct device_node \*

    :param prefix:
        prefix for property name if any
    :type prefix: const char \*

    :param index:
        index to start to parse
    :type index: int

    :param busno:
        Returns busno if supported. Otherwise pass NULL
    :type busno: unsigned long \*

    :param addr:
        Returns address that DMA starts
    :type addr: dma_addr_t \*

    :param size:
        Returns the range that DMA can handle
    :type size: size_t \*

.. _`of_get_dma_window.description`:

Description
-----------

This supports different formats flexibly. "prefix" can be
configured if any. "busno" and "index" are optionally
specified. Set 0(or NULL) if not used.

.. This file was automatic generated / don't edit.

