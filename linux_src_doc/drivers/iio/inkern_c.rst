.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/inkern.c

.. _`__of_iio_simple_xlate`:

\__of_iio_simple_xlate
======================

.. c:function:: int __of_iio_simple_xlate(struct iio_dev *indio_dev, const struct of_phandle_args *iiospec)

    translate iiospec to the IIO channel index

    :param struct iio_dev \*indio_dev:
        pointer to the iio_dev structure

    :param const struct of_phandle_args \*iiospec:
        IIO specifier as found in the device tree

.. _`__of_iio_simple_xlate.description`:

Description
-----------

This is simple translation function, suitable for the most 1:1 mapped
channels in IIO chips. This function performs only one sanity check:
whether IIO index is less than num_channels (that is specified in the
iio_dev).

.. This file was automatic generated / don't edit.

