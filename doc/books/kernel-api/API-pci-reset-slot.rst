.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-reset-slot:

==============
pci_reset_slot
==============

*man pci_reset_slot(9)*

*4.6.0-rc5*

reset a PCI slot


Synopsis
========

.. c:function:: int pci_reset_slot( struct pci_slot * slot )

Arguments
=========

``slot``
    PCI slot to reset


Description
===========

A PCI bus may host multiple slots, each slot may support a reset
mechanism independent of other slots. For instance, some slots may
support slot power control. In the case of a 1:1 bus to slot
architecture, this function may wrap the bus reset to avoid spurious
slot related events such as hotplug. Generally a slot reset should be
attempted before a bus reset. All of the function of the slot and any
subordinate buses behind the slot are reset through this function. PCI
config space of all devices in the slot and behind the slot is saved
before and restored after reset.

Return 0 on success, non-zero on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
