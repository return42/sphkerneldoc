.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/buffer/industrialio-buffer-dmaengine.c

.. _`iio_dmaengine_buffer_alloc`:

iio_dmaengine_buffer_alloc
==========================

.. c:function:: struct iio_buffer *iio_dmaengine_buffer_alloc(struct device *dev, const char *channel)

    Allocate new buffer which uses DMAengine

    :param dev:
        Parent device for the buffer
    :type dev: struct device \*

    :param channel:
        DMA channel name, typically "rx".
    :type channel: const char \*

.. _`iio_dmaengine_buffer_alloc.description`:

Description
-----------

This allocates a new IIO buffer which internally uses the DMAengine framework
to perform its transfers. The parent device will be used to request the DMA
channel.

Once done using the buffer \ :c:func:`iio_dmaengine_buffer_free`\  should be used to
release it.

.. _`iio_dmaengine_buffer_free`:

iio_dmaengine_buffer_free
=========================

.. c:function:: void iio_dmaengine_buffer_free(struct iio_buffer *buffer)

    Free dmaengine buffer

    :param buffer:
        Buffer to free
    :type buffer: struct iio_buffer \*

.. _`iio_dmaengine_buffer_free.description`:

Description
-----------

Frees a buffer previously allocated with \ :c:func:`iio_dmaengine_buffer_alloc`\ .

.. This file was automatic generated / don't edit.

