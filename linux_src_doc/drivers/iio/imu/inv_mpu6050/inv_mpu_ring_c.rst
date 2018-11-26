.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/imu/inv_mpu6050/inv_mpu_ring.c

.. _`inv_mpu6050_update_period`:

inv_mpu6050_update_period
=========================

.. c:function:: void inv_mpu6050_update_period(struct inv_mpu6050_state *st, s64 timestamp, size_t nb)

    Update chip internal period estimation

    :param st:
        driver state
    :type st: struct inv_mpu6050_state \*

    :param timestamp:
        the interrupt timestamp
    :type timestamp: s64

    :param nb:
        number of data set in the fifo
    :type nb: size_t

.. _`inv_mpu6050_update_period.description`:

Description
-----------

This function uses interrupt timestamps to estimate the chip period and
to choose the data timestamp to come.

.. _`inv_mpu6050_get_timestamp`:

inv_mpu6050_get_timestamp
=========================

.. c:function:: s64 inv_mpu6050_get_timestamp(struct inv_mpu6050_state *st)

    Return the current data timestamp

    :param st:
        driver state
    :type st: struct inv_mpu6050_state \*

.. _`inv_mpu6050_get_timestamp.description`:

Description
-----------

This function returns the current data timestamp and prepares for next one.

.. _`inv_mpu6050_read_fifo`:

inv_mpu6050_read_fifo
=====================

.. c:function:: irqreturn_t inv_mpu6050_read_fifo(int irq, void *p)

    Transfer data from hardware FIFO to KFIFO.

    :param irq:
        *undescribed*
    :type irq: int

    :param p:
        *undescribed*
    :type p: void \*

.. This file was automatic generated / don't edit.

