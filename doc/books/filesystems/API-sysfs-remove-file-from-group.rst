.. -*- coding: utf-8; mode: rst -*-

.. _API-sysfs-remove-file-from-group:

============================
sysfs_remove_file_from_group
============================

*man sysfs_remove_file_from_group(9)*

*4.6.0-rc5*

remove an attribute file from a group.


Synopsis
========

.. c:function:: void sysfs_remove_file_from_group( struct kobject * kobj, const struct attribute * attr, const char * group )

Arguments
=========

``kobj``
    object we're acting for.

``attr``
    attribute descriptor.

``group``
    group name.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
