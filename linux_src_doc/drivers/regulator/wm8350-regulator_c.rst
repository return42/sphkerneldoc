.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/regulator/wm8350-regulator.c

.. _`wm8350_register_led`:

wm8350_register_led
===================

.. c:function:: int wm8350_register_led(struct wm8350 *wm8350, int lednum, int dcdc, int isink, struct wm8350_led_platform_data *pdata)

    Register a WM8350 LED output

    :param struct wm8350 \*wm8350:
        *undescribed*

    :param int lednum:
        *undescribed*

    :param int dcdc:
        *undescribed*

    :param int isink:
        *undescribed*

    :param struct wm8350_led_platform_data \*pdata:
        *undescribed*

.. _`wm8350_register_led.description`:

Description
-----------

@param wm8350 The WM8350 device to configure.
\ ``param``\  lednum LED device index to create.
\ ``param``\  dcdc The DCDC to use for the LED.
\ ``param``\  isink The ISINK to use for the LED.
\ ``param``\  pdata Configuration for the LED.

The WM8350 supports the use of an ISINK together with a DCDC to
provide a power-efficient LED driver.  This function registers the
regulators and instantiates the platform device for a LED.  The
operating modes for the LED regulators must be configured using
\ :c:func:`wm8350_isink_set_flash`\ , \ :c:func:`wm8350_dcdc25_set_mode`\  and
\ :c:func:`wm8350_dcdc_set_slot`\  prior to calling this function.

.. This file was automatic generated / don't edit.

