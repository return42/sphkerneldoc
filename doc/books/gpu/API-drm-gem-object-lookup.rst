
.. _API-drm-gem-object-lookup:

=====================
drm_gem_object_lookup
=====================

*man drm_gem_object_lookup(9)*

*4.6.0-rc1*

look up a GEM object from it's handle


Synopsis
========

.. c:function:: struct drm_gem_object ⋆ drm_gem_object_lookup( struct drm_device * dev, struct drm_file * filp, u32 handle )

Arguments
=========

``dev``
    DRM device

``filp``
    DRM file private date

``handle``
    userspace handle


Returns
=======

A reference to the object named by the handle if such exists on ``filp``, NULL otherwise.
