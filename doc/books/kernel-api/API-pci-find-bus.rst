.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-find-bus:

============
pci_find_bus
============

*man pci_find_bus(9)*

*4.6.0-rc5*

locate PCI bus from a given domain and bus number


Synopsis
========

.. c:function:: struct pci_bus * pci_find_bus( int domain, int busnr )

Arguments
=========

``domain``
    number of PCI domain to search

``busnr``
    number of desired PCI bus


Description
===========

Given a PCI bus number and domain number, the desired PCI bus is located
in the global list of PCI buses. If the bus is found, a pointer to its
data structure is returned. If no bus is found, ``NULL`` is returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
