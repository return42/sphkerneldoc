.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/leds/leds-lp3944.c

.. _`lp3944_dim_set_period`:

lp3944_dim_set_period
=====================

.. c:function:: int lp3944_dim_set_period(struct i2c_client *client, u8 dim, u16 period)

    :param client:
        the i2c client
    :type client: struct i2c_client \*

    :param dim:
        either LP3944_DIM0 or LP3944_DIM1
    :type dim: u8

    :param period:
        period of a blink, that is a on/off cycle, expressed in ms.
    :type period: u16

.. _`lp3944_dim_set_dutycycle`:

lp3944_dim_set_dutycycle
========================

.. c:function:: int lp3944_dim_set_dutycycle(struct i2c_client *client, u8 dim, u8 duty_cycle)

    :param client:
        the i2c client
    :type client: struct i2c_client \*

    :param dim:
        either LP3944_DIM0 or LP3944_DIM1
    :type dim: u8

    :param duty_cycle:
        percentage of a period during which a led is ON
    :type duty_cycle: u8

.. _`lp3944_led_set`:

lp3944_led_set
==============

.. c:function:: int lp3944_led_set(struct lp3944_led_data *led, u8 status)

    :param led:
        a lp3944_led_data structure
    :type led: struct lp3944_led_data \*

    :param status:
        one of LP3944_LED_STATUS_OFF
        LP3944_LED_STATUS_ON
        LP3944_LED_STATUS_DIM0
        LP3944_LED_STATUS_DIM1
    :type status: u8

.. This file was automatic generated / don't edit.

