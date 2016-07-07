.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-104-idio-16.c

.. _`idio_16_gpio`:

struct idio_16_gpio
===================

.. c:type:: struct idio_16_gpio

    GPIO device private data structure

.. _`idio_16_gpio.definition`:

Definition
----------

.. code-block:: c

    struct idio_16_gpio {
        struct gpio_chip chip;
        spinlock_t lock;
        unsigned long irq_mask;
        unsigned base;
        unsigned irq;
        unsigned out_state;
    }

.. _`idio_16_gpio.members`:

Members
-------

chip
    instance of the gpio_chip

lock
    synchronization lock to prevent I/O race conditions

irq_mask
    I/O bits affected by interrupts

base
    base port address of the GPIO device

irq
    Interrupt line number

out_state
    output bits state

.. This file was automatic generated / don't edit.

