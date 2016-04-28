.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-fbc-global-disable:

========================
intel_fbc_global_disable
========================

*man intel_fbc_global_disable(9)*

*4.6.0-rc5*

globally disable FBC


Synopsis
========

.. c:function:: void intel_fbc_global_disable( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

This function disables FBC regardless of which CRTC is associated with
it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
