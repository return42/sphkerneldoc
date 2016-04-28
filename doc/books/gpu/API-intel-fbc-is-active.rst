.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-fbc-is-active:

===================
intel_fbc_is_active
===================

*man intel_fbc_is_active(9)*

*4.6.0-rc5*

Is FBC active?


Synopsis
========

.. c:function:: bool intel_fbc_is_active( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

This function is used to verify the current state of FBC.


FIXME
=====

This should be tracked in the plane config eventually instead of queried
at runtime for most callers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
