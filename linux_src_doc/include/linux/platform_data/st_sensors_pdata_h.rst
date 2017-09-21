.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/st_sensors_pdata.h

.. _`st_sensors_platform_data`:

struct st_sensors_platform_data
===============================

.. c:type:: struct st_sensors_platform_data

    Platform data for the ST sensors

.. _`st_sensors_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct st_sensors_platform_data {
        u8 drdy_int_pin;
        bool open_drain;
        bool spi_3wire;
    }

.. _`st_sensors_platform_data.members`:

Members
-------

drdy_int_pin
    Redirect DRDY on pin 1 (1) or pin 2 (2).
    Available only for accelerometer and pressure sensors.
    Accelerometer DRDY on LSM330 available only on pin 1 (see datasheet).

open_drain
    set the interrupt line to be open drain if possible.

spi_3wire
    enable spi-3wire mode.

.. This file was automatic generated / don't edit.

