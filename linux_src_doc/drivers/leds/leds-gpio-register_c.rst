.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/leds/leds-gpio-register.c

.. _`gpio_led_register_device`:

gpio_led_register_device
========================

.. c:function:: struct platform_device *gpio_led_register_device(int id, const struct gpio_led_platform_data *pdata)

    register a gpio-led device

    :param id:
        *undescribed*
    :type id: int

    :param pdata:
        the platform data used for the new device
    :type pdata: const struct gpio_led_platform_data \*

.. _`gpio_led_register_device.description`:

Description
-----------

Makes a copy of pdata and pdata->leds and registers a new leds-gpio device
with the result. This allows to have pdata and pdata-leds in .init.rodata
and so saves some bytes compared to a static struct platform_device with
static platform data.

Returns the registered device or an error pointer.

.. This file was automatic generated / don't edit.

