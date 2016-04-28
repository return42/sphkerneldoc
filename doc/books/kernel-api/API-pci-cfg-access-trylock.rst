.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-cfg-access-trylock:

======================
pci_cfg_access_trylock
======================

*man pci_cfg_access_trylock(9)*

*4.6.0-rc5*

try to lock PCI config reads/writes


Synopsis
========

.. c:function:: bool pci_cfg_access_trylock( struct pci_dev * dev )

Arguments
=========

``dev``
    pci device struct


Description
===========

Same as pci_cfg_access_lock, but will return 0 if access is already
locked, 1 otherwise. This function can be used from atomic contexts.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
