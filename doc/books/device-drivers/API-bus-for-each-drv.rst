
.. _API-bus-for-each-drv:

================
bus_for_each_drv
================

*man bus_for_each_drv(9)*

*4.6.0-rc1*

driver iterator


Synopsis
========

.. c:function:: int bus_for_each_drv( struct bus_type * bus, struct device_driver * start, void * data, int (*fn) struct device_driver *, void * )

Arguments
=========

``bus``
    bus we're dealing with.

``start``
    driver to start iterating on.

``data``
    data to pass to the callback.

``fn``
    function to call for each driver.


Description
===========

This is nearly identical to the device iterator above. We iterate over each driver that belongs to ``bus``, and call ``fn`` for each. If ``fn`` returns anything but 0, we break out
and return it. If ``start`` is not NULL, we use it as the head of the list.


NOTE
====

we don't return the driver that returns a non-zero value, nor do we leave the reference count incremented for that driver. If the caller needs to know that info, it must set it in
the callback. It must also be sure to increment the refcount so it doesn't disappear before returning to the caller.
