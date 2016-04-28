.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-crtc-get-hv-timing:

======================
drm_crtc_get_hv_timing
======================

*man drm_crtc_get_hv_timing(9)*

*4.6.0-rc5*

Fetches hdisplay/vdisplay for given mode


Synopsis
========

.. c:function:: void drm_crtc_get_hv_timing( const struct drm_display_mode * mode, int * hdisplay, int * vdisplay )

Arguments
=========

``mode``
    mode to query

``hdisplay``
    hdisplay value to fill in

``vdisplay``
    vdisplay value to fill in


Description
===========

The vdisplay value will be doubled if the specified mode is a stereo
mode of the appropriate layout.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
