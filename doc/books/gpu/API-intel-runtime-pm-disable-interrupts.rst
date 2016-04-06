
.. _API-intel-runtime-pm-disable-interrupts:

===================================
intel_runtime_pm_disable_interrupts
===================================

*man intel_runtime_pm_disable_interrupts(9)*

*4.6.0-rc1*

runtime interrupt disabling


Synopsis
========

.. c:function:: void intel_runtime_pm_disable_interrupts( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

This function is used to disable interrupts at runtime, both in the runtime pm and the system suspend/resume code.
