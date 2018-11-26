.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/pci_root.c

.. _`acpi_is_root_bridge`:

acpi_is_root_bridge
===================

.. c:function:: int acpi_is_root_bridge(acpi_handle handle)

    determine whether an ACPI CA node is a PCI root bridge \ ``handle``\  - the ACPI CA node in question.

    :param handle:
        *undescribed*
    :type handle: acpi_handle

.. _`acpi_is_root_bridge.note`:

Note
----

we could make this API take a struct acpi_device \* instead, but
for now, it's more convenient to operate on an acpi_handle.

.. _`acpi_get_pci_dev`:

acpi_get_pci_dev
================

.. c:function:: struct pci_dev *acpi_get_pci_dev(acpi_handle handle)

    convert ACPI CA handle to struct pci_dev

    :param handle:
        the handle in question
    :type handle: acpi_handle

.. _`acpi_get_pci_dev.description`:

Description
-----------

Given an ACPI CA handle, the desired PCI device is located in the
list of PCI devices.

If the device is found, its reference count is increased and this
function returns a pointer to its data structure.  The caller must
decrement the reference count by calling \ :c:func:`pci_dev_put`\ .
If no device is found, \ ``NULL``\  is returned.

.. _`acpi_pci_osc_control_set`:

acpi_pci_osc_control_set
========================

.. c:function:: acpi_status acpi_pci_osc_control_set(acpi_handle handle, u32 *mask, u32 req)

    Request control of PCI root \_OSC features.

    :param handle:
        ACPI handle of a PCI root bridge (or PCIe Root Complex).
    :type handle: acpi_handle

    :param mask:
        Mask of \_OSC bits to request control of, place to store control mask.
    :type mask: u32 \*

    :param req:
        Mask of \_OSC bits the control of is essential to the caller.
    :type req: u32

.. _`acpi_pci_osc_control_set.description`:

Description
-----------

Run \_OSC query for \ ``mask``\  and if that is successful, compare the returned
mask of control bits with \ ``req``\ .  If all of the \ ``req``\  bits are set in the
returned mask, run \_OSC request for it.

The variable at the \ ``mask``\  address may be modified regardless of whether or
not the function returns success.  On success it will contain the mask of
\_OSC bits the BIOS has granted control of, but its contents are meaningless
on failure.

.. This file was automatic generated / don't edit.

