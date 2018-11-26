.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/resource.c

.. _`acpi_dev_resource_memory`:

acpi_dev_resource_memory
========================

.. c:function:: bool acpi_dev_resource_memory(struct acpi_resource *ares, struct resource *res)

    Extract ACPI memory resource information.

    :param ares:
        Input ACPI resource object.
    :type ares: struct acpi_resource \*

    :param res:
        Output generic resource object.
    :type res: struct resource \*

.. _`acpi_dev_resource_memory.description`:

Description
-----------

Check if the given ACPI resource object represents a memory resource and
if that's the case, use the information in it to populate the generic
resource object pointed to by \ ``res``\ .

.. _`acpi_dev_resource_memory.return`:

Return
------

1) false with res->flags setting to zero: not the expected resource type
2) false with IORESOURCE_DISABLED in res->flags: valid unassigned resource
3) true: valid assigned resource

.. _`acpi_dev_resource_io`:

acpi_dev_resource_io
====================

.. c:function:: bool acpi_dev_resource_io(struct acpi_resource *ares, struct resource *res)

    Extract ACPI I/O resource information.

    :param ares:
        Input ACPI resource object.
    :type ares: struct acpi_resource \*

    :param res:
        Output generic resource object.
    :type res: struct resource \*

.. _`acpi_dev_resource_io.description`:

Description
-----------

Check if the given ACPI resource object represents an I/O resource and
if that's the case, use the information in it to populate the generic
resource object pointed to by \ ``res``\ .

.. _`acpi_dev_resource_io.return`:

Return
------

1) false with res->flags setting to zero: not the expected resource type
2) false with IORESOURCE_DISABLED in res->flags: valid unassigned resource
3) true: valid assigned resource

.. _`acpi_dev_resource_address_space`:

acpi_dev_resource_address_space
===============================

.. c:function:: bool acpi_dev_resource_address_space(struct acpi_resource *ares, struct resource_win *win)

    Extract ACPI address space information.

    :param ares:
        Input ACPI resource object.
    :type ares: struct acpi_resource \*

    :param win:
        Output generic resource object.
    :type win: struct resource_win \*

.. _`acpi_dev_resource_address_space.description`:

Description
-----------

Check if the given ACPI resource object represents an address space resource
and if that's the case, use the information in it to populate the generic
resource object pointed to by \ ``win``\ .

.. _`acpi_dev_resource_address_space.return`:

Return
------

1) false with win->res.flags setting to zero: not the expected resource type
2) false with IORESOURCE_DISABLED in win->res.flags: valid unassigned
resource
3) true: valid assigned resource

.. _`acpi_dev_resource_ext_address_space`:

acpi_dev_resource_ext_address_space
===================================

.. c:function:: bool acpi_dev_resource_ext_address_space(struct acpi_resource *ares, struct resource_win *win)

    Extract ACPI address space information.

    :param ares:
        Input ACPI resource object.
    :type ares: struct acpi_resource \*

    :param win:
        Output generic resource object.
    :type win: struct resource_win \*

.. _`acpi_dev_resource_ext_address_space.description`:

Description
-----------

Check if the given ACPI resource object represents an extended address space
resource and if that's the case, use the information in it to populate the
generic resource object pointed to by \ ``win``\ .

.. _`acpi_dev_resource_ext_address_space.return`:

Return
------

1) false with win->res.flags setting to zero: not the expected resource type
2) false with IORESOURCE_DISABLED in win->res.flags: valid unassigned
resource
3) true: valid assigned resource

.. _`acpi_dev_irq_flags`:

acpi_dev_irq_flags
==================

.. c:function:: unsigned long acpi_dev_irq_flags(u8 triggering, u8 polarity, u8 shareable)

    Determine IRQ resource flags.

    :param triggering:
        Triggering type as provided by ACPI.
    :type triggering: u8

    :param polarity:
        Interrupt polarity as provided by ACPI.
    :type polarity: u8

    :param shareable:
        Whether or not the interrupt is shareable.
    :type shareable: u8

.. _`acpi_dev_get_irq_type`:

acpi_dev_get_irq_type
=====================

.. c:function:: unsigned int acpi_dev_get_irq_type(int triggering, int polarity)

    Determine irq type.

    :param triggering:
        Triggering type as provided by ACPI.
    :type triggering: int

    :param polarity:
        Interrupt polarity as provided by ACPI.
    :type polarity: int

.. _`acpi_dev_resource_interrupt`:

acpi_dev_resource_interrupt
===========================

.. c:function:: bool acpi_dev_resource_interrupt(struct acpi_resource *ares, int index, struct resource *res)

    Extract ACPI interrupt resource information.

    :param ares:
        Input ACPI resource object.
    :type ares: struct acpi_resource \*

    :param index:
        Index into the array of GSIs represented by the resource.
    :type index: int

    :param res:
        Output generic resource object.
    :type res: struct resource \*

.. _`acpi_dev_resource_interrupt.description`:

Description
-----------

Check if the given ACPI resource object represents an interrupt resource
and \ ``index``\  does not exceed the resource's interrupt count (true is returned
in that case regardless of the results of the other checks)).  If that's the
case, register the GSI corresponding to \ ``index``\  from the array of interrupts
represented by the resource and populate the generic resource object pointed
to by \ ``res``\  accordingly.  If the registration of the GSI is not successful,
IORESOURCE_DISABLED will be set it that object's flags.

.. _`acpi_dev_resource_interrupt.return`:

Return
------

1) false with res->flags setting to zero: not the expected resource type
2) false with IORESOURCE_DISABLED in res->flags: valid unassigned resource
3) true: valid assigned resource

.. _`acpi_dev_free_resource_list`:

acpi_dev_free_resource_list
===========================

.. c:function:: void acpi_dev_free_resource_list(struct list_head *list)

    Free resource from \ ``acpi_dev_get_resources``\ ().

    :param list:
        The head of the resource list to free.
    :type list: struct list_head \*

.. _`acpi_dev_get_resources`:

acpi_dev_get_resources
======================

.. c:function:: int acpi_dev_get_resources(struct acpi_device *adev, struct list_head *list, int (*preproc)(struct acpi_resource *, void *), void *preproc_data)

    Get current resources of a device.

    :param adev:
        ACPI device node to get the resources for.
    :type adev: struct acpi_device \*

    :param list:
        Head of the resultant list of resources (must be empty).
    :type list: struct list_head \*

    :param int (\*preproc)(struct acpi_resource \*, void \*):
        The caller's preprocessing routine.

    :param preproc_data:
        Pointer passed to the caller's preprocessing routine.
    :type preproc_data: void \*

.. _`acpi_dev_get_resources.description`:

Description
-----------

Evaluate the \_CRS method for the given device node and process its output by
(1) executing the \ ``preproc``\ () rountine provided by the caller, passing the
resource pointer and \ ``preproc_data``\  to it as arguments, for each ACPI resource
returned and (2) converting all of the returned ACPI resources into struct
resource objects if possible.  If the return value of \ ``preproc``\ () in step (1)
is different from 0, step (2) is not applied to the given ACPI resource and
if that value is negative, the whole processing is aborted and that value is
returned as the final error code.

The resultant struct resource objects are put on the list pointed to by
\ ``list``\ , that must be empty initially, as members of struct resource_entry
objects.  Callers of this routine should use \ ``acpi_dev_free_resource_list``\ () to
free that list.

The number of resources in the output list is returned on success, an error
code reflecting the error condition is returned otherwise.

.. _`acpi_dev_get_dma_resources`:

acpi_dev_get_dma_resources
==========================

.. c:function:: int acpi_dev_get_dma_resources(struct acpi_device *adev, struct list_head *list)

    Get current DMA resources of a device.

    :param adev:
        ACPI device node to get the resources for.
    :type adev: struct acpi_device \*

    :param list:
        Head of the resultant list of resources (must be empty).
    :type list: struct list_head \*

.. _`acpi_dev_get_dma_resources.description`:

Description
-----------

Evaluate the \_DMA method for the given device node and process its
output.

The resultant struct resource objects are put on the list pointed to
by \ ``list``\ , that must be empty initially, as members of struct
resource_entry objects.  Callers of this routine should use
\ ``acpi_dev_free_resource_list``\ () to free that list.

The number of resources in the output list is returned on success,
an error code reflecting the error condition is returned otherwise.

.. _`acpi_dev_filter_resource_type`:

acpi_dev_filter_resource_type
=============================

.. c:function:: int acpi_dev_filter_resource_type(struct acpi_resource *ares, unsigned long types)

    Filter ACPI resource according to resource types

    :param ares:
        Input ACPI resource object.
    :type ares: struct acpi_resource \*

    :param types:
        Valid resource types of IORESOURCE_XXX
    :type types: unsigned long

.. _`acpi_dev_filter_resource_type.description`:

Description
-----------

This is a helper function to support \ :c:func:`acpi_dev_get_resources`\ , which filters
ACPI resource objects according to resource types.

.. _`acpi_resource_consumer`:

acpi_resource_consumer
======================

.. c:function:: struct acpi_device *acpi_resource_consumer(struct resource *res)

    Find the ACPI device that consumes \ ``res``\ .

    :param res:
        Resource to search for.
    :type res: struct resource \*

.. _`acpi_resource_consumer.description`:

Description
-----------

Search the current resource settings (_CRS) of every ACPI device node
for \ ``res``\ .  If we find an ACPI device whose \_CRS includes \ ``res``\ , return
it.  Otherwise, return NULL.

.. This file was automatic generated / don't edit.

