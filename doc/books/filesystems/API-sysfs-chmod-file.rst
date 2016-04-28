.. -*- coding: utf-8; mode: rst -*-

.. _API-sysfs-chmod-file:

================
sysfs_chmod_file
================

*man sysfs_chmod_file(9)*

*4.6.0-rc5*

update the modified mode value on an object attribute.


Synopsis
========

.. c:function:: int sysfs_chmod_file( struct kobject * kobj, const struct attribute * attr, umode_t mode )

Arguments
=========

``kobj``
    object we're acting for.

``attr``
    attribute descriptor.

``mode``
    file permissions.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
