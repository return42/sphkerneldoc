.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinmux.c

.. _`pin_request`:

pin_request
===========

.. c:function:: int pin_request(struct pinctrl_dev *pctldev, int pin, const char *owner, struct pinctrl_gpio_range *gpio_range)

    request a single pin to be muxed in, typically for GPIO

    :param pctldev:
        *undescribed*
    :type pctldev: struct pinctrl_dev \*

    :param pin:
        the pin number in the global pin space
    :type pin: int

    :param owner:
        a representation of the owner of this pin; typically the device
        name that controls its mux function, or the requested GPIO name
    :type owner: const char \*

    :param gpio_range:
        the range matching the GPIO pin if this is a request for a
        single GPIO pin
    :type gpio_range: struct pinctrl_gpio_range \*

.. _`pin_free`:

pin_free
========

.. c:function:: const char *pin_free(struct pinctrl_dev *pctldev, int pin, struct pinctrl_gpio_range *gpio_range)

    release a single muxed in pin so something else can be muxed

    :param pctldev:
        pin controller device handling this pin
    :type pctldev: struct pinctrl_dev \*

    :param pin:
        the pin to free
    :type pin: int

    :param gpio_range:
        the range matching the GPIO pin if this is a request for a
        single GPIO pin
    :type gpio_range: struct pinctrl_gpio_range \*

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

    :param pctldev:
        pin controller device affected
    :type pctldev: struct pinctrl_dev \*

    :param range:
        the applicable GPIO range
    :type range: struct pinctrl_gpio_range \*

    :param pin:
        the pin to mux in for GPIO
    :type pin: unsigned

    :param gpio:
        *undescribed*
    :type gpio: unsigned

.. _`pinmux_free_gpio`:

pinmux_free_gpio
================

.. c:function:: void pinmux_free_gpio(struct pinctrl_dev *pctldev, unsigned pin, struct pinctrl_gpio_range *range)

    release a pin from GPIO muxing

    :param pctldev:
        the pin controller device for the pin
    :type pctldev: struct pinctrl_dev \*

    :param pin:
        the affected currently GPIO-muxed in pin
    :type pin: unsigned

    :param range:
        applicable GPIO range
    :type range: struct pinctrl_gpio_range \*

.. _`pinmux_gpio_direction`:

pinmux_gpio_direction
=====================

.. c:function:: int pinmux_gpio_direction(struct pinctrl_dev *pctldev, struct pinctrl_gpio_range *range, unsigned pin, bool input)

    set the direction of a single muxed-in GPIO pin

    :param pctldev:
        the pin controller handling this pin
    :type pctldev: struct pinctrl_dev \*

    :param range:
        applicable GPIO range
    :type range: struct pinctrl_gpio_range \*

    :param pin:
        the affected GPIO pin in this controller
    :type pin: unsigned

    :param input:
        true if we set the pin as input, false for output
    :type input: bool

.. _`pinmux_generic_get_function_count`:

pinmux_generic_get_function_count
=================================

.. c:function:: int pinmux_generic_get_function_count(struct pinctrl_dev *pctldev)

    returns number of functions

    :param pctldev:
        pin controller device
    :type pctldev: struct pinctrl_dev \*

.. _`pinmux_generic_get_function_name`:

pinmux_generic_get_function_name
================================

.. c:function:: const char *pinmux_generic_get_function_name(struct pinctrl_dev *pctldev, unsigned int selector)

    returns the function name

    :param pctldev:
        pin controller device
    :type pctldev: struct pinctrl_dev \*

    :param selector:
        function number
    :type selector: unsigned int

.. _`pinmux_generic_get_function_groups`:

pinmux_generic_get_function_groups
==================================

.. c:function:: int pinmux_generic_get_function_groups(struct pinctrl_dev *pctldev, unsigned int selector, const char * const **groups, unsigned * const num_groups)

    gets the function groups

    :param pctldev:
        pin controller device
    :type pctldev: struct pinctrl_dev \*

    :param selector:
        function number
    :type selector: unsigned int

    :param groups:
        array of pin groups
    :type groups: const char \* const \*\*

    :param num_groups:
        number of pin groups
    :type num_groups: unsigned \* const

.. _`pinmux_generic_get_function`:

pinmux_generic_get_function
===========================

.. c:function:: struct function_desc *pinmux_generic_get_function(struct pinctrl_dev *pctldev, unsigned int selector)

    returns a function based on the number

    :param pctldev:
        pin controller device
    :type pctldev: struct pinctrl_dev \*

    :param selector:
        *undescribed*
    :type selector: unsigned int

.. _`pinmux_generic_add_function`:

pinmux_generic_add_function
===========================

.. c:function:: int pinmux_generic_add_function(struct pinctrl_dev *pctldev, const char *name, const char **groups, const unsigned int num_groups, void *data)

    adds a function group

    :param pctldev:
        pin controller device
    :type pctldev: struct pinctrl_dev \*

    :param name:
        name of the function
    :type name: const char \*

    :param groups:
        array of pin groups
    :type groups: const char \*\*

    :param num_groups:
        number of pin groups
    :type num_groups: const unsigned int

    :param data:
        pin controller driver specific data
    :type data: void \*

.. _`pinmux_generic_remove_function`:

pinmux_generic_remove_function
==============================

.. c:function:: int pinmux_generic_remove_function(struct pinctrl_dev *pctldev, unsigned int selector)

    removes a numbered function

    :param pctldev:
        pin controller device
    :type pctldev: struct pinctrl_dev \*

    :param selector:
        function number
    :type selector: unsigned int

.. _`pinmux_generic_remove_function.description`:

Description
-----------

Note that the caller must take care of locking.

.. _`pinmux_generic_free_functions`:

pinmux_generic_free_functions
=============================

.. c:function:: void pinmux_generic_free_functions(struct pinctrl_dev *pctldev)

    removes all functions

    :param pctldev:
        pin controller device
    :type pctldev: struct pinctrl_dev \*

.. _`pinmux_generic_free_functions.description`:

Description
-----------

Note that the caller must take care of locking. The pinctrl
functions are allocated with \ :c:func:`devm_kzalloc`\  so no need to free
them here.

.. This file was automatic generated / don't edit.

