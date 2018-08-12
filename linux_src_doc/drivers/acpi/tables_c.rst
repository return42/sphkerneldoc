.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/tables.c

.. _`acpi_parse_entries_array`:

acpi_parse_entries_array
========================

.. c:function:: int acpi_parse_entries_array(char *id, unsigned long table_size, struct acpi_table_header *table_header, struct acpi_subtable_proc *proc, int proc_num, unsigned int max_entries)

    for each proc_num find a suitable subtable

    :param char \*id:
        table id (for debugging purposes)

    :param unsigned long table_size:
        size of the root table

    :param struct acpi_table_header \*table_header:
        where does the table start?

    :param struct acpi_subtable_proc \*proc:
        array of acpi_subtable_proc struct containing entry id
        and associated handler with it

    :param int proc_num:
        how big proc is?

    :param unsigned int max_entries:
        how many entries can we process?

.. _`acpi_parse_entries_array.description`:

Description
-----------

For each proc_num find a subtable with proc->id and run proc->handler
on it. Assumption is that there's only single handler for particular
entry id.

The table_size is not the size of the complete ACPI table (the length
field in the header struct), but only the size of the root table; i.e.,
the offset from the very first byte of the complete ACPI table, to the
first byte of the very first subtable.

On success returns sum of all matching entries for all proc handlers.
Otherwise, -ENODEV or -EINVAL is returned.

.. _`acpi_table_parse`:

acpi_table_parse
================

.. c:function:: int acpi_table_parse(char *id, acpi_tbl_table_handler handler)

    find table with \ ``id``\ , run \ ``handler``\  on it

    :param char \*id:
        table id to find

    :param acpi_tbl_table_handler handler:
        handler to run

.. _`acpi_table_parse.description`:

Description
-----------

Scan the ACPI System Descriptor Table (STD) for a table matching \ ``id``\ ,
run \ ``handler``\  on it.

Return 0 if table found, -errno if not.

.. This file was automatic generated / don't edit.

