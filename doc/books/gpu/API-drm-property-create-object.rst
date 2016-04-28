.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-property-create-object:

==========================
drm_property_create_object
==========================

*man drm_property_create_object(9)*

*4.6.0-rc5*

create a new object property type


Synopsis
========

.. c:function:: struct drm_property * drm_property_create_object( struct drm_device * dev, int flags, const char * name, uint32_t type )

Arguments
=========

``dev``
    drm device

``flags``
    flags specifying the property type

``name``
    name of the property

``type``
    object type from DRM_MODE_OBJECT_* defines


Description
===========

This creates a new generic drm property which can then be attached to a
drm object with drm_object_attach_property. The returned property
object must be freed with drm_property_destroy.

Userspace is only allowed to set this to any property value of the given
``type``. Only useful for atomic properties, which is enforced.


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
