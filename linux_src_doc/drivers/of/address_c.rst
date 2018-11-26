.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/of/address.c

.. _`of_address_to_resource`:

of_address_to_resource
======================

.. c:function:: int of_address_to_resource(struct device_node *dev, int index, struct resource *r)

    Translate device tree address and return as resource

    :param dev:
        *undescribed*
    :type dev: struct device_node \*

    :param index:
        *undescribed*
    :type index: int

    :param r:
        *undescribed*
    :type r: struct resource \*

.. _`of_address_to_resource.description`:

Description
-----------

Note that if your address is a PIO address, the conversion will fail if
the physical address can't be internally converted to an IO token with
\ :c:func:`pci_address_to_pio`\ , that is because it's either called too early or it
can't be matched to any host bridge IO space

.. _`of_iomap`:

of_iomap
========

.. c:function:: void __iomem *of_iomap(struct device_node *np, int index)

    Maps the memory mapped IO for a given device_node

    :param np:
        *undescribed*
    :type np: struct device_node \*

    :param index:
        index of the io range
    :type index: int

.. _`of_iomap.description`:

Description
-----------

Returns a pointer to the mapped memory

.. _`of_dma_get_range`:

of_dma_get_range
================

.. c:function:: int of_dma_get_range(struct device_node *np, u64 *dma_addr, u64 *paddr, u64 *size)

    Get DMA range info

    :param np:
        device node to get DMA range info
    :type np: struct device_node \*

    :param dma_addr:
        pointer to store initial DMA address of DMA range
    :type dma_addr: u64 \*

    :param paddr:
        pointer to store initial CPU address of DMA range
    :type paddr: u64 \*

    :param size:
        pointer to store size of DMA range
    :type size: u64 \*

.. _`of_dma_get_range.description`:

Description
-----------

Look in bottom up direction for the first "dma-ranges" property
and parse it.
dma-ranges format:
DMA addr (dma_addr)     : naddr cells
CPU addr (phys_addr_t)  : pna cells
size                    : nsize cells

It returns -ENODEV if "dma-ranges" property was not found
for this device in DT.

.. _`of_dma_is_coherent`:

of_dma_is_coherent
==================

.. c:function:: bool of_dma_is_coherent(struct device_node *np)

    Check if device is coherent

    :param np:
        device node
    :type np: struct device_node \*

.. _`of_dma_is_coherent.description`:

Description
-----------

It returns true if "dma-coherent" property was found
for this device in DT.

.. This file was automatic generated / don't edit.

