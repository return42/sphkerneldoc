
.. _API-drm-helper-crtc-in-use:

======================
drm_helper_crtc_in_use
======================

*man drm_helper_crtc_in_use(9)*

*4.6.0-rc1*

check if a given CRTC is in a mode_config


Synopsis
========

.. c:function:: bool drm_helper_crtc_in_use( struct drm_crtc * crtc )

Arguments
=========

``crtc``
    CRTC to check


Description
===========

Checks whether ``crtc`` is with the current mode setting output configuration in use by any connector. This doesn't mean that it is actually enabled since the DPMS state is tracked
separately.


Returns
=======

True if ``crtc`` is used, false otherwise.
