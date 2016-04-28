.. -*- coding: utf-8; mode: rst -*-

.. _API-dev-driver-string:

=================
dev_driver_string
=================

*man dev_driver_string(9)*

*4.6.0-rc5*

Return a device's driver name, if at all possible


Synopsis
========

.. c:function:: const char * dev_driver_string( const struct device * dev )

Arguments
=========

``dev``
    struct device to get the name of


Description
===========

Will return the device's driver's name if it is bound to a device. If
the device is not bound to a driver, it will return the name of the bus
it is attached to. If it is not attached to a bus either, an empty
string will be returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
