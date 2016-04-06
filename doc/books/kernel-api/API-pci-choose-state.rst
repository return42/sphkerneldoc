
.. _API-pci-choose-state:

================
pci_choose_state
================

*man pci_choose_state(9)*

*4.6.0-rc1*

Choose the power state of a PCI device


Synopsis
========

.. c:function:: pci_power_t pci_choose_state( struct pci_dev * dev, pm_message_t state )

Arguments
=========

``dev``
    PCI device to be suspended

``state``
    target sleep state for the whole system. This is the value that is passed to ``suspend`` function.


Description
===========

Returns PCI power state suitable for given device and given system message.
