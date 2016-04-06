
.. _API-intel-uncore-forcewake-put--locked:

==================================
intel_uncore_forcewake_put__locked
==================================

*man intel_uncore_forcewake_put__locked(9)*

*4.6.0-rc1*

grab forcewake domain references


Synopsis
========

.. c:function:: void intel_uncore_forcewake_put__locked( struct drm_i915_private * dev_priv, enum forcewake_domains fw_domains )

Arguments
=========

``dev_priv``
    i915 device instance

``fw_domains``
    forcewake domains to get reference on


Description
===========

See ``intel_uncore_forcewake_put``. This variant places the onus on the caller to explicitly handle the dev_priv->uncore.lock spinlock.
