.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/i2c-mux-gpio.h

.. _`i2c_mux_gpio_platform_data`:

struct i2c_mux_gpio_platform_data
=================================

.. c:type:: struct i2c_mux_gpio_platform_data

    Platform-dependent data for i2c-mux-gpio

.. _`i2c_mux_gpio_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct i2c_mux_gpio_platform_data {
        int parent;
        int base_nr;
        const unsigned *values;
        int n_values;
        const unsigned *classes;
        char *gpio_chip;
        const unsigned *gpios;
        int n_gpios;
        unsigned idle;
    }

.. _`i2c_mux_gpio_platform_data.members`:

Members
-------

parent
    Parent I2C bus adapter number

base_nr
    Base I2C bus number to number adapters from or zero for dynamic

values
    Array of bitmasks of GPIO settings (low/high) for each
    position

n_values
    Number of multiplexer positions (busses to instantiate)

classes
    Optional I2C auto-detection classes

gpio_chip
    Optional GPIO chip name; if set, GPIO pin numbers are given
    relative to the base GPIO number of that chip

gpios
    Array of GPIO numbers used to control MUX

n_gpios
    Number of GPIOs used to control MUX

idle
    Bitmask to write to MUX when idle or GPIO_I2CMUX_NO_IDLE if not used

.. This file was automatic generated / don't edit.

