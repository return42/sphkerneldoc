.. -*- coding: utf-8; mode: rst -*-

.. _API-sysfs-remove-link:

=================
sysfs_remove_link
=================

*man sysfs_remove_link(9)*

*4.6.0-rc5*

remove symlink in object's directory.


Synopsis
========

.. c:function:: void sysfs_remove_link( struct kobject * kobj, const char * name )

Arguments
=========

``kobj``
    object we're acting for.

``name``
    name of the symlink to remove.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
