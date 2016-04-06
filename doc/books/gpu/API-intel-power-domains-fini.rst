
.. _API-intel-power-domains-fini:

========================
intel_power_domains_fini
========================

*man intel_power_domains_fini(9)*

*4.6.0-rc1*

finalizes the power domain structures


Synopsis
========

.. c:function:: void intel_power_domains_fini( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

Finalizes the power domain structures for ``dev_priv`` depending upon the supported platform. This function also disables runtime pm and ensures that the device stays powered up so
that the driver can be reloaded.
