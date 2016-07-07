.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/buffer/kfifo_buf.c

.. _`devm_iio_kfifo_allocate`:

devm_iio_kfifo_allocate
=======================

.. c:function:: struct iio_buffer *devm_iio_kfifo_allocate(struct device *dev)

    Resource-managed \ :c:func:`iio_kfifo_allocate`\ 

    :param struct device \*dev:
        Device to allocate kfifo buffer for

.. _`devm_iio_kfifo_allocate.return`:

Return
------

Pointer to allocated iio_buffer on success, NULL on failure.

.. _`devm_iio_kfifo_free`:

devm_iio_kfifo_free
===================

.. c:function:: void devm_iio_kfifo_free(struct device *dev, struct iio_buffer *r)

    Resource-managed \ :c:func:`iio_kfifo_free`\ 

    :param struct device \*dev:
        Device the buffer belongs to

    :param struct iio_buffer \*r:
        The buffer associated with the device

.. This file was automatic generated / don't edit.

