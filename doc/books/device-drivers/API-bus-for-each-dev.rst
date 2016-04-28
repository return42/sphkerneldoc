.. -*- coding: utf-8; mode: rst -*-

.. _API-bus-for-each-dev:

================
bus_for_each_dev
================

*man bus_for_each_dev(9)*

*4.6.0-rc5*

device iterator.


Synopsis
========

.. c:function:: int bus_for_each_dev( struct bus_type * bus, struct device * start, void * data, int (*fn) struct device *, void * )

Arguments
=========

``bus``
    bus type.

``start``
    device to start iterating from.

``data``
    data for the callback.

``fn``
    function to be called for each device.


Description
===========

Iterate over ``bus``'s list of devices, and call ``fn`` for each,
passing it ``data``. If ``start`` is not NULL, we use that device to
begin iterating from.

We check the return of ``fn`` each time. If it returns anything other
than 0, we break out and return that value.


NOTE
====

The device that returns a non-zero value is not retained in any way, nor
is its refcount incremented. If the caller needs to retain this data, it
should do so, and increment the reference count in the supplied
callback.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
