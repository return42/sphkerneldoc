
.. _API-drm-mm-replace-node:

===================
drm_mm_replace_node
===================

*man drm_mm_replace_node(9)*

*4.6.0-rc1*

move an allocation from ``old`` to ``new``


Synopsis
========

.. c:function:: void drm_mm_replace_node( struct drm_mm_node * old, struct drm_mm_node * new )

Arguments
=========

``old``
    drm_mm_node to remove from the allocator

``new``
    drm_mm_node which should inherit ``old``'s allocation


Description
===========

This is useful for when drivers embed the drm_mm_node structure and hence can't move allocations by reassigning pointers. It's a combination of remove and insert with the
guarantee that the allocation start will match.
