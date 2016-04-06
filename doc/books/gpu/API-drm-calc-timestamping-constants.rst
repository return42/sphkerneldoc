
.. _API-drm-calc-timestamping-constants:

===============================
drm_calc_timestamping_constants
===============================

*man drm_calc_timestamping_constants(9)*

*4.6.0-rc1*

calculate vblank timestamp constants


Synopsis
========

.. c:function:: void drm_calc_timestamping_constants( struct drm_crtc * crtc, const struct drm_display_mode * mode )

Arguments
=========

``crtc``
    drm_crtc whose timestamp constants should be updated.

``mode``
    display mode containing the scanout timings


Description
===========

Calculate and store various constants which are later needed by vblank and swap-completion timestamping, e.g, by ``drm_calc_vbltimestamp_from_scanoutpos``. They are derived from
CRTC's true scanout timing, so they take things like panel scaling or other adjustments into account.
