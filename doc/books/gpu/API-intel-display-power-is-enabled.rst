
.. _API-intel-display-power-is-enabled:

==============================
intel_display_power_is_enabled
==============================

*man intel_display_power_is_enabled(9)*

*4.6.0-rc1*

check for a power domain


Synopsis
========

.. c:function:: bool intel_display_power_is_enabled( struct drm_i915_private * dev_priv, enum intel_display_power_domain domain )

Arguments
=========

``dev_priv``
    i915 device instance

``domain``
    power domain to check


Description
===========

This function can be used to check the hw power domain state. It is mostly used in hardware state readout functions. Everywhere else code should rely upon explicit power domain
reference counting to ensure that the hardware block is powered up before accessing it.

Callers must hold the relevant modesetting locks to ensure that concurrent threads can't disable the power well while the caller tries to read a few registers.


Returns
=======

True when the power domain is enabled, false otherwise.
