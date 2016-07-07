.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/hotplug/acpiphp_glue.c

.. _`acpiphp_init_context`:

acpiphp_init_context
====================

.. c:function:: struct acpiphp_context *acpiphp_init_context(struct acpi_device *adev)

    Create hotplug context and grab a reference to it.

    :param struct acpi_device \*adev:
        ACPI device object to create the context for.

.. _`acpiphp_init_context.description`:

Description
-----------

Call under acpi_hp_context_lock.

.. _`acpiphp_get_context`:

acpiphp_get_context
===================

.. c:function:: struct acpiphp_context *acpiphp_get_context(struct acpi_device *adev)

    Get hotplug context and grab a reference to it.

    :param struct acpi_device \*adev:
        ACPI device object to get the context for.

.. _`acpiphp_get_context.description`:

Description
-----------

Call under acpi_hp_context_lock.

.. _`acpiphp_put_context`:

acpiphp_put_context
===================

.. c:function:: void acpiphp_put_context(struct acpiphp_context *context)

    Drop a reference to ACPI hotplug context.

    :param struct acpiphp_context \*context:
        ACPI hotplug context to drop a reference to.

.. _`acpiphp_put_context.description`:

Description
-----------

The context object is removed if there are no more references to it.

Call under acpi_hp_context_lock.

.. _`acpiphp_post_dock_fixup`:

acpiphp_post_dock_fixup
=======================

.. c:function:: void acpiphp_post_dock_fixup(struct acpi_device *adev)

    Post-dock fixups for PCI devices.

    :param struct acpi_device \*adev:
        ACPI device object corresponding to a PCI device.

.. _`acpiphp_post_dock_fixup.description`:

Description
-----------

TBD - figure out a way to only call fixups for systems that require them.

.. _`acpiphp_add_context`:

acpiphp_add_context
===================

.. c:function:: acpi_status acpiphp_add_context(acpi_handle handle, u32 lvl, void *data, void **rv)

    Add ACPIPHP context to an ACPI device object.

    :param acpi_handle handle:
        ACPI handle of the object to add a context to.

    :param u32 lvl:
        Not used.

    :param void \*data:
        The object's parent ACPIPHP bridge.

    :param void \*\*rv:
        Not used.

.. _`acpiphp_max_busnr`:

acpiphp_max_busnr
=================

.. c:function:: unsigned char acpiphp_max_busnr(struct pci_bus *bus)

    return the highest reserved bus number under the given bus.

    :param struct pci_bus \*bus:
        bus to start search with

.. _`enable_slot`:

enable_slot
===========

.. c:function:: void enable_slot(struct acpiphp_slot *slot)

    enable, configure a slot

    :param struct acpiphp_slot \*slot:
        slot to be enabled

.. _`enable_slot.description`:

Description
-----------

This function should be called per \*physical slot\*,
not per each slot object in ACPI namespace.

.. _`disable_slot`:

disable_slot
============

.. c:function:: void disable_slot(struct acpiphp_slot *slot)

    disable a slot

    :param struct acpiphp_slot \*slot:
        ACPI PHP slot

.. _`get_slot_status`:

get_slot_status
===============

.. c:function:: unsigned int get_slot_status(struct acpiphp_slot *slot)

    get ACPI slot status

    :param struct acpiphp_slot \*slot:
        ACPI PHP slot

.. _`get_slot_status.description`:

Description
-----------

If a slot has \_STA for each function and if any one of them
returned non-zero status, return it.

If a slot doesn't have \_STA and if any one of its functions'
configuration space is configured, return 0x0f as a \_STA.

Otherwise return 0.

.. _`trim_stale_devices`:

trim_stale_devices
==================

.. c:function:: void trim_stale_devices(struct pci_dev *dev)

    remove PCI devices that are not responding.

    :param struct pci_dev \*dev:
        PCI device to start walking the hierarchy from.

.. _`acpiphp_check_bridge`:

acpiphp_check_bridge
====================

.. c:function:: void acpiphp_check_bridge(struct acpiphp_bridge *bridge)

    re-enumerate devices

    :param struct acpiphp_bridge \*bridge:
        where to begin re-enumeration

.. _`acpiphp_check_bridge.description`:

Description
-----------

Iterate over all slots under this bridge and make sure that if a
card is present they are enabled, and if not they are disabled.

.. _`acpiphp_enumerate_slots`:

acpiphp_enumerate_slots
=======================

.. c:function:: void acpiphp_enumerate_slots(struct pci_bus *bus)

    Enumerate PCI slots for a given bus.

    :param struct pci_bus \*bus:
        PCI bus to enumerate the slots for.

.. _`acpiphp_enumerate_slots.description`:

Description
-----------

A "slot" is an object associated with a PCI device number.  All functions
(PCI devices) with the same bus and device number belong to the same slot.

.. _`acpiphp_remove_slots`:

acpiphp_remove_slots
====================

.. c:function:: void acpiphp_remove_slots(struct pci_bus *bus)

    Remove slot objects associated with a given bus.

    :param struct pci_bus \*bus:
        PCI bus to remove the slot objects for.

.. _`acpiphp_enable_slot`:

acpiphp_enable_slot
===================

.. c:function:: int acpiphp_enable_slot(struct acpiphp_slot *slot)

    power on slot

    :param struct acpiphp_slot \*slot:
        ACPI PHP slot

.. _`acpiphp_disable_and_eject_slot`:

acpiphp_disable_and_eject_slot
==============================

.. c:function:: int acpiphp_disable_and_eject_slot(struct acpiphp_slot *slot)

    power off and eject slot

    :param struct acpiphp_slot \*slot:
        ACPI PHP slot

.. This file was automatic generated / don't edit.

