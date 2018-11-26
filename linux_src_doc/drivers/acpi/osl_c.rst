.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/osl.c

.. _`acpi_os_unmap_iomem`:

acpi_os_unmap_iomem
===================

.. c:function:: void __ref acpi_os_unmap_iomem(void __iomem *virt, acpi_size size)

    Drop a memory mapping reference.

    :param virt:
        Start of the address range to drop a reference to.
    :type virt: void __iomem \*

    :param size:
        Size of the address range to drop a reference to.
    :type size: acpi_size

.. _`acpi_os_unmap_iomem.description`:

Description
-----------

Look up the given virtual address range in the list of existing ACPI memory
mappings, drop a reference to it and unmap it if there are no more active
references to it.

During early init (when acpi_permanent_mmap has not been set yet) this
routine simply calls \__acpi_unmap_table() to get the job done.  Since
\__acpi_unmap_table() is an \__init function, the \__ref annotation is needed
here.

.. _`acpi_release_memory`:

acpi_release_memory
===================

.. c:function:: acpi_status acpi_release_memory(acpi_handle handle, struct resource *res, u32 level)

    Release any mappings done to a memory region

    :param handle:
        Handle to namespace node
    :type handle: acpi_handle

    :param res:
        Memory resource
    :type res: struct resource \*

    :param level:
        A level that terminates the search
    :type level: u32

.. _`acpi_release_memory.description`:

Description
-----------

Walks through \ ``handle``\  and unmaps all SystemMemory Operation Regions that
overlap with \ ``res``\  and that have already been activated (mapped).

This is a helper that allows drivers to place special requirements on memory
region that may overlap with operation regions, primarily allowing them to
safely map the region as non-cached memory.

The unmapped Operation Regions will be automatically remapped next time they
are called, so the drivers do not need to do anything else.

.. This file was automatic generated / don't edit.

