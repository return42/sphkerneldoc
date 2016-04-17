.. -*- coding: utf-8; mode: rst -*-

=========
w1-gpio.h
=========


.. _`w1_gpio_platform_data`:

struct w1_gpio_platform_data
============================

.. c:type:: w1_gpio_platform_data

    Platform-dependent data for w1-gpio


.. _`w1_gpio_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct w1_gpio_platform_data {
    unsigned int pin;
    unsigned int is_open_drain:1;
  };


.. _`w1_gpio_platform_data.members`:

Members
-------

:``pin``:
    GPIO pin to use

:``is_open_drain``:
    GPIO pin is configured as open drain


