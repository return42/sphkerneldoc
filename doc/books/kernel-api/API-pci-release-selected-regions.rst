.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-release-selected-regions:

============================
pci_release_selected_regions
============================

*man pci_release_selected_regions(9)*

*4.6.0-rc5*

Release selected PCI I/O and memory resources


Synopsis
========

.. c:function:: void pci_release_selected_regions( struct pci_dev * pdev, int bars )

Arguments
=========

``pdev``
    PCI device whose resources were previously reserved

``bars``
    Bitmask of BARs to be released


Description
===========

Release selected PCI I/O and memory resources previously reserved. Call
this function only after all use of the PCI regions has ceased.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
