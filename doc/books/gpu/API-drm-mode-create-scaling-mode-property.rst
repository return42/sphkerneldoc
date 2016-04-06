
.. _API-drm-mode-create-scaling-mode-property:

=====================================
drm_mode_create_scaling_mode_property
=====================================

*man drm_mode_create_scaling_mode_property(9)*

*4.6.0-rc1*

create scaling mode property


Synopsis
========

.. c:function:: int drm_mode_create_scaling_mode_property( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device


Description
===========

Called by a driver the first time it's needed, must be attached to desired connectors.
