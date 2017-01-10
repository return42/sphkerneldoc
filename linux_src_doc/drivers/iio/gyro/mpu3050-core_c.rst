.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/gyro/mpu3050-core.c

.. _`mpu3050_read_mem`:

mpu3050_read_mem
================

.. c:function:: int mpu3050_read_mem(struct mpu3050 *mpu3050, u8 bank, u8 addr, u8 len, u8 *buf)

    read MPU-3050 internal memory

    :param struct mpu3050 \*mpu3050:
        device to read from

    :param u8 bank:
        target bank

    :param u8 addr:
        target address

    :param u8 len:
        number of bytes

    :param u8 \*buf:
        the buffer to store the read bytes in

.. _`mpu3050_drdy_trigger_set_state`:

mpu3050_drdy_trigger_set_state
==============================

.. c:function:: int mpu3050_drdy_trigger_set_state(struct iio_trigger *trig, bool enable)

    set data ready interrupt state

    :param struct iio_trigger \*trig:
        trigger instance

    :param bool enable:
        true if trigger should be enabled, false to disable

.. This file was automatic generated / don't edit.

