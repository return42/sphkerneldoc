.. -*- coding: utf-8; mode: rst -*-

.. _API-subsys-dev-iter-init:

====================
subsys_dev_iter_init
====================

*man subsys_dev_iter_init(9)*

*4.6.0-rc5*

initialize subsys device iterator


Synopsis
========

.. c:function:: void subsys_dev_iter_init( struct subsys_dev_iter * iter, struct bus_type * subsys, struct device * start, const struct device_type * type )

Arguments
=========

``iter``
    subsys iterator to initialize

``subsys``
    the subsys we wanna iterate over

``start``
    the device to start iterating from, if any

``type``
    device_type of the devices to iterate over, NULL for all


Description
===========

Initialize subsys iterator ``iter`` such that it iterates over devices
of ``subsys``. If ``start`` is set, the list iteration will start there,
otherwise if it is NULL, the iteration starts at the beginning of the
list.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
