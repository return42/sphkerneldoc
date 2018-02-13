.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/imu/st_lsm6dsx/st_lsm6dsx.h

.. _`st_lsm6dsx_fifo_ops`:

struct st_lsm6dsx_fifo_ops
==========================

.. c:type:: struct st_lsm6dsx_fifo_ops

    ST IMU FIFO settings

.. _`st_lsm6dsx_fifo_ops.definition`:

Definition
----------

.. code-block:: c

    struct st_lsm6dsx_fifo_ops {
        struct {
            u8 addr;
            u16 mask;
        } fifo_th;
        struct {
            u8 addr;
            u16 mask;
        } fifo_diff;
        u8 th_wl;
    }

.. _`st_lsm6dsx_fifo_ops.members`:

Members
-------

fifo_th
    FIFO threshold register info (addr + mask).

fifo_diff
    FIFO diff status register info (addr + mask).

th_wl
    FIFO threshold word length.

.. _`st_lsm6dsx_settings`:

struct st_lsm6dsx_settings
==========================

.. c:type:: struct st_lsm6dsx_settings

    ST IMU sensor settings

.. _`st_lsm6dsx_settings.definition`:

Definition
----------

.. code-block:: c

    struct st_lsm6dsx_settings {
        u8 wai;
        u16 max_fifo_size;
        enum st_lsm6dsx_hw_id id[ST_LSM6DSX_MAX_ID];
        struct st_lsm6dsx_reg decimator[ST_LSM6DSX_MAX_ID];
        struct st_lsm6dsx_fifo_ops fifo_ops;
    }

.. _`st_lsm6dsx_settings.members`:

Members
-------

wai
    Sensor WhoAmI default value.

max_fifo_size
    Sensor max fifo length in FIFO words.

id
    List of hw id supported by the driver configuration.

decimator
    List of decimator register info (addr + mask).

fifo_ops
    Sensor hw FIFO parameters.

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
        struct regmap *regmap;
        int irq;
        struct mutex fifo_lock;
        struct mutex conf_lock;
        enum st_lsm6dsx_fifo_mode fifo_mode;
        u8 enable_mask;
        u8 sip;
        u8 *buff;
        struct iio_dev *iio_devs[ST_LSM6DSX_ID_MAX];
        const struct st_lsm6dsx_settings *settings;
    }

.. _`st_lsm6dsx_hw.members`:

Members
-------

dev
    Pointer to instance of struct device (I2C or SPI).

regmap
    Register map of the device.

irq
    Device interrupt line (I2C or SPI).

fifo_lock
    Mutex to prevent concurrent access to the hw FIFO.

conf_lock
    Mutex to prevent concurrent FIFO configuration update.

fifo_mode
    FIFO operating mode supported by the device.

enable_mask
    Enabled sensor bitmask.

sip
    Total number of samples (acc/gyro) in a given pattern.

buff
    Device read buffer.

iio_devs
    Pointers to acc/gyro iio_dev instances.

settings
    Pointer to the specific sensor settings in use.

.. This file was automatic generated / don't edit.

