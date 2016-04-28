.. -*- coding: utf-8; mode: rst -*-

.. _API-device-for-each-child:

=====================
device_for_each_child
=====================

*man device_for_each_child(9)*

*4.6.0-rc5*

device child iterator.


Synopsis
========

.. c:function:: int device_for_each_child( struct device * parent, void * data, int (*fn) struct device *dev, void *data )

Arguments
=========

``parent``
    parent struct device.

``data``
    data for the callback.

``fn``
    function to be called for each device.


Description
===========

Iterate over ``parent``'s child devices, and call ``fn`` for each,
passing it ``data``.

We check the return of ``fn`` each time. If it returns anything other
than 0, we break out and return that value.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
