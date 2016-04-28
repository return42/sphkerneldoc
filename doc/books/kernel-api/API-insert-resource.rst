.. -*- coding: utf-8; mode: rst -*-

.. _API-insert-resource:

===============
insert_resource
===============

*man insert_resource(9)*

*4.6.0-rc5*

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

This function is intended for producers of resources, such as FW modules
and bus drivers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
