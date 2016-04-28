.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-runtime-pm-get-noresume:

=============================
intel_runtime_pm_get_noresume
=============================

*man intel_runtime_pm_get_noresume(9)*

*4.6.0-rc5*

grab a runtime pm reference


Synopsis
========

.. c:function:: void intel_runtime_pm_get_noresume( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

This function grabs a device-level runtime pm reference (mostly used for
GEM code to ensure the GTT or GT is on).

It will _not_ power up the device but instead only check that it's
powered on. Therefore it is only valid to call this functions from
contexts where the device is known to be powered up and where trying to
power it up would result in hilarity and deadlocks. That pretty much
means only the system suspend/resume code where this is used to grab
runtime pm references for delayed setup down in work items.

Any runtime pm reference obtained by this function must have a symmetric
call to ``intel_runtime_pm_put`` to release the reference again.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
