.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-bus-max-busnr:

=================
pci_bus_max_busnr
=================

*man pci_bus_max_busnr(9)*

*4.6.0-rc5*

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

Given a PCI bus, returns the highest PCI bus number present in the set
including the given PCI bus and its list of child PCI buses.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
