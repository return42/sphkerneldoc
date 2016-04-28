.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-prepare-to-sleep:

====================
pci_prepare_to_sleep
====================

*man pci_prepare_to_sleep(9)*

*4.6.0-rc5*

prepare PCI device for system-wide transition into a sleep state


Synopsis
========

.. c:function:: int pci_prepare_to_sleep( struct pci_dev * dev )

Arguments
=========

``dev``
    Device to handle.


Description
===========

Choose the power state appropriate for the device depending on whether
it can wake up the system and/or is power manageable by the platform
(PCI_D3hot is the default) and put the device into that state.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
