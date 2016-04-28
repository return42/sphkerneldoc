.. -*- coding: utf-8; mode: rst -*-

.. _API---intel-display-power-is-enabled:

================================
__intel_display_power_is_enabled
================================

*man __intel_display_power_is_enabled(9)*

*4.6.0-rc5*

unlocked check for a power domain


Synopsis
========

.. c:function:: bool __intel_display_power_is_enabled( struct drm_i915_private * dev_priv, enum intel_display_power_domain domain )

Arguments
=========

``dev_priv``
    i915 device instance

``domain``
    power domain to check


Description
===========

This is the unlocked version of ``intel_display_power_is_enabled`` and
should only be used from error capture and recovery code where deadlocks
are possible.


Returns
=======

True when the power domain is enabled, false otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
