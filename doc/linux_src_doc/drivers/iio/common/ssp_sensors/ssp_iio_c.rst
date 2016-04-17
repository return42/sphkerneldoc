.. -*- coding: utf-8; mode: rst -*-

=========
ssp_iio.c
=========


.. _`ssp_common_buffer_postenable`:

ssp_common_buffer_postenable
============================

.. c:function:: int ssp_common_buffer_postenable (struct iio_dev *indio_dev)

    generic postenable callback for ssp buffer

    :param struct iio_dev \*indio_dev:
        iio device



.. _`ssp_common_buffer_postenable.description`:

Description
-----------

Returns 0 or negative value in case of error



.. _`ssp_common_buffer_postdisable`:

ssp_common_buffer_postdisable
=============================

.. c:function:: int ssp_common_buffer_postdisable (struct iio_dev *indio_dev)

    generic postdisable callback for ssp buffer

    :param struct iio_dev \*indio_dev:
        iio device



.. _`ssp_common_buffer_postdisable.description`:

Description
-----------

Returns 0 or negative value in case of error



.. _`ssp_common_process_data`:

ssp_common_process_data
=======================

.. c:function:: int ssp_common_process_data (struct iio_dev *indio_dev, void *buf, unsigned int len, int64_t timestamp)

    Common process data callback for ssp sensors

    :param struct iio_dev \*indio_dev:
        iio device

    :param void \*buf:
        source buffer

    :param unsigned int len:
        sensor data length

    :param int64_t timestamp:
        system timestamp



.. _`ssp_common_process_data.description`:

Description
-----------

Returns 0 or negative value in case of error

