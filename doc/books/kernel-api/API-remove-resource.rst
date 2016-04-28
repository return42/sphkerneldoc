.. -*- coding: utf-8; mode: rst -*-

.. _API-remove-resource:

===============
remove_resource
===============

*man remove_resource(9)*

*4.6.0-rc5*

Remove a resource in the resource tree


Synopsis
========

.. c:function:: int remove_resource( struct resource * old )

Arguments
=========

``old``
    resource to remove


Description
===========

Returns 0 on success, -EINVAL if the resource is not valid.

This function removes a resource previously inserted by
``insert_resource`` or ``insert_resource_conflict``, and moves the
children (if any) up to where they were before. ``insert_resource`` and
``insert_resource_conflict`` insert a new resource, and move any
conflicting resources down to the children of the new resource.

``insert_resource``, ``insert_resource_conflict`` and
``remove_resource`` are intended for producers of resources, such as FW
modules and bus drivers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
