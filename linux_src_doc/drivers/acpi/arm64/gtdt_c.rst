.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/arm64/gtdt.c

.. _`acpi_gtdt_descriptor`:

struct acpi_gtdt_descriptor
===========================

.. c:type:: struct acpi_gtdt_descriptor

    Store the key info of GTDT for all functions

.. _`acpi_gtdt_descriptor.definition`:

Definition
----------

.. code-block:: c

    struct acpi_gtdt_descriptor {
        struct acpi_table_gtdt *gtdt;
        void *gtdt_end;
        void *platform_timer;
    }

.. _`acpi_gtdt_descriptor.members`:

Members
-------

gtdt
    The pointer to the struct acpi_table_gtdt of GTDT table.

gtdt_end
    The pointer to the end of GTDT table.

platform_timer
    The pointer to the start of Platform Timer Structure

.. _`acpi_gtdt_descriptor.description`:

Description
-----------

The struct store the key info of GTDT table, it should be initialized by
acpi_gtdt_init.

.. _`acpi_gtdt_map_ppi`:

acpi_gtdt_map_ppi
=================

.. c:function:: int acpi_gtdt_map_ppi(int type)

    Map the PPIs of per-cpu arch_timer.

    :param int type:
        the type of PPI.

.. _`acpi_gtdt_map_ppi.note`:

Note
----

Secure state is not managed by the kernel on ARM64 systems.
So we only handle the non-secure timer PPIs,
ARCH_TIMER_PHYS_SECURE_PPI is treated as invalid type.

.. _`acpi_gtdt_map_ppi.return`:

Return
------

the mapped PPI value, 0 if error.

.. _`acpi_gtdt_c3stop`:

acpi_gtdt_c3stop
================

.. c:function:: bool acpi_gtdt_c3stop(int type)

    Got c3stop info from GTDT according to the type of PPI.

    :param int type:
        the type of PPI.

.. _`acpi_gtdt_c3stop.return`:

Return
------

true if the timer HW state is lost when a CPU enters an idle state,
false otherwise

.. _`acpi_gtdt_init`:

acpi_gtdt_init
==============

.. c:function:: int acpi_gtdt_init(struct acpi_table_header *table, int *platform_timer_count)

    Get the info of GTDT table to prepare for further init.

    :param struct acpi_table_header \*table:
        The pointer to GTDT table.

    :param int \*platform_timer_count:
        It points to a integer variable which is used
        for storing the number of platform timers.
        This pointer could be NULL, if the caller
        doesn't need this info.

.. _`acpi_gtdt_init.return`:

Return
------

0 if success, -EINVAL if error.

.. _`acpi_arch_timer_mem_init`:

acpi_arch_timer_mem_init
========================

.. c:function:: int acpi_arch_timer_mem_init(struct arch_timer_mem *timer_mem, int *timer_count)

    Get the info of all GT blocks in GTDT table.

    :param struct arch_timer_mem \*timer_mem:
        The pointer to the array of struct arch_timer_mem for returning
        the result of parsing. The element number of this array should
        be platform_timer_count(the total number of platform timers).

    :param int \*timer_count:
        It points to a integer variable which is used for storing the
        number of GT blocks we have parsed.

.. _`acpi_arch_timer_mem_init.return`:

Return
------

0 if success, -EINVAL/-ENODEV if error.

.. This file was automatic generated / don't edit.

