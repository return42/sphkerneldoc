.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/gpio_mouse.h

.. _`gpio_mouse_platform_data`:

struct gpio_mouse_platform_data
===============================

.. c:type:: struct gpio_mouse_platform_data


.. _`gpio_mouse_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct gpio_mouse_platform_data {
        int scan_ms;
        int polarity;
        union {
            struct {
                int up;
                int down;
                int left;
                int right;
                int bleft;
                int bmiddle;
                int bright;
            } ;
            int pins[GPIO_MOUSE_PIN_MAX];
        } ;
    }

.. _`gpio_mouse_platform_data.members`:

Members
-------

scan_ms
    integer in ms specifying the scan periode.

polarity
    Pin polarity, active high or low.

struct
    *undescribed*

pins
    *undescribed*

}
    *undescribed*

.. _`gpio_mouse_platform_data.description`:

Description
-----------

This struct must be added to the platform_device in the board code.
It is used by the gpio_mouse driver to setup GPIO lines and to
calculate mouse movement.

.. This file was automatic generated / don't edit.

