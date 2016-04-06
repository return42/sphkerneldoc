
.. _API-kobject-rename:

==============
kobject_rename
==============

*man kobject_rename(9)*

*4.6.0-rc1*

change the name of an object


Synopsis
========

.. c:function:: int kobject_rename( struct kobject * kobj, const char * new_name )

Arguments
=========

``kobj``
    object in question.

``new_name``
    object's new name


Description
===========

It is the responsibility of the caller to provide mutual exclusion between two different calls of kobject_rename on the same kobject and to ensure that new_name is valid and
won't conflict with other kobjects.
