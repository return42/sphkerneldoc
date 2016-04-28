.. -*- coding: utf-8; mode: rst -*-

.. _API-kset-find-obj:

=============
kset_find_obj
=============

*man kset_find_obj(9)*

*4.6.0-rc5*

search for object in kset.


Synopsis
========

.. c:function:: struct kobject * kset_find_obj( struct kset * kset, const char * name )

Arguments
=========

``kset``
    kset we're looking in.

``name``
    object's name.


Description
===========

Lock kset via ``kset``->subsys, and iterate over ``kset``->list, looking
for a matching kobject. If matching object is found take a reference and
return the object.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
