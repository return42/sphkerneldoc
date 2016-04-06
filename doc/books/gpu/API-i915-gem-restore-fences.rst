
.. _API-i915-gem-restore-fences:

=======================
i915_gem_restore_fences
=======================

*man i915_gem_restore_fences(9)*

*4.6.0-rc1*

restore fence state


Synopsis
========

.. c:function:: void i915_gem_restore_fences( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device


Description
===========

Restore the hw fence state to match the software tracking again, to be called after a gpu reset and on resume.
