.. -*- coding: utf-8; mode: rst -*-

.. _API-sysfs-rename-link-ns:

====================
sysfs_rename_link_ns
====================

*man sysfs_rename_link_ns(9)*

*4.6.0-rc5*

rename symlink in object's directory.


Synopsis
========

.. c:function:: int sysfs_rename_link_ns( struct kobject * kobj, struct kobject * targ, const char * old, const char * new, const void * new_ns )

Arguments
=========

``kobj``
    object we're acting for.

``targ``
    object we're pointing to.

``old``
    previous name of the symlink.

``new``
    new name of the symlink.

``new_ns``
    new namespace of the symlink.


Description
===========

A helper function for the common rename symlink idiom.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
