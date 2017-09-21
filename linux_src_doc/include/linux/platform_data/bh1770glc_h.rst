.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/bh1770glc.h

.. _`bh1770_platform_data`:

struct bh1770_platform_data
===========================

.. c:type:: struct bh1770_platform_data

    platform data for bh1770glc driver

.. _`bh1770_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct bh1770_platform_data {
    #define BH1770_LED_5mA 0
    #define BH1770_LED_10mA 1
    #define BH1770_LED_20mA 2
    #define BH1770_LED_50mA 3
    #define BH1770_LED_100mA 4
    #define BH1770_LED_150mA 5
    #define BH1770_LED_200mA 6
        __u8 led_def_curr;
    #define BH1770_NEUTRAL_GA 16384
        __u32 glass_attenuation;
        int (*setup_resources)(void);
        int (*release_resources)(void);
    }

.. _`bh1770_platform_data.members`:

Members
-------

led_def_curr
    IR led driving current.

glass_attenuation
    Attenuation factor for covering window.

setup_resources
    Call back for interrupt line setup function

release_resources
    Call back for interrupte line release function

.. _`bh1770_platform_data.example-of-glass-attenuation`:

Example of glass attenuation
----------------------------

16384 \* 385 / 100 means attenuation factor
of 3.85. i.e. light_above_sensor = light_above_cover_window / 3.85

.. This file was automatic generated / don't edit.

