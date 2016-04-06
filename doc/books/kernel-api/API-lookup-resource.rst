
.. _API-lookup-resource:

===============
lookup_resource
===============

*man lookup_resource(9)*

*4.6.0-rc1*

find an existing resource by a resource start address


Synopsis
========

.. c:function:: struct resource ⋆ lookup_resource( struct resource * root, resource_size_t start )

Arguments
=========

``root``
    root resource descriptor

``start``
    resource start address


Description
===========

Returns a pointer to the resource if found, NULL otherwise
