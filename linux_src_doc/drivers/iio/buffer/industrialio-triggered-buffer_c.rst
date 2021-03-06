.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/buffer/industrialio-triggered-buffer.c

.. _`iio_triggered_buffer_setup`:

iio_triggered_buffer_setup
==========================

.. c:function:: int iio_triggered_buffer_setup(struct iio_dev *indio_dev, irqreturn_t (*h)(int irq, void *p), irqreturn_t (*thread)(int irq, void *p), const struct iio_buffer_setup_ops *setup_ops)

    Setup triggered buffer and pollfunc

    :param indio_dev:
        IIO device structure
    :type indio_dev: struct iio_dev \*

    :param irqreturn_t (\*h)(int irq, void \*p):
        Function which will be used as pollfunc top half

    :param irqreturn_t (\*thread)(int irq, void \*p):
        Function which will be used as pollfunc bottom half

    :param setup_ops:
        Buffer setup functions to use for this device.
        If NULL the default setup functions for triggered
        buffers will be used.
    :type setup_ops: const struct iio_buffer_setup_ops \*

.. _`iio_triggered_buffer_setup.description`:

Description
-----------

This function combines some common tasks which will normally be performed
when setting up a triggered buffer. It will allocate the buffer and the
pollfunc.

Before calling this function the indio_dev structure should already be
completely initialized, but not yet registered. In practice this means that
this function should be called right before \ :c:func:`iio_device_register`\ .

To free the resources allocated by this function call
\ :c:func:`iio_triggered_buffer_cleanup`\ .

.. _`iio_triggered_buffer_cleanup`:

iio_triggered_buffer_cleanup
============================

.. c:function:: void iio_triggered_buffer_cleanup(struct iio_dev *indio_dev)

    Free resources allocated by \ :c:func:`iio_triggered_buffer_setup`\ 

    :param indio_dev:
        IIO device structure
    :type indio_dev: struct iio_dev \*

.. This file was automatic generated / don't edit.

