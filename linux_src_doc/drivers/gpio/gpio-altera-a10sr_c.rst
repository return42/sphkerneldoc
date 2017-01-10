.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-altera-a10sr.c

.. _`altr_a10sr_gpio`:

struct altr_a10sr_gpio
======================

.. c:type:: struct altr_a10sr_gpio

    Altera Max5 GPIO device private data structure

.. _`altr_a10sr_gpio.definition`:

Definition
----------

.. code-block:: c

    struct altr_a10sr_gpio {
        struct gpio_chip gp;
        struct regmap *regmap;
    }

.. _`altr_a10sr_gpio.members`:

Members
-------

gp
    : instance of the gpio_chip

regmap
    the regmap from the parent device.

.. This file was automatic generated / don't edit.

