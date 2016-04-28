.. -*- coding: utf-8; mode: rst -*-

.. _API-insert-resource-expand-to-fit:

=============================
insert_resource_expand_to_fit
=============================

*man insert_resource_expand_to_fit(9)*

*4.6.0-rc5*

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

Insert a resource into the resource tree, possibly expanding it in order
to make it encompass any conflicting resources.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
