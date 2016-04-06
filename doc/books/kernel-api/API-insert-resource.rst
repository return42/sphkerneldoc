
.. _API-insert-resource:

===============
insert_resource
===============

*man insert_resource(9)*

*4.6.0-rc1*

Inserts a resource in the resource tree


Synopsis
========

.. c:function:: int insert_resource( struct resource * parent, struct resource * new )

Arguments
=========

``parent``
    parent of the new resource

``new``
    new resource to insert


Description
===========

Returns 0 on success, -EBUSY if the resource can't be inserted.

This function is intended for producers of resources, such as FW modules and bus drivers.
