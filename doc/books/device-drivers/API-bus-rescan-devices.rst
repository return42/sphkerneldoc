.. -*- coding: utf-8; mode: rst -*-

.. _API-bus-rescan-devices:

==================
bus_rescan_devices
==================

*man bus_rescan_devices(9)*

*4.6.0-rc5*

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

This function will look for devices on the bus with no driver attached
and rescan it against existing drivers to see if it matches any by
calling ``device_attach`` for the unbound devices.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
