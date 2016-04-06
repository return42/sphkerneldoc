
.. _API-drm-plane-force-disable:

=======================
drm_plane_force_disable
=======================

*man drm_plane_force_disable(9)*

*4.6.0-rc1*

Forcibly disable a plane


Synopsis
========

.. c:function:: void drm_plane_force_disable( struct drm_plane * plane )

Arguments
=========

``plane``
    plane to disable


Description
===========

Forces the plane to be disabled.

Used when the plane's current framebuffer is destroyed, and when restoring fbdev mode.
