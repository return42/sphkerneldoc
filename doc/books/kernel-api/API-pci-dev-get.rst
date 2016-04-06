
.. _API-pci-dev-get:

===========
pci_dev_get
===========

*man pci_dev_get(9)*

*4.6.0-rc1*

increments the reference count of the pci device structure


Synopsis
========

.. c:function:: struct pci_dev ⋆ pci_dev_get( struct pci_dev * dev )

Arguments
=========

``dev``
    the device being referenced


Description
===========

Each live reference to a device should be refcounted.

Drivers for PCI devices should normally record such references in their ``probe`` methods, when they bind to a device, and release them by calling ``pci_dev_put``, in their
``disconnect`` methods.

A pointer to the device with the incremented reference counter is returned.
