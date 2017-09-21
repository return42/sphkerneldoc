.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpiolib-legacy.c

.. _`gpio_request_one`:

gpio_request_one
================

.. c:function:: int gpio_request_one(unsigned gpio, unsigned long flags, const char *label)

    request a single GPIO with initial configuration

    :param unsigned gpio:
        the GPIO number

    :param unsigned long flags:
        GPIO configuration as specified by GPIOF_*

    :param const char \*label:
        a literal description string of this GPIO

.. _`gpio_request_array`:

gpio_request_array
==================

.. c:function:: int gpio_request_array(const struct gpio *array, size_t num)

    request multiple GPIOs in a single call

    :param const struct gpio \*array:
        array of the 'struct gpio'

    :param size_t num:
        how many GPIOs in the array

.. _`gpio_free_array`:

gpio_free_array
===============

.. c:function:: void gpio_free_array(const struct gpio *array, size_t num)

    release multiple GPIOs in a single call

    :param const struct gpio \*array:
        array of the 'struct gpio'

    :param size_t num:
        how many GPIOs in the array

.. This file was automatic generated / don't edit.

