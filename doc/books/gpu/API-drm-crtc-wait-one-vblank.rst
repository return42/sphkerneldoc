
.. _API-drm-crtc-wait-one-vblank:

========================
drm_crtc_wait_one_vblank
========================

*man drm_crtc_wait_one_vblank(9)*

*4.6.0-rc1*

wait for one vblank


Synopsis
========

.. c:function:: void drm_crtc_wait_one_vblank( struct drm_crtc * crtc )

Arguments
=========

``crtc``
    DRM crtc


Description
===========

This waits for one vblank to pass on ``crtc``, using the irq driver interfaces. It is a failure to call this when the vblank irq for ``crtc`` is disabled, e.g. due to lack of
driver support or because the crtc is off.
