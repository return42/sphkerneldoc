
.. _API-pci-prepare-to-sleep:

====================
pci_prepare_to_sleep
====================

*man pci_prepare_to_sleep(9)*

*4.6.0-rc1*

prepare PCI device for system-wide transition into a sleep state


Synopsis
========

.. c:function:: int pci_prepare_to_sleep( struct pci_dev * dev )

Arguments
=========

``dev``
    Device to handle.


Description
===========

Choose the power state appropriate for the device depending on whether it can wake up the system and/or is power manageable by the platform (PCI_D3hot is the default) and put the
device into that state.
