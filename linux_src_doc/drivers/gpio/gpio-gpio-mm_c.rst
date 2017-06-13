.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-gpio-mm.c

.. _`gpiomm_gpio`:

struct gpiomm_gpio
==================

.. c:type:: struct gpiomm_gpio

    GPIO device private data structure

.. _`gpiomm_gpio.definition`:

Definition
----------

.. code-block:: c

    struct gpiomm_gpio {
        struct gpio_chip chip;
        unsigned char io_state;
        unsigned char out_state;
        unsigned char control;
        spinlock_t lock;
        unsigned int base;
    }

.. _`gpiomm_gpio.members`:

Members
-------

chip
    instance of the gpio_chip

io_state
    bit I/O state (whether bit is set to input or output)

out_state
    output bits state

control
    Control registers state

lock
    synchronization lock to prevent I/O race conditions

base
    base port address of the GPIO device

.. This file was automatic generated / don't edit.

