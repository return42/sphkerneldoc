.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-crystalcove.c

.. _`crystalcove_gpio`:

struct crystalcove_gpio
=======================

.. c:type:: struct crystalcove_gpio

    Crystal Cove GPIO controller

.. _`crystalcove_gpio.definition`:

Definition
----------

.. code-block:: c

    struct crystalcove_gpio {
        struct mutex buslock;
        struct gpio_chip chip;
        struct regmap *regmap;
        int update;
        int intcnt_value;
        bool set_irq_mask;
    }

.. _`crystalcove_gpio.members`:

Members
-------

buslock
    for bus lock/sync and unlock.

chip
    the abstract gpio_chip structure.

regmap
    the regmap from the parent device.

update
    pending IRQ setting update, to be written to the chip upon unlock.

intcnt_value
    the Interrupt Detect value to be written.

set_irq_mask
    true if the IRQ mask needs to be set, false to clear.

.. This file was automatic generated / don't edit.

