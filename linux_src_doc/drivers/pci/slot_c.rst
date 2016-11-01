.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/slot.c

.. _`pci_create_slot`:

pci_create_slot
===============

.. c:function:: struct pci_slot *pci_create_slot(struct pci_bus *parent, int slot_nr, const char *name, struct hotplug_slot *hotplug)

    create or increment refcount for physical PCI slot

    :param struct pci_bus \*parent:
        struct pci_bus of parent bridge

    :param int slot_nr:
        PCI_SLOT(pci_dev->devfn) or -1 for placeholder

    :param const char \*name:
        user visible string presented in /sys/bus/pci/slots/<name>

    :param struct hotplug_slot \*hotplug:
        set if caller is hotplug driver, NULL otherwise

.. _`pci_create_slot.description`:

Description
-----------

PCI slots have first class attributes such as address, speed, width,
and a \ :c:type:`struct pci_slot <pci_slot>`\  is used to manage them. This interface will
either return a new \ :c:type:`struct pci_slot <pci_slot>`\  to the caller, or if the pci_slot
already exists, its refcount will be incremented.

Slots are uniquely identified by a \ ``pci_bus``\ , \ ``slot_nr``\  tuple.

There are known platforms with broken firmware that assign the same
name to multiple slots. Workaround these broken platforms by renaming
the slots on behalf of the caller. If firmware assigns name N to

.. _`pci_create_slot.multiple-slots`:

multiple slots
--------------


The first slot is assigned N
The second slot is assigned N-1
The third slot is assigned N-2
etc.

.. _`pci_create_slot.placeholder-slots`:

Placeholder slots
-----------------

In most cases, \ ``pci_bus``\ , \ ``slot_nr``\  will be sufficient to uniquely identify
a slot. There is one notable exception - pSeries (rpaphp), where the
\ ``slot_nr``\  cannot be determined until a device is actually inserted into
the slot. In this scenario, the caller may pass -1 for \ ``slot_nr``\ .

The following semantics are imposed when the caller passes \ ``slot_nr``\  ==
-1. First, we no longer check for an existing \ ``struct``\  pci_slot, as there
may be many slots with \ ``slot_nr``\  of -1.  The other change in semantics is
user-visible, which is the 'address' parameter presented in sysfs will
consist solely of a dddd:bb tuple, where dddd is the PCI domain of the
\ ``struct``\  pci_bus and bb is the bus number. In other words, the devfn of
the 'placeholder' slot will not be displayed.

.. _`pci_destroy_slot`:

pci_destroy_slot
================

.. c:function:: void pci_destroy_slot(struct pci_slot *slot)

    decrement refcount for physical PCI slot

    :param struct pci_slot \*slot:
        struct pci_slot to decrement

.. _`pci_destroy_slot.description`:

Description
-----------

%struct pci_slot is refcounted, so destroying them is really easy; we
just call kobject_put on its kobj and let our release methods do the
rest.

.. _`pci_hp_create_module_link`:

pci_hp_create_module_link
=========================

.. c:function:: void pci_hp_create_module_link(struct pci_slot *pci_slot)

    create symbolic link to the hotplug driver module.

    :param struct pci_slot \*pci_slot:
        struct pci_slot

.. _`pci_hp_create_module_link.description`:

Description
-----------

Helper function for pci_hotplug_core.c to create symbolic link to
the hotplug driver module.

.. _`pci_hp_remove_module_link`:

pci_hp_remove_module_link
=========================

.. c:function:: void pci_hp_remove_module_link(struct pci_slot *pci_slot)

    remove symbolic link to the hotplug driver module.

    :param struct pci_slot \*pci_slot:
        struct pci_slot

.. _`pci_hp_remove_module_link.description`:

Description
-----------

Helper function for pci_hotplug_core.c to remove symbolic link to
the hotplug driver module.

.. This file was automatic generated / don't edit.

