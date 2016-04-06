
.. _API-drm-mode-create-dvi-i-properties:

================================
drm_mode_create_dvi_i_properties
================================

*man drm_mode_create_dvi_i_properties(9)*

*4.6.0-rc1*

create DVI-I specific connector properties


Synopsis
========

.. c:function:: int drm_mode_create_dvi_i_properties( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device


Description
===========

Called by a driver the first time a DVI-I connector is made.
