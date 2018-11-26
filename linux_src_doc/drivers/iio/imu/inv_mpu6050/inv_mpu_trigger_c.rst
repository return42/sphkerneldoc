.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/imu/inv_mpu6050/inv_mpu_trigger.c

.. _`inv_mpu6050_set_enable`:

inv_mpu6050_set_enable
======================

.. c:function:: int inv_mpu6050_set_enable(struct iio_dev *indio_dev, bool enable)

    enable chip functions.

    :param indio_dev:
        Device driver instance.
    :type indio_dev: struct iio_dev \*

    :param enable:
        enable/disable
    :type enable: bool

.. _`inv_mpu_data_rdy_trigger_set_state`:

inv_mpu_data_rdy_trigger_set_state
==================================

.. c:function:: int inv_mpu_data_rdy_trigger_set_state(struct iio_trigger *trig, bool state)

    set data ready interrupt state

    :param trig:
        Trigger instance
    :type trig: struct iio_trigger \*

    :param state:
        Desired trigger state
    :type state: bool

.. This file was automatic generated / don't edit.

