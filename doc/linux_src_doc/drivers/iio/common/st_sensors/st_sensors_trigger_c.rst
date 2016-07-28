.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/common/st_sensors/st_sensors_trigger.c

.. _`st_sensors_irq_handler`:

st_sensors_irq_handler
======================

.. c:function:: irqreturn_t st_sensors_irq_handler(int irq, void *p)

    top half of the IRQ-based triggers

    :param int irq:
        irq number

    :param void \*p:
        private handler data

.. _`st_sensors_irq_thread`:

st_sensors_irq_thread
=====================

.. c:function:: irqreturn_t st_sensors_irq_thread(int irq, void *p)

    bottom half of the IRQ-based triggers

    :param int irq:
        irq number

    :param void \*p:
        private handler data

.. This file was automatic generated / don't edit.

