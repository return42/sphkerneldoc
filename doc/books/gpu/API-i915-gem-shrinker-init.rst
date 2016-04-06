
.. _API-i915-gem-shrinker-init:

======================
i915_gem_shrinker_init
======================

*man i915_gem_shrinker_init(9)*

*4.6.0-rc1*

Initialize i915 shrinker


Synopsis
========

.. c:function:: void i915_gem_shrinker_init( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device


Description
===========

This function registers and sets up the i915 shrinker and OOM handler.
