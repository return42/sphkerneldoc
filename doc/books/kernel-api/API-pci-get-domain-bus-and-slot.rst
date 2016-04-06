
.. _API-pci-get-domain-bus-and-slot:

===========================
pci_get_domain_bus_and_slot
===========================

*man pci_get_domain_bus_and_slot(9)*

*4.6.0-rc1*

locate PCI device for a given PCI domain (segment), bus, and slot


Synopsis
========

.. c:function:: struct pci_dev ⋆ pci_get_domain_bus_and_slot( int domain, unsigned int bus, unsigned int devfn )

Arguments
=========

``domain``
    PCI domain/segment on which the PCI device resides.

``bus``
    PCI bus on which desired PCI device resides

``devfn``
    encodes number of PCI slot in which the desired PCI device resides and the logical device number within that slot in case of multi-function devices.


Description
===========

Given a PCI domain, bus, and slot/function number, the desired PCI device is located in the list of PCI devices. If the device is found, its reference count is increased and this
function returns a pointer to its data structure. The caller must decrement the reference count by calling ``pci_dev_put``. If no device is found, ``NULL`` is returned.
