.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-pisosr.c

.. _`pisosr_gpio`:

struct pisosr_gpio
==================

.. c:type:: struct pisosr_gpio

    GPIO driver data

.. _`pisosr_gpio.definition`:

Definition
----------

.. code-block:: c

    struct pisosr_gpio {
        struct gpio_chip chip;
        struct spi_device *spi;
        u8 *buffer;
        size_t buffer_size;
        struct gpio_desc *load_gpio;
        struct mutex lock;
    }

.. _`pisosr_gpio.members`:

Members
-------

chip
    GPIO controller chip

spi
    SPI device pointer

buffer
    Buffer for device reads

buffer_size
    Size of buffer

load_gpio
    GPIO pin used to load input into device

lock
    Protects read sequences

.. This file was automatic generated / don't edit.

