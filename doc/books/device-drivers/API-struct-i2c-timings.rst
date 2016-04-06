
.. _API-struct-i2c-timings:

==================
struct i2c_timings
==================

*man struct i2c_timings(9)*

*4.6.0-rc1*

I2C timing information


Synopsis
========

.. code-block:: c

    struct i2c_timings {
      u32 bus_freq_hz;
      u32 scl_rise_ns;
      u32 scl_fall_ns;
      u32 scl_int_delay_ns;
      u32 sda_fall_ns;
    };


Members
=======

bus_freq_hz
    the bus frequency in Hz

scl_rise_ns
    time SCL signal takes to rise in ns; t(r) in the I2C specification

scl_fall_ns
    time SCL signal takes to fall in ns; t(f) in the I2C specification

scl_int_delay_ns
    time IP core additionally needs to setup SCL in ns

sda_fall_ns
    time SDA signal takes to fall in ns; t(f) in the I2C specification
