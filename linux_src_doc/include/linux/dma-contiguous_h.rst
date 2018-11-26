.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/dma-contiguous.h

.. _`dma_declare_contiguous`:

dma_declare_contiguous
======================

.. c:function:: int dma_declare_contiguous(struct device *dev, phys_addr_t size, phys_addr_t base, phys_addr_t limit)

    reserve area for contiguous memory handling for particular device

    :param dev:
        Pointer to device structure.
    :type dev: struct device \*

    :param size:
        Size of the reserved memory.
    :type size: phys_addr_t

    :param base:
        Start address of the reserved memory (optional, 0 for any).
    :type base: phys_addr_t

    :param limit:
        End address of the reserved memory (optional, 0 for any).
    :type limit: phys_addr_t

.. _`dma_declare_contiguous.description`:

Description
-----------

This function reserves memory for specified device. It should be
called by board specific code when early allocator (memblock or bootmem)
is still activate.

.. This file was automatic generated / don't edit.

