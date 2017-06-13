.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/i2c/s5k6a3.c

.. _`s5k6a3`:

struct s5k6a3
=============

.. c:type:: struct s5k6a3

    fimc-is sensor data structure

.. _`s5k6a3.definition`:

Definition
----------

.. code-block:: c

    struct s5k6a3 {
        struct device *dev;
        struct v4l2_subdev subdev;
        struct media_pad pad;
        struct regulator_bulk_data supplies;
        int gpio_reset;
        struct mutex lock;
        struct v4l2_mbus_framefmt format;
        struct clk *clock;
        u32 clock_frequency;
        int power_count;
    }

.. _`s5k6a3.members`:

Members
-------

dev
    pointer to this I2C client device structure

subdev
    the image sensor's v4l2 subdev

pad
    subdev media source pad

supplies
    image sensor's voltage regulator supplies

gpio_reset
    GPIO connected to the sensor's reset pin

lock
    mutex protecting the structure's members below

format
    media bus format at the sensor's source pad

clock
    *undescribed*

clock_frequency
    *undescribed*

power_count
    *undescribed*

.. This file was automatic generated / don't edit.

