.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/lp855x.h

.. _`lp855x_platform_data`:

struct lp855x_platform_data
===========================

.. c:type:: struct lp855x_platform_data


.. _`lp855x_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct lp855x_platform_data {
        const char *name;
        u8 device_control;
        u8 initial_brightness;
        unsigned int period_ns;
        int size_program;
        struct lp855x_rom_data *rom_data;
    }

.. _`lp855x_platform_data.members`:

Members
-------

name
    Backlight driver name. If it is not defined, default name is set.

device_control
    value of DEVICE CONTROL register

initial_brightness
    initial value of backlight brightness

period_ns
    platform specific pwm period value. unit is nano.

size_program
    total size of lp855x_rom_data

rom_data
    list of new eeprom/eprom registers

.. This file was automatic generated / don't edit.

