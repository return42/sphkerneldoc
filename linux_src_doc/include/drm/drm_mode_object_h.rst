.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_mode_object.h

.. _`drm_mode_object`:

struct drm_mode_object
======================

.. c:type:: struct drm_mode_object

    base structure for modeset objects

.. _`drm_mode_object.definition`:

Definition
----------

.. code-block:: c

    struct drm_mode_object {
        uint32_t id;
        uint32_t type;
        struct drm_object_properties *properties;
        struct kref refcount;
        void (*free_cb)(struct kref *kref);
    }

.. _`drm_mode_object.members`:

Members
-------

id
    userspace visible identifier

type
    type of the object, one of DRM_MODE_OBJECT\_\*

properties
    properties attached to this object, including values

refcount
    reference count for objects which with dynamic lifetime

free_cb
    free function callback, only set for objects with dynamic lifetime

.. _`drm_mode_object.description`:

Description
-----------

Base structure for modeset objects visible to userspace. Objects can be
looked up using \ :c:func:`drm_mode_object_find`\ . Besides basic uapi interface
properties like \ ``id``\  and \ ``type``\  it provides two services:

- It tracks attached properties and their values. This is used by \ :c:type:`struct drm_crtc <drm_crtc>`\ ,
  \ :c:type:`struct drm_plane <drm_plane>`\  and \ :c:type:`struct drm_connector <drm_connector>`\ . Properties are attached by calling
  \ :c:func:`drm_object_attach_property`\  before the object is visible to userspace.

- For objects with dynamic lifetimes (as indicated by a non-NULL \ ``free_cb``\ ) it
  provides reference counting through \ :c:func:`drm_mode_object_get`\  and
  \ :c:func:`drm_mode_object_put`\ . This is used by \ :c:type:`struct drm_framebuffer <drm_framebuffer>`\ , \ :c:type:`struct drm_connector <drm_connector>`\ 
  and \ :c:type:`struct drm_property_blob <drm_property_blob>`\ . These objects provide specialized reference
  counting wrappers.

.. _`drm_object_properties`:

struct drm_object_properties
============================

.. c:type:: struct drm_object_properties

    property tracking for \ :c:type:`struct drm_mode_object <drm_mode_object>`\ 

.. _`drm_object_properties.definition`:

Definition
----------

.. code-block:: c

    struct drm_object_properties {
        int count;
        struct drm_property *properties[DRM_OBJECT_MAX_PROPERTY];
        uint64_t values[DRM_OBJECT_MAX_PROPERTY];
    }

.. _`drm_object_properties.members`:

Members
-------

count
    number of valid properties, must be less than or equal toDRM_OBJECT_MAX_PROPERTY.

properties
    Array of pointers to \ :c:type:`struct drm_property <drm_property>`\ .
    NOTE: if we ever start dynamically destroying properties (ie.
    not at \ :c:func:`drm_mode_config_cleanup`\  time), then we'd have to do
    a better job of detaching property from mode objects to avoid
    dangling property pointers:

values
    Array to store the property values, matching \ ``properties``\ . Donot read/write values directly, but use
    \ :c:func:`drm_object_property_get_value`\  and \ :c:func:`drm_object_property_set_value`\ .

    Note that atomic drivers do not store mutable properties in this
    array, but only the decoded values in the corresponding state
    structure. The decoding is done using the \ :c:type:`drm_crtc.atomic_get_property <drm_crtc>`\  and
    \ :c:type:`drm_crtc.atomic_set_property <drm_crtc>`\  hooks for \ :c:type:`struct drm_crtc <drm_crtc>`\ . For
    \ :c:type:`struct drm_plane <drm_plane>`\  the hooks are \ :c:type:`drm_plane_funcs.atomic_get_property <drm_plane_funcs>`\  and
    \ :c:type:`drm_plane_funcs.atomic_set_property <drm_plane_funcs>`\ . And for \ :c:type:`struct drm_connector <drm_connector>`\ 
    the hooks are \ :c:type:`drm_connector_funcs.atomic_get_property <drm_connector_funcs>`\  and
    \ :c:type:`drm_connector_funcs.atomic_set_property <drm_connector_funcs>`\  .

    Hence atomic drivers should not use \ :c:func:`drm_object_property_set_value`\ 
    and \ :c:func:`drm_object_property_get_value`\  on mutable objects, i.e. those
    without the DRM_MODE_PROP_IMMUTABLE flag set.

.. This file was automatic generated / don't edit.

