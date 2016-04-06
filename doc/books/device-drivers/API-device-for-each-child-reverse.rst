
.. _API-device-for-each-child-reverse:

=============================
device_for_each_child_reverse
=============================

*man device_for_each_child_reverse(9)*

*4.6.0-rc1*

device child iterator in reversed order.


Synopsis
========

.. c:function:: int device_for_each_child_reverse( struct device * parent, void * data, int (*fn) struct device *dev, void *data )

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
