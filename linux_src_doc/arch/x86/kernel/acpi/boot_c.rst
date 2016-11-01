.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/acpi/boot.c

.. _`acpi_register_lapic`:

acpi_register_lapic
===================

.. c:function:: int acpi_register_lapic(int id, u32 acpiid, u8 enabled)

    register a local apic and generates a logic cpu number

    :param int id:
        local apic id to register

    :param u32 acpiid:
        ACPI id to register

    :param u8 enabled:
        this cpu is enabled or not

.. _`acpi_register_lapic.description`:

Description
-----------

Returns the logic cpu number which maps to the local apic

.. _`acpi_ioapic_registered`:

acpi_ioapic_registered
======================

.. c:function:: int acpi_ioapic_registered(acpi_handle handle, u32 gsi_base)

    Check whether IOAPIC assoicatied with \ ``gsi_base``\  has been registered

    :param acpi_handle handle:
        ACPI handle of the IOAPIC deivce

    :param u32 gsi_base:
        GSI base associated with the IOAPIC

.. _`acpi_ioapic_registered.description`:

Description
-----------

Assume caller holds some type of lock to serialize \ :c:func:`acpi_ioapic_registered`\ 
with \ :c:func:`acpi_register_ioapic`\ /acpi_unregister_ioapic().

.. This file was automatic generated / don't edit.

