.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-runtime-pm-put:

====================
intel_runtime_pm_put
====================

*man intel_runtime_pm_put(9)*

*4.6.0-rc5*

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

This function drops the device-level runtime pm reference obtained by
``intel_runtime_pm_get`` and might power down the corresponding hardware
block right away if this is the last reference.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
