.. -*- coding: utf-8; mode: rst -*-

.. _API-allocate-resource:

=================
allocate_resource
=================

*man allocate_resource(9)*

*4.6.0-rc5*

allocate empty slot in the resource tree given range & alignment. The
resource will be reallocated with a new size if it was already allocated


Synopsis
========

.. c:function:: int allocate_resource( struct resource * root, struct resource * new, resource_size_t size, resource_size_t min, resource_size_t max, resource_size_t align, resource_size_t (*alignf) void *, const struct resource *, resource_size_t, resource_size_t, void * alignf_data )

Arguments
=========

``root``
    root resource descriptor

``new``
    resource descriptor desired by caller

``size``
    requested resource region size

``min``
    minimum boundary to allocate

``max``
    maximum boundary to allocate

``align``
    alignment requested, in bytes

``alignf``
    alignment function, optional, called if not NULL

``alignf_data``
    arbitrary data to pass to the ``alignf`` function


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
