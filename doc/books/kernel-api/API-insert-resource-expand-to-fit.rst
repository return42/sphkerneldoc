
.. _API-insert-resource-expand-to-fit:

=============================
insert_resource_expand_to_fit
=============================

*man insert_resource_expand_to_fit(9)*

*4.6.0-rc1*

Insert a resource into the resource tree


Synopsis
========

.. c:function:: void insert_resource_expand_to_fit( struct resource * root, struct resource * new )

Arguments
=========

``root``
    root resource descriptor

``new``
    new resource to insert


Description
===========

Insert a resource into the resource tree, possibly expanding it in order to make it encompass any conflicting resources.
