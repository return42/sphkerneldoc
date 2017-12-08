.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/mouse/gpio_mouse.c

.. _`gpio_mouse`:

struct gpio_mouse
=================

.. c:type:: struct gpio_mouse


.. _`gpio_mouse.definition`:

Definition
----------

.. code-block:: c

    struct gpio_mouse {
        u32 scan_ms;
        struct gpio_desc *up;
        struct gpio_desc *down;
        struct gpio_desc *left;
        struct gpio_desc *right;
        struct gpio_desc *bleft;
        struct gpio_desc *bmiddle;
        struct gpio_desc *bright;
    }

.. _`gpio_mouse.members`:

Members
-------

scan_ms
    the scan interval in milliseconds.

up
    GPIO line for up value.

down
    GPIO line for down value.

left
    GPIO line for left value.

right
    GPIO line for right value.

bleft
    GPIO line for left button.

bmiddle
    GPIO line for middle button.

bright
    GPIO line for right button.

.. _`gpio_mouse.description`:

Description
-----------

This struct must be added to the platform_device in the board code.
It is used by the gpio_mouse driver to setup GPIO lines and to
calculate mouse movement.

.. This file was automatic generated / don't edit.

