
.. _API-drm-vma-offset-remove:

=====================
drm_vma_offset_remove
=====================

*man drm_vma_offset_remove(9)*

*4.6.0-rc1*

Remove offset node from manager


Synopsis
========

.. c:function:: void drm_vma_offset_remove( struct drm_vma_offset_manager * mgr, struct drm_vma_offset_node * node )

Arguments
=========

``mgr``
    Manager object

``node``
    Node to be removed


Description
===========

Remove a node from the offset manager. If the node wasn't added before, this does nothing. After this call returns, the offset and size will be 0 until a new offset is allocated
via ``drm_vma_offset_add`` again. Helper functions like ``drm_vma_node_start`` and ``drm_vma_node_offset_addr`` will return 0 if no offset is allocated.
