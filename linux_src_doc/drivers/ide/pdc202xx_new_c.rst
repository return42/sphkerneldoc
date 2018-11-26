.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/pdc202xx_new.c

.. _`get_indexed_reg`:

get_indexed_reg
===============

.. c:function:: u8 get_indexed_reg(ide_hwif_t *hwif, u8 index)

    Get indexed register

    :param hwif:
        for the port address
    :type hwif: ide_hwif_t \*

    :param index:
        index of the indexed register
    :type index: u8

.. _`set_indexed_reg`:

set_indexed_reg
===============

.. c:function:: void set_indexed_reg(ide_hwif_t *hwif, u8 index, u8 value)

    Set indexed register

    :param hwif:
        for the port address
    :type hwif: ide_hwif_t \*

    :param index:
        index of the indexed register
    :type index: u8

    :param value:
        *undescribed*
    :type value: u8

.. _`read_counter`:

read_counter
============

.. c:function:: long read_counter(u32 dma_base)

    Read the byte count registers

    :param dma_base:
        for the port address
    :type dma_base: u32

.. _`detect_pll_input_clock`:

detect_pll_input_clock
======================

.. c:function:: long detect_pll_input_clock(unsigned long dma_base)

    Detect the PLL input clock in Hz.

    :param dma_base:
        for the port address
        E.g. 16949000 on 33 MHz PCI bus, i.e. half of the PCI clock.
    :type dma_base: unsigned long

.. _`pdc202new_init_one`:

pdc202new_init_one
==================

.. c:function:: int pdc202new_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    called when a pdc202xx is found

    :param dev:
        the pdc202new device
    :type dev: struct pci_dev \*

    :param id:
        the matching pci id
    :type id: const struct pci_device_id \*

.. _`pdc202new_init_one.description`:

Description
-----------

Called when the PCI registration layer (or the IDE initialization)
finds a device matching our IDE device tables.

.. This file was automatic generated / don't edit.

