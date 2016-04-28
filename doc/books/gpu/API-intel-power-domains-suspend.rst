.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-power-domains-suspend:

===========================
intel_power_domains_suspend
===========================

*man intel_power_domains_suspend(9)*

*4.6.0-rc5*

suspend power domain state


Synopsis
========

.. c:function:: void intel_power_domains_suspend( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

This function prepares the hardware power domain state before entering
system suspend. It must be paired with ``intel_power_domains_init_hw``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
