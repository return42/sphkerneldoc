.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpiolib-of.c

.. _`of_get_named_gpiod_flags`:

of_get_named_gpiod_flags
========================

.. c:function:: struct gpio_desc *of_get_named_gpiod_flags(struct device_node *np, const char *propname, int index, enum of_gpio_flags *flags)

    Get a GPIO descriptor and flags for GPIO API

    :param np:
        device node to get GPIO from
    :type np: struct device_node \*

    :param propname:
        property name containing gpio specifier(s)
    :type propname: const char \*

    :param index:
        index of the GPIO
    :type index: int

    :param flags:
        a flags pointer to fill in
    :type flags: enum of_gpio_flags \*

.. _`of_get_named_gpiod_flags.description`:

Description
-----------

Returns GPIO descriptor to use with Linux GPIO API, or one of the errno
value on the error condition. If \ ``flags``\  is not NULL the function also fills
in flags for the GPIO.

.. _`of_parse_own_gpio`:

of_parse_own_gpio
=================

.. c:function:: struct gpio_desc *of_parse_own_gpio(struct device_node *np, struct gpio_chip *chip, unsigned int idx, const char **name, enum gpio_lookup_flags *lflags, enum gpiod_flags *dflags)

    Get a GPIO hog descriptor, names and flags for GPIO API

    :param np:
        device node to get GPIO from
    :type np: struct device_node \*

    :param chip:
        GPIO chip whose hog is parsed
    :type chip: struct gpio_chip \*

    :param idx:
        Index of the GPIO to parse
    :type idx: unsigned int

    :param name:
        GPIO line name
    :type name: const char \*\*

    :param lflags:
        gpio_lookup_flags - returned from \ :c:func:`of_find_gpio`\  or
        \ :c:func:`of_parse_own_gpio`\ 
    :type lflags: enum gpio_lookup_flags \*

    :param dflags:
        gpiod_flags - optional GPIO initialization flags
    :type dflags: enum gpiod_flags \*

.. _`of_parse_own_gpio.description`:

Description
-----------

Returns GPIO descriptor to use with Linux GPIO API, or one of the errno
value on the error condition.

.. _`of_gpiochip_scan_gpios`:

of_gpiochip_scan_gpios
======================

.. c:function:: int of_gpiochip_scan_gpios(struct gpio_chip *chip)

    Scan gpio-controller for gpio definitions

    :param chip:
        gpio chip to act on
    :type chip: struct gpio_chip \*

.. _`of_gpiochip_scan_gpios.description`:

Description
-----------

This is only used by of_gpiochip_add to request/set GPIO initial
configuration.
It returns error if it fails otherwise 0 on success.

.. _`of_gpio_simple_xlate`:

of_gpio_simple_xlate
====================

.. c:function:: int of_gpio_simple_xlate(struct gpio_chip *gc, const struct of_phandle_args *gpiospec, u32 *flags)

    translate gpiospec to the GPIO number and flags

    :param gc:
        pointer to the gpio_chip structure
    :type gc: struct gpio_chip \*

    :param gpiospec:
        GPIO specifier as found in the device tree
    :type gpiospec: const struct of_phandle_args \*

    :param flags:
        a flags pointer to fill in
    :type flags: u32 \*

.. _`of_gpio_simple_xlate.description`:

Description
-----------

This is simple translation function, suitable for the most 1:1 mapped
GPIO chips. This function performs only one sanity check: whether GPIO
is less than ngpios (that is specified in the gpio_chip).

.. _`of_mm_gpiochip_add_data`:

of_mm_gpiochip_add_data
=======================

.. c:function:: int of_mm_gpiochip_add_data(struct device_node *np, struct of_mm_gpio_chip *mm_gc, void *data)

    Add memory mapped GPIO chip (bank)

    :param np:
        device node of the GPIO chip
    :type np: struct device_node \*

    :param mm_gc:
        pointer to the of_mm_gpio_chip allocated structure
    :type mm_gc: struct of_mm_gpio_chip \*

    :param data:
        driver data to store in the struct gpio_chip
    :type data: void \*

.. _`of_mm_gpiochip_add_data.to-use-this-function-you-should-allocate-and-fill-mm_gc-with`:

To use this function you should allocate and fill mm_gc with
------------------------------------------------------------


1) In the gpio_chip structure:
   - all the callbacks
   - of_gpio_n_cells
   - of_xlate callback (optional)

3) In the of_mm_gpio_chip structure:
   - save_regs callback (optional)

If succeeded, this function will map bank's memory and will
do all necessary work for you. Then you'll able to use .regs
to manage GPIOs from the callbacks.

.. _`of_mm_gpiochip_remove`:

of_mm_gpiochip_remove
=====================

.. c:function:: void of_mm_gpiochip_remove(struct of_mm_gpio_chip *mm_gc)

    Remove memory mapped GPIO chip (bank)

    :param mm_gc:
        pointer to the of_mm_gpio_chip allocated structure
    :type mm_gc: struct of_mm_gpio_chip \*

.. This file was automatic generated / don't edit.

