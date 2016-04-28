.. -*- coding: utf-8; mode: rst -*-

.. _API-kobject-add:

===========
kobject_add
===========

*man kobject_add(9)*

*4.6.0-rc5*

the main kobject add function


Synopsis
========

.. c:function:: int kobject_add( struct kobject * kobj, struct kobject * parent, const char * fmt, ... )

Arguments
=========

``kobj``
    the kobject to add

``parent``
    pointer to the parent of the kobject.

``fmt``
    format to name the kobject with.

``...``
    variable arguments


Description
===========

The kobject name is set and added to the kobject hierarchy in this
function.

If ``parent`` is set, then the parent of the ``kobj`` will be set to it.
If ``parent`` is NULL, then the parent of the ``kobj`` will be set to
the kobject associated with the kset assigned to this kobject. If no
kset is assigned to the kobject, then the kobject will be located in the
root of the sysfs tree.

If this function returns an error, ``kobject_put`` must be called to
properly clean up the memory associated with the object. Under no
instance should the kobject that is passed to this function be directly
freed with a call to ``kfree``, that can leak memory.

Note, no “add” uevent will be created with this call, the caller should
set up all of the necessary sysfs files for the object and then call
``kobject_uevent`` with the UEVENT_ADD parameter to ensure that
userspace is properly notified of this kobject's creation.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
