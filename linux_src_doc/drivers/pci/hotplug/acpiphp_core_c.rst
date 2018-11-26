.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/hotplug/acpiphp_core.c

.. _`acpiphp_register_attention`:

acpiphp_register_attention
==========================

.. c:function:: int acpiphp_register_attention(struct acpiphp_attention_info *info)

    set attention LED callback

    :param info:
        must be completely filled with LED callbacks
    :type info: struct acpiphp_attention_info \*

.. _`acpiphp_register_attention.description`:

Description
-----------

This is used to register a hardware specific ACPI
driver that manipulates the attention LED.  All the fields in
info must be set.

.. _`acpiphp_unregister_attention`:

acpiphp_unregister_attention
============================

.. c:function:: int acpiphp_unregister_attention(struct acpiphp_attention_info *info)

    unset attention LED callback

    :param info:
        must match the pointer used to register
    :type info: struct acpiphp_attention_info \*

.. _`acpiphp_unregister_attention.description`:

Description
-----------

This is used to un-register a hardware specific acpi
driver that manipulates the attention LED.  The pointer to the
info struct must be the same as the one used to set it.

.. _`enable_slot`:

enable_slot
===========

.. c:function:: int enable_slot(struct hotplug_slot *hotplug_slot)

    power on and enable a slot

    :param hotplug_slot:
        slot to enable
    :type hotplug_slot: struct hotplug_slot \*

.. _`enable_slot.description`:

Description
-----------

Actual tasks are done in \ :c:func:`acpiphp_enable_slot`\ 

.. _`disable_slot`:

disable_slot
============

.. c:function:: int disable_slot(struct hotplug_slot *hotplug_slot)

    disable and power off a slot

    :param hotplug_slot:
        slot to disable
    :type hotplug_slot: struct hotplug_slot \*

.. _`disable_slot.description`:

Description
-----------

Actual tasks are done in \ :c:func:`acpiphp_disable_slot`\ 

.. _`set_attention_status`:

set_attention_status
====================

.. c:function:: int set_attention_status(struct hotplug_slot *hotplug_slot, u8 status)

    set attention LED

    :param hotplug_slot:
        slot to set attention LED on
    :type hotplug_slot: struct hotplug_slot \*

    :param status:
        value to set attention LED to (0 or 1)
    :type status: u8

.. _`set_attention_status.description`:

Description
-----------

attention status LED, so we use a callback that
was registered with us.  This allows hardware specific
ACPI implementations to blink the light for us.

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

.. _`get_power_status.description`:

Description
-----------

Some platforms may not implement \_STA method properly.
In that case, the value returned may not be reliable.

.. _`get_attention_status`:

get_attention_status
====================

.. c:function:: int get_attention_status(struct hotplug_slot *hotplug_slot, u8 *value)

    get attention LED status

    :param hotplug_slot:
        slot to get status from
    :type hotplug_slot: struct hotplug_slot \*

    :param value:
        returns with value of attention LED
    :type value: u8 \*

.. _`get_attention_status.description`:

Description
-----------

ACPI doesn't have known method to determine the state
of the attention status LED, so we use a callback that
was registered with us.  This allows hardware specific
ACPI implementations to determine its state.

.. _`get_latch_status`:

get_latch_status
================

.. c:function:: int get_latch_status(struct hotplug_slot *hotplug_slot, u8 *value)

    get latch status of a slot

    :param hotplug_slot:
        slot to get status
    :type hotplug_slot: struct hotplug_slot \*

    :param value:
        pointer to store status
    :type value: u8 \*

.. _`get_latch_status.description`:

Description
-----------

ACPI doesn't provide any formal means to access latch status.
Instead, we fake latch status from \_STA.

.. _`get_adapter_status`:

get_adapter_status
==================

.. c:function:: int get_adapter_status(struct hotplug_slot *hotplug_slot, u8 *value)

    get adapter status of a slot

    :param hotplug_slot:
        slot to get status
    :type hotplug_slot: struct hotplug_slot \*

    :param value:
        pointer to store status
    :type value: u8 \*

.. _`get_adapter_status.description`:

Description
-----------

ACPI doesn't provide any formal means to access adapter status.
Instead, we fake adapter status from \_STA.

.. This file was automatic generated / don't edit.

