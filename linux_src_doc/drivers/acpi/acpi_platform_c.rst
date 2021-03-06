.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/acpi_platform.c

.. _`acpi_create_platform_device`:

acpi_create_platform_device
===========================

.. c:function:: struct platform_device *acpi_create_platform_device(struct acpi_device *adev, struct property_entry *properties)

    Create platform device for ACPI device node

    :param adev:
        ACPI device node to create a platform device for.
    :type adev: struct acpi_device \*

    :param properties:
        Optional collection of build-in properties.
    :type properties: struct property_entry \*

.. _`acpi_create_platform_device.description`:

Description
-----------

Check if the given \ ``adev``\  can be represented as a platform device and, if
that's the case, create and register a platform device, populate its common
resources and returns a pointer to it.  Otherwise, return \ ``NULL``\ .

Name of the platform device will be the same as \ ``adev``\ 's.

.. This file was automatic generated / don't edit.

