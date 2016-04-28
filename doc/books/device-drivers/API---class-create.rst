.. -*- coding: utf-8; mode: rst -*-

.. _API---class-create:

==============
__class_create
==============

*man __class_create(9)*

*4.6.0-rc5*

create a struct class structure


Synopsis
========

.. c:function:: struct class * __class_create( struct module * owner, const char * name, struct lock_class_key * key )

Arguments
=========

``owner``
    pointer to the module that is to “own” this struct class

``name``
    pointer to a string for the name of this class.

``key``
    the lock_class_key for this class; used by mutex lock debugging


Description
===========

This is used to create a struct class pointer that can then be used in
calls to ``device_create``.

Returns ``struct class`` pointer on success, or ``ERR_PTR`` on error.

Note, the pointer created here is to be destroyed when finished by
making a call to ``class_destroy``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
