.. -*- coding: utf-8; mode: rst -*-

================
fimc-is-sensor.h
================



.. _xref_struct_fimc_is_sensor:

struct fimc_is_sensor
=====================

.. c:type:: struct fimc_is_sensor

    fimc-is sensor data structure



Definition
----------

.. code-block:: c

  struct fimc_is_sensor {
    const struct sensor_drv_data * drvdata;
    unsigned int i2c_bus;
    u8 test_pattern;
  };



Members
-------

:``const struct sensor_drv_data * drvdata``:
    a pointer to the sensor's parameters data structure

:``unsigned int i2c_bus``:
    ISP I2C bus index (0...1)

:``u8 test_pattern``:
    true to enable video test pattern



