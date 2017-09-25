.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-ws16c48.c

.. _`ws16c48_gpio`:

struct ws16c48_gpio
===================

.. c:type:: struct ws16c48_gpio

    GPIO device private data structure

.. _`ws16c48_gpio.definition`:

Definition
----------

.. code-block:: c

    struct ws16c48_gpio {
        struct gpio_chip chip;
        unsigned char io_state[6];
        unsigned char out_state[6];
        raw_spinlock_t lock;
        unsigned long irq_mask;
        unsigned long flow_mask;
        unsigned base;
    }

.. _`ws16c48_gpio.members`:

Members
-------

chip
    instance of the gpio_chip

io_state
    bit I/O state (whether bit is set to input or output)

out_state
    output bits state

lock
    synchronization lock to prevent I/O race conditions

irq_mask
    I/O bits affected by interrupts

flow_mask
    IRQ flow type mask for the respective I/O bits

base
    base port address of the GPIO device

.. This file was automatic generated / don't edit.

