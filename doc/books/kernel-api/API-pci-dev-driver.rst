.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-dev-driver:

==============
pci_dev_driver
==============

*man pci_dev_driver(9)*

*4.6.0-rc5*

get the pci_driver of a device


Synopsis
========

.. c:function:: struct pci_driver * pci_dev_driver( const struct pci_dev * dev )

Arguments
=========

``dev``
    the device to query


Description
===========

Returns the appropriate pci_driver structure or ``NULL`` if there is no
registered driver for the device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
