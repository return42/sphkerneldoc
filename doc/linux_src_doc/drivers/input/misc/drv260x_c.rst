.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/misc/drv260x.c

.. _`drv260x_data`:

struct drv260x_data
===================

.. c:type:: struct drv260x_data

    \ ``input_dev``\  - Pointer to the input device \ ``client``\  - Pointer to the I2C client \ ``regmap``\  - Register map of the device \ ``work``\  - Work item used to off load the enable/disable of the vibration \ ``enable_gpio``\  - Pointer to the gpio used for enable/disabling \ ``regulator``\  - Pointer to the regulator for the IC \ ``magnitude``\  - Magnitude of the vibration event \ ``mode``\  - The operating mode of the IC (LRA_NO_CAL, ERM or LRA) \ ``library``\  - The vibration library to be used \ ``rated_voltage``\  - The rated_voltage of the actuator \ ``overdriver_voltage``\  - The over drive voltage of the actuator

.. _`drv260x_data.definition`:

Definition
----------

.. code-block:: c

    struct drv260x_data {
        struct input_dev *input_dev;
        struct i2c_client *client;
        struct regmap *regmap;
        struct work_struct work;
        struct gpio_desc *enable_gpio;
        struct regulator *regulator;
        u32 magnitude;
        u32 mode;
        u32 library;
        int rated_voltage;
        int overdrive_voltage;
    }

.. _`drv260x_data.members`:

Members
-------

input_dev
    *undescribed*

client
    *undescribed*

regmap
    *undescribed*

work
    *undescribed*

enable_gpio
    *undescribed*

regulator
    *undescribed*

magnitude
    *undescribed*

mode
    *undescribed*

library
    *undescribed*

rated_voltage
    *undescribed*

overdrive_voltage
    *undescribed*

.. _`drv260x_calculate_voltage`:

drv260x_calculate_voltage
=========================

.. c:function:: int drv260x_calculate_voltage(unsigned int voltage)

    Calculated using the formula r = v \* 255 / 5.6 where r is what will be written to the register and v is the rated or overdriver voltage of the actuator

    :param unsigned int voltage:
        *undescribed*

.. This file was automatic generated / don't edit.

