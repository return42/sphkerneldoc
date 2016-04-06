
.. _API-drm-atomic-helper-set-config:

============================
drm_atomic_helper_set_config
============================

*man drm_atomic_helper_set_config(9)*

*4.6.0-rc1*

set a new config from userspace


Synopsis
========

.. c:function:: int drm_atomic_helper_set_config( struct drm_mode_set * set )

Arguments
=========

``set``
    mode set configuration


Description
===========

Provides a default crtc set_config handler using the atomic driver interface.


Returns
=======

Returns 0 on success, negative errno numbers on failure.
