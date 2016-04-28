.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-select-bars:

===============
pci_select_bars
===============

*man pci_select_bars(9)*

*4.6.0-rc5*

Make BAR mask from the type of resource


Synopsis
========

.. c:function:: int pci_select_bars( struct pci_dev * dev, unsigned long flags )

Arguments
=========

``dev``
    the PCI device for which BAR mask is made

``flags``
    resource type mask to be selected


Description
===========

This helper routine makes bar mask from the type of resource.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
