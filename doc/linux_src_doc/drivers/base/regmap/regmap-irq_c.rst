.. -*- coding: utf-8; mode: rst -*-

============
regmap-irq.c
============


.. _`regmap_add_irq_chip`:

regmap_add_irq_chip
===================

.. c:function:: int regmap_add_irq_chip (struct regmap *map, int irq, int irq_flags, int irq_base, const struct regmap_irq_chip *chip, struct regmap_irq_chip_data **data)

    :param struct regmap \*map:

        *undescribed*

    :param int irq:

        *undescribed*

    :param int irq_flags:

        *undescribed*

    :param int irq_base:

        *undescribed*

    :param const struct regmap_irq_chip \*chip:

        *undescribed*

    :param struct regmap_irq_chip_data \*\*data:

        *undescribed*



.. _`regmap_add_irq_chip.map`:

map
---

The regmap for the device.



.. _`regmap_add_irq_chip.irq`:

irq
---

The IRQ the device uses to signal interrupts



.. _`regmap_add_irq_chip.irq_flags`:

irq_flags
---------

The IRQF_ flags to use for the primary interrupt.



.. _`regmap_add_irq_chip.chip`:

chip
----

Configuration for the interrupt controller.



.. _`regmap_add_irq_chip.data`:

data
----

Runtime data structure for the controller, allocated on success

Returns 0 on success or an errno on failure.

In order for this to be efficient the chip really should use a
register cache.  The chip driver is responsible for restoring the
register values used by the IRQ controller over suspend and resume.



.. _`regmap_del_irq_chip`:

regmap_del_irq_chip
===================

.. c:function:: void regmap_del_irq_chip (int irq, struct regmap_irq_chip_data *d)

    :param int irq:
        Primary IRQ for the device

    :param struct regmap_irq_chip_data \*d:
        regmap_irq_chip_data allocated by :c:func:`regmap_add_irq_chip`



.. _`regmap_del_irq_chip.description`:

Description
-----------

This function also dispose all mapped irq on chip.



.. _`devm_regmap_add_irq_chip`:

devm_regmap_add_irq_chip
========================

.. c:function:: int devm_regmap_add_irq_chip (struct device *dev, struct regmap *map, int irq, int irq_flags, int irq_base, const struct regmap_irq_chip *chip, struct regmap_irq_chip_data **data)

    :param struct device \*dev:
        The device pointer on which irq_chip belongs to.

    :param struct regmap \*map:
        The regmap for the device.

    :param int irq:
        The IRQ the device uses to signal interrupts

    :param int irq_flags:
        The IRQF_ flags to use for the primary interrupt.

    :param int irq_base:

        *undescribed*

    :param const struct regmap_irq_chip \*chip:
        Configuration for the interrupt controller.

    :param struct regmap_irq_chip_data \*\*data:
        Runtime data structure for the controller, allocated on success



.. _`devm_regmap_add_irq_chip.description`:

Description
-----------

Returns 0 on success or an errno on failure.

The regmap_irq_chip data automatically be released when the device is
unbound.



.. _`devm_regmap_del_irq_chip`:

devm_regmap_del_irq_chip
========================

.. c:function:: void devm_regmap_del_irq_chip (struct device *dev, int irq, struct regmap_irq_chip_data *data)

    :param struct device \*dev:
        Device for which which resource was allocated.

    :param int irq:
        Primary IRQ for the device

    :param struct regmap_irq_chip_data \*data:

        *undescribed*



.. _`regmap_irq_chip_get_base`:

regmap_irq_chip_get_base
========================

.. c:function:: int regmap_irq_chip_get_base (struct regmap_irq_chip_data *data)

    :param struct regmap_irq_chip_data \*data:
        regmap_irq controller to operate on.



.. _`regmap_irq_chip_get_base.description`:

Description
-----------


Useful for drivers to request their own IRQs.



.. _`regmap_irq_get_virq`:

regmap_irq_get_virq
===================

.. c:function:: int regmap_irq_get_virq (struct regmap_irq_chip_data *data, int irq)

    :param struct regmap_irq_chip_data \*data:
        regmap_irq controller to operate on.

    :param int irq:
        index of the interrupt requested in the chip IRQs



.. _`regmap_irq_get_virq.description`:

Description
-----------


Useful for drivers to request their own IRQs.



.. _`regmap_irq_get_domain`:

regmap_irq_get_domain
=====================

.. c:function:: struct irq_domain *regmap_irq_get_domain (struct regmap_irq_chip_data *data)

    :param struct regmap_irq_chip_data \*data:
        regmap_irq controller to operate on.



.. _`regmap_irq_get_domain.description`:

Description
-----------


Useful for drivers to request their own IRQs and for integration
with subsystems.  For ease of integration NULL is accepted as a
domain, allowing devices to just call this even if no domain is
allocated.

