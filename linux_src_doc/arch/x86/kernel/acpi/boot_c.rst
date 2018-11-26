.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/acpi/boot.c

.. _`acpi_register_lapic`:

acpi_register_lapic
===================

.. c:function:: int acpi_register_lapic(int id, u32 acpiid, u8 enabled)

    register a local apic and generates a logic cpu number

    :param id:
        local apic id to register
    :type id: int

    :param acpiid:
        ACPI id to register
    :type acpiid: u32

    :param enabled:
        this cpu is enabled or not
    :type enabled: u8

.. _`acpi_register_lapic.description`:

Description
-----------

Returns the logic cpu number which maps to the local apic

.. _`acpi_ioapic_registered`:

acpi_ioapic_registered
======================

.. c:function:: int acpi_ioapic_registered(acpi_handle handle, u32 gsi_base)

    Check whether IOAPIC assoicatied with \ ``gsi_base``\  has been registered

    :param handle:
        ACPI handle of the IOAPIC deivce
    :type handle: acpi_handle

    :param gsi_base:
        GSI base associated with the IOAPIC
    :type gsi_base: u32

.. _`acpi_ioapic_registered.description`:

Description
-----------

Assume caller holds some type of lock to serialize \ :c:func:`acpi_ioapic_registered`\ 
with \ :c:func:`acpi_register_ioapic`\ /acpi_unregister_ioapic().

.. This file was automatic generated / don't edit.

