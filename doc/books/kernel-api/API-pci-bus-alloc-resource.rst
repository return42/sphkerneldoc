
.. _API-pci-bus-alloc-resource:

======================
pci_bus_alloc_resource
======================

*man pci_bus_alloc_resource(9)*

*4.6.0-rc1*

allocate a resource from a parent bus


Synopsis
========

.. c:function:: int pci_bus_alloc_resource( struct pci_bus * bus, struct resource * res, resource_size_t size, resource_size_t align, resource_size_t min, unsigned long type_mask, resource_size_t (*alignf) void *, const struct resource *, resource_size_t, resource_size_t, void * alignf_data )

Arguments
=========

``bus``
    PCI bus

``res``
    resource to allocate

``size``
    size of resource to allocate

``align``
    alignment of resource to allocate

``min``
    minimum /proc/iomem address to allocate

``type_mask``
    IORESOURCE_⋆ type flags

``alignf``
    resource alignment function

``alignf_data``
    data argument for resource alignment function


Description
===========

Given the PCI bus a device resides on, the size, minimum address, alignment and type, try to find an acceptable resource allocation for a specific device resource.
