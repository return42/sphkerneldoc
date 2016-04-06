
.. _API-drm-modeset-unlock-crtc:

=======================
drm_modeset_unlock_crtc
=======================

*man drm_modeset_unlock_crtc(9)*

*4.6.0-rc1*

drop crtc lock


Synopsis
========

.. c:function:: void drm_modeset_unlock_crtc( struct drm_crtc * crtc )

Arguments
=========

``crtc``
    drm crtc


Description
===========

This drops the crtc lock acquire with ``drm_modeset_lock_crtc`` and all other locks acquired through the hidden context.
