.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-set-mode-for-crtc:

============================
drm_atomic_set_mode_for_crtc
============================

*man drm_atomic_set_mode_for_crtc(9)*

*4.6.0-rc5*

set mode for CRTC


Synopsis
========

.. c:function:: int drm_atomic_set_mode_for_crtc( struct drm_crtc_state * state, struct drm_display_mode * mode )

Arguments
=========

``state``
    the CRTC whose incoming state to update

``mode``
    kernel-internal mode to use for the CRTC, or NULL to disable


Description
===========

Set a mode (originating from the kernel) on the desired CRTC state. Does
not change any other state properties, including enable, active, or
mode_changed.


RETURNS
=======

Zero on success, error code on failure. Cannot return -EDEADLK.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
