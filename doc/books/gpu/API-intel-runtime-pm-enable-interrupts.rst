.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-runtime-pm-enable-interrupts:

==================================
intel_runtime_pm_enable_interrupts
==================================

*man intel_runtime_pm_enable_interrupts(9)*

*4.6.0-rc5*

runtime interrupt enabling


Synopsis
========

.. c:function:: void intel_runtime_pm_enable_interrupts( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

This function is used to enable interrupts at runtime, both in the
runtime pm and the system suspend/resume code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
