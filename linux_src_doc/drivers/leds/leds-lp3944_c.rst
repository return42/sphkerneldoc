.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/leds/leds-lp3944.c

.. _`lp3944_dim_set_period`:

lp3944_dim_set_period
=====================

.. c:function:: int lp3944_dim_set_period(struct i2c_client *client, u8 dim, u16 period)

    :param struct i2c_client \*client:
        the i2c client

    :param u8 dim:
        either LP3944_DIM0 or LP3944_DIM1

    :param u16 period:
        period of a blink, that is a on/off cycle, expressed in ms.

.. _`lp3944_dim_set_dutycycle`:

lp3944_dim_set_dutycycle
========================

.. c:function:: int lp3944_dim_set_dutycycle(struct i2c_client *client, u8 dim, u8 duty_cycle)

    :param struct i2c_client \*client:
        the i2c client

    :param u8 dim:
        either LP3944_DIM0 or LP3944_DIM1

    :param u8 duty_cycle:
        percentage of a period during which a led is ON

.. _`lp3944_led_set`:

lp3944_led_set
==============

.. c:function:: int lp3944_led_set(struct lp3944_led_data *led, u8 status)

    :param struct lp3944_led_data \*led:
        a lp3944_led_data structure

    :param u8 status:
        one of LP3944_LED_STATUS_OFF
        LP3944_LED_STATUS_ON
        LP3944_LED_STATUS_DIM0
        LP3944_LED_STATUS_DIM1

.. This file was automatic generated / don't edit.

