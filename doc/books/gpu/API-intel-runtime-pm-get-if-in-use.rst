.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-runtime-pm-get-if-in-use:

==============================
intel_runtime_pm_get_if_in_use
==============================

*man intel_runtime_pm_get_if_in_use(9)*

*4.6.0-rc5*

grab a runtime pm reference if device in use


Synopsis
========

.. c:function:: bool intel_runtime_pm_get_if_in_use( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

This function grabs a device-level runtime pm reference if the device is
already in use and ensures that it is powered up.

Any runtime pm reference obtained by this function must have a symmetric
call to ``intel_runtime_pm_put`` to release the reference again.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
