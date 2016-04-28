.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-choose-state:

================
pci_choose_state
================

*man pci_choose_state(9)*

*4.6.0-rc5*

Choose the power state of a PCI device


Synopsis
========

.. c:function:: pci_power_t pci_choose_state( struct pci_dev * dev, pm_message_t state )

Arguments
=========

``dev``
    PCI device to be suspended

``state``
    target sleep state for the whole system. This is the value that is
    passed to ``suspend`` function.


Description
===========

Returns PCI power state suitable for given device and given system
message.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
