
.. _API-drm-gem-create-mmap-offset:

==========================
drm_gem_create_mmap_offset
==========================

*man drm_gem_create_mmap_offset(9)*

*4.6.0-rc1*

create a fake mmap offset for an object


Synopsis
========

.. c:function:: int drm_gem_create_mmap_offset( struct drm_gem_object * obj )

Arguments
=========

``obj``
    obj in question


Description
===========

GEM memory mapping works by handing back to userspace a fake mmap offset it can use in a subsequent mmap(2) call. The DRM core code then looks up the object based on the offset and
sets up the various memory mapping structures.

This routine allocates and attaches a fake offset for ``obj``.
