.. -*- coding: utf-8; mode: rst -*-

.. _API-resource-alignment:

==================
resource_alignment
==================

*man resource_alignment(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
