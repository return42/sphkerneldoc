.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpiolib-legacy.c

.. _`gpio_request_one`:

gpio_request_one
================

.. c:function:: int gpio_request_one(unsigned gpio, unsigned long flags, const char *label)

    request a single GPIO with initial configuration

    :param gpio:
        the GPIO number
    :type gpio: unsigned

    :param flags:
        GPIO configuration as specified by GPIOF_*
    :type flags: unsigned long

    :param label:
        a literal description string of this GPIO
    :type label: const char \*

.. _`gpio_request_array`:

gpio_request_array
==================

.. c:function:: int gpio_request_array(const struct gpio *array, size_t num)

    request multiple GPIOs in a single call

    :param array:
        array of the 'struct gpio'
    :type array: const struct gpio \*

    :param num:
        how many GPIOs in the array
    :type num: size_t

.. _`gpio_free_array`:

gpio_free_array
===============

.. c:function:: void gpio_free_array(const struct gpio *array, size_t num)

    release multiple GPIOs in a single call

    :param array:
        array of the 'struct gpio'
    :type array: const struct gpio \*

    :param num:
        how many GPIOs in the array
    :type num: size_t

.. This file was automatic generated / don't edit.

