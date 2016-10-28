.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/leds/leds-syscon.c

.. _`syscon_led`:

struct syscon_led
=================

.. c:type:: struct syscon_led

    state container for syscon based LEDs

.. _`syscon_led.definition`:

Definition
----------

.. code-block:: c

    struct syscon_led {
        struct led_classdev cdev;
        struct regmap *map;
        u32 offset;
        u32 mask;
        bool state;
    }

.. _`syscon_led.members`:

Members
-------

cdev
    LED class device for this LED

map
    regmap to access the syscon device backing this LED

offset
    the offset into the syscon regmap for the LED register

mask
    the bit in the register corresponding to the LED

state
    current state of the LED

.. This file was automatic generated / don't edit.

