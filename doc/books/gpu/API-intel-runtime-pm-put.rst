
.. _API-intel-runtime-pm-put:

====================
intel_runtime_pm_put
====================

*man intel_runtime_pm_put(9)*

*4.6.0-rc1*

release a runtime pm reference


Synopsis
========

.. c:function:: void intel_runtime_pm_put( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

This function drops the device-level runtime pm reference obtained by ``intel_runtime_pm_get`` and might power down the corresponding hardware block right away if this is the last
reference.
