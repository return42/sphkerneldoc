.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/imu/inv_mpu6050/inv_mpu_iio.h

.. _`inv_mpu6050_reg_map`:

struct inv_mpu6050_reg_map
==========================

.. c:type:: struct inv_mpu6050_reg_map

    Notable registers.

.. _`inv_mpu6050_reg_map.definition`:

Definition
----------

.. code-block:: c

    struct inv_mpu6050_reg_map {
        u8 sample_rate_div;
        u8 lpf;
        u8 accel_lpf;
        u8 user_ctrl;
        u8 fifo_en;
        u8 gyro_config;
        u8 accl_config;
        u8 fifo_count_h;
        u8 fifo_r_w;
        u8 raw_gyro;
        u8 raw_accl;
        u8 temperature;
        u8 int_enable;
        u8 pwr_mgmt_1;
        u8 pwr_mgmt_2;
        u8 int_pin_cfg;
        u8 accl_offset;
        u8 gyro_offset;
    }

.. _`inv_mpu6050_reg_map.members`:

Members
-------

sample_rate_div
    Divider applied to gyro output rate.

lpf
    Configures internal low pass filter.

accel_lpf
    Configures accelerometer low pass filter.

user_ctrl
    Enables/resets the FIFO.

fifo_en
    Determines which data will appear in FIFO.

gyro_config
    gyro config register.

accl_config
    accel config register

fifo_count_h
    Upper byte of FIFO count.

fifo_r_w
    FIFO register.

raw_gyro
    Address of first gyro register.

raw_accl
    Address of first accel register.

temperature
    temperature register

int_enable
    Interrupt enable register.

pwr_mgmt_1
    Controls chip's power state and clock source.

pwr_mgmt_2
    Controls power state of individual sensors.
    \ ``int_pin_cfg``\ ;       Controls interrupt pin configuration.

int_pin_cfg
    *undescribed*

accl_offset
    Controls the accelerometer calibration offset.

gyro_offset
    Controls the gyroscope calibration offset.

.. _`inv_mpu6050_chip_config`:

struct inv_mpu6050_chip_config
==============================

.. c:type:: struct inv_mpu6050_chip_config

    Cached chip configuration data.

.. _`inv_mpu6050_chip_config.definition`:

Definition
----------

.. code-block:: c

    struct inv_mpu6050_chip_config {
        unsigned int fsr:2;
        unsigned int lpf:3;
        unsigned int accl_fs:2;
        unsigned int accl_fifo_enable:1;
        unsigned int gyro_fifo_enable:1;
        u16 fifo_rate;
    }

.. _`inv_mpu6050_chip_config.members`:

Members
-------

fsr
    Full scale range.

lpf
    Digital low pass filter frequency.

accl_fs
    accel full scale range.

accl_fifo_enable
    enable accel data output

gyro_fifo_enable
    enable gyro data output

fifo_rate
    FIFO update rate.

.. _`inv_mpu6050_hw`:

struct inv_mpu6050_hw
=====================

.. c:type:: struct inv_mpu6050_hw

    Other important hardware information.

.. _`inv_mpu6050_hw.definition`:

Definition
----------

.. code-block:: c

    struct inv_mpu6050_hw {
        u8 whoami;
        u8 *name;
        const struct inv_mpu6050_reg_map *reg;
        const struct inv_mpu6050_chip_config *config;
    }

.. _`inv_mpu6050_hw.members`:

Members
-------

whoami
    Self identification byte from WHO_AM_I register

name
    name of the chip.

reg
    register map of the chip.

config
    configuration of the chip.

.. This file was automatic generated / don't edit.

