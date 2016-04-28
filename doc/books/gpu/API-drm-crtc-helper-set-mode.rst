.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-crtc-helper-set-mode:

========================
drm_crtc_helper_set_mode
========================

*man drm_crtc_helper_set_mode(9)*

*4.6.0-rc5*

internal helper to set a mode


Synopsis
========

.. c:function:: bool drm_crtc_helper_set_mode( struct drm_crtc * crtc, struct drm_display_mode * mode, int x, int y, struct drm_framebuffer * old_fb )

Arguments
=========

``crtc``
    CRTC to program

``mode``
    mode to use

``x``
    horizontal offset into the surface

``y``
    vertical offset into the surface

``old_fb``
    old framebuffer, for cleanup


Description
===========

Try to set ``mode`` on ``crtc``. Give ``crtc`` and its associated
connectors a chance to fixup or reject the mode prior to trying to set
it. This is an internal helper that drivers could e.g. use to update
properties that require the entire output pipe to be disabled and
re-enabled in a new configuration. For example for changing whether
audio is enabled on a hdmi link or for changing panel fitter or dither
attributes. It is also called by the ``drm_crtc_helper_set_config``
helper function to drive the mode setting sequence.


Returns
=======

True if the mode was set successfully, false otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
