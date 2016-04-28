.. -*- coding: utf-8; mode: rst -*-

.. _API-lookup-resource:

===============
lookup_resource
===============

*man lookup_resource(9)*

*4.6.0-rc5*

find an existing resource by a resource start address


Synopsis
========

.. c:function:: struct resource * lookup_resource( struct resource * root, resource_size_t start )

Arguments
=========

``root``
    root resource descriptor

``start``
    resource start address


Description
===========

Returns a pointer to the resource if found, NULL otherwise


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
