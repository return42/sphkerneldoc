
.. _API-kset-find-obj:

=============
kset_find_obj
=============

*man kset_find_obj(9)*

*4.6.0-rc1*

search for object in kset.


Synopsis
========

.. c:function:: struct kobject ⋆ kset_find_obj( struct kset * kset, const char * name )

Arguments
=========

``kset``
    kset we're looking in.

``name``
    object's name.


Description
===========

Lock kset via ``kset``->subsys, and iterate over ``kset``->list, looking for a matching kobject. If matching object is found take a reference and return the object.
