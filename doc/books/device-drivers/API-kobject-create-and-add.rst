
.. _API-kobject-create-and-add:

======================
kobject_create_and_add
======================

*man kobject_create_and_add(9)*

*4.6.0-rc1*

create a struct kobject dynamically and register it with sysfs


Synopsis
========

.. c:function:: struct kobject ⋆ kobject_create_and_add( const char * name, struct kobject * parent )

Arguments
=========

``name``
    the name for the kobject

``parent``
    the parent kobject of this kobject, if any.


Description
===========

This function creates a kobject structure dynamically and registers it with sysfs. When you are finished with this structure, call ``kobject_put`` and the structure will be
dynamically freed when it is no longer being used.

If the kobject was not able to be created, NULL will be returned.
