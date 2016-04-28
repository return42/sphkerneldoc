.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-save-state:

==============
pci_save_state
==============

*man pci_save_state(9)*

*4.6.0-rc5*

save the PCI configuration space of a device before suspending


Synopsis
========

.. c:function:: int pci_save_state( struct pci_dev * dev )

Arguments
=========

``dev``
    - PCI device that we're dealing with


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
