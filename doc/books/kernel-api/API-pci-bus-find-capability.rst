.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-bus-find-capability:

=======================
pci_bus_find_capability
=======================

*man pci_bus_find_capability(9)*

*4.6.0-rc5*

query for devices' capabilities


Synopsis
========

.. c:function:: int pci_bus_find_capability( struct pci_bus * bus, unsigned int devfn, int cap )

Arguments
=========

``bus``
    the PCI bus to query

``devfn``
    PCI device to query

``cap``
    capability code


Description
===========

Like ``pci_find_capability`` but works for pci devices that do not have
a pci_dev structure set up yet.

Returns the address of the requested capability structure within the
device's PCI configuration space or 0 in case the device does not
support it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
