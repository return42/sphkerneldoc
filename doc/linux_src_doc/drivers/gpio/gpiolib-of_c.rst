.. -*- coding: utf-8; mode: rst -*-

============
gpiolib-of.c
============


.. _`of_get_named_gpiod_flags`:

of_get_named_gpiod_flags
========================

.. c:function:: struct gpio_desc *of_get_named_gpiod_flags (struct device_node *np, const char *propname, int index, enum of_gpio_flags *flags)

    Get a GPIO descriptor and flags for GPIO API

    :param struct device_node \*np:
        device node to get GPIO from

    :param const char \*propname:
        property name containing gpio specifier(s)

    :param int index:
        index of the GPIO

    :param enum of_gpio_flags \*flags:
        a flags pointer to fill in



.. _`of_get_named_gpiod_flags.description`:

Description
-----------

Returns GPIO descriptor to use with Linux GPIO API, or one of the errno
value on the error condition. If ``flags`` is not NULL the function also fills
in flags for the GPIO.



.. _`of_parse_own_gpio`:

of_parse_own_gpio
=================

.. c:function:: struct gpio_desc *of_parse_own_gpio (struct device_node *np, const char **name, enum gpio_lookup_flags *lflags, enum gpiod_flags *dflags)

    Get a GPIO hog descriptor, names and flags for GPIO API

    :param struct device_node \*np:
        device node to get GPIO from

    :param const char \*\*name:
        GPIO line name

    :param enum gpio_lookup_flags \*lflags:
        gpio_lookup_flags - returned from :c:func:`of_find_gpio` or
        :c:func:`of_parse_own_gpio`

    :param enum gpiod_flags \*dflags:
        gpiod_flags - optional GPIO initialization flags



.. _`of_parse_own_gpio.description`:

Description
-----------

Returns GPIO descriptor to use with Linux GPIO API, or one of the errno
value on the error condition.



.. _`of_gpiochip_scan_gpios`:

of_gpiochip_scan_gpios
======================

.. c:function:: void of_gpiochip_scan_gpios (struct gpio_chip *chip)

    Scan gpio-controller for gpio definitions

    :param struct gpio_chip \*chip:
        gpio chip to act on



.. _`of_gpiochip_scan_gpios.description`:

Description
-----------

This is only used by of_gpiochip_add to request/set GPIO initial
configuration.



.. _`of_gpio_simple_xlate`:

of_gpio_simple_xlate
====================

.. c:function:: int of_gpio_simple_xlate (struct gpio_chip *gc, const struct of_phandle_args *gpiospec, u32 *flags)

    translate gpio_spec to the GPIO number and flags

    :param struct gpio_chip \*gc:
        pointer to the gpio_chip structure

    :param const struct of_phandle_args \*gpiospec:

        *undescribed*

    :param u32 \*flags:
        a flags pointer to fill in



.. _`of_gpio_simple_xlate.description`:

Description
-----------

This is simple translation function, suitable for the most 1:1 mapped
gpio chips. This function performs only one sanity check: whether gpio
is less than ngpios (that is specified in the gpio_chip).



.. _`of_mm_gpiochip_add_data`:

of_mm_gpiochip_add_data
=======================

.. c:function:: int of_mm_gpiochip_add_data (struct device_node *np, struct of_mm_gpio_chip *mm_gc, void *data)

    Add memory mapped GPIO chip (bank)

    :param struct device_node \*np:
        device node of the GPIO chip

    :param struct of_mm_gpio_chip \*mm_gc:
        pointer to the of_mm_gpio_chip allocated structure

    :param void \*data:
        driver data to store in the struct gpio_chip



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

.. c:function:: void of_mm_gpiochip_remove (struct of_mm_gpio_chip *mm_gc)

    Remove memory mapped GPIO chip (bank)

    :param struct of_mm_gpio_chip \*mm_gc:
        pointer to the of_mm_gpio_chip allocated structure

