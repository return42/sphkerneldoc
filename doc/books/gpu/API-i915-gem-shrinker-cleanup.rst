.. -*- coding: utf-8; mode: rst -*-

.. _API-i915-gem-shrinker-cleanup:

=========================
i915_gem_shrinker_cleanup
=========================

*man i915_gem_shrinker_cleanup(9)*

*4.6.0-rc5*

Clean up i915 shrinker


Synopsis
========

.. c:function:: void i915_gem_shrinker_cleanup( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device


Description
===========

This function unregisters the i915 shrinker and OOM handler.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
