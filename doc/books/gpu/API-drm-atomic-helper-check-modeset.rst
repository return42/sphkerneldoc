.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-helper-check-modeset:

===============================
drm_atomic_helper_check_modeset
===============================

*man drm_atomic_helper_check_modeset(9)*

*4.6.0-rc5*

validate state object for modeset changes


Synopsis
========

.. c:function:: int drm_atomic_helper_check_modeset( struct drm_device * dev, struct drm_atomic_state * state )

Arguments
=========

``dev``
    DRM device

``state``
    the driver state object


Description
===========

Check the state object to see if the requested state is physically
possible. This does all the crtc and connector related computations for
an atomic update and adds any additional connectors needed for full
modesets and calls down into ->mode_fixup functions of the driver
backend.

crtc_state->mode_changed is set when the input mode is changed.
crtc_state->connectors_changed is set when a connector is added or
removed from the crtc. crtc_state->active_changed is set when
crtc_state->active changes, which is used for dpms.


IMPORTANT
=========

Drivers which update ->mode_changed (e.g. in their ->atomic_check
hooks if a plane update can't be done without a full modeset) _must_
call this function afterwards after that change. It is permitted to call
this function multiple times for the same update, e.g. when the
->atomic_check functions depend upon the adjusted dotclock for fifo
space allocation and watermark computation.

RETURNS Zero for success or -errno


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
