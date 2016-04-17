.. -*- coding: utf-8; mode: rst -*-

==================
st_sensors_pdata.h
==================


.. _`st_sensors_platform_data`:

struct st_sensors_platform_data
===============================

.. c:type:: st_sensors_platform_data

    Platform data for the ST sensors


.. _`st_sensors_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct st_sensors_platform_data {
    u8 drdy_int_pin;
  };


.. _`st_sensors_platform_data.members`:

Members
-------

:``drdy_int_pin``:
    Redirect DRDY on pin 1 (1) or pin 2 (2).
    Available only for accelerometer and pressure sensors.
    Accelerometer DRDY on LSM330 available only on pin 1 (see datasheet).


