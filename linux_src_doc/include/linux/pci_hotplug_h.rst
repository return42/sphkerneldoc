.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/pci_hotplug.h

.. _`hotplug_slot_ops`:

struct hotplug_slot_ops
=======================

.. c:type:: struct hotplug_slot_ops

    the callbacks that the hotplug pci core can use

.. _`hotplug_slot_ops.definition`:

Definition
----------

.. code-block:: c

    struct hotplug_slot_ops {
        int (*enable_slot) (struct hotplug_slot *slot);
        int (*disable_slot) (struct hotplug_slot *slot);
        int (*set_attention_status) (struct hotplug_slot *slot, u8 value);
        int (*hardware_test) (struct hotplug_slot *slot, u32 value);
        int (*get_power_status) (struct hotplug_slot *slot, u8 *value);
        int (*get_attention_status) (struct hotplug_slot *slot, u8 *value);
        int (*get_latch_status) (struct hotplug_slot *slot, u8 *value);
        int (*get_adapter_status) (struct hotplug_slot *slot, u8 *value);
        int (*reset_slot) (struct hotplug_slot *slot, int probe);
    }

.. _`hotplug_slot_ops.members`:

Members
-------

enable_slot
    Called when the user wants to enable a specific pci slot

disable_slot
    Called when the user wants to disable a specific pci slot

set_attention_status
    Called to set the specific slot's attention LED to
    the specified value

hardware_test
    Called to run a specified hardware test on the specified
    slot.

get_power_status
    Called to get the current power status of a slot.

get_attention_status
    Called to get the current attention status of a slot.

get_latch_status
    Called to get the current latch status of a slot.

get_adapter_status
    Called to get see if an adapter is present in the slot or not.

reset_slot
    Optional interface to allow override of a bus reset for the
    slot for cases where a secondary bus reset can result in spurious
    hotplug events or where a slot can be reset independent of the bus.

.. _`hotplug_slot_ops.description`:

Description
-----------

The table of function pointers that is passed to the hotplug pci core by a
hotplug pci driver.  These functions are called by the hotplug pci core when
the user wants to do something to a specific slot (query it for information,
set an LED, enable / disable power, etc.)

.. _`hotplug_slot`:

struct hotplug_slot
===================

.. c:type:: struct hotplug_slot

    used to register a physical slot with the hotplug pci core

.. _`hotplug_slot.definition`:

Definition
----------

.. code-block:: c

    struct hotplug_slot {
        const struct hotplug_slot_ops *ops;
        struct list_head slot_list;
        struct pci_slot *pci_slot;
        struct module *owner;
        const char *mod_name;
    }

.. _`hotplug_slot.members`:

Members
-------

ops
    pointer to the \ :c:type:`struct hotplug_slot_ops <hotplug_slot_ops>`\  to be used for this slot

slot_list
    *undescribed*

pci_slot
    *undescribed*

owner
    The module owner of this structure

mod_name
    The module name (KBUILD_MODNAME) of this structure

.. This file was automatic generated / don't edit.

