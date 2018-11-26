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
        int (*read_fifo)(struct st_lsm6dsx_hw *hw);
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

read_fifo
    Read FIFO callback.

fifo_th
    FIFO threshold register info (addr + mask).

fifo_diff
    FIFO diff status register info (addr + mask).

th_wl
    FIFO threshold word length.

.. _`st_lsm6dsx_hw_ts_settings`:

struct st_lsm6dsx_hw_ts_settings
================================

.. c:type:: struct st_lsm6dsx_hw_ts_settings

    ST IMU hw timer settings

.. _`st_lsm6dsx_hw_ts_settings.definition`:

Definition
----------

.. code-block:: c

    struct st_lsm6dsx_hw_ts_settings {
        struct st_lsm6dsx_reg timer_en;
        struct st_lsm6dsx_reg hr_timer;
        struct st_lsm6dsx_reg fifo_en;
        struct st_lsm6dsx_reg decimator;
    }

.. _`st_lsm6dsx_hw_ts_settings.members`:

Members
-------

timer_en
    Hw timer enable register info (addr + mask).

hr_timer
    Hw timer resolution register info (addr + mask).

fifo_en
    Hw timer FIFO enable register info (addr + mask).

decimator
    Hw timer FIFO decimator register info (addr + mask).

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
        struct st_lsm6dsx_reg batch[ST_LSM6DSX_MAX_ID];
        struct st_lsm6dsx_fifo_ops fifo_ops;
        struct st_lsm6dsx_hw_ts_settings ts_settings;
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

batch
    List of FIFO batching register info (addr + mask).

fifo_ops
    Sensor hw FIFO parameters.

ts_settings
    Hw timer related settings.

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
        s64 ts_ref;
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

ts_ref
    Sensor timestamp reference for hw one.

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
        u8 ts_sip;
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

ts_sip
    Total number of timestamp samples in a given pattern.

sip
    Total number of samples (acc/gyro/ts) in a given pattern.

buff
    Device read buffer.

iio_devs
    Pointers to acc/gyro iio_dev instances.

settings
    Pointer to the specific sensor settings in use.

.. This file was automatic generated / don't edit.

