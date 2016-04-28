.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-msi-enabled:

===============
pci_msi_enabled
===============

*man pci_msi_enabled(9)*

*4.6.0-rc5*

is MSI enabled?


Synopsis
========

.. c:function:: int pci_msi_enabled( void )

Arguments
=========

``void``
    no arguments


Description
===========

Returns true if MSI has not been disabled by the command-line option
pci=nomsi.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
