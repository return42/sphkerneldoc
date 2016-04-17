.. -*- coding: utf-8; mode: rst -*-

========
driver.h
========


.. _`iio_map_array_register`:

iio_map_array_register
======================

.. c:function:: int iio_map_array_register (struct iio_dev *indio_dev, struct iio_map *map)

    tell the core about inkernel consumers

    :param struct iio_dev \*indio_dev:
        provider device

    :param struct iio_map \*map:
        array of mappings specifying association of channel with client



.. _`iio_map_array_unregister`:

iio_map_array_unregister
========================

.. c:function:: int iio_map_array_unregister (struct iio_dev *indio_dev)

    tell the core to remove consumer mappings for the given provider device

    :param struct iio_dev \*indio_dev:
        provider device

