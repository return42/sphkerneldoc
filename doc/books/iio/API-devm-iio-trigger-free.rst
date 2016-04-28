.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-iio-trigger-free:

=====================
devm_iio_trigger_free
=====================

*man devm_iio_trigger_free(9)*

*4.6.0-rc5*

Resource-managed ``iio_trigger_free``


Synopsis
========

.. c:function:: void devm_iio_trigger_free( struct device * dev, struct iio_trigger * iio_trig )

Arguments
=========

``dev``
    Device this iio_dev belongs to

``iio_trig``
    the iio_trigger associated with the device


Description
===========

Free iio_trigger allocated with ``devm_iio_trigger_alloc``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
