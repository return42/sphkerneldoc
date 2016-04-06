
.. _API-drm-gem-object-unreference-unlocked:

===================================
drm_gem_object_unreference_unlocked
===================================

*man drm_gem_object_unreference_unlocked(9)*

*4.6.0-rc1*

release a GEM BO reference


Synopsis
========

.. c:function:: void drm_gem_object_unreference_unlocked( struct drm_gem_object * obj )

Arguments
=========

``obj``
    GEM buffer object


Description
===========

This releases a reference to ``obj``. Callers must not hold the dev->struct_mutex lock when calling this function.
