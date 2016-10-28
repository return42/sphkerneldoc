.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/imu/inv_mpu6050/inv_mpu_trigger.c

.. _`inv_mpu6050_set_enable`:

inv_mpu6050_set_enable
======================

.. c:function:: int inv_mpu6050_set_enable(struct iio_dev *indio_dev, bool enable)

    enable chip functions.

    :param struct iio_dev \*indio_dev:
        Device driver instance.

    :param bool enable:
        enable/disable

.. _`inv_mpu_data_rdy_trigger_set_state`:

inv_mpu_data_rdy_trigger_set_state
==================================

.. c:function:: int inv_mpu_data_rdy_trigger_set_state(struct iio_trigger *trig, bool state)

    set data ready interrupt state

    :param struct iio_trigger \*trig:
        Trigger instance

    :param bool state:
        Desired trigger state

.. This file was automatic generated / don't edit.

