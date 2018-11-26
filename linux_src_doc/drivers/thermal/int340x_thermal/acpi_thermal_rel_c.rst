.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/int340x_thermal/acpi_thermal_rel.c

.. _`acpi_parse_trt`:

acpi_parse_trt
==============

.. c:function:: int acpi_parse_trt(acpi_handle handle, int *trt_count, struct trt **trtp, bool create_dev)

    Thermal Relationship Table \_TRT for passive cooling

    :param handle:
        ACPI handle of the device contains \_TRT
    :type handle: acpi_handle

    :param trt_count:
        the number of valid entries resulted from parsing \_TRT
    :type trt_count: int \*

    :param trtp:
        pointer to pointer of array of \_TRT entries in parsing result
    :type trtp: struct trt \*\*

    :param create_dev:
        whether to create platform devices for target and source
    :type create_dev: bool

.. _`acpi_parse_art`:

acpi_parse_art
==============

.. c:function:: int acpi_parse_art(acpi_handle handle, int *art_count, struct art **artp, bool create_dev)

    Parse Active Relationship Table \_ART

    :param handle:
        ACPI handle of the device contains \_ART
    :type handle: acpi_handle

    :param art_count:
        the number of valid entries resulted from parsing \_ART
    :type art_count: int \*

    :param artp:
        pointer to pointer of array of art entries in parsing result
    :type artp: struct art \*\*

    :param create_dev:
        whether to create platform devices for target and source
    :type create_dev: bool

.. This file was automatic generated / don't edit.

