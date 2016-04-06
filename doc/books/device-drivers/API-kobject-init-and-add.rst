
.. _API-kobject-init-and-add:

====================
kobject_init_and_add
====================

*man kobject_init_and_add(9)*

*4.6.0-rc1*

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

This function combines the call to ``kobject_init`` and ``kobject_add``. The same type of error handling after a call to ``kobject_add`` and kobject lifetime rules are the same
here.
