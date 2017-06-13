.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/acpi.h

.. _`acpi_device_class`:

ACPI_DEVICE_CLASS
=================

.. c:function::  ACPI_DEVICE_CLASS( _cls,  _msk)

    macro used to describe an ACPI device with the PCI-defined class-code information

    :param  _cls:
        the class, subclass, prog-if triple for this device

    :param  _msk:
        the class mask for this device

.. _`acpi_device_class.description`:

Description
-----------

This macro is used to create a struct acpi_device_id that matches a
specific PCI class. The .id and .driver_data fields will be left
initialized with the default value.

.. _`acpi_probe_entry`:

struct acpi_probe_entry
=======================

.. c:type:: struct acpi_probe_entry

    boot-time probing entry

.. _`acpi_probe_entry.definition`:

Definition
----------

.. code-block:: c

    struct acpi_probe_entry {
        __u8 id;
        __u8 type;
        acpi_probe_entry_validate_subtbl subtable_valid;
        union {unnamed_union};
        kernel_ulong_t driver_data;
    }

.. _`acpi_probe_entry.members`:

Members
-------

id
    ACPI table name

type
    Optional subtable type to match
    (if \ ``id``\  contains subtables)

subtable_valid
    Optional callback to check the validity of
    the subtable

{unnamed_union}
    anonymous


driver_data
    Sideband data provided back to the driver

.. This file was automatic generated / don't edit.

