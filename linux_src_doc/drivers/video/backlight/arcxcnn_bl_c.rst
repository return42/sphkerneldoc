.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/backlight/arcxcnn_bl.c

.. _`arcxcnn_platform_data`:

struct arcxcnn_platform_data
============================

.. c:type:: struct arcxcnn_platform_data


.. _`arcxcnn_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct arcxcnn_platform_data {
        const char *name;
        u16 initial_brightness;
        u8 leden;
        u8 led_config_0;
        u8 led_config_1;
        u8 dim_freq;
        u8 comp_config;
        u8 filter_config;
        u8 trim_config;
    }

.. _`arcxcnn_platform_data.members`:

Members
-------

name
    Backlight driver name (NULL will use default)

initial_brightness
    initial value of backlight brightness

leden
    initial LED string enables, upper bit is global on/off

led_config_0
    fading speed (period between intensity steps)

led_config_1
    misc settings, see datasheet

dim_freq
    pwm dimming frequency if in pwm mode

comp_config
    misc config, see datasheet

filter_config
    RC/PWM filter config, see datasheet

trim_config
    full scale current trim, see datasheet

.. This file was automatic generated / don't edit.

