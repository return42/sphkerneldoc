.. -*- coding: utf-8; mode: rst -*-

.. _API-sysfs-add-file-to-group:

=======================
sysfs_add_file_to_group
=======================

*man sysfs_add_file_to_group(9)*

*4.6.0-rc5*

add an attribute file to a pre-existing group.


Synopsis
========

.. c:function:: int sysfs_add_file_to_group( struct kobject * kobj, const struct attribute * attr, const char * group )

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
