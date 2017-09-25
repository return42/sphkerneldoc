.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/imu/st_lsm6dsx/st_lsm6dsx.h

.. _`st_lsm6dsx_sensor`:

struct st_lsm6dsx_sensor
========================

.. c:type:: struct st_lsm6dsx_sensor

    ST IMU sensor instance

.. _`st_lsm6dsx_sensor.definition`:

Definition
----------

.. code-block:: c

    struct st_lsm6dsx_sensor {
        char name[32];
        enum st_lsm6dsx_sensor_id id;
        struct st_lsm6dsx_hw *hw;
        u32 gain;
        u16 odr;
        u16 watermark;
        u8 sip;
        u8 decimator;
        u8 decimator_mask;
        s64 delta_ts;
        s64 ts;
    }

.. _`st_lsm6dsx_sensor.members`:

Members
-------

name
    Sensor name.

id
    Sensor identifier.

hw
    Pointer to instance of struct st_lsm6dsx_hw.

gain
    Configured sensor sensitivity.

odr
    Output data rate of the sensor [Hz].

watermark
    Sensor watermark level.

sip
    Number of samples in a given pattern.

decimator
    FIFO decimation factor.

decimator_mask
    Sensor mask for decimation register.

delta_ts
    Delta time between two consecutive interrupts.

ts
    Latest timestamp from the interrupt handler.

.. _`st_lsm6dsx_hw`:

struct st_lsm6dsx_hw
====================

.. c:type:: struct st_lsm6dsx_hw

    ST IMU MEMS hw instance

.. _`st_lsm6dsx_hw.definition`:

Definition
----------

.. code-block:: c

    struct st_lsm6dsx_hw {
        struct device *dev;
        int irq;
        struct mutex lock;
        struct mutex fifo_lock;
        enum st_lsm6dsx_fifo_mode fifo_mode;
        u8 enable_mask;
        u8 sip;
        struct iio_dev *iio_devs[ST_LSM6DSX_ID_MAX];
        const struct st_lsm6dsx_settings *settings;
        const struct st_lsm6dsx_transfer_function *tf;
    #if defined(CONFIG_SPI_MASTER)
        struct st_lsm6dsx_transfer_buffer tb;
    #endif 
    }

.. _`st_lsm6dsx_hw.members`:

Members
-------

dev
    Pointer to instance of struct device (I2C or SPI).

irq
    Device interrupt line (I2C or SPI).

lock
    Mutex to protect read and write operations.

fifo_lock
    Mutex to prevent concurrent access to the hw FIFO.

fifo_mode
    FIFO operating mode supported by the device.

enable_mask
    Enabled sensor bitmask.

sip
    Total number of samples (acc/gyro) in a given pattern.

iio_devs
    Pointers to acc/gyro iio_dev instances.

settings
    Pointer to the specific sensor settings in use.

tf
    Transfer function structure used by I/O operations.

tb
    Transfer buffers used by SPI I/O operations.

.. This file was automatic generated / don't edit.

