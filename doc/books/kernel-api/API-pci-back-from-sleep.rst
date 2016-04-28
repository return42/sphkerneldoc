.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-back-from-sleep:

===================
pci_back_from_sleep
===================

*man pci_back_from_sleep(9)*

*4.6.0-rc5*

turn PCI device on during system-wide transition into working state


Synopsis
========

.. c:function:: int pci_back_from_sleep( struct pci_dev * dev )

Arguments
=========

``dev``
    Device to handle.


Description
===========

Disable device's system wake-up capability and put it into D0.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
