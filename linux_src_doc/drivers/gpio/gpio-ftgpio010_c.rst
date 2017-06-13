.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-ftgpio010.c

.. _`ftgpio_gpio`:

struct ftgpio_gpio
==================

.. c:type:: struct ftgpio_gpio

    Gemini GPIO state container

.. _`ftgpio_gpio.definition`:

Definition
----------

.. code-block:: c

    struct ftgpio_gpio {
        struct device *dev;
        struct gpio_chip gc;
        void __iomem *base;
    }

.. _`ftgpio_gpio.members`:

Members
-------

dev
    containing device for this instance

gc
    gpiochip for this instance

base
    *undescribed*

.. This file was automatic generated / don't edit.

