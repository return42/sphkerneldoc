
.. _API-drm-mode-set-crtcinfo:

=====================
drm_mode_set_crtcinfo
=====================

*man drm_mode_set_crtcinfo(9)*

*4.6.0-rc1*

set CRTC modesetting timing parameters


Synopsis
========

.. c:function:: void drm_mode_set_crtcinfo( struct drm_display_mode * p, int adjust_flags )

Arguments
=========

``p``
    mode

``adjust_flags``
    a combination of adjustment flags


Description
===========

Setup the CRTC modesetting timing parameters for ``p``, adjusting if necessary.

- The CRTC_INTERLACE_HALVE_V flag can be used to halve vertical timings of interlaced modes. - The CRTC_STEREO_DOUBLE flag can be used to compute the timings for buffers
containing two eyes (only adjust the timings when needed, eg. for “frame packing” or “side by side full”). - The CRTC_NO_DBLSCAN and CRTC_NO_VSCAN flags request that adjustment
⋆not⋆ be performed for doublescan and vscan > 1 modes respectively.
