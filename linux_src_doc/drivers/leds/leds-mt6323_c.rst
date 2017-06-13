.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/leds/leds-mt6323.c

.. _`mt6323_led`:

struct mt6323_led
=================

.. c:type:: struct mt6323_led

    state container for the LED device

.. _`mt6323_led.definition`:

Definition
----------

.. code-block:: c

    struct mt6323_led {
        int id;
        struct mt6323_leds *parent;
        struct led_classdev cdev;
        enum led_brightness current_brightness;
    }

.. _`mt6323_led.members`:

Members
-------

id
    the identifier in MT6323 LED device

parent
    the pointer to MT6323 LED controller

cdev
    LED class device for this LED device

current_brightness
    current state of the LED device

.. _`mt6323_leds`:

struct mt6323_leds
==================

.. c:type:: struct mt6323_leds

    state container for holding LED controller of the driver

.. _`mt6323_leds.definition`:

Definition
----------

.. code-block:: c

    struct mt6323_leds {
        struct device *dev;
        struct mt6397_chip *hw;
        struct mutex lock;
        struct mt6323_led  *led;
    }

.. _`mt6323_leds.members`:

Members
-------

dev
    the device pointer

hw
    the underlying hardware providing shared
    bus for the register operations

lock
    the lock among process context

led
    the array that contains the state of individual
    LED device

.. This file was automatic generated / don't edit.

