.. -*- coding: utf-8; mode: rst -*-

.. _API-device-remove-file:

==================
device_remove_file
==================

*man device_remove_file(9)*

*4.6.0-rc5*

remove sysfs attribute file.


Synopsis
========

.. c:function:: void device_remove_file( struct device * dev, const struct device_attribute * attr )

Arguments
=========

``dev``
    device.

``attr``
    device attribute descriptor.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
