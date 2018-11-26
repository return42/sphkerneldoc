.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/spcr.c

.. _`acpi_parse_spcr`:

acpi_parse_spcr
===============

.. c:function:: int acpi_parse_spcr(bool enable_earlycon, bool enable_console)

    parse ACPI SPCR table and add preferred console

    :param enable_earlycon:
        set up earlycon for the console specified by the table
    :type enable_earlycon: bool

    :param enable_console:
        setup the console specified by the table.
    :type enable_console: bool

.. _`acpi_parse_spcr.description`:

Description
-----------

For the architectures with support for ACPI, CONFIG_ACPI_SPCR_TABLE may be
defined to parse ACPI SPCR table.  As a result of the parsing preferred
console is registered and if \ ``enable_earlycon``\  is true, earlycon is set up.
If \ ``enable_console``\  is true the system console is also configured.

When CONFIG_ACPI_SPCR_TABLE is defined, this function should be called
from arch initialization code as soon as the DT/ACPI decision is made.

.. This file was automatic generated / don't edit.

