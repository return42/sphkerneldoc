.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-uncore-forcewake-get--locked:

==================================
intel_uncore_forcewake_get__locked
==================================

*man intel_uncore_forcewake_get__locked(9)*

*4.6.0-rc5*

grab forcewake domain references


Synopsis
========

.. c:function:: void intel_uncore_forcewake_get__locked( struct drm_i915_private * dev_priv, enum forcewake_domains fw_domains )

Arguments
=========

``dev_priv``
    i915 device instance

``fw_domains``
    forcewake domains to get reference on


Description
===========

See ``intel_uncore_forcewake_get``. This variant places the onus on the
caller to explicitly handle the dev_priv->uncore.lock spinlock.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
