
.. _API-drm-mode-crtc-set-gamma-size:

============================
drm_mode_crtc_set_gamma_size
============================

*man drm_mode_crtc_set_gamma_size(9)*

*4.6.0-rc1*

set the gamma table size


Synopsis
========

.. c:function:: int drm_mode_crtc_set_gamma_size( struct drm_crtc * crtc, int gamma_size )

Arguments
=========

``crtc``
    CRTC to set the gamma table size for

``gamma_size``
    size of the gamma table


Description
===========

Drivers which support gamma tables should set this to the supported gamma table size when initializing the CRTC. Currently the drm core only supports a fixed gamma table size.


Returns
=======

Zero on success, negative errno on failure.
