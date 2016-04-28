.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-set-vpd-size:

================
pci_set_vpd_size
================

*man pci_set_vpd_size(9)*

*4.6.0-rc5*

Set size of Vital Product Data space


Synopsis
========

.. c:function:: int pci_set_vpd_size( struct pci_dev * dev, size_t len )

Arguments
=========

``dev``
    pci device struct

``len``
    size of vpd space


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
