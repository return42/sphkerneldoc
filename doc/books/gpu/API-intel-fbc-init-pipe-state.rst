
.. _API-intel-fbc-init-pipe-state:

=========================
intel_fbc_init_pipe_state
=========================

*man intel_fbc_init_pipe_state(9)*

*4.6.0-rc1*

initialize FBC's CRTC visibility tracking


Synopsis
========

.. c:function:: void intel_fbc_init_pipe_state( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

The FBC code needs to track CRTC visibility since the older platforms can't have FBC enabled while multiple pipes are used. This function does the initial setup at driver load to
make sure FBC is matching the real hardware.
