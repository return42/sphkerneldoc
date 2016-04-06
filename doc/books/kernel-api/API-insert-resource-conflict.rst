
.. _API-insert-resource-conflict:

========================
insert_resource_conflict
========================

*man insert_resource_conflict(9)*

*4.6.0-rc1*

Inserts resource in the resource tree


Synopsis
========

.. c:function:: struct resource ⋆ insert_resource_conflict( struct resource * parent, struct resource * new )

Arguments
=========

``parent``
    parent of the new resource

``new``
    new resource to insert


Description
===========

Returns 0 on success, conflict resource if the resource can't be inserted.

This function is equivalent to request_resource_conflict when no conflict happens. If a conflict happens, and the conflicting resources entirely fit within the range of the new
resource, then the new resource is inserted and the conflicting resources become children of the new resource.

This function is intended for producers of resources, such as FW modules and bus drivers.
