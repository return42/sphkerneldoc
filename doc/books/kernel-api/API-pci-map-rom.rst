
.. _API-pci-map-rom:

===========
pci_map_rom
===========

*man pci_map_rom(9)*

*4.6.0-rc1*

map a PCI ROM to kernel space


Synopsis
========

.. c:function:: void __iomem ⋆ pci_map_rom( struct pci_dev * pdev, size_t * size )

Arguments
=========

``pdev``
    pointer to pci device struct

``size``
    pointer to receive size of pci window over ROM


Return
======

kernel virtual pointer to image of ROM

Map a PCI ROM into kernel space. If ROM is boot video ROM, the shadow BIOS copy will be returned instead of the actual ROM.
