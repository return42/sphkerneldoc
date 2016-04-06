
.. _API-pci-set-master:

==============
pci_set_master
==============

*man pci_set_master(9)*

*4.6.0-rc1*

enables bus-mastering for device dev


Synopsis
========

.. c:function:: void pci_set_master( struct pci_dev * dev )

Arguments
=========

``dev``
    the PCI device to enable


Description
===========

Enables bus-mastering on the device and calls ``pcibios_set_master`` to do the needed arch specific settings.
