.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/gyro/mpu3050-core.c

.. _`mpu3050_read_mem`:

mpu3050_read_mem
================

.. c:function:: int mpu3050_read_mem(struct mpu3050 *mpu3050, u8 bank, u8 addr, u8 len, u8 *buf)

    read MPU-3050 internal memory

    :param mpu3050:
        device to read from
    :type mpu3050: struct mpu3050 \*

    :param bank:
        target bank
    :type bank: u8

    :param addr:
        target address
    :type addr: u8

    :param len:
        number of bytes
    :type len: u8

    :param buf:
        the buffer to store the read bytes in
    :type buf: u8 \*

.. _`mpu3050_drdy_trigger_set_state`:

mpu3050_drdy_trigger_set_state
==============================

.. c:function:: int mpu3050_drdy_trigger_set_state(struct iio_trigger *trig, bool enable)

    set data ready interrupt state

    :param trig:
        trigger instance
    :type trig: struct iio_trigger \*

    :param enable:
        true if trigger should be enabled, false to disable
    :type enable: bool

.. This file was automatic generated / don't edit.

