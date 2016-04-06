
.. _API-class-for-each-device:

=====================
class_for_each_device
=====================

*man class_for_each_device(9)*

*4.6.0-rc1*

device iterator


Synopsis
========

.. c:function:: int class_for_each_device( struct class * class, struct device * start, void * data, int (*fn) struct device *, void * )

Arguments
=========

``class``
    the class we're iterating

``start``
    the device to start with in the list, if any.

``data``
    data for the callback

``fn``
    function to be called for each device


Description
===========

Iterate over ``class``'s list of devices, and call ``fn`` for each, passing it ``data``. If ``start`` is set, the list iteration will start there, otherwise if it is NULL, the
iteration starts at the beginning of the list.

We check the return of ``fn`` each time. If it returns anything other than 0, we break out and return that value.

``fn`` is allowed to do anything including calling back into class code. There's no locking restriction.
