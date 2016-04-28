.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-bus-add-device:

==================
pci_bus_add_device
==================

*man pci_bus_add_device(9)*

*4.6.0-rc5*

start driver for a single device


Synopsis
========

.. c:function:: void pci_bus_add_device( struct pci_dev * dev )

Arguments
=========

``dev``
    device to add


Description
===========

This adds add sysfs entries and start device drivers


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
