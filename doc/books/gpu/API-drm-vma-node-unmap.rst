
.. _API-drm-vma-node-unmap:

==================
drm_vma_node_unmap
==================

*man drm_vma_node_unmap(9)*

*4.6.0-rc1*

Unmap offset node


Synopsis
========

.. c:function:: void drm_vma_node_unmap( struct drm_vma_offset_node * node, struct address_space * file_mapping )

Arguments
=========

``node``
    Offset node

``file_mapping``
    Address space to unmap ``node`` from


Description
===========

Unmap all userspace mappings for a given offset node. The mappings must be associated with the ``file_mapping`` address-space. If no offset exists nothing is done.

This call is unlocked. The caller must guarantee that ``drm_vma_offset_remove`` is not called on this node concurrently.
