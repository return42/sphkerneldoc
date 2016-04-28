.. -*- coding: utf-8; mode: rst -*-

.. _API-device-remove-file-self:

=======================
device_remove_file_self
=======================

*man device_remove_file_self(9)*

*4.6.0-rc5*

remove sysfs attribute file from its own method.


Synopsis
========

.. c:function:: bool device_remove_file_self( struct device * dev, const struct device_attribute * attr )

Arguments
=========

``dev``
    device.

``attr``
    device attribute descriptor.


Description
===========

See ``kernfs_remove_self`` for details.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
