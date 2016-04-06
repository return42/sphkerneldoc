
.. _API-intel-display-power-put:

=======================
intel_display_power_put
=======================

*man intel_display_power_put(9)*

*4.6.0-rc1*

release a power domain reference


Synopsis
========

.. c:function:: void intel_display_power_put( struct drm_i915_private * dev_priv, enum intel_display_power_domain domain )

Arguments
=========

``dev_priv``
    i915 device instance

``domain``
    power domain to reference


Description
===========

This function drops the power domain reference obtained by ``intel_display_power_get`` and might power down the corresponding hardware block right away if this is the last
reference.
