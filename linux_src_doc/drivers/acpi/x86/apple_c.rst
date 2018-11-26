.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/x86/apple.c

.. _`acpi_extract_apple_properties`:

acpi_extract_apple_properties
=============================

.. c:function:: void acpi_extract_apple_properties(struct acpi_device *adev)

    retrieve and convert Apple \_DSM properties

    :param adev:
        ACPI device for which to retrieve the properties
    :type adev: struct acpi_device \*

.. _`acpi_extract_apple_properties.description`:

Description
-----------

Invoke Apple's custom \_DSM once to check the protocol version and once more
to retrieve the properties.  They are marshalled up in a single package as
alternating key/value elements, unlike \_DSD which stores them as a package
of 2-element packages.  Convert to \_DSD format and make them available under
the primary fwnode.

.. This file was automatic generated / don't edit.

