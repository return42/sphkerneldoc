
.. _API-intel-display-power-get-if-enabled:

==================================
intel_display_power_get_if_enabled
==================================

*man intel_display_power_get_if_enabled(9)*

*4.6.0-rc1*

grab a reference for an enabled display power domain


Synopsis
========

.. c:function:: bool intel_display_power_get_if_enabled( struct drm_i915_private * dev_priv, enum intel_display_power_domain domain )

Arguments
=========

``dev_priv``
    i915 device instance

``domain``
    power domain to reference


Description
===========

This function grabs a power domain reference for ``domain`` and ensures that the power domain and all its parents are powered up. Therefore users should only grab a reference to
the innermost power domain they need.

Any power domain reference obtained by this function must have a symmetric call to ``intel_display_power_put`` to release the reference again.
