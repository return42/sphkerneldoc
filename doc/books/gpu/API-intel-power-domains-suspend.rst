
.. _API-intel-power-domains-suspend:

===========================
intel_power_domains_suspend
===========================

*man intel_power_domains_suspend(9)*

*4.6.0-rc1*

suspend power domain state


Synopsis
========

.. c:function:: void intel_power_domains_suspend( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

This function prepares the hardware power domain state before entering system suspend. It must be paired with ``intel_power_domains_init_hw``.
