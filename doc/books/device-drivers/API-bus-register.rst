
.. _API-bus-register:

============
bus_register
============

*man bus_register(9)*

*4.6.0-rc1*

register a driver-core subsystem


Synopsis
========

.. c:function:: int bus_register( struct bus_type * bus )

Arguments
=========

``bus``
    bus to register


Description
===========

Once we have that, we register the bus with the kobject infrastructure, then register the children subsystems it has: the devices and drivers that belong to the subsystem.
