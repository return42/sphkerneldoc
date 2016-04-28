.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-power-domains-init:

========================
intel_power_domains_init
========================

*man intel_power_domains_init(9)*

*4.6.0-rc5*

initializes the power domain structures


Synopsis
========

.. c:function:: int intel_power_domains_init( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

Initializes the power domain structures for ``dev_priv`` depending upon
the supported platform.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
