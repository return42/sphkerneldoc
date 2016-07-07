.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/imu/inv_mpu6050/inv_mpu_ring.c

.. _`inv_mpu6050_irq_handler`:

inv_mpu6050_irq_handler
=======================

.. c:function:: irqreturn_t inv_mpu6050_irq_handler(int irq, void *p)

    Cache a timestamp at each data ready interrupt.

    :param int irq:
        *undescribed*

    :param void \*p:
        *undescribed*

.. _`inv_mpu6050_read_fifo`:

inv_mpu6050_read_fifo
=====================

.. c:function:: irqreturn_t inv_mpu6050_read_fifo(int irq, void *p)

    Transfer data from hardware FIFO to KFIFO.

    :param int irq:
        *undescribed*

    :param void \*p:
        *undescribed*

.. This file was automatic generated / don't edit.

