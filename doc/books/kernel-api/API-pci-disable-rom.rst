
.. _API-pci-disable-rom:

===============
pci_disable_rom
===============

*man pci_disable_rom(9)*

*4.6.0-rc1*

disable ROM decoding for a PCI device


Synopsis
========

.. c:function:: void pci_disable_rom( struct pci_dev * pdev )

Arguments
=========

``pdev``
    PCI device to disable


Description
===========

Disable ROM decoding on a PCI device by turning off the last bit in the ROM BAR.
