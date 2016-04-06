
.. _API-drm-helper-disable-unused-functions:

===================================
drm_helper_disable_unused_functions
===================================

*man drm_helper_disable_unused_functions(9)*

*4.6.0-rc1*

disable unused objects


Synopsis
========

.. c:function:: void drm_helper_disable_unused_functions( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device


Description
===========

This function walks through the entire mode setting configuration of ``dev``. It will remove any CRTC links of unused encoders and encoder links of disconnected connectors. Then it
will disable all unused encoders and CRTCs either by calling their disable callback if available or by calling their dpms callback with DRM_MODE_DPMS_OFF.


NOTE
====

This function is part of the legacy modeset helper library and will cause major confusion with atomic drivers. This is because atomic helpers guarantee to never call ->``disable``
hooks on a disabled function, or ->``enable`` hooks on an enabled functions. ``drm_helper_disable_unused_functions`` on the other hand throws such guarantees into the wind and
calls disable hooks unconditionally on unused functions.
