
.. _API---pci-hp-register:

=================
__pci_hp_register
=================

*man __pci_hp_register(9)*

*4.6.0-rc1*

register a hotplug_slot with the PCI hotplug subsystem


Synopsis
========

.. c:function:: int __pci_hp_register( struct hotplug_slot * slot, struct pci_bus * bus, int devnr, const char * name, struct module * owner, const char * mod_name )

Arguments
=========

``slot``
    pointer to the ``struct hotplug_slot`` to register

``bus``
    bus this slot is on

``devnr``
    device number

``name``
    name registered with kobject core

``owner``
    caller module owner

``mod_name``
    caller module name


Description
===========

Registers a hotplug slot with the pci hotplug subsystem, which will allow userspace interaction to the slot.

Returns 0 if successful, anything else for an error.
