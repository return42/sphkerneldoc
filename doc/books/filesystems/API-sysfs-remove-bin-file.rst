.. -*- coding: utf-8; mode: rst -*-

.. _API-sysfs-remove-bin-file:

=====================
sysfs_remove_bin_file
=====================

*man sysfs_remove_bin_file(9)*

*4.6.0-rc5*

remove binary file for object.


Synopsis
========

.. c:function:: void sysfs_remove_bin_file( struct kobject * kobj, const struct bin_attribute * attr )

Arguments
=========

``kobj``
    object.

``attr``
    attribute descriptor.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
