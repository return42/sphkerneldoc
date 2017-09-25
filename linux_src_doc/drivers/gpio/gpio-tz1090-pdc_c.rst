.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-tz1090-pdc.c

.. _`tz1090_pdc_gpio`:

struct tz1090_pdc_gpio
======================

.. c:type:: struct tz1090_pdc_gpio

    GPIO bank private data

.. _`tz1090_pdc_gpio.definition`:

Definition
----------

.. code-block:: c

    struct tz1090_pdc_gpio {
        struct gpio_chip chip;
        void __iomem *reg;
        int irq[GPIO_PDC_NIRQ];
    }

.. _`tz1090_pdc_gpio.members`:

Members
-------

chip
    Generic GPIO chip for GPIO bank

reg
    Base of registers, offset for this GPIO bank

irq
    IRQ numbers for Syswake GPIOs

.. _`tz1090_pdc_gpio.description`:

Description
-----------

This is the main private data for the PDC GPIO driver. It encapsulates a
gpio_chip, and the callbacks for the gpio_chip can access the private data
with the \ :c:func:`to_pdc`\  macro below.

.. This file was automatic generated / don't edit.

