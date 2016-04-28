.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-bus-add-devices:

===================
pci_bus_add_devices
===================

*man pci_bus_add_devices(9)*

*4.6.0-rc5*

start driver for PCI devices


Synopsis
========

.. c:function:: void pci_bus_add_devices( const struct pci_bus * bus )

Arguments
=========

``bus``
    bus to check for new devices


Description
===========

Start driver for PCI devices and add some sysfs entries.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
