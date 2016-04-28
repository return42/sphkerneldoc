.. -*- coding: utf-8; mode: rst -*-

.. _API-iio-device-alloc:

================
iio_device_alloc
================

*man iio_device_alloc(9)*

*4.6.0-rc5*

allocate an iio_dev from a driver


Synopsis
========

.. c:function:: struct iio_dev * iio_device_alloc( int sizeof_priv )

Arguments
=========

``sizeof_priv``
    Space to allocate for private structure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
