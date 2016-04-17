.. -*- coding: utf-8; mode: rst -*-

=========
machine.h
=========


.. _`gpiod_lookup`:

struct gpiod_lookup
===================

.. c:type:: gpiod_lookup

    lookup table


.. _`gpiod_lookup.definition`:

Definition
----------

.. code-block:: c

  struct gpiod_lookup {
    const char * chip_label;
    u16 chip_hwnum;
    const char * con_id;
    unsigned int idx;
    enum gpio_lookup_flags flags;
  };


.. _`gpiod_lookup.members`:

Members
-------

:``chip_label``:
    name of the chip the GPIO belongs to

:``chip_hwnum``:
    hardware number (i.e. relative to the chip) of the GPIO

:``con_id``:
    name of the GPIO from the device's point of view

:``idx``:
    index of the GPIO in case several GPIOs share the same name

:``flags``:
    mask of GPIO\_\* values




.. _`gpiod_lookup.description`:

Description
-----------

gpiod_lookup is a lookup table for associating GPIOs to specific devices and
functions using platform data.

