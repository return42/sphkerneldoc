.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/leds/leds-lp8860.c

.. _`lp8860_led`:

struct lp8860_led
=================

.. c:type:: struct lp8860_led

    @lock - Lock for reading/writing the device \ ``client``\  - Pointer to the I2C client \ ``led_dev``\  - led class device pointer \ ``regmap``\  - Devices register map \ ``eeprom_regmap``\  - EEPROM register map \ ``enable_gpio``\  - VDDIO/EN gpio to enable communication interface \ ``regulator``\  - LED supply regulator pointer \ ``label``\  - LED label

.. _`lp8860_led.definition`:

Definition
----------

.. code-block:: c

    struct lp8860_led {
        struct mutex lock;
        struct i2c_client *client;
        struct led_classdev led_dev;
        struct regmap *regmap;
        struct regmap *eeprom_regmap;
        struct gpio_desc *enable_gpio;
        struct regulator *regulator;
        const char *label;
    }

.. _`lp8860_led.members`:

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

eeprom_regmap
    *undescribed*

enable_gpio
    *undescribed*

regulator
    *undescribed*

label
    *undescribed*

.. This file was automatic generated / don't edit.

