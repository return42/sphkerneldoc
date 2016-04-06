
.. _API-pci-hp-create-module-link:

=========================
pci_hp_create_module_link
=========================

*man pci_hp_create_module_link(9)*

*4.6.0-rc1*

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

Helper function for pci_hotplug_core.c to create symbolic link to the hotplug driver module.
