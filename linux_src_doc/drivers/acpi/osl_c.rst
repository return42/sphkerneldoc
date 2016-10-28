.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/osl.c

.. _`acpi_os_unmap_iomem`:

acpi_os_unmap_iomem
===================

.. c:function:: void __ref acpi_os_unmap_iomem(void __iomem *virt, acpi_size size)

    Drop a memory mapping reference.

    :param void __iomem \*virt:
        Start of the address range to drop a reference to.

    :param acpi_size size:
        Size of the address range to drop a reference to.

.. _`acpi_os_unmap_iomem.description`:

Description
-----------

Look up the given virtual address range in the list of existing ACPI memory
mappings, drop a reference to it and unmap it if there are no more active
references to it.

During early init (when acpi_gbl_permanent_mmap has not been set yet) this
routine simply calls \\ :c:func:`__acpi_unmap_table`\  to get the job done.  Since
\\ :c:func:`__acpi_unmap_table`\  is an \__init function, the \__ref annotation is needed
here.

.. This file was automatic generated / don't edit.

