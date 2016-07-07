.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/acpi_lpat.c

.. _`acpi_lpat_raw_to_temp`:

acpi_lpat_raw_to_temp
=====================

.. c:function:: int acpi_lpat_raw_to_temp(struct acpi_lpat_conversion_table *lpat_table, int raw)

    Return temperature from raw value through LPAT conversion table

    :param struct acpi_lpat_conversion_table \*lpat_table:
        the temperature_raw mapping table structure

    :param int raw:
        the raw value, used as a key to get the temerature from the
        above mapping table

.. _`acpi_lpat_raw_to_temp.description`:

Description
-----------

A positive converted temperarure value will be returned on success,
a negative errno will be returned in error cases.

.. _`acpi_lpat_temp_to_raw`:

acpi_lpat_temp_to_raw
=====================

.. c:function:: int acpi_lpat_temp_to_raw(struct acpi_lpat_conversion_table *lpat_table, int temp)

    Return raw value from temperature through LPAT conversion table

    :param struct acpi_lpat_conversion_table \*lpat_table:
        *undescribed*

    :param int temp:
        the temperature, used as a key to get the raw value from the
        above mapping table

.. _`acpi_lpat_temp_to_raw.description`:

Description
-----------

A positive converted temperature value will be returned on success,
a negative errno will be returned in error cases.

.. _`acpi_lpat_get_conversion_table`:

acpi_lpat_get_conversion_table
==============================

.. c:function:: struct acpi_lpat_conversion_table *acpi_lpat_get_conversion_table(acpi_handle handle)

    Parse ACPI LPAT table if present.

    :param acpi_handle handle:
        Handle to acpi device

.. _`acpi_lpat_get_conversion_table.description`:

Description
-----------

Parse LPAT table to a struct of type acpi_lpat_table. On success
it returns a pointer to newly allocated table. This table must
be freed by the caller when finished processing, using a call to
acpi_lpat_free_conversion_table.

.. _`acpi_lpat_free_conversion_table`:

acpi_lpat_free_conversion_table
===============================

.. c:function:: void acpi_lpat_free_conversion_table(struct acpi_lpat_conversion_table *lpat_table)

    Free LPAT table.

    :param struct acpi_lpat_conversion_table \*lpat_table:
        the temperature_raw mapping table structure

.. _`acpi_lpat_free_conversion_table.description`:

Description
-----------

Frees the LPAT table previously allocated by a call to
acpi_lpat_get_conversion_table.

.. This file was automatic generated / don't edit.

