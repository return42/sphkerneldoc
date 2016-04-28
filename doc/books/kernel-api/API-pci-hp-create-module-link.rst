.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-hp-create-module-link:

=========================
pci_hp_create_module_link
=========================

*man pci_hp_create_module_link(9)*

*4.6.0-rc5*

create symbolic link to the hotplug driver module.


Synopsis
========

.. c:function:: void pci_hp_create_module_link( struct pci_slot * pci_slot )

Arguments
=========

``pci_slot``
    struct pci_slot


Description
===========

Helper function for pci_hotplug_core.c to create symbolic link to the
hotplug driver module.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
