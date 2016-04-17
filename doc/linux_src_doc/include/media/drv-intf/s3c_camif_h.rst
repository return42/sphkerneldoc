.. -*- coding: utf-8; mode: rst -*-

===========
s3c_camif.h
===========


.. _`s3c_camif_sensor_info`:

struct s3c_camif_sensor_info
============================

.. c:type:: s3c_camif_sensor_info

    an image sensor description


.. _`s3c_camif_sensor_info.definition`:

Definition
----------

.. code-block:: c

  struct s3c_camif_sensor_info {
    struct i2c_board_info i2c_board_info;
    unsigned long clock_frequency;
    enum v4l2_mbus_type mbus_type;
    u16 i2c_bus_num;
    u16 flags;
    u8 use_field;
  };


.. _`s3c_camif_sensor_info.members`:

Members
-------

:``i2c_board_info``:
    pointer to an I2C sensor subdevice board info

:``clock_frequency``:
    frequency of the clock the host provides to a sensor

:``mbus_type``:
    media bus type

:``i2c_bus_num``:
    i2c control bus id the sensor is attached to

:``flags``:
    the parallel bus flags defining signals polarity (V4L2_MBUS\_\*)

:``use_field``:
    1 if parallel bus FIELD signal is used (only s3c64xx)


