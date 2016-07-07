.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/leds/leds-bcm6358.c

.. _`bcm6358_led`:

struct bcm6358_led
==================

.. c:type:: struct bcm6358_led

    state container for bcm6358 based LEDs

.. _`bcm6358_led.definition`:

Definition
----------

.. code-block:: c

    struct bcm6358_led {
        struct led_classdev cdev;
        void __iomem *mem;
        spinlock_t *lock;
        unsigned long pin;
        bool active_low;
    }

.. _`bcm6358_led.members`:

Members
-------

cdev
    LED class device for this LED

mem
    memory resource

lock
    memory lock

pin
    LED pin number

active_low
    LED is active low

.. This file was automatic generated / don't edit.

