
.. _API-drm-vma-node-reset:

==================
drm_vma_node_reset
==================

*man drm_vma_node_reset(9)*

*4.6.0-rc1*

Initialize or reset node object


Synopsis
========

.. c:function:: void drm_vma_node_reset( struct drm_vma_offset_node * node )

Arguments
=========

``node``
    Node to initialize or reset


Description
===========

Reset a node to its initial state. This must be called before using it with any VMA offset manager.

This must not be called on an already allocated node, or you will leak memory.
