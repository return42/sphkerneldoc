
.. _API-iio-device-alloc:

================
iio_device_alloc
================

*man iio_device_alloc(9)*

*4.6.0-rc1*

allocate an iio_dev from a driver


Synopsis
========

.. c:function:: struct iio_dev ⋆ iio_device_alloc( int sizeof_priv )

Arguments
=========

``sizeof_priv``
    Space to allocate for private structure.
