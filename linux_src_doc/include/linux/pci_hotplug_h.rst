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
        struct module *owner;
        const char *mod_name;
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

owner
    The module owner of this structure

mod_name
    The module name (KBUILD_MODNAME) of this structure

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
    If this field is NULL, the value passed in the struct hotplug_slot_info
    will be used when this value is requested by a user.

get_attention_status
    Called to get the current attention status of a slot.
    If this field is NULL, the value passed in the struct hotplug_slot_info
    will be used when this value is requested by a user.

get_latch_status
    Called to get the current latch status of a slot.
    If this field is NULL, the value passed in the struct hotplug_slot_info
    will be used when this value is requested by a user.

get_adapter_status
    Called to get see if an adapter is present in the slot or not.
    If this field is NULL, the value passed in the struct hotplug_slot_info
    will be used when this value is requested by a user.

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

.. _`hotplug_slot_info`:

struct hotplug_slot_info
========================

.. c:type:: struct hotplug_slot_info

    used to notify the hotplug pci core of the state of the slot

.. _`hotplug_slot_info.definition`:

Definition
----------

.. code-block:: c

    struct hotplug_slot_info {
        u8 power_status;
        u8 attention_status;
        u8 latch_status;
        u8 adapter_status;
    }

.. _`hotplug_slot_info.members`:

Members
-------

power_status
    if power is enabled or not (1/0)

attention_status
    if the attention light is enabled or not (1/0)

latch_status
    if the latch (if any) is open or closed (1/0)

adapter_status
    if there is a pci board present in the slot or not (1/0)

.. _`hotplug_slot_info.description`:

Description
-----------

Used to notify the hotplug pci core of the status of a specific slot.

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
        struct hotplug_slot_ops *ops;
        struct hotplug_slot_info *info;
        void (*release) (struct hotplug_slot *slot);
        void *private;
        struct list_head slot_list;
        struct pci_slot *pci_slot;
    }

.. _`hotplug_slot.members`:

Members
-------

ops
    pointer to the \ :c:type:`struct hotplug_slot_ops <hotplug_slot_ops>`\  to be used for this slot

info
    pointer to the \ :c:type:`struct hotplug_slot_info <hotplug_slot_info>`\  for the initial values for
    this slot.

release
    called during pci_hp_deregister to free memory allocated in a
    hotplug_slot structure.

private
    used by the hotplug pci controller driver to store whatever it
    needs.

slot_list
    *undescribed*

pci_slot
    *undescribed*

.. This file was automatic generated / don't edit.

