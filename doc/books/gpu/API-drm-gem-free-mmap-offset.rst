
.. _API-drm-gem-free-mmap-offset:

========================
drm_gem_free_mmap_offset
========================

*man drm_gem_free_mmap_offset(9)*

*4.6.0-rc1*

release a fake mmap offset for an object


Synopsis
========

.. c:function:: void drm_gem_free_mmap_offset( struct drm_gem_object * obj )

Arguments
=========

``obj``
    obj in question


Description
===========

This routine frees fake offsets allocated by ``drm_gem_create_mmap_offset``.
