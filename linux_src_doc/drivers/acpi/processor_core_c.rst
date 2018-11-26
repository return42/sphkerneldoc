.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/processor_core.c

.. _`acpi_get_ioapic_id`:

acpi_get_ioapic_id
==================

.. c:function:: int acpi_get_ioapic_id(acpi_handle handle, u32 gsi_base, u64 *phys_addr)

    Get IOAPIC ID and physical address matching \ ``gsi_base``\ 

    :param handle:
        ACPI object for IOAPIC device
    :type handle: acpi_handle

    :param gsi_base:
        GSI base to match with
    :type gsi_base: u32

    :param phys_addr:
        Pointer to store physical address of matching IOAPIC record
    :type phys_addr: u64 \*

.. _`acpi_get_ioapic_id.description`:

Description
-----------

Walk resources returned by ACPI_MAT method, then ACPI MADT table, to search
for an ACPI IOAPIC record matching \ ``gsi_base``\ .
Return IOAPIC id and store physical address in \ ``phys_addr``\  if found a match,
otherwise return <0.

.. This file was automatic generated / don't edit.

