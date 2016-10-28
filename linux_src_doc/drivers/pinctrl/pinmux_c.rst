.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinmux.c

.. _`pin_request`:

pin_request
===========

.. c:function:: int pin_request(struct pinctrl_dev *pctldev, int pin, const char *owner, struct pinctrl_gpio_range *gpio_range)

    request a single pin to be muxed in, typically for GPIO

    :param struct pinctrl_dev \*pctldev:
        *undescribed*

    :param int pin:
        the pin number in the global pin space

    :param const char \*owner:
        a representation of the owner of this pin; typically the device
        name that controls its mux function, or the requested GPIO name

    :param struct pinctrl_gpio_range \*gpio_range:
        the range matching the GPIO pin if this is a request for a
        single GPIO pin

.. _`pin_free`:

pin_free
========

.. c:function:: const char *pin_free(struct pinctrl_dev *pctldev, int pin, struct pinctrl_gpio_range *gpio_range)

    release a single muxed in pin so something else can be muxed

    :param struct pinctrl_dev \*pctldev:
        pin controller device handling this pin

    :param int pin:
        the pin to free

    :param struct pinctrl_gpio_range \*gpio_range:
        the range matching the GPIO pin if this is a request for a
        single GPIO pin

.. _`pin_free.description`:

Description
-----------

This function returns a pointer to the previous owner. This is used
for callers that dynamically allocate an owner name so it can be freed
once the pin is free. This is done for GPIO request functions.

.. _`pinmux_request_gpio`:

pinmux_request_gpio
===================

.. c:function:: int pinmux_request_gpio(struct pinctrl_dev *pctldev, struct pinctrl_gpio_range *range, unsigned pin, unsigned gpio)

    request pinmuxing for a GPIO pin

    :param struct pinctrl_dev \*pctldev:
        pin controller device affected

    :param struct pinctrl_gpio_range \*range:
        the applicable GPIO range

    :param unsigned pin:
        the pin to mux in for GPIO

    :param unsigned gpio:
        *undescribed*

.. _`pinmux_free_gpio`:

pinmux_free_gpio
================

.. c:function:: void pinmux_free_gpio(struct pinctrl_dev *pctldev, unsigned pin, struct pinctrl_gpio_range *range)

    release a pin from GPIO muxing

    :param struct pinctrl_dev \*pctldev:
        the pin controller device for the pin

    :param unsigned pin:
        the affected currently GPIO-muxed in pin

    :param struct pinctrl_gpio_range \*range:
        applicable GPIO range

.. _`pinmux_gpio_direction`:

pinmux_gpio_direction
=====================

.. c:function:: int pinmux_gpio_direction(struct pinctrl_dev *pctldev, struct pinctrl_gpio_range *range, unsigned pin, bool input)

    set the direction of a single muxed-in GPIO pin

    :param struct pinctrl_dev \*pctldev:
        the pin controller handling this pin

    :param struct pinctrl_gpio_range \*range:
        applicable GPIO range

    :param unsigned pin:
        the affected GPIO pin in this controller

    :param bool input:
        true if we set the pin as input, false for output

.. This file was automatic generated / don't edit.

