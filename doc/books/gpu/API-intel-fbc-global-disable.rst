
.. _API-intel-fbc-global-disable:

========================
intel_fbc_global_disable
========================

*man intel_fbc_global_disable(9)*

*4.6.0-rc1*

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

This function disables FBC regardless of which CRTC is associated with it.
