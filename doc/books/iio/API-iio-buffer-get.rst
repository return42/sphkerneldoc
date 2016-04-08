
.. _API-iio-buffer-get:

==============
iio_buffer_get
==============

*man iio_buffer_get(9)*

*4.6.0-rc1*

Grab a reference to the buffer


Synopsis
========

.. c:function:: struct iio_buffer ⋆ iio_buffer_get( struct iio_buffer * buffer )

Arguments
=========

``buffer``
    The buffer to grab a reference for, may be NULL


Description
===========

Returns the pointer to the buffer that was passed into the function.
