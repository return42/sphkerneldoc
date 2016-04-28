.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-load-saved-state:

====================
pci_load_saved_state
====================

*man pci_load_saved_state(9)*

*4.6.0-rc5*

Reload the provided save state into struct pci_dev.


Synopsis
========

.. c:function:: int pci_load_saved_state( struct pci_dev * dev, struct pci_saved_state * state )

Arguments
=========

``dev``
    PCI device that we're dealing with

``state``
    Saved state returned from ``pci_store_saved_state``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
