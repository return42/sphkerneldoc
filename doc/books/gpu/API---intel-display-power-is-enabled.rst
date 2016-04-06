
.. _API---intel-display-power-is-enabled:

================================
__intel_display_power_is_enabled
================================

*man __intel_display_power_is_enabled(9)*

*4.6.0-rc1*

unlocked check for a power domain


Synopsis
========

.. c:function:: bool __intel_display_power_is_enabled( struct drm_i915_private * dev_priv, enum intel_display_power_domain domain )

Arguments
=========

``dev_priv``
    i915 device instance

``domain``
    power domain to check


Description
===========

This is the unlocked version of ``intel_display_power_is_enabled`` and should only be used from error capture and recovery code where deadlocks are possible.


Returns
=======

True when the power domain is enabled, false otherwise.
