.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/common/st_sensors/st_sensors_trigger.c

.. _`st_sensors_new_samples_available`:

st_sensors_new_samples_available
================================

.. c:function:: int st_sensors_new_samples_available(struct iio_dev *indio_dev, struct st_sensor_data *sdata)

    check if more samples came in

    :param indio_dev:
        *undescribed*
    :type indio_dev: struct iio_dev \*

    :param sdata:
        *undescribed*
    :type sdata: struct st_sensor_data \*

.. _`st_sensors_new_samples_available.return`:

Return
------

0 - no new samples available
1 - new samples available
negative - error or unknown

.. _`st_sensors_irq_handler`:

st_sensors_irq_handler
======================

.. c:function:: irqreturn_t st_sensors_irq_handler(int irq, void *p)

    top half of the IRQ-based triggers

    :param irq:
        irq number
    :type irq: int

    :param p:
        private handler data
    :type p: void \*

.. _`st_sensors_irq_thread`:

st_sensors_irq_thread
=====================

.. c:function:: irqreturn_t st_sensors_irq_thread(int irq, void *p)

    bottom half of the IRQ-based triggers

    :param irq:
        irq number
    :type irq: int

    :param p:
        private handler data
    :type p: void \*

.. This file was automatic generated / don't edit.

