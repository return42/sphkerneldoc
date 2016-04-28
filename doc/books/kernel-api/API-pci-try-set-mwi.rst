.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-try-set-mwi:

===============
pci_try_set_mwi
===============

*man pci_try_set_mwi(9)*

*4.6.0-rc5*

enables memory-write-invalidate PCI transaction


Synopsis
========

.. c:function:: int pci_try_set_mwi( struct pci_dev * dev )

Arguments
=========

``dev``
    the PCI device for which MWI is enabled


Description
===========

Enables the Memory-Write-Invalidate transaction in ``PCI_COMMAND``.
Callers are not required to check the return value.


RETURNS
=======

An appropriate -ERRNO error value on error, or zero for success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
