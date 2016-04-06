
.. _API-intel-uncore-forcewake-get:

==========================
intel_uncore_forcewake_get
==========================

*man intel_uncore_forcewake_get(9)*

*4.6.0-rc1*

grab forcewake domain references


Synopsis
========

.. c:function:: void intel_uncore_forcewake_get( struct drm_i915_private * dev_priv, enum forcewake_domains fw_domains )

Arguments
=========

``dev_priv``
    i915 device instance

``fw_domains``
    forcewake domains to get reference on


Description
===========

This function can be used get GT's forcewake domain references. Normal register access will handle the forcewake domains automatically. However if some sequence requires the GT to
not power down a particular forcewake domains this function should be called at the beginning of the sequence. And subsequently the reference should be dropped by symmetric call to
``intel_unforce_forcewake_put``. Usually caller wants all the domains to be kept awake so the ``fw_domains`` would be then FORCEWAKE_ALL.
