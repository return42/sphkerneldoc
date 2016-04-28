.. -*- coding: utf-8; mode: rst -*-

.. _API-device-create-bin-file:

======================
device_create_bin_file
======================

*man device_create_bin_file(9)*

*4.6.0-rc5*

create sysfs binary attribute file for device.


Synopsis
========

.. c:function:: int device_create_bin_file( struct device * dev, const struct bin_attribute * attr )

Arguments
=========

``dev``
    device.

``attr``
    device binary attribute descriptor.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
