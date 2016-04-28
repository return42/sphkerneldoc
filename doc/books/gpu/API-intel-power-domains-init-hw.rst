.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-power-domains-init-hw:

===========================
intel_power_domains_init_hw
===========================

*man intel_power_domains_init_hw(9)*

*4.6.0-rc5*

initialize hardware power domain state


Synopsis
========

.. c:function:: void intel_power_domains_init_hw( struct drm_i915_private * dev_priv, bool resume )

Arguments
=========

``dev_priv``
    i915 device instance

``resume``
    -- undescribed --


Description
===========

This function initializes the hardware power domain state and enables
all power domains using ``intel_display_set_init_power``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
