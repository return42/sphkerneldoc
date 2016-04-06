
.. _API-pci-bus-max-busnr:

=================
pci_bus_max_busnr
=================

*man pci_bus_max_busnr(9)*

*4.6.0-rc1*

returns maximum PCI bus number of given bus' children


Synopsis
========

.. c:function:: unsigned char pci_bus_max_busnr( struct pci_bus * bus )

Arguments
=========

``bus``
    pointer to PCI bus structure to search


Description
===========

Given a PCI bus, returns the highest PCI bus number present in the set including the given PCI bus and its list of child PCI buses.
