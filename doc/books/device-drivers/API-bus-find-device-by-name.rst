
.. _API-bus-find-device-by-name:

=======================
bus_find_device_by_name
=======================

*man bus_find_device_by_name(9)*

*4.6.0-rc1*

device iterator for locating a particular device of a specific name


Synopsis
========

.. c:function:: struct device ⋆ bus_find_device_by_name( struct bus_type * bus, struct device * start, const char * name )

Arguments
=========

``bus``
    bus type

``start``
    Device to begin with

``name``
    name of the device to match


Description
===========

This is similar to the ``bus_find_device`` function above, but it handles searching by a name automatically, no need to write another strcmp matching function.
