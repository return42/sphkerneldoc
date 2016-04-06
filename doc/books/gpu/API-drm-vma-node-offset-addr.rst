
.. _API-drm-vma-node-offset-addr:

========================
drm_vma_node_offset_addr
========================

*man drm_vma_node_offset_addr(9)*

*4.6.0-rc1*

Return sanitized offset for user-space mmaps


Synopsis
========

.. c:function:: __u64 drm_vma_node_offset_addr( struct drm_vma_offset_node * node )

Arguments
=========

``node``
    Linked offset node


Description
===========

Same as ``drm_vma_node_start`` but returns the address as a valid offset that can be used for user-space mappings during ``mmap``. This must not be called on unlinked nodes.


RETURNS
=======

Offset of ``node`` for byte-based addressing. 0 if the node does not have an object allocated.
