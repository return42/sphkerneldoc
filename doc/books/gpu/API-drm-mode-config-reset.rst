
.. _API-drm-mode-config-reset:

=====================
drm_mode_config_reset
=====================

*man drm_mode_config_reset(9)*

*4.6.0-rc1*

call ->reset callbacks


Synopsis
========

.. c:function:: void drm_mode_config_reset( struct drm_device * dev )

Arguments
=========

``dev``
    drm device


Description
===========

This functions calls all the crtc's, encoder's and connector's ->reset callback. Drivers can use this in e.g. their driver load or resume code to reset hardware and software state.
