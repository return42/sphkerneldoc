.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-probe-reset-bus:

===================
pci_probe_reset_bus
===================

*man pci_probe_reset_bus(9)*

*4.6.0-rc5*

probe whether a PCI bus can be reset


Synopsis
========

.. c:function:: int pci_probe_reset_bus( struct pci_bus * bus )

Arguments
=========

``bus``
    PCI bus to probe


Description
===========

Return 0 if bus can be reset, negative if a bus reset is not supported.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
