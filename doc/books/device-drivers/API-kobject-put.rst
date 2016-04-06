
.. _API-kobject-put:

===========
kobject_put
===========

*man kobject_put(9)*

*4.6.0-rc1*

decrement refcount for object.


Synopsis
========

.. c:function:: void kobject_put( struct kobject * kobj )

Arguments
=========

``kobj``
    object.


Description
===========

Decrement the refcount, and if 0, call ``kobject_cleanup``.
