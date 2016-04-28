.. -*- coding: utf-8; mode: rst -*-

.. _API-kobject-init-and-add:

====================
kobject_init_and_add
====================

*man kobject_init_and_add(9)*

*4.6.0-rc5*

initialize a kobject structure and add it to the kobject hierarchy


Synopsis
========

.. c:function:: int kobject_init_and_add( struct kobject * kobj, struct kobj_type * ktype, struct kobject * parent, const char * fmt, ... )

Arguments
=========

``kobj``
    pointer to the kobject to initialize

``ktype``
    pointer to the ktype for this kobject.

``parent``
    pointer to the parent of this kobject.

``fmt``
    the name of the kobject.

``...``
    variable arguments


Description
===========

This function combines the call to ``kobject_init`` and ``kobject_add``.
The same type of error handling after a call to ``kobject_add`` and
kobject lifetime rules are the same here.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
