
.. _API-drm-mm-for-each-node:

====================
drm_mm_for_each_node
====================

*man drm_mm_for_each_node(9)*

*4.6.0-rc1*

iterator to walk over all allocated nodes


Synopsis
========

.. c:function:: drm_mm_for_each_node( entry, mm )

Arguments
=========

``entry``
    drm_mm_node structure to assign to in each iteration step

``mm``
    drm_mm allocator to walk


Description
===========

This iterator walks over all nodes in the range allocator. It is implemented with list_for_each, so not save against removal of elements.
