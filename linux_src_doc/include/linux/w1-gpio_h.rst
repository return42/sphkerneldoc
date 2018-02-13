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
        struct gpio_desc *gpiod;
        struct gpio_desc *pullup_gpiod;
        void (*enable_external_pullup)(int enable);
        unsigned int pullup_duration;
    }

.. _`w1_gpio_platform_data.members`:

Members
-------

gpiod
    *undescribed*

pullup_gpiod
    *undescribed*

enable_external_pullup
    *undescribed*

pullup_duration
    *undescribed*

.. This file was automatic generated / don't edit.

