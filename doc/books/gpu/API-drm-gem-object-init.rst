
.. _API-drm-gem-object-init:

===================
drm_gem_object_init
===================

*man drm_gem_object_init(9)*

*4.6.0-rc1*

initialize an allocated shmem-backed GEM object


Synopsis
========

.. c:function:: int drm_gem_object_init( struct drm_device * dev, struct drm_gem_object * obj, size_t size )

Arguments
=========

``dev``
    drm_device the object should be initialized for

``obj``
    drm_gem_object to initialize

``size``
    object size


Description
===========

Initialize an already allocated GEM object of the specified size with shmfs backing store.
