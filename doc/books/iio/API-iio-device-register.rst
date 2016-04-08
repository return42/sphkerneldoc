
.. _API-iio-device-register:

===================
iio_device_register
===================

*man iio_device_register(9)*

*4.6.0-rc1*

register a device with the IIO subsystem


Synopsis
========

.. c:function:: int iio_device_register( struct iio_dev * indio_dev )

Arguments
=========

``indio_dev``
    Device structure filled by the device driver
