.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/imu/inv_mpu6050/inv_mpu_core.c

.. _`inv_mpu6050_set_lpf_regs`:

inv_mpu6050_set_lpf_regs
========================

.. c:function:: int inv_mpu6050_set_lpf_regs(struct inv_mpu6050_state *st, enum inv_mpu6050_filter_e val)

    set low pass filter registers, chip dependent

    :param st:
        *undescribed*
    :type st: struct inv_mpu6050_state \*

    :param val:
        *undescribed*
    :type val: enum inv_mpu6050_filter_e

.. _`inv_mpu6050_set_lpf_regs.description`:

Description
-----------

MPU60xx/MPU9150 use only 1 register for accelerometer + gyroscope
MPU6500 and above have a dedicated register for accelerometer

.. _`inv_mpu6050_init_config`:

inv_mpu6050_init_config
=======================

.. c:function:: int inv_mpu6050_init_config(struct iio_dev *indio_dev)

    Initialize hardware, disable FIFO.

    :param indio_dev:
        *undescribed*
    :type indio_dev: struct iio_dev \*

.. _`inv_mpu6050_init_config.fsr`:

FSR
---

± 2000DPS

.. _`inv_mpu6050_init_config.dlpf`:

DLPF
----

20Hz

.. _`inv_mpu6050_init_config.fifo-rate`:

FIFO rate
---------

50Hz

.. _`inv_mpu6050_init_config.clock-source`:

Clock source
------------

Gyro PLL

.. _`inv_mpu6050_set_lpf`:

inv_mpu6050_set_lpf
===================

.. c:function:: int inv_mpu6050_set_lpf(struct inv_mpu6050_state *st, int rate)

    set low pass filer based on fifo rate.

    :param st:
        *undescribed*
    :type st: struct inv_mpu6050_state \*

    :param rate:
        *undescribed*
    :type rate: int

.. _`inv_mpu6050_set_lpf.description`:

Description
-----------

Based on the Nyquist principle, the sampling rate must
exceed twice of the bandwidth of the signal, or there
would be alising. This function basically search for the
correct low pass parameters based on the fifo rate, e.g,
sampling frequency.

lpf is set automatically when setting sampling rate to avoid any aliases.

.. _`inv_mpu6050_fifo_rate_store`:

inv_mpu6050_fifo_rate_store
===========================

.. c:function:: ssize_t inv_mpu6050_fifo_rate_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Set fifo rate.

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        *undescribed*
    :type buf: const char \*

    :param count:
        *undescribed*
    :type count: size_t

.. _`inv_fifo_rate_show`:

inv_fifo_rate_show
==================

.. c:function:: ssize_t inv_fifo_rate_show(struct device *dev, struct device_attribute *attr, char *buf)

    Get the current sampling rate.

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        *undescribed*
    :type buf: char \*

.. _`inv_attr_show`:

inv_attr_show
=============

.. c:function:: ssize_t inv_attr_show(struct device *dev, struct device_attribute *attr, char *buf)

    calling this function will show current parameters.

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        *undescribed*
    :type buf: char \*

.. _`inv_attr_show.description`:

Description
-----------

Deprecated in favor of IIO mounting matrix API.

See \ :c:func:`inv_get_mount_matrix`\ 

.. _`inv_mpu6050_validate_trigger`:

inv_mpu6050_validate_trigger
============================

.. c:function:: int inv_mpu6050_validate_trigger(struct iio_dev *indio_dev, struct iio_trigger *trig)

    validate_trigger callback for invensense MPU6050 device.

    :param indio_dev:
        The IIO device
    :type indio_dev: struct iio_dev \*

    :param trig:
        The new trigger
    :type trig: struct iio_trigger \*

.. _`inv_mpu6050_validate_trigger.return`:

Return
------

0 if the 'trig' matches the trigger registered by the MPU6050
device, -EINVAL otherwise.

.. _`inv_check_and_setup_chip`:

inv_check_and_setup_chip
========================

.. c:function:: int inv_check_and_setup_chip(struct inv_mpu6050_state *st)

    check and setup chip.

    :param st:
        *undescribed*
    :type st: struct inv_mpu6050_state \*

.. This file was automatic generated / don't edit.

