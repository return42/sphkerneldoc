
.. _API-intel-runtime-pm-get:

====================
intel_runtime_pm_get
====================

*man intel_runtime_pm_get(9)*

*4.6.0-rc1*

grab a runtime pm reference


Synopsis
========

.. c:function:: void intel_runtime_pm_get( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

This function grabs a device-level runtime pm reference (mostly used for GEM code to ensure the GTT or GT is on) and ensures that it is powered up.

Any runtime pm reference obtained by this function must have a symmetric call to ``intel_runtime_pm_put`` to release the reference again.
