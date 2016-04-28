.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-property-create:

===================
drm_property_create
===================

*man drm_property_create(9)*

*4.6.0-rc5*

create a new property type


Synopsis
========

.. c:function:: struct drm_property * drm_property_create( struct drm_device * dev, int flags, const char * name, int num_values )

Arguments
=========

``dev``
    drm device

``flags``
    flags specifying the property type

``name``
    name of the property

``num_values``
    number of pre-defined values


Description
===========

This creates a new generic drm property which can then be attached to a
drm object with drm_object_attach_property. The returned property
object must be freed with drm_property_destroy.

Note that the DRM core keeps a per-device list of properties and that,
if ``drm_mode_config_cleanup`` is called, it will destroy all properties
created by the driver.


Returns
=======

A pointer to the newly created property on success, NULL on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
