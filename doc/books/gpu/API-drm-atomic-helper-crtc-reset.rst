
.. _API-drm-atomic-helper-crtc-reset:

============================
drm_atomic_helper_crtc_reset
============================

*man drm_atomic_helper_crtc_reset(9)*

*4.6.0-rc1*

default ->reset hook for CRTCs


Synopsis
========

.. c:function:: void drm_atomic_helper_crtc_reset( struct drm_crtc * crtc )

Arguments
=========

``crtc``
    drm CRTC


Description
===========

Resets the atomic state for ``crtc`` by freeing the state pointer (which might be NULL, e.g. at driver load time) and allocating a new empty state object.
