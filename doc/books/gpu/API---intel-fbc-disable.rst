
.. _API---intel-fbc-disable:

===================
__intel_fbc_disable
===================

*man __intel_fbc_disable(9)*

*4.6.0-rc1*

disable FBC


Synopsis
========

.. c:function:: void __intel_fbc_disable( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

This is the low level function that actually disables FBC. Callers should grab the FBC lock.
