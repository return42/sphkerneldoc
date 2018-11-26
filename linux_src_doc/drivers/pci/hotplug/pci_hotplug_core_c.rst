.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/hotplug/pci_hotplug_core.c

.. _`__pci_hp_register`:

__pci_hp_register
=================

.. c:function:: int __pci_hp_register(struct hotplug_slot *slot, struct pci_bus *bus, int devnr, const char *name, struct module *owner, const char *mod_name)

    register a hotplug_slot with the PCI hotplug subsystem

    :param slot:
        pointer to the \ :c:type:`struct hotplug_slot <hotplug_slot>`\  to register
    :type slot: struct hotplug_slot \*

    :param bus:
        bus this slot is on
    :type bus: struct pci_bus \*

    :param devnr:
        device number
    :type devnr: int

    :param name:
        name registered with kobject core
    :type name: const char \*

    :param owner:
        caller module owner
    :type owner: struct module \*

    :param mod_name:
        caller module name
    :type mod_name: const char \*

.. _`__pci_hp_register.description`:

Description
-----------

Prepares a hotplug slot for in-kernel use and immediately publishes it to
user space in one go.  Drivers may alternatively carry out the two steps
separately by invoking \ :c:func:`pci_hp_initialize`\  and \ :c:func:`pci_hp_add`\ .

Returns 0 if successful, anything else for an error.

.. _`__pci_hp_initialize`:

__pci_hp_initialize
===================

.. c:function:: int __pci_hp_initialize(struct hotplug_slot *slot, struct pci_bus *bus, int devnr, const char *name, struct module *owner, const char *mod_name)

    prepare hotplug slot for in-kernel use

    :param slot:
        pointer to the \ :c:type:`struct hotplug_slot <hotplug_slot>`\  to initialize
    :type slot: struct hotplug_slot \*

    :param bus:
        bus this slot is on
    :type bus: struct pci_bus \*

    :param devnr:
        slot number
    :type devnr: int

    :param name:
        name registered with kobject core
    :type name: const char \*

    :param owner:
        caller module owner
    :type owner: struct module \*

    :param mod_name:
        caller module name
    :type mod_name: const char \*

.. _`__pci_hp_initialize.description`:

Description
-----------

Allocate and fill in a PCI slot for use by a hotplug driver.  Once this has
been called, the driver may invoke \ :c:func:`hotplug_slot_name`\  to get the slot's
unique name.  The driver must be prepared to handle a ->reset_slot callback
from this point on.

Returns 0 on success or a negative int on error.

.. _`pci_hp_add`:

pci_hp_add
==========

.. c:function:: int pci_hp_add(struct hotplug_slot *slot)

    publish hotplug slot to user space

    :param slot:
        pointer to the \ :c:type:`struct hotplug_slot <hotplug_slot>`\  to publish
    :type slot: struct hotplug_slot \*

.. _`pci_hp_add.description`:

Description
-----------

Make a hotplug slot's sysfs interface available and inform user space of its
addition by sending a uevent.  The hotplug driver must be prepared to handle
all \ :c:type:`struct hotplug_slot_ops <hotplug_slot_ops>`\  callbacks from this point on.

Returns 0 on success or a negative int on error.

.. _`pci_hp_deregister`:

pci_hp_deregister
=================

.. c:function:: void pci_hp_deregister(struct hotplug_slot *slot)

    deregister a hotplug_slot with the PCI hotplug subsystem

    :param slot:
        pointer to the \ :c:type:`struct hotplug_slot <hotplug_slot>`\  to deregister
    :type slot: struct hotplug_slot \*

.. _`pci_hp_deregister.description`:

Description
-----------

The \ ``slot``\  must have been registered with the pci hotplug subsystem
previously with a call to \ :c:func:`pci_hp_register`\ .

Returns 0 if successful, anything else for an error.

.. _`pci_hp_del`:

pci_hp_del
==========

.. c:function:: void pci_hp_del(struct hotplug_slot *slot)

    unpublish hotplug slot from user space

    :param slot:
        pointer to the \ :c:type:`struct hotplug_slot <hotplug_slot>`\  to unpublish
    :type slot: struct hotplug_slot \*

.. _`pci_hp_del.description`:

Description
-----------

Remove a hotplug slot's sysfs interface.

Returns 0 on success or a negative int on error.

.. _`pci_hp_destroy`:

pci_hp_destroy
==============

.. c:function:: void pci_hp_destroy(struct hotplug_slot *slot)

    remove hotplug slot from in-kernel use

    :param slot:
        pointer to the \ :c:type:`struct hotplug_slot <hotplug_slot>`\  to destroy
    :type slot: struct hotplug_slot \*

.. _`pci_hp_destroy.description`:

Description
-----------

Destroy a PCI slot used by a hotplug driver.  Once this has been called,
the driver may no longer invoke \ :c:func:`hotplug_slot_name`\  to get the slot's
unique name.  The driver no longer needs to handle a ->reset_slot callback
from this point on.

Returns 0 on success or a negative int on error.

.. This file was automatic generated / don't edit.

