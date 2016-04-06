
.. _API-device-for-each-child:

=====================
device_for_each_child
=====================

*man device_for_each_child(9)*

*4.6.0-rc1*

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

Iterate over ``parent``'s child devices, and call ``fn`` for each, passing it ``data``.

We check the return of ``fn`` each time. If it returns anything other than 0, we break out and return that value.
