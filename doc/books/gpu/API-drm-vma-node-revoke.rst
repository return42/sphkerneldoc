
.. _API-drm-vma-node-revoke:

===================
drm_vma_node_revoke
===================

*man drm_vma_node_revoke(9)*

*4.6.0-rc1*

Remove open-file from list of allowed users


Synopsis
========

.. c:function:: void drm_vma_node_revoke( struct drm_vma_offset_node * node, struct file * filp )

Arguments
=========

``node``
    Node to modify

``filp``
    Open file to remove


Description
===========

Decrement the ref-count of ``filp`` in the list of allowed open-files on ``node``. If the ref-count drops to zero, remove ``filp`` from the list. You must call this once for every
``drm_vma_node_allow`` on ``filp``.

This is locked against concurrent access internally.

If ``filp`` is not on the list, nothing is done.
