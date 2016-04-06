
.. _API-drm-vma-offset-manager-destroy:

==============================
drm_vma_offset_manager_destroy
==============================

*man drm_vma_offset_manager_destroy(9)*

*4.6.0-rc1*

Destroy offset manager


Synopsis
========

.. c:function:: void drm_vma_offset_manager_destroy( struct drm_vma_offset_manager * mgr )

Arguments
=========

``mgr``
    Manager object


Description
===========

Destroy an object manager which was previously created via ``drm_vma_offset_manager_init``. The caller must remove all allocated nodes before destroying the manager. Otherwise,
drm_mm will refuse to free the requested resources.

The manager must not be accessed after this function is called.
