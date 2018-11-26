.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/hotplug/rpaphp_core.c

.. _`set_attention_status`:

set_attention_status
====================

.. c:function:: int set_attention_status(struct hotplug_slot *hotplug_slot, u8 value)

    set attention LED

    :param hotplug_slot:
        target \ :c:type:`struct hotplug_slot <hotplug_slot>`\ 
    :type hotplug_slot: struct hotplug_slot \*

    :param value:
        LED control value
    :type value: u8

.. _`set_attention_status.description`:

Description
-----------

echo 0 > attention -- set LED OFF
echo 1 > attention -- set LED ON
echo 2 > attention -- set LED ID(identify, light is blinking)

.. _`get_power_status`:

get_power_status
================

.. c:function:: int get_power_status(struct hotplug_slot *hotplug_slot, u8 *value)

    get power status of a slot

    :param hotplug_slot:
        slot to get status
    :type hotplug_slot: struct hotplug_slot \*

    :param value:
        pointer to store status
    :type value: u8 \*

.. _`get_attention_status`:

get_attention_status
====================

.. c:function:: int get_attention_status(struct hotplug_slot *hotplug_slot, u8 *value)

    get attention LED status

    :param hotplug_slot:
        slot to get status
    :type hotplug_slot: struct hotplug_slot \*

    :param value:
        pointer to store status
    :type value: u8 \*

.. _`is_php_dn`:

is_php_dn
=========

.. c:function:: int is_php_dn(struct device_node *dn, const int **indexes, const int **names, const int **types, const int **power_domains)

    return 1 if this is a hotpluggable pci slot, else 0

    :param dn:
        target \ :c:type:`struct device_node <device_node>`\ 
    :type dn: struct device_node \*

    :param indexes:
        passed to \ :c:func:`get_children_props`\ 
    :type indexes: const int \*\*

    :param names:
        passed to \ :c:func:`get_children_props`\ 
    :type names: const int \*\*

    :param types:
        returned from \ :c:func:`get_children_props`\ 
    :type types: const int \*\*

    :param power_domains:
        *undescribed*
    :type power_domains: const int \*\*

.. _`is_php_dn.description`:

Description
-----------

This routine will return true only if the device node is
a hotpluggable slot. This routine will return false
for built-in pci slots (even when the built-in slots are
dlparable.)

.. _`rpaphp_add_slot`:

rpaphp_add_slot
===============

.. c:function:: int rpaphp_add_slot(struct device_node *dn)

    - declare a hotplug slot to the hotplug subsystem.

    :param dn:
        device node of slot
    :type dn: struct device_node \*

.. _`rpaphp_add_slot.description`:

Description
-----------

This subroutine will register a hotpluggable slot with the
PCI hotplug infrastructure. This routine is typically called
during boot time, if the hotplug slots are present at boot time,
or is called later, by the dlpar add code, if the slot is
being dynamically added during runtime.

If the device node points at an embedded (built-in) slot, this
routine will just return without doing anything, since embedded
slots cannot be hotplugged.

To remove a slot, it suffices to call \ :c:func:`rpaphp_deregister_slot`\ .

.. This file was automatic generated / don't edit.

