
.. _API-drm-gem-object-reference:

========================
drm_gem_object_reference
========================

*man drm_gem_object_reference(9)*

*4.6.0-rc1*

acquire a GEM BO reference


Synopsis
========

.. c:function:: void drm_gem_object_reference( struct drm_gem_object * obj )

Arguments
=========

``obj``
    GEM buffer object


Description
===========

This acquires additional reference to ``obj``. It is illegal to call this without already holding a reference. No locks required.
