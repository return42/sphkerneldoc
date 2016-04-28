.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-cfg-access-unlock:

=====================
pci_cfg_access_unlock
=====================

*man pci_cfg_access_unlock(9)*

*4.6.0-rc5*

Unlock PCI config reads/writes


Synopsis
========

.. c:function:: void pci_cfg_access_unlock( struct pci_dev * dev )

Arguments
=========

``dev``
    pci device struct


Description
===========

This function allows PCI config accesses to resume.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
