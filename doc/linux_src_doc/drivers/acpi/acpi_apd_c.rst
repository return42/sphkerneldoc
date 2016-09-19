.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/acpi_apd.c

.. _`acpi_apd_sysfs`:

ACPI_APD_SYSFS
==============

.. c:function::  ACPI_APD_SYSFS()

    add device attributes in sysfs ACPI_APD_PM : attach power domain to device

.. _`apd_device_desc`:

struct apd_device_desc
======================

.. c:type:: struct apd_device_desc

    a descriptor for apd device

.. _`apd_device_desc.definition`:

Definition
----------

.. code-block:: c

    struct apd_device_desc {
        unsigned int flags;
        unsigned int fixed_clk_rate;
        int (*setup)(struct apd_private_data *pdata);
    }

.. _`apd_device_desc.members`:

Members
-------

flags
    device flags like \ ``ACPI_APD_SYSFS``\ , \ ``ACPI_APD_PM``\ 

fixed_clk_rate
    fixed rate input clock source for acpi device;
    0 means no fixed rate input clock source

setup
    a hook routine to set device resource during create platform device

.. _`apd_device_desc.description`:

Description
-----------

Device description defined as acpi_device_id.driver_data

.. _`acpi_apd_create_device`:

acpi_apd_create_device
======================

.. c:function:: int acpi_apd_create_device(struct acpi_device *adev, const struct acpi_device_id *id)

    Return value > 0 on success of creating device.

    :param struct acpi_device \*adev:
        *undescribed*

    :param const struct acpi_device_id \*id:
        *undescribed*

.. This file was automatic generated / don't edit.

