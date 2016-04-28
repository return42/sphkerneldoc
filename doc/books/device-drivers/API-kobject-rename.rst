.. -*- coding: utf-8; mode: rst -*-

.. _API-kobject-rename:

==============
kobject_rename
==============

*man kobject_rename(9)*

*4.6.0-rc5*

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

It is the responsibility of the caller to provide mutual exclusion
between two different calls of kobject_rename on the same kobject and
to ensure that new_name is valid and won't conflict with other
kobjects.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
