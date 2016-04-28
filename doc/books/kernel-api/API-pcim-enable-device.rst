.. -*- coding: utf-8; mode: rst -*-

.. _API-pcim-enable-device:

==================
pcim_enable_device
==================

*man pcim_enable_device(9)*

*4.6.0-rc5*

Managed ``pci_enable_device``


Synopsis
========

.. c:function:: int pcim_enable_device( struct pci_dev * pdev )

Arguments
=========

``pdev``
    PCI device to be initialized


Description
===========

Managed ``pci_enable_device``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
