
.. _API-intel-power-domains-init:

========================
intel_power_domains_init
========================

*man intel_power_domains_init(9)*

*4.6.0-rc1*

initializes the power domain structures


Synopsis
========

.. c:function:: int intel_power_domains_init( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

Initializes the power domain structures for ``dev_priv`` depending upon the supported platform.
