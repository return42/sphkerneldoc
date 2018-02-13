.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/leds/leds-lm3692x.c

.. _`lm3692x_led`:

struct lm3692x_led
==================

.. c:type:: struct lm3692x_led

    @lock - Lock for reading/writing the device \ ``client``\  - Pointer to the I2C client \ ``led_dev``\  - LED class device pointer \ ``regmap``\  - Devices register map \ ``enable_gpio``\  - VDDIO/EN gpio to enable communication interface \ ``regulator``\  - LED supply regulator pointer \ ``label``\  - LED label

.. _`lm3692x_led.definition`:

Definition
----------

.. code-block:: c

    struct lm3692x_led {
        struct mutex lock;
        struct i2c_client *client;
        struct led_classdev led_dev;
        struct regmap *regmap;
        struct gpio_desc *enable_gpio;
        struct regulator *regulator;
        char label[LED_MAX_NAME_SIZE];
    }

.. _`lm3692x_led.members`:

Members
-------

lock
    *undescribed*

client
    *undescribed*

led_dev
    *undescribed*

regmap
    *undescribed*

enable_gpio
    *undescribed*

regulator
    *undescribed*

label
    *undescribed*

.. This file was automatic generated / don't edit.

