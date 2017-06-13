.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/spcr.c

.. _`parse_spcr`:

parse_spcr
==========

.. c:function:: int parse_spcr(bool earlycon)

    parse ACPI SPCR table and add preferred console

    :param bool earlycon:
        set up earlycon for the console specified by the table

.. _`parse_spcr.description`:

Description
-----------

For the architectures with support for ACPI, CONFIG_ACPI_SPCR_TABLE may be
defined to parse ACPI SPCR table.  As a result of the parsing preferred
console is registered and if \ ``earlycon``\  is true, earlycon is set up.

When CONFIG_ACPI_SPCR_TABLE is defined, this function should be called
from arch initialization code as soon as the DT/ACPI decision is made.

.. This file was automatic generated / don't edit.

