
.. _API-pci-platform-rom:

================
pci_platform_rom
================

*man pci_platform_rom(9)*

*4.6.0-rc1*

provides a pointer to any ROM image provided by the platform


Synopsis
========

.. c:function:: void __iomem ⋆ pci_platform_rom( struct pci_dev * pdev, size_t * size )

Arguments
=========

``pdev``
    pointer to pci device struct

``size``
    pointer to receive size of pci window over ROM
