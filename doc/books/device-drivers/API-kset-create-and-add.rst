.. -*- coding: utf-8; mode: rst -*-

.. _API-kset-create-and-add:

===================
kset_create_and_add
===================

*man kset_create_and_add(9)*

*4.6.0-rc5*

create a struct kset dynamically and add it to sysfs


Synopsis
========

.. c:function:: struct kset * kset_create_and_add( const char * name, const struct kset_uevent_ops * uevent_ops, struct kobject * parent_kobj )

Arguments
=========

``name``
    the name for the kset

``uevent_ops``
    a struct kset_uevent_ops for the kset

``parent_kobj``
    the parent kobject of this kset, if any.


Description
===========

This function creates a kset structure dynamically and registers it with
sysfs. When you are finished with this structure, call
``kset_unregister`` and the structure will be dynamically freed when it
is no longer being used.

If the kset was not able to be created, NULL will be returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
