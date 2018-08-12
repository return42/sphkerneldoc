.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/gpio/machine.h

.. _`gpiod_lookup`:

struct gpiod_lookup
===================

.. c:type:: struct gpiod_lookup

    lookup table

.. _`gpiod_lookup.definition`:

Definition
----------

.. code-block:: c

    struct gpiod_lookup {
        const char *chip_label;
        u16 chip_hwnum;
        const char *con_id;
        unsigned int idx;
        enum gpio_lookup_flags flags;
    }

.. _`gpiod_lookup.members`:

Members
-------

chip_label
    name of the chip the GPIO belongs to

chip_hwnum
    hardware number (i.e. relative to the chip) of the GPIO

con_id
    name of the GPIO from the device's point of view

idx
    index of the GPIO in case several GPIOs share the same name

flags
    mask of GPIO\_\* values

.. _`gpiod_lookup.description`:

Description
-----------

gpiod_lookup is a lookup table for associating GPIOs to specific devices and
functions using platform data.

.. _`gpiod_hog`:

struct gpiod_hog
================

.. c:type:: struct gpiod_hog

    GPIO line hog table

.. _`gpiod_hog.definition`:

Definition
----------

.. code-block:: c

    struct gpiod_hog {
        struct list_head list;
        const char *chip_label;
        u16 chip_hwnum;
        const char *line_name;
        enum gpio_lookup_flags lflags;
        int dflags;
    }

.. _`gpiod_hog.members`:

Members
-------

list
    *undescribed*

chip_label
    name of the chip the GPIO belongs to

chip_hwnum
    hardware number (i.e. relative to the chip) of the GPIO

line_name
    consumer name for the hogged line

lflags
    mask of GPIO lookup flags

dflags
    GPIO flags used to specify the direction and value

.. This file was automatic generated / don't edit.

