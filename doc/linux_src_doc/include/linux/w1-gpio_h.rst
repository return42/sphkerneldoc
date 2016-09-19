.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/w1-gpio.h

.. _`w1_gpio_platform_data`:

struct w1_gpio_platform_data
============================

.. c:type:: struct w1_gpio_platform_data

    Platform-dependent data for w1-gpio

.. _`w1_gpio_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct w1_gpio_platform_data {
        unsigned int pin;
        unsigned int is_open_drain:1;
        void (*enable_external_pullup)(int enable);
        unsigned int ext_pullup_enable_pin;
        unsigned int pullup_duration;
    }

.. _`w1_gpio_platform_data.members`:

Members
-------

pin
    GPIO pin to use

is_open_drain
    GPIO pin is configured as open drain

enable_external_pullup
    *undescribed*

ext_pullup_enable_pin
    *undescribed*

pullup_duration
    *undescribed*

.. This file was automatic generated / don't edit.

