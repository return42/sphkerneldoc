
.. _API-adjust-resource:

===============
adjust_resource
===============

*man adjust_resource(9)*

*4.6.0-rc1*

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

Given an existing resource, change its start and size to match the arguments. Returns 0 on success, -EBUSY if it can't fit. Existing children of the resource are assumed to be
immutable.
