
.. _API-pci-destroy-slot:

================
pci_destroy_slot
================

*man pci_destroy_slot(9)*

*4.6.0-rc1*

decrement refcount for physical PCI slot


Synopsis
========

.. c:function:: void pci_destroy_slot( struct pci_slot * slot )

Arguments
=========

``slot``
    struct pci_slot to decrement


Description
===========

``struct`` pci_slot is refcounted, so destroying them is really easy; we just call kobject_put on its kobj and let our release methods do the rest.
