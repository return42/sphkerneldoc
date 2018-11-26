.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/irq.c

.. _`acpi_gsi_to_irq`:

acpi_gsi_to_irq
===============

.. c:function:: int acpi_gsi_to_irq(u32 gsi, unsigned int *irq)

    Retrieve the linux irq number for a given GSI

    :param gsi:
        GSI IRQ number to map
    :type gsi: u32

    :param irq:
        pointer where linux IRQ number is stored
    :type irq: unsigned int \*

.. _`acpi_gsi_to_irq.description`:

Description
-----------

irq location updated with irq value [>0 on success, 0 on failure]

.. _`acpi_gsi_to_irq.return`:

Return
------

0 on success
-EINVAL on failure

.. _`acpi_register_gsi`:

acpi_register_gsi
=================

.. c:function:: int acpi_register_gsi(struct device *dev, u32 gsi, int trigger, int polarity)

    Map a GSI to a linux IRQ number

    :param dev:
        device for which IRQ has to be mapped
    :type dev: struct device \*

    :param gsi:
        GSI IRQ number
    :type gsi: u32

    :param trigger:
        trigger type of the GSI number to be mapped
    :type trigger: int

    :param polarity:
        polarity of the GSI to be mapped
    :type polarity: int

.. _`acpi_register_gsi.return`:

Return
------

a valid linux IRQ number on success
-EINVAL on failure

.. _`acpi_unregister_gsi`:

acpi_unregister_gsi
===================

.. c:function:: void acpi_unregister_gsi(u32 gsi)

    Free a GSI<->linux IRQ number mapping

    :param gsi:
        GSI IRQ number
    :type gsi: u32

.. _`acpi_get_irq_source_fwhandle`:

acpi_get_irq_source_fwhandle
============================

.. c:function:: struct fwnode_handle *acpi_get_irq_source_fwhandle(const struct acpi_resource_source *source)

    Retrieve fwhandle from IRQ resource source.

    :param source:
        acpi_resource_source to use for the lookup.
    :type source: const struct acpi_resource_source \*

.. _`acpi_get_irq_source_fwhandle.description`:

Description
-----------

Retrieve the fwhandle of the device referenced by the given IRQ resource
source.

.. _`acpi_get_irq_source_fwhandle.return`:

Return
------

The referenced device fwhandle or NULL on failure

.. _`acpi_irq_parse_one_match`:

acpi_irq_parse_one_match
========================

.. c:function:: void acpi_irq_parse_one_match(struct fwnode_handle *fwnode, u32 hwirq, u8 triggering, u8 polarity, u8 shareable, struct acpi_irq_parse_one_ctx *ctx)

    Handle a matching IRQ resource.

    :param fwnode:
        matching fwnode
    :type fwnode: struct fwnode_handle \*

    :param hwirq:
        hardware IRQ number
    :type hwirq: u32

    :param triggering:
        triggering attributes of hwirq
    :type triggering: u8

    :param polarity:
        polarity attributes of hwirq
    :type polarity: u8

    :param shareable:
        shareable attributes of hwirq
    :type shareable: u8

    :param ctx:
        acpi_irq_parse_one_ctx updated by this function
    :type ctx: struct acpi_irq_parse_one_ctx \*

.. _`acpi_irq_parse_one_match.description`:

Description
-----------

Handle a matching IRQ resource by populating the given ctx with
the information passed.

.. _`acpi_irq_parse_one_cb`:

acpi_irq_parse_one_cb
=====================

.. c:function:: acpi_status acpi_irq_parse_one_cb(struct acpi_resource *ares, void *context)

    Handle the given resource.

    :param ares:
        resource to handle
    :type ares: struct acpi_resource \*

    :param context:
        context for the walk
    :type context: void \*

.. _`acpi_irq_parse_one_cb.description`:

Description
-----------

This is called by acpi_walk_resources passing each resource returned by
the \_CRS method. We only inspect IRQ resources. Since IRQ resources
might contain multiple interrupts we check if the index is within this
one's interrupt array, otherwise we subtract the current resource IRQ
count from the lookup index to prepare for the next resource.
Once a match is found we call acpi_irq_parse_one_match to populate
the result and end the walk by returning AE_CTRL_TERMINATE.

.. _`acpi_irq_parse_one_cb.return`:

Return
------

AE_OK if the walk should continue, AE_CTRL_TERMINATE if a matching
IRQ resource was found.

.. _`acpi_irq_parse_one`:

acpi_irq_parse_one
==================

.. c:function:: int acpi_irq_parse_one(acpi_handle handle, unsigned int index, struct irq_fwspec *fwspec, unsigned long *flags)

    Resolve an interrupt for a device

    :param handle:
        the device whose interrupt is to be resolved
    :type handle: acpi_handle

    :param index:
        index of the interrupt to resolve
    :type index: unsigned int

    :param fwspec:
        structure irq_fwspec filled by this function
    :type fwspec: struct irq_fwspec \*

    :param flags:
        resource flags filled by this function
    :type flags: unsigned long \*

.. _`acpi_irq_parse_one.description`:

Description
-----------

Resolves an interrupt for a device by walking its CRS resources to find
the appropriate ACPI IRQ resource and populating the given struct irq_fwspec
and flags.

.. _`acpi_irq_parse_one.return`:

Return
------

The result stored in ctx.rc by the callback, or the default -EINVAL value
if an error occurs.

.. _`acpi_irq_get`:

acpi_irq_get
============

.. c:function:: int acpi_irq_get(acpi_handle handle, unsigned int index, struct resource *res)

    Lookup an ACPI IRQ resource and use it to initialize resource.

    :param handle:
        ACPI device handle
    :type handle: acpi_handle

    :param index:
        ACPI IRQ resource index to lookup
    :type index: unsigned int

    :param res:
        Linux IRQ resource to initialize
    :type res: struct resource \*

.. _`acpi_irq_get.description`:

Description
-----------

Look for the ACPI IRQ resource with the given index and use it to initialize
the given Linux IRQ resource.

.. _`acpi_irq_get.return`:

Return
------

0 on success
-EINVAL if an error occurs
-EPROBE_DEFER if the IRQ lookup/conversion failed

.. _`acpi_set_irq_model`:

acpi_set_irq_model
==================

.. c:function:: void acpi_set_irq_model(enum acpi_irq_model_id model, struct fwnode_handle *fwnode)

    Setup the GSI irqdomain information

    :param model:
        the value assigned to acpi_irq_model
    :type model: enum acpi_irq_model_id

    :param fwnode:
        the irq_domain identifier for mapping and looking up
        GSI interrupts
    :type fwnode: struct fwnode_handle \*

.. This file was automatic generated / don't edit.

