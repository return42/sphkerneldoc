.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-104-dio-48e.c

.. _`dio48e_gpio`:

struct dio48e_gpio
==================

.. c:type:: struct dio48e_gpio

    GPIO device private data structure

.. _`dio48e_gpio.definition`:

Definition
----------

.. code-block:: c

    struct dio48e_gpio {
        struct gpio_chip chip;
        unsigned char io_state;
        unsigned char out_state;
        unsigned char control;
        raw_spinlock_t lock;
        unsigned base;
        unsigned char irq_mask;
    }

.. _`dio48e_gpio.members`:

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

irq_mask
    I/O bits affected by interrupts

.. This file was automatic generated / don't edit.

