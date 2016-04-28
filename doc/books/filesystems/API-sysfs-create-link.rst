.. -*- coding: utf-8; mode: rst -*-

.. _API-sysfs-create-link:

=================
sysfs_create_link
=================

*man sysfs_create_link(9)*

*4.6.0-rc5*

create symlink between two objects.


Synopsis
========

.. c:function:: int sysfs_create_link( struct kobject * kobj, struct kobject * target, const char * name )

Arguments
=========

``kobj``
    object whose directory we're creating the link in.

``target``
    object we're pointing to.

``name``
    name of the symlink.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
