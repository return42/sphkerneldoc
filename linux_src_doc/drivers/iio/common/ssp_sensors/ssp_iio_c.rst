.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/common/ssp_sensors/ssp_iio.c

.. _`ssp_common_buffer_postenable`:

ssp_common_buffer_postenable
============================

.. c:function:: int ssp_common_buffer_postenable(struct iio_dev *indio_dev)

    generic postenable callback for ssp buffer

    :param indio_dev:
        iio device
    :type indio_dev: struct iio_dev \*

.. _`ssp_common_buffer_postenable.description`:

Description
-----------

Returns 0 or negative value in case of error

.. _`ssp_common_buffer_postdisable`:

ssp_common_buffer_postdisable
=============================

.. c:function:: int ssp_common_buffer_postdisable(struct iio_dev *indio_dev)

    generic postdisable callback for ssp buffer

    :param indio_dev:
        iio device
    :type indio_dev: struct iio_dev \*

.. _`ssp_common_buffer_postdisable.description`:

Description
-----------

Returns 0 or negative value in case of error

.. _`ssp_common_process_data`:

ssp_common_process_data
=======================

.. c:function:: int ssp_common_process_data(struct iio_dev *indio_dev, void *buf, unsigned int len, int64_t timestamp)

    Common process data callback for ssp sensors

    :param indio_dev:
        iio device
    :type indio_dev: struct iio_dev \*

    :param buf:
        source buffer
    :type buf: void \*

    :param len:
        sensor data length
    :type len: unsigned int

    :param timestamp:
        system timestamp
    :type timestamp: int64_t

.. _`ssp_common_process_data.description`:

Description
-----------

Returns 0 or negative value in case of error

.. This file was automatic generated / don't edit.

