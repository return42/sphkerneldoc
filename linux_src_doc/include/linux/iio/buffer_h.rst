.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/iio/buffer.h

.. _`iio_push_to_buffers_with_timestamp`:

iio_push_to_buffers_with_timestamp
==================================

.. c:function:: int iio_push_to_buffers_with_timestamp(struct iio_dev *indio_dev, void *data, int64_t timestamp)

    push data and timestamp to buffers

    :param struct iio_dev \*indio_dev:
        iio_dev structure for device.

    :param void \*data:
        sample data

    :param int64_t timestamp:
        timestamp for the sample data

.. _`iio_push_to_buffers_with_timestamp.description`:

Description
-----------

Pushes data to the IIO device's buffers. If timestamps are enabled for the
device the function will store the supplied timestamp as the last element in
the sample data buffer before pushing it to the device buffers. The sample
data buffer needs to be large enough to hold the additional timestamp
(usually the buffer should be indio->scan_bytes bytes large).

Returns 0 on success, a negative error code otherwise.

.. This file was automatic generated / don't edit.

