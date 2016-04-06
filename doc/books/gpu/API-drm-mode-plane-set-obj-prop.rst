
.. _API-drm-mode-plane-set-obj-prop:

===========================
drm_mode_plane_set_obj_prop
===========================

*man drm_mode_plane_set_obj_prop(9)*

*4.6.0-rc1*

set the value of a property


Synopsis
========

.. c:function:: int drm_mode_plane_set_obj_prop( struct drm_plane * plane, struct drm_property * property, uint64_t value )

Arguments
=========

``plane``
    drm plane object to set property value for

``property``
    property to set

``value``
    value the property should be set to


Description
===========

This functions sets a given property on a given plane object. This function calls the driver's ->set_property callback and changes the software state of the property if the
callback succeeds.


Returns
=======

Zero on success, error code on failure.
