.. -*- coding: utf-8; mode: rst -*-

==============================
industrialio-triggered-event.c
==============================


.. _`iio_triggered_event_setup`:

iio_triggered_event_setup
=========================

.. c:function:: int iio_triggered_event_setup (struct iio_dev *indio_dev, irqreturn_t (*h) (int irq, void *p, irqreturn_t (*thread) (int irq, void *p)

    Setup pollfunc_event for triggered event

    :param struct iio_dev \*indio_dev:
        IIO device structure

    :param irqreturn_t (\*h) (int irq, void \*p):
        Function which will be used as pollfunc_event top half

    :param irqreturn_t (\*thread) (int irq, void \*p):
        Function which will be used as pollfunc_event bottom half



.. _`iio_triggered_event_setup.description`:

Description
-----------

This function combines some common tasks which will normally be performed
when setting up a triggered event. It will allocate the pollfunc_event and
set mode to use it for triggered event.

Before calling this function the indio_dev structure should already be
completely initialized, but not yet registered. In practice this means that
this function should be called right before :c:func:`iio_device_register`.

To free the resources allocated by this function call
:c:func:`iio_triggered_event_cleanup`.



.. _`iio_triggered_event_cleanup`:

iio_triggered_event_cleanup
===========================

.. c:function:: void iio_triggered_event_cleanup (struct iio_dev *indio_dev)

    Free resources allocated by iio_triggered_event_setup()

    :param struct iio_dev \*indio_dev:
        IIO device structure

