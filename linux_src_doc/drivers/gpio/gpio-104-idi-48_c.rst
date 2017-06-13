.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-104-idi-48.c

.. _`idi_48_gpio`:

struct idi_48_gpio
==================

.. c:type:: struct idi_48_gpio

    GPIO device private data structure

.. _`idi_48_gpio.definition`:

Definition
----------

.. code-block:: c

    struct idi_48_gpio {
        struct gpio_chip chip;
        raw_spinlock_t lock;
        spinlock_t ack_lock;
        unsigned char irq_mask[6];
        unsigned base;
        unsigned char cos_enb;
    }

.. _`idi_48_gpio.members`:

Members
-------

chip
    instance of the gpio_chip

lock
    synchronization lock to prevent I/O race conditions

ack_lock
    synchronization lock to prevent IRQ handler race conditions

irq_mask
    input bits affected by interrupts

base
    base port address of the GPIO device

cos_enb
    Change-Of-State IRQ enable boundaries mask

.. This file was automatic generated / don't edit.

