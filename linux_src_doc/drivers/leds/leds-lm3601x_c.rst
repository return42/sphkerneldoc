.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/leds/leds-lm3601x.c

.. _`lm3601x_led`:

struct lm3601x_led
==================

.. c:type:: struct lm3601x_led


.. _`lm3601x_led.definition`:

Definition
----------

.. code-block:: c

    struct lm3601x_led {
        struct led_classdev_flash fled_cdev;
        struct i2c_client *client;
        struct regmap *regmap;
        struct mutex lock;
        char led_name[LED_MAX_NAME_SIZE];
        unsigned int flash_timeout;
        unsigned int last_flag;
        u32 torch_current_max;
        u32 flash_current_max;
        u32 max_flash_timeout;
        u32 led_mode;
    }

.. _`lm3601x_led.members`:

Members
-------

fled_cdev
    flash LED class device pointer

client
    Pointer to the I2C client

regmap
    Devices register map

lock
    Lock for reading/writing the device

led_name
    LED label for the Torch or IR LED

flash_timeout
    the timeout for the flash

last_flag
    last known flags register value

torch_current_max
    maximum current for the torch

flash_current_max
    maximum current for the flash

max_flash_timeout
    maximum timeout for the flash

led_mode
    The mode to enable either IR or Torch

.. This file was automatic generated / don't edit.

