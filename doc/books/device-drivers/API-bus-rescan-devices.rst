
.. _API-bus-rescan-devices:

==================
bus_rescan_devices
==================

*man bus_rescan_devices(9)*

*4.6.0-rc1*

rescan devices on the bus for possible drivers


Synopsis
========

.. c:function:: int bus_rescan_devices( struct bus_type * bus )

Arguments
=========

``bus``
    the bus to scan.


Description
===========

This function will look for devices on the bus with no driver attached and rescan it against existing drivers to see if it matches any by calling ``device_attach`` for the unbound
devices.
