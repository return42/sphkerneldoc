
.. _API-drm-vma-node-allow:

==================
drm_vma_node_allow
==================

*man drm_vma_node_allow(9)*

*4.6.0-rc1*

Add open-file to list of allowed users


Synopsis
========

.. c:function:: int drm_vma_node_allow( struct drm_vma_offset_node * node, struct file * filp )

Arguments
=========

``node``
    Node to modify

``filp``
    Open file to add


Description
===========

Add ``filp`` to the list of allowed open-files for this node. If ``filp`` is already on this list, the ref-count is incremented.

The list of allowed-users is preserved across ``drm_vma_offset_add`` and ``drm_vma_offset_remove`` calls. You may even call it if the node is currently not added to any
offset-manager.

You must remove all open-files the same number of times as you added them before destroying the node. Otherwise, you will leak memory.

This is locked against concurrent access internally.


RETURNS
=======

0 on success, negative error code on internal failure (out-of-mem)
