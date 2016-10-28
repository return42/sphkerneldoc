.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/gsi.c

.. _`acpi_gsi_to_irq`:

acpi_gsi_to_irq
===============

.. c:function:: int acpi_gsi_to_irq(u32 gsi, unsigned int *irq)

    Retrieve the linux irq number for a given GSI

    :param u32 gsi:
        GSI IRQ number to map

    :param unsigned int \*irq:
        pointer where linux IRQ number is stored

.. _`acpi_gsi_to_irq.description`:

Description
-----------

irq location updated with irq value [>0 on success, 0 on failure]

.. _`acpi_gsi_to_irq.return`:

Return
------

linux IRQ number on success (>0)
-EINVAL on failure

.. _`acpi_register_gsi`:

acpi_register_gsi
=================

.. c:function:: int acpi_register_gsi(struct device *dev, u32 gsi, int trigger, int polarity)

    Map a GSI to a linux IRQ number

    :param struct device \*dev:
        device for which IRQ has to be mapped

    :param u32 gsi:
        GSI IRQ number

    :param int trigger:
        trigger type of the GSI number to be mapped

    :param int polarity:
        polarity of the GSI to be mapped

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

    :param u32 gsi:
        GSI IRQ number

.. _`acpi_set_irq_model`:

acpi_set_irq_model
==================

.. c:function:: void acpi_set_irq_model(enum acpi_irq_model_id model, struct fwnode_handle *fwnode)

    Setup the GSI irqdomain information

    :param enum acpi_irq_model_id model:
        the value assigned to acpi_irq_model

    :param struct fwnode_handle \*fwnode:
        the irq_domain identifier for mapping and looking up
        GSI interrupts

.. This file was automatic generated / don't edit.

