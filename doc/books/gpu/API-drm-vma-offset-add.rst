
.. _API-drm-vma-offset-add:

==================
drm_vma_offset_add
==================

*man drm_vma_offset_add(9)*

*4.6.0-rc1*

Add offset node to manager


Synopsis
========

.. c:function:: int drm_vma_offset_add( struct drm_vma_offset_manager * mgr, struct drm_vma_offset_node * node, unsigned long pages )

Arguments
=========

``mgr``
    Manager object

``node``
    Node to be added

``pages``
    Allocation size visible to user-space (in number of pages)


Description
===========

Add a node to the offset-manager. If the node was already added, this does nothing and return 0. ``pages`` is the size of the object given in number of pages. After this call
succeeds, you can access the offset of the node until it is removed again.

If this call fails, it is safe to retry the operation or call ``drm_vma_offset_remove``, anyway. However, no cleanup is required in that case.

``pages`` is not required to be the same size as the underlying memory object that you want to map. It only limits the size that user-space can map into their address space.


RETURNS
=======

0 on success, negative error code on failure.
