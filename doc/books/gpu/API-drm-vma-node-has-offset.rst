
.. _API-drm-vma-node-has-offset:

=======================
drm_vma_node_has_offset
=======================

*man drm_vma_node_has_offset(9)*

*4.6.0-rc1*

Check whether node is added to offset manager


Synopsis
========

.. c:function:: bool drm_vma_node_has_offset( struct drm_vma_offset_node * node )

Arguments
=========

``node``
    Node to be checked


RETURNS
=======

true iff the node was previously allocated an offset and added to an vma offset manager.
