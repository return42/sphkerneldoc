
.. _API-drm-vma-node-verify-access:

==========================
drm_vma_node_verify_access
==========================

*man drm_vma_node_verify_access(9)*

*4.6.0-rc1*

Access verification helper for TTM


Synopsis
========

.. c:function:: int drm_vma_node_verify_access( struct drm_vma_offset_node * node, struct file * filp )

Arguments
=========

``node``
    Offset node

``filp``
    Open-file


Description
===========

This checks whether ``filp`` is granted access to ``node``. It is the same as ``drm_vma_node_is_allowed`` but suitable as drop-in helper for TTM ``verify_access`` callbacks.


RETURNS
=======

0 if access is granted, -EACCES otherwise.
