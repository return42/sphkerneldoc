.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-reset-bus:

=============
pci_reset_bus
=============

*man pci_reset_bus(9)*

*4.6.0-rc5*

reset a PCI bus


Synopsis
========

.. c:function:: int pci_reset_bus( struct pci_bus * bus )

Arguments
=========

``bus``
    top level PCI bus to reset


Description
===========

Do a bus reset on the given bus and any subordinate buses, saving and
restoring state of all devices.

Return 0 on success, non-zero on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
