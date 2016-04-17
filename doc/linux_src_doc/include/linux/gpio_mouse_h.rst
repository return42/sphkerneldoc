.. -*- coding: utf-8; mode: rst -*-

============
gpio_mouse.h
============


.. _`gpio_mouse_platform_data`:

struct gpio_mouse_platform_data
===============================

.. c:type:: gpio_mouse_platform_data

    


.. _`gpio_mouse_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct gpio_mouse_platform_data {
    int scan_ms;
    int polarity;
    union {unnamed_union};
  };


.. _`gpio_mouse_platform_data.members`:

Members
-------

:``scan_ms``:
    integer in ms specifying the scan periode.

:``polarity``:
    Pin polarity, active high or low.

:``{unnamed_union}``:
    anonymous




.. _`gpio_mouse_platform_data.description`:

Description
-----------

This struct must be added to the platform_device in the board code.
It is used by the gpio_mouse driver to setup GPIO lines and to
calculate mouse movement.

