.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_property.h

.. _`drm_property_enum`:

struct drm_property_enum
========================

.. c:type:: struct drm_property_enum

    symbolic values for enumerations

.. _`drm_property_enum.definition`:

Definition
----------

.. code-block:: c

    struct drm_property_enum {
        uint64_t value;
        struct list_head head;
        char name[DRM_PROP_NAME_LEN];
    }

.. _`drm_property_enum.members`:

Members
-------

value
    numeric property value for this enum entry

head
    list of enum values, linked to \ :c:type:`drm_property.enum_list <drm_property>`\ 

name
    symbolic name for the enum

.. _`drm_property_enum.description`:

Description
-----------

For enumeration and bitmask properties this structure stores the symbolic
decoding for each value. This is used for example for the rotation property.

.. _`drm_property`:

struct drm_property
===================

.. c:type:: struct drm_property

    modeset object property

.. _`drm_property.definition`:

Definition
----------

.. code-block:: c

    struct drm_property {
        struct list_head head;
        struct drm_mode_object base;
        uint32_t flags;
        char name[DRM_PROP_NAME_LEN];
        uint32_t num_values;
        uint64_t *values;
        struct drm_device *dev;
        struct list_head enum_list;
    }

.. _`drm_property.members`:

Members
-------

head
    per-device list of properties, for cleanup.

base
    base KMS object

flags

    Property flags and type. A property needs to be one of the following
    types:

    DRM_MODE_PROP_RANGE
        Range properties report their minimum and maximum admissible unsigned values.
        The KMS core verifies that values set by application fit in that
        range. The range is unsigned. Range properties are created using
        \ :c:func:`drm_property_create_range`\ .

    DRM_MODE_PROP_SIGNED_RANGE
        Range properties report their minimum and maximum admissible unsigned values.
        The KMS core verifies that values set by application fit in that
        range. The range is signed. Range properties are created using
        \ :c:func:`drm_property_create_signed_range`\ .

    DRM_MODE_PROP_ENUM
        Enumerated properties take a numerical value that ranges from 0 to
        the number of enumerated values defined by the property minus one,
        and associate a free-formed string name to each value. Applications
        can retrieve the list of defined value-name pairs and use the
        numerical value to get and set property instance values. Enum
        properties are created using \ :c:func:`drm_property_create_enum`\ .

    DRM_MODE_PROP_BITMASK
        Bitmask properties are enumeration properties that additionally
        restrict all enumerated values to the 0..63 range. Bitmask property
        instance values combine one or more of the enumerated bits defined
        by the property. Bitmask properties are created using
        \ :c:func:`drm_property_create_bitmask`\ .

    DRM_MODE_PROB_OBJECT
        Object properties are used to link modeset objects. This is used
        extensively in the atomic support to create the display pipeline,
        by linking \ :c:type:`struct drm_framebuffer <drm_framebuffer>`\  to \ :c:type:`struct drm_plane <drm_plane>`\ , \ :c:type:`struct drm_plane <drm_plane>`\  to
        \ :c:type:`struct drm_crtc <drm_crtc>`\  and \ :c:type:`struct drm_connector <drm_connector>`\  to \ :c:type:`struct drm_crtc <drm_crtc>`\ . An object property can
        only link to a specific type of \ :c:type:`struct drm_mode_object <drm_mode_object>`\ , this limit is
        enforced by the core. Object properties are created using
        \ :c:func:`drm_property_create_object`\ .

        Object properties work like blob properties, but in a more
        general fashion. They are limited to atomic drivers and must have
        the DRM_MODE_PROP_ATOMIC flag set.

    DRM_MODE_PROP_BLOB
        Blob properties store a binary blob without any format restriction.
        The binary blobs are created as KMS standalone objects, and blob
        property instance values store the ID of their associated blob
        object. Blob properties are created by calling
        \ :c:func:`drm_property_create`\  with DRM_MODE_PROP_BLOB as the type.

        Actual blob objects to contain blob data are created using
        \ :c:func:`drm_property_create_blob`\ , or through the corresponding IOCTL.

        Besides the built-in limit to only accept blob objects blob
        properties work exactly like object properties. The only reasons
        blob properties exist is backwards compatibility with existing
        userspace.

    In addition a property can have any combination of the below flags:

    DRM_MODE_PROP_ATOMIC
        Set for properties which encode atomic modeset state. Such
        properties are not exposed to legacy userspace.

    DRM_MODE_PROP_IMMUTABLE
        Set for properties where userspace cannot be changed by
        userspace. The kernel is allowed to update the value of these
        properties. This is generally used to expose probe state to
        usersapce, e.g. the EDID, or the connector path property on DP
        MST sinks.

name
    symbolic name of the properties

num_values
    size of the \ ``values``\  array.

values

    Array with limits and values for the property. The
    interpretation of these limits is dependent upon the type per \ ``flags``\ .

dev
    DRM device

enum_list

    List of \ :c:type:`struct drm_prop_enum_list <drm_prop_enum_list>`\  structures with the symbolic names for
    enum and bitmask values.

.. _`drm_property.description`:

Description
-----------

This structure represent a modeset object property. It combines both the name
of the property with the set of permissible values. This means that when a
driver wants to use a property with the same name on different objects, but
with different value ranges, then it must create property for each one. An
example would be rotation of \ :c:type:`struct drm_plane <drm_plane>`\ , when e.g. the primary plane cannot
be rotated. But if both the name and the value range match, then the same
property structure can be instantiated multiple times for the same object.
Userspace must be able to cope with this and cannot assume that the same
symbolic property will have the same modeset object ID on all modeset
objects.

Properties are created by one of the special functions, as explained in
detail in the \ ``flags``\  structure member.

To actually expose a property it must be attached to each object using
\ :c:func:`drm_object_attach_property`\ . Currently properties can only be attached to
\ :c:type:`struct drm_connector <drm_connector>`\ , \ :c:type:`struct drm_crtc <drm_crtc>`\  and \ :c:type:`struct drm_plane <drm_plane>`\ .

Properties are also used as the generic metadatatransport for the atomic
IOCTL. Everything that was set directly in structures in the legacy modeset
IOCTLs (like the plane source or destination windows, or e.g. the links to
the CRTC) is exposed as a property with the DRM_MODE_PROP_ATOMIC flag set.

.. _`drm_property_blob`:

struct drm_property_blob
========================

.. c:type:: struct drm_property_blob

    Blob data for \ :c:type:`struct drm_property <drm_property>`\ 

.. _`drm_property_blob.definition`:

Definition
----------

.. code-block:: c

    struct drm_property_blob {
        struct drm_mode_object base;
        struct drm_device *dev;
        struct list_head head_global;
        struct list_head head_file;
        size_t length;
        void *data;
    }

.. _`drm_property_blob.members`:

Members
-------

base
    base KMS object

dev
    DRM device

head_global
    entry on the global blob list in
    \ :c:type:`drm_mode_config.property_blob_list <drm_mode_config>`\ .

head_file
    entry on the per-file blob list in \ :c:type:`drm_file.blobs <drm_file>`\  list.

length
    size of the blob in bytes, invariant over the lifetime of the object

data
    actual data, embedded at the end of this structure

.. _`drm_property_blob.description`:

Description
-----------

Blobs are used to store bigger values than what fits directly into the 64
bits available for a \ :c:type:`struct drm_property <drm_property>`\ .

Blobs are reference counted using \ :c:func:`drm_property_blob_get`\  and
\ :c:func:`drm_property_blob_put`\ . They are created using \ :c:func:`drm_property_create_blob`\ .

.. _`drm_property_type_is`:

drm_property_type_is
====================

.. c:function:: bool drm_property_type_is(struct drm_property *property, uint32_t type)

    check the type of a property

    :param struct drm_property \*property:
        property to check

    :param uint32_t type:
        property type to compare with

.. _`drm_property_type_is.description`:

Description
-----------

This is a helper function becauase the uapi encoding of property types is
a bit special for historical reasons.

.. _`drm_property_find`:

drm_property_find
=================

.. c:function:: struct drm_property *drm_property_find(struct drm_device *dev, struct drm_file *file_priv, uint32_t id)

    find property object

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_file \*file_priv:
        drm file to check for lease against.

    :param uint32_t id:
        property object id

.. _`drm_property_find.description`:

Description
-----------

This function looks up the property object specified by id and returns it.

.. This file was automatic generated / don't edit.

