.. -*- coding: utf-8; mode: rst -*-

.. _API-bus-register:

============
bus_register
============

*man bus_register(9)*

*4.6.0-rc5*

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

Once we have that, we register the bus with the kobject infrastructure,
then register the children subsystems it has: the devices and drivers
that belong to the subsystem.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
