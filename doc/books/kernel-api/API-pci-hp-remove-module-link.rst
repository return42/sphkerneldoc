.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-hp-remove-module-link:

=========================
pci_hp_remove_module_link
=========================

*man pci_hp_remove_module_link(9)*

*4.6.0-rc5*

remove symbolic link to the hotplug driver module.


Synopsis
========

.. c:function:: void pci_hp_remove_module_link( struct pci_slot * pci_slot )

Arguments
=========

``pci_slot``
    struct pci_slot


Description
===========

Helper function for pci_hotplug_core.c to remove symbolic link to the
hotplug driver module.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
