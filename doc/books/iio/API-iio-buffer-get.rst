.. -*- coding: utf-8; mode: rst -*-

.. _API-iio-buffer-get:

==============
iio_buffer_get
==============

*man iio_buffer_get(9)*

*4.6.0-rc5*

Grab a reference to the buffer


Synopsis
========

.. c:function:: struct iio_buffer * iio_buffer_get( struct iio_buffer * buffer )

Arguments
=========

``buffer``
    The buffer to grab a reference for, may be NULL


Description
===========

Returns the pointer to the buffer that was passed into the function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
