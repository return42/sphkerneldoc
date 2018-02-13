.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpiolib-devprop.c

.. _`devprop_gpiochip_set_names`:

devprop_gpiochip_set_names
==========================

.. c:function:: void devprop_gpiochip_set_names(struct gpio_chip *chip, const struct fwnode_handle *fwnode)

    Set GPIO line names using device properties

    :param struct gpio_chip \*chip:
        GPIO chip whose lines should be named, if possible

    :param const struct fwnode_handle \*fwnode:
        Property Node containing the gpio-line-names property

.. _`devprop_gpiochip_set_names.description`:

Description
-----------

Looks for device property "gpio-line-names" and if it exists assigns
GPIO line names for the chip. The memory allocated for the assigned
names belong to the underlying firmware node and should not be released
by the caller.

.. This file was automatic generated / don't edit.

