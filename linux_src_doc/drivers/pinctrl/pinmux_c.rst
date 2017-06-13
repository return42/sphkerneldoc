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

.. _`pinmux_generic_get_function_count`:

pinmux_generic_get_function_count
=================================

.. c:function:: int pinmux_generic_get_function_count(struct pinctrl_dev *pctldev)

    returns number of functions

    :param struct pinctrl_dev \*pctldev:
        pin controller device

.. _`pinmux_generic_get_function_name`:

pinmux_generic_get_function_name
================================

.. c:function:: const char *pinmux_generic_get_function_name(struct pinctrl_dev *pctldev, unsigned int selector)

    returns the function name

    :param struct pinctrl_dev \*pctldev:
        pin controller device

    :param unsigned int selector:
        function number

.. _`pinmux_generic_get_function_groups`:

pinmux_generic_get_function_groups
==================================

.. c:function:: int pinmux_generic_get_function_groups(struct pinctrl_dev *pctldev, unsigned int selector, const char * const **groups, unsigned * const num_groups)

    gets the function groups

    :param struct pinctrl_dev \*pctldev:
        pin controller device

    :param unsigned int selector:
        function number

    :param const char \* const \*\*groups:
        array of pin groups

    :param unsigned \* const num_groups:
        number of pin groups

.. _`pinmux_generic_get_function`:

pinmux_generic_get_function
===========================

.. c:function:: struct function_desc *pinmux_generic_get_function(struct pinctrl_dev *pctldev, unsigned int selector)

    returns a function based on the number

    :param struct pinctrl_dev \*pctldev:
        pin controller device

    :param unsigned int selector:
        *undescribed*

.. _`pinmux_generic_add_function`:

pinmux_generic_add_function
===========================

.. c:function:: int pinmux_generic_add_function(struct pinctrl_dev *pctldev, const char *name, const char **groups, const unsigned int num_groups, void *data)

    adds a function group

    :param struct pinctrl_dev \*pctldev:
        pin controller device

    :param const char \*name:
        name of the function

    :param const char \*\*groups:
        array of pin groups

    :param const unsigned int num_groups:
        number of pin groups

    :param void \*data:
        pin controller driver specific data

.. _`pinmux_generic_remove_function`:

pinmux_generic_remove_function
==============================

.. c:function:: int pinmux_generic_remove_function(struct pinctrl_dev *pctldev, unsigned int selector)

    removes a numbered function

    :param struct pinctrl_dev \*pctldev:
        pin controller device

    :param unsigned int selector:
        function number

.. _`pinmux_generic_remove_function.description`:

Description
-----------

Note that the caller must take care of locking.

.. _`pinmux_generic_free_functions`:

pinmux_generic_free_functions
=============================

.. c:function:: void pinmux_generic_free_functions(struct pinctrl_dev *pctldev)

    removes all functions

    :param struct pinctrl_dev \*pctldev:
        pin controller device

.. _`pinmux_generic_free_functions.description`:

Description
-----------

Note that the caller must take care of locking.

.. This file was automatic generated / don't edit.

