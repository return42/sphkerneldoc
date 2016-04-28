.. -*- coding: utf-8; mode: rst -*-

.. _API-adjust-resource:

===============
adjust_resource
===============

*man adjust_resource(9)*

*4.6.0-rc5*

modify a resource's start and size


Synopsis
========

.. c:function:: int adjust_resource( struct resource * res, resource_size_t start, resource_size_t size )

Arguments
=========

``res``
    resource to modify

``start``
    new start value

``size``
    new size


Description
===========

Given an existing resource, change its start and size to match the
arguments. Returns 0 on success, -EBUSY if it can't fit. Existing
children of the resource are assumed to be immutable.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
