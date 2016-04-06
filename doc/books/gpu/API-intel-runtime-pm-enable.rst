
.. _API-intel-runtime-pm-enable:

=======================
intel_runtime_pm_enable
=======================

*man intel_runtime_pm_enable(9)*

*4.6.0-rc1*

enable runtime pm


Synopsis
========

.. c:function:: void intel_runtime_pm_enable( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

This function enables runtime pm at the end of the driver load sequence.

Note that this function does currently not enable runtime pm for the subordinate display power domains. That is only done on the first modeset using
``intel_display_set_init_power``.
