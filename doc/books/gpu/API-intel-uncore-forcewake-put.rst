
.. _API-intel-uncore-forcewake-put:

==========================
intel_uncore_forcewake_put
==========================

*man intel_uncore_forcewake_put(9)*

*4.6.0-rc1*

release a forcewake domain reference


Synopsis
========

.. c:function:: void intel_uncore_forcewake_put( struct drm_i915_private * dev_priv, enum forcewake_domains fw_domains )

Arguments
=========

``dev_priv``
    i915 device instance

``fw_domains``
    forcewake domains to put references


Description
===========

This function drops the device-level forcewakes for specified domains obtained by ``intel_uncore_forcewake_get``.
