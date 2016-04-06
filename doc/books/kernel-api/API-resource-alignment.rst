
.. _API-resource-alignment:

==================
resource_alignment
==================

*man resource_alignment(9)*

*4.6.0-rc1*

calculate resource's alignment


Synopsis
========

.. c:function:: resource_size_t resource_alignment( struct resource * res )

Arguments
=========

``res``
    resource pointer


Description
===========

Returns alignment on success, 0 (invalid alignment) on failure.
