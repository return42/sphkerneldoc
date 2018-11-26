.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/pci/pci-octeon.c

.. _`pcibios_map_irq`:

pcibios_map_irq
===============

.. c:function:: int pcibios_map_irq(const struct pci_dev *dev, u8 slot, u8 pin)

    :param dev:
        The Linux PCI device structure for the device to map
    :type dev: const struct pci_dev \*

    :param slot:
        The slot number for this device on \__BUS 0__. Linux
        enumerates through all the bridges and figures out the
        slot on Bus 0 where this device eventually hooks to.
    :type slot: u8

    :param pin:
        The PCI interrupt pin read from the device, then swizzled
        as it goes through each bridge.
        Returns Interrupt number for the device
    :type pin: u8

.. _`octeon_get_pci_interrupts`:

octeon_get_pci_interrupts
=========================

.. c:function:: const char *octeon_get_pci_interrupts( void)

    character in the return string represents the interrupt line for the device at that position. Device 1 maps to the first character, etc. The characters A-D are used for PCI interrupts.

    :param void:
        no arguments
    :type void: 

.. _`octeon_get_pci_interrupts.description`:

Description
-----------

Returns PCI interrupt mapping

.. _`octeon_pci_pcibios_map_irq`:

octeon_pci_pcibios_map_irq
==========================

.. c:function:: int octeon_pci_pcibios_map_irq(const struct pci_dev *dev, u8 slot, u8 pin)

    :param dev:
        The Linux PCI device structure for the device to map
    :type dev: const struct pci_dev \*

    :param slot:
        The slot number for this device on \__BUS 0__. Linux
        enumerates through all the bridges and figures out the
        slot on Bus 0 where this device eventually hooks to.
    :type slot: u8

    :param pin:
        The PCI interrupt pin read from the device, then swizzled
        as it goes through each bridge.
        Returns Interrupt number for the device
    :type pin: u8

.. This file was automatic generated / don't edit.

