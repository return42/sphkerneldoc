
.. _API-pci-get-slot:

============
pci_get_slot
============

*man pci_get_slot(9)*

*4.6.0-rc1*

locate PCI device for a given PCI slot


Synopsis
========

.. c:function:: struct pci_dev ⋆ pci_get_slot( struct pci_bus * bus, unsigned int devfn )

Arguments
=========

``bus``
    PCI bus on which desired PCI device resides

``devfn``
    encodes number of PCI slot in which the desired PCI device resides and the logical device number within that slot in case of multi-function devices.


Description
===========

Given a PCI bus and slot/function number, the desired PCI device is located in the list of PCI devices. If the device is found, its reference count is increased and this function
returns a pointer to its data structure. The caller must decrement the reference count by calling ``pci_dev_put``. If no device is found, ``NULL`` is returned.
