
.. _API-pci-reset-bus:

=============
pci_reset_bus
=============

*man pci_reset_bus(9)*

*4.6.0-rc1*

reset a PCI bus


Synopsis
========

.. c:function:: int pci_reset_bus( struct pci_bus * bus )

Arguments
=========

``bus``
    top level PCI bus to reset


Description
===========

Do a bus reset on the given bus and any subordinate buses, saving and restoring state of all devices.

Return 0 on success, non-zero on error.
