
.. _API-drm-mode-config-init:

====================
drm_mode_config_init
====================

*man drm_mode_config_init(9)*

*4.6.0-rc1*

initialize DRM mode_configuration structure


Synopsis
========

.. c:function:: void drm_mode_config_init( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device


Description
===========

Initialize ``dev``'s mode_config structure, used for tracking the graphics configuration of ``dev``.

Since this initializes the modeset locks, no locking is possible. Which is no problem, since this should happen single threaded at init time. It is the driver's problem to ensure
this guarantee.
