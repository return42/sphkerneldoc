.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/i2c-gpio.h

.. _`i2c_gpio_platform_data`:

struct i2c_gpio_platform_data
=============================

.. c:type:: struct i2c_gpio_platform_data

    Platform-dependent data for i2c-gpio

.. _`i2c_gpio_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct i2c_gpio_platform_data {
        int udelay;
        int timeout;
        unsigned int sda_is_open_drain:1;
        unsigned int scl_is_open_drain:1;
        unsigned int scl_is_output_only:1;
    }

.. _`i2c_gpio_platform_data.members`:

Members
-------

udelay
    signal toggle delay. SCL frequency is (500 / udelay) kHz

timeout
    clock stretching timeout in jiffies. If the slave keeps
    SCL low for longer than this, the transfer will time out.

sda_is_open_drain
    SDA is configured as open drain, i.e. the pin
    isn't actively driven high when setting the output value high.
    \ :c:func:`gpio_get_value`\  must return the actual pin state even if the
    pin is configured as an output.

scl_is_open_drain
    SCL is set up as open drain. Same requirements
    as for sda_is_open_drain apply.

scl_is_output_only
    SCL output drivers cannot be turned off.

.. This file was automatic generated / don't edit.

