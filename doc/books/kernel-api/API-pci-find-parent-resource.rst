
.. _API-pci-find-parent-resource:

========================
pci_find_parent_resource
========================

*man pci_find_parent_resource(9)*

*4.6.0-rc1*

return resource region of parent bus of given region


Synopsis
========

.. c:function:: struct resource ⋆ pci_find_parent_resource( const struct pci_dev * dev, struct resource * res )

Arguments
=========

``dev``
    PCI device structure contains resources to be searched

``res``
    child resource record for which parent is sought


Description
===========

For given resource region of given device, return the resource region of parent bus the given region is contained in.
