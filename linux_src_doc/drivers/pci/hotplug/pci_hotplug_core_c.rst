.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/hotplug/pci_hotplug_core.c

.. _`__pci_hp_register`:

__pci_hp_register
=================

.. c:function:: int __pci_hp_register(struct hotplug_slot *slot, struct pci_bus *bus, int devnr, const char *name, struct module *owner, const char *mod_name)

    register a hotplug_slot with the PCI hotplug subsystem

    :param struct hotplug_slot \*slot:
        pointer to the \ :c:type:`struct hotplug_slot <hotplug_slot>`\  to register

    :param struct pci_bus \*bus:
        bus this slot is on

    :param int devnr:
        device number

    :param const char \*name:
        name registered with kobject core

    :param struct module \*owner:
        caller module owner

    :param const char \*mod_name:
        caller module name

.. _`__pci_hp_register.description`:

Description
-----------

Registers a hotplug slot with the pci hotplug subsystem, which will allow
userspace interaction to the slot.

Returns 0 if successful, anything else for an error.

.. _`pci_hp_deregister`:

pci_hp_deregister
=================

.. c:function:: int pci_hp_deregister(struct hotplug_slot *slot)

    deregister a hotplug_slot with the PCI hotplug subsystem

    :param struct hotplug_slot \*slot:
        pointer to the \ :c:type:`struct hotplug_slot <hotplug_slot>`\  to deregister

.. _`pci_hp_deregister.description`:

Description
-----------

The \ ``slot``\  must have been registered with the pci hotplug subsystem
previously with a call to \ :c:func:`pci_hp_register`\ .

Returns 0 if successful, anything else for an error.

.. _`pci_hp_change_slot_info`:

pci_hp_change_slot_info
=======================

.. c:function:: int pci_hp_change_slot_info(struct hotplug_slot *slot, struct hotplug_slot_info *info)

    changes the slot's information structure in the core

    :param struct hotplug_slot \*slot:
        pointer to the slot whose info has changed

    :param struct hotplug_slot_info \*info:
        pointer to the info copy into the slot's info structure

.. _`pci_hp_change_slot_info.description`:

Description
-----------

\ ``slot``\  must have been registered with the pci
hotplug subsystem previously with a call to \ :c:func:`pci_hp_register`\ .

Returns 0 if successful, anything else for an error.

.. This file was automatic generated / don't edit.

