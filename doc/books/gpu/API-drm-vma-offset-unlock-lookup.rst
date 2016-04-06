
.. _API-drm-vma-offset-unlock-lookup:

============================
drm_vma_offset_unlock_lookup
============================

*man drm_vma_offset_unlock_lookup(9)*

*4.6.0-rc1*

Unlock lookup for extended private use


Synopsis
========

.. c:function:: void drm_vma_offset_unlock_lookup( struct drm_vma_offset_manager * mgr )

Arguments
=========

``mgr``
    Manager object


Description
===========

Release lookup-lock. See ``drm_vma_offset_lock_lookup`` for more information.
