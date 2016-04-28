.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-set-master:

==============
pci_set_master
==============

*man pci_set_master(9)*

*4.6.0-rc5*

enables bus-mastering for device dev


Synopsis
========

.. c:function:: void pci_set_master( struct pci_dev * dev )

Arguments
=========

``dev``
    the PCI device to enable


Description
===========

Enables bus-mastering on the device and calls ``pcibios_set_master`` to
do the needed arch specific settings.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
