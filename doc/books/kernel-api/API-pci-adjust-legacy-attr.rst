.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-adjust-legacy-attr:

======================
pci_adjust_legacy_attr
======================

*man pci_adjust_legacy_attr(9)*

*4.6.0-rc5*

adjustment of legacy file attributes


Synopsis
========

.. c:function:: void pci_adjust_legacy_attr( struct pci_bus * b, enum pci_mmap_state mmap_type )

Arguments
=========

``b``
    bus to create files under

``mmap_type``
    I/O port or memory


Description
===========

Stub implementation. Can be overridden by arch if necessary.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
