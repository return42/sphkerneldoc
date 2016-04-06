
.. _API-dev-set-name:

============
dev_set_name
============

*man dev_set_name(9)*

*4.6.0-rc1*

set a device name


Synopsis
========

.. c:function:: int dev_set_name( struct device * dev, const char * fmt, ... )

Arguments
=========

``dev``
    device

``fmt``
    format string for the device's name

``...``
    variable arguments
