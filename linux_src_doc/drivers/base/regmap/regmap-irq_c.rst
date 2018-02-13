.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/regmap/regmap-irq.c

.. _`regmap_add_irq_chip`:

regmap_add_irq_chip
===================

.. c:function:: int regmap_add_irq_chip(struct regmap *map, int irq, int irq_flags, int irq_base, const struct regmap_irq_chip *chip, struct regmap_irq_chip_data **data)

    Use standard regmap IRQ controller handling

    :param struct regmap \*map:
        The regmap for the device.

    :param int irq:
        The IRQ the device uses to signal interrupts.

    :param int irq_flags:
        The IRQF\_ flags to use for the primary interrupt.

    :param int irq_base:
        Allocate at specific IRQ number if irq_base > 0.

    :param const struct regmap_irq_chip \*chip:
        Configuration for the interrupt controller.

    :param struct regmap_irq_chip_data \*\*data:
        Runtime data structure for the controller, allocated on success.

.. _`regmap_add_irq_chip.description`:

Description
-----------

Returns 0 on success or an errno on failure.

In order for this to be efficient the chip really should use a
register cache.  The chip driver is responsible for restoring the
register values used by the IRQ controller over suspend and resume.

.. _`regmap_del_irq_chip`:

regmap_del_irq_chip
===================

.. c:function:: void regmap_del_irq_chip(int irq, struct regmap_irq_chip_data *d)

    Stop interrupt handling for a regmap IRQ chip

    :param int irq:
        Primary IRQ for the device

    :param struct regmap_irq_chip_data \*d:
        \ :c:type:`struct regmap_irq_chip_data <regmap_irq_chip_data>`\  allocated by \ :c:func:`regmap_add_irq_chip`\ 

.. _`regmap_del_irq_chip.description`:

Description
-----------

This function also disposes of all mapped IRQs on the chip.

.. _`devm_regmap_add_irq_chip`:

devm_regmap_add_irq_chip
========================

.. c:function:: int devm_regmap_add_irq_chip(struct device *dev, struct regmap *map, int irq, int irq_flags, int irq_base, const struct regmap_irq_chip *chip, struct regmap_irq_chip_data **data)

    Resource manager \ :c:func:`regmap_add_irq_chip`\ 

    :param struct device \*dev:
        The device pointer on which irq_chip belongs to.

    :param struct regmap \*map:
        The regmap for the device.

    :param int irq:
        The IRQ the device uses to signal interrupts

    :param int irq_flags:
        The IRQF\_ flags to use for the primary interrupt.

    :param int irq_base:
        Allocate at specific IRQ number if irq_base > 0.

    :param const struct regmap_irq_chip \*chip:
        Configuration for the interrupt controller.

    :param struct regmap_irq_chip_data \*\*data:
        Runtime data structure for the controller, allocated on success

.. _`devm_regmap_add_irq_chip.description`:

Description
-----------

Returns 0 on success or an errno on failure.

The \ :c:type:`struct regmap_irq_chip_data <regmap_irq_chip_data>`\  will be automatically released when the device is
unbound.

.. _`devm_regmap_del_irq_chip`:

devm_regmap_del_irq_chip
========================

.. c:function:: void devm_regmap_del_irq_chip(struct device *dev, int irq, struct regmap_irq_chip_data *data)

    Resource managed \ :c:func:`regmap_del_irq_chip`\ 

    :param struct device \*dev:
        Device for which which resource was allocated.

    :param int irq:
        Primary IRQ for the device.

    :param struct regmap_irq_chip_data \*data:
        \ :c:type:`struct regmap_irq_chip_data <regmap_irq_chip_data>`\  allocated by \ :c:func:`regmap_add_irq_chip`\ .

.. _`devm_regmap_del_irq_chip.description`:

Description
-----------

A resource managed version of \ :c:func:`regmap_del_irq_chip`\ .

.. _`regmap_irq_chip_get_base`:

regmap_irq_chip_get_base
========================

.. c:function:: int regmap_irq_chip_get_base(struct regmap_irq_chip_data *data)

    Retrieve interrupt base for a regmap IRQ chip

    :param struct regmap_irq_chip_data \*data:
        regmap irq controller to operate on.

.. _`regmap_irq_chip_get_base.description`:

Description
-----------

Useful for drivers to request their own IRQs.

.. _`regmap_irq_get_virq`:

regmap_irq_get_virq
===================

.. c:function:: int regmap_irq_get_virq(struct regmap_irq_chip_data *data, int irq)

    Map an interrupt on a chip to a virtual IRQ

    :param struct regmap_irq_chip_data \*data:
        regmap irq controller to operate on.

    :param int irq:
        index of the interrupt requested in the chip IRQs.

.. _`regmap_irq_get_virq.description`:

Description
-----------

Useful for drivers to request their own IRQs.

.. _`regmap_irq_get_domain`:

regmap_irq_get_domain
=====================

.. c:function:: struct irq_domain *regmap_irq_get_domain(struct regmap_irq_chip_data *data)

    Retrieve the irq_domain for the chip

    :param struct regmap_irq_chip_data \*data:
        regmap_irq controller to operate on.

.. _`regmap_irq_get_domain.description`:

Description
-----------

Useful for drivers to request their own IRQs and for integration
with subsystems.  For ease of integration NULL is accepted as a
domain, allowing devices to just call this even if no domain is
allocated.

.. This file was automatic generated / don't edit.

