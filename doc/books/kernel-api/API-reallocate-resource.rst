.. -*- coding: utf-8; mode: rst -*-

.. _API-reallocate-resource:

===================
reallocate_resource
===================

*man reallocate_resource(9)*

*4.6.0-rc5*

allocate a slot in the resource tree given range & alignment. The
resource will be relocated if the new size cannot be reallocated in the
current location.


Synopsis
========

.. c:function:: int reallocate_resource( struct resource * root, struct resource * old, resource_size_t newsize, struct resource_constraint * constraint )

Arguments
=========

``root``
    root resource descriptor

``old``
    resource descriptor desired by caller

``newsize``
    new size of the resource descriptor

``constraint``
    the size and alignment constraints to be met.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
