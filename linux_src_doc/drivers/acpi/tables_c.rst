.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/tables.c

.. _`acpi_parse_entries_array`:

acpi_parse_entries_array
========================

.. c:function:: int acpi_parse_entries_array(char *id, unsigned long table_size, struct acpi_table_header *table_header, struct acpi_subtable_proc *proc, int proc_num, unsigned int max_entries)

    for each proc_num find a suitable subtable

    :param id:
        table id (for debugging purposes)
    :type id: char \*

    :param table_size:
        size of the root table
    :type table_size: unsigned long

    :param table_header:
        where does the table start?
    :type table_header: struct acpi_table_header \*

    :param proc:
        array of acpi_subtable_proc struct containing entry id
        and associated handler with it
    :type proc: struct acpi_subtable_proc \*

    :param proc_num:
        how big proc is?
    :type proc_num: int

    :param max_entries:
        how many entries can we process?
    :type max_entries: unsigned int

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

    :param id:
        table id to find
    :type id: char \*

    :param handler:
        handler to run
    :type handler: acpi_tbl_table_handler

.. _`acpi_table_parse.description`:

Description
-----------

Scan the ACPI System Descriptor Table (STD) for a table matching \ ``id``\ ,
run \ ``handler``\  on it.

Return 0 if table found, -errno if not.

.. This file was automatic generated / don't edit.

