
.. _API-iio-buffer-put:

==============
iio_buffer_put
==============

*man iio_buffer_put(9)*

*4.6.0-rc1*

Release the reference to the buffer


Synopsis
========

.. c:function:: void iio_buffer_put( struct iio_buffer * buffer )

Arguments
=========

``buffer``
    The buffer to release the reference for, may be NULL
