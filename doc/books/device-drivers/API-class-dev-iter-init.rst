
.. _API-class-dev-iter-init:

===================
class_dev_iter_init
===================

*man class_dev_iter_init(9)*

*4.6.0-rc1*

initialize class device iterator


Synopsis
========

.. c:function:: void class_dev_iter_init( struct class_dev_iter * iter, struct class * class, struct device * start, const struct device_type * type )

Arguments
=========

``iter``
    class iterator to initialize

``class``
    the class we wanna iterate over

``start``
    the device to start iterating from, if any

``type``
    device_type of the devices to iterate over, NULL for all


Description
===========

Initialize class iterator ``iter`` such that it iterates over devices of ``class``. If ``start`` is set, the list iteration will start there, otherwise if it is NULL, the iteration
starts at the beginning of the list.
