
.. _API-intel-fbc-choose-crtc:

=====================
intel_fbc_choose_crtc
=====================

*man intel_fbc_choose_crtc(9)*

*4.6.0-rc1*

select a CRTC to enable FBC on


Synopsis
========

.. c:function:: void intel_fbc_choose_crtc( struct drm_i915_private * dev_priv, struct drm_atomic_state * state )

Arguments
=========

``dev_priv``
    i915 device instance

``state``
    the atomic state structure


Description
===========

This function looks at the proposed state for CRTCs and planes, then chooses which pipe is going to have FBC by setting intel_crtc_state->enable_fbc to true.

Later, intel_fbc_enable is going to look for state->enable_fbc and then maybe enable FBC for the chosen CRTC. If it does, it will set dev_priv->fbc.crtc.
