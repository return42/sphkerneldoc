.. -*- coding: utf-8; mode: rst -*-

==================
acpi_thermal_rel.c
==================


.. _`acpi_parse_trt`:

acpi_parse_trt
==============

.. c:function:: int acpi_parse_trt (acpi_handle handle, int *trt_count, struct trt **trtp, bool create_dev)

    Thermal Relationship Table _TRT for passive cooling

    :param acpi_handle handle:
        ACPI handle of the device contains _TRT

    :param int \*trt_count:

        *undescribed*

    :param struct trt \*\*trtp:

        *undescribed*

    :param bool create_dev:
        whether to create platform devices for target and source



.. _`acpi_parse_art`:

acpi_parse_art
==============

.. c:function:: int acpi_parse_art (acpi_handle handle, int *art_count, struct art **artp, bool create_dev)

    Parse Active Relationship Table _ART

    :param acpi_handle handle:
        ACPI handle of the device contains _ART

    :param int \*art_count:
        the number of valid entries resulted from parsing _ART

    :param struct art \*\*artp:
        pointer to pointer of array of art entries in parsing result

    :param bool create_dev:
        whether to create platform devices for target and source

