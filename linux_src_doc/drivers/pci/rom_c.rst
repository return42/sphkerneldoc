.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/rom.c

.. _`pci_enable_rom`:

pci_enable_rom
==============

.. c:function:: int pci_enable_rom(struct pci_dev *pdev)

    enable ROM decoding for a PCI device

    :param struct pci_dev \*pdev:
        PCI device to enable

.. _`pci_enable_rom.description`:

Description
-----------

Enable ROM decoding on \ ``dev``\ .  This involves simply turning on the last
bit of the PCI ROM BAR.  Note that some cards may share address decoders
between the ROM and other resources, so enabling it may disable access
to MMIO registers or other card memory.

.. _`pci_disable_rom`:

pci_disable_rom
===============

.. c:function:: void pci_disable_rom(struct pci_dev *pdev)

    disable ROM decoding for a PCI device

    :param struct pci_dev \*pdev:
        PCI device to disable

.. _`pci_disable_rom.description`:

Description
-----------

Disable ROM decoding on a PCI device by turning off the last bit in the
ROM BAR.

.. _`pci_get_rom_size`:

pci_get_rom_size
================

.. c:function:: size_t pci_get_rom_size(struct pci_dev *pdev, void __iomem *rom, size_t size)

    obtain the actual size of the ROM image

    :param struct pci_dev \*pdev:
        target PCI device

    :param void __iomem \*rom:
        kernel virtual pointer to image of ROM

    :param size_t size:
        size of PCI window

.. _`pci_get_rom_size.return`:

Return
------

size of actual ROM image

Determine the actual length of the ROM image.
The PCI window size could be much larger than the
actual image size.

.. _`pci_map_rom`:

pci_map_rom
===========

.. c:function:: void __iomem *pci_map_rom(struct pci_dev *pdev, size_t *size)

    map a PCI ROM to kernel space

    :param struct pci_dev \*pdev:
        pointer to pci device struct

    :param size_t \*size:
        pointer to receive size of pci window over ROM

.. _`pci_map_rom.return`:

Return
------

kernel virtual pointer to image of ROM

Map a PCI ROM into kernel space. If ROM is boot video ROM,
the shadow BIOS copy will be returned instead of the
actual ROM.

.. _`pci_unmap_rom`:

pci_unmap_rom
=============

.. c:function:: void pci_unmap_rom(struct pci_dev *pdev, void __iomem *rom)

    unmap the ROM from kernel space

    :param struct pci_dev \*pdev:
        pointer to pci device struct

    :param void __iomem \*rom:
        virtual address of the previous mapping

.. _`pci_unmap_rom.description`:

Description
-----------

Remove a mapping of a previously mapped ROM

.. _`pci_platform_rom`:

pci_platform_rom
================

.. c:function:: void __iomem *pci_platform_rom(struct pci_dev *pdev, size_t *size)

    provides a pointer to any ROM image provided by the platform

    :param struct pci_dev \*pdev:
        pointer to pci device struct

    :param size_t \*size:
        pointer to receive size of pci window over ROM

.. This file was automatic generated / don't edit.

