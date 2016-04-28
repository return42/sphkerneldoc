.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mm-remove-node:

==================
drm_mm_remove_node
==================

*man drm_mm_remove_node(9)*

*4.6.0-rc5*

Remove a memory node from the allocator.


Synopsis
========

.. c:function:: void drm_mm_remove_node( struct drm_mm_node * node )

Arguments
=========

``node``
    drm_mm_node to remove


Description
===========

This just removes a node from its drm_mm allocator. The node does not
need to be cleared again before it can be re-inserted into this or any
other drm_mm allocator. It is a bug to call this function on a
un-allocated node.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
