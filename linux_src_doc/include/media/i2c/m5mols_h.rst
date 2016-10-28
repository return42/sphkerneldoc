.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/i2c/m5mols.h

.. _`m5mols_platform_data`:

struct m5mols_platform_data
===========================

.. c:type:: struct m5mols_platform_data

    platform data for M-5MOLS driver

.. _`m5mols_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct m5mols_platform_data {
        int gpio_reset;
        u8 reset_polarity;
        int (*set_power)(struct device *dev, int on);
    }

.. _`m5mols_platform_data.members`:

Members
-------

gpio_reset
    GPIO driving the reset pin of M-5MOLS

reset_polarity
    active state for gpio_reset pin, 0 or 1

set_power
    an additional callback to the board setup code
    to be called after enabling and before disabling
    the sensor's supply regulators

.. This file was automatic generated / don't edit.

