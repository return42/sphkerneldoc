.. -*- coding: utf-8; mode: rst -*-

========
s5k6a3.c
========



.. _xref_struct_s5k6a3:

struct s5k6a3
=============

.. c:type:: struct s5k6a3

    fimc-is sensor data structure



Definition
----------

.. code-block:: c

  struct s5k6a3 {
    struct device * dev;
    struct v4l2_subdev subdev;
    struct media_pad pad;
    struct regulator_bulk_data supplies[S5K6A3_NUM_SUPPLIES];
    int gpio_reset;
    struct mutex lock;
    struct v4l2_mbus_framefmt format;
  };



Members
-------

:``struct device * dev``:
    pointer to this I2C client device structure

:``struct v4l2_subdev subdev``:
    the image sensor's v4l2 subdev

:``struct media_pad pad``:
    subdev media source pad

:``struct regulator_bulk_data supplies[S5K6A3_NUM_SUPPLIES]``:
    image sensor's voltage regulator supplies

:``int gpio_reset``:
    GPIO connected to the sensor's reset pin

:``struct mutex lock``:
    mutex protecting the structure's members below

:``struct v4l2_mbus_framefmt format``:
    media bus format at the sensor's source pad



