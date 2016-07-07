.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/iio/meter/ade7758_ring.c

.. _`ade7758_spi_read_burst`:

ade7758_spi_read_burst
======================

.. c:function:: int ade7758_spi_read_burst(struct iio_dev *indio_dev)

    read data registers

    :param struct iio_dev \*indio_dev:
        the IIO device

.. _`ade7758_ring_preenable`:

ade7758_ring_preenable
======================

.. c:function:: int ade7758_ring_preenable(struct iio_dev *indio_dev)

    :param struct iio_dev \*indio_dev:
        *undescribed*

.. _`ade7758_ring_preenable.description`:

Description
-----------

The complex nature of the setting of the number of bytes per datum is due
to this driver currently ensuring that the timestamp is stored at an 8
byte boundary.

.. This file was automatic generated / don't edit.

