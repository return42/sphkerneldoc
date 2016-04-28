.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-uncore-forcewake-put:

==========================
intel_uncore_forcewake_put
==========================

*man intel_uncore_forcewake_put(9)*

*4.6.0-rc5*

release a forcewake domain reference


Synopsis
========

.. c:function:: void intel_uncore_forcewake_put( struct drm_i915_private * dev_priv, enum forcewake_domains fw_domains )

Arguments
=========

``dev_priv``
    i915 device instance

``fw_domains``
    forcewake domains to put references


Description
===========

This function drops the device-level forcewakes for specified domains
obtained by ``intel_uncore_forcewake_get``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
