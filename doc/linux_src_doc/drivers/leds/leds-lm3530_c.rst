.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/leds/leds-lm3530.c

.. _`lm3530_data`:

struct lm3530_data
==================

.. c:type:: struct lm3530_data


.. _`lm3530_data.definition`:

Definition
----------

.. code-block:: c

    struct lm3530_data {
        struct led_classdev led_dev;
        struct i2c_client *client;
        struct lm3530_platform_data *pdata;
        enum lm3530_mode mode;
        struct regulator *regulator;
        enum led_brightness brightness;
        bool enable;
    }

.. _`lm3530_data.members`:

Members
-------

led_dev
    led class device

client
    i2c client

pdata
    LM3530 platform data

mode
    mode of operation - manual, ALS, PWM

regulator
    regulator

brightness
    *undescribed*

enable
    regulator is enabled

.. This file was automatic generated / don't edit.

