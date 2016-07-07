.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/leds/leds-bcm6328.c

.. _`bcm6328_led`:

struct bcm6328_led
==================

.. c:type:: struct bcm6328_led

    state container for bcm6328 based LEDs

.. _`bcm6328_led.definition`:

Definition
----------

.. code-block:: c

    struct bcm6328_led {
        struct led_classdev cdev;
        void __iomem *mem;
        spinlock_t *lock;
        unsigned long pin;
        unsigned long *blink_leds;
        unsigned long *blink_delay;
        bool active_low;
    }

.. _`bcm6328_led.members`:

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

blink_leds
    blinking LEDs

blink_delay
    blinking delay

active_low
    LED is active low

.. _`bcm6328_pin2shift`:

bcm6328_pin2shift
=================

.. c:function:: unsigned long bcm6328_pin2shift(unsigned long pin)

    bits [31:0] -> LEDs 8-23 bits [47:32] -> LEDs 0-7 bits [63:48] -> unused

    :param unsigned long pin:
        *undescribed*

.. This file was automatic generated / don't edit.

