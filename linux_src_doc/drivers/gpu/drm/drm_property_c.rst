.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_property.c

.. _`overview`:

overview
========

Properties as represented by \ :c:type:`struct drm_property <drm_property>`\  are used to extend the modeset
interface exposed to userspace. For the atomic modeset IOCTL properties are
even the only way to transport metadata about the desired new modeset
configuration from userspace to the kernel. Properties have a well-defined
value range, which is enforced by the drm core. See the documentation of the
flags member of \ :c:type:`struct drm_property <drm_property>`\  for an overview of the different
property types and ranges.

Properties don't store the current value directly, but need to be
instatiated by attaching them to a \ :c:type:`struct drm_mode_object <drm_mode_object>`\  with
\ :c:func:`drm_object_attach_property`\ .

Property values are only 64bit. To support bigger piles of data (like gamma
tables, color correction matrices or large structures) a property can instead
point at a \ :c:type:`struct drm_property_blob <drm_property_blob>`\  with that additional data.

Properties are defined by their symbolic name, userspace must keep a
per-object mapping from those names to the property ID used in the atomic
IOCTL and in the get/set property IOCTL.

.. _`drm_property_create`:

drm_property_create
===================

.. c:function:: struct drm_property *drm_property_create(struct drm_device *dev, u32 flags, const char *name, int num_values)

    create a new property type

    :param struct drm_device \*dev:
        drm device

    :param u32 flags:
        flags specifying the property type

    :param const char \*name:
        name of the property

    :param int num_values:
        number of pre-defined values

.. _`drm_property_create.description`:

Description
-----------

This creates a new generic drm property which can then be attached to a drm
object with \ :c:func:`drm_object_attach_property`\ . The returned property object must
be freed with \ :c:func:`drm_property_destroy`\ , which is done automatically when
calling \ :c:func:`drm_mode_config_cleanup`\ .

.. _`drm_property_create.return`:

Return
------

A pointer to the newly created property on success, NULL on failure.

.. _`drm_property_create_enum`:

drm_property_create_enum
========================

.. c:function:: struct drm_property *drm_property_create_enum(struct drm_device *dev, u32 flags, const char *name, const struct drm_prop_enum_list *props, int num_values)

    create a new enumeration property type

    :param struct drm_device \*dev:
        drm device

    :param u32 flags:
        flags specifying the property type

    :param const char \*name:
        name of the property

    :param const struct drm_prop_enum_list \*props:
        enumeration lists with property values

    :param int num_values:
        number of pre-defined values

.. _`drm_property_create_enum.description`:

Description
-----------

This creates a new generic drm property which can then be attached to a drm
object with \ :c:func:`drm_object_attach_property`\ . The returned property object must
be freed with \ :c:func:`drm_property_destroy`\ , which is done automatically when
calling \ :c:func:`drm_mode_config_cleanup`\ .

Userspace is only allowed to set one of the predefined values for enumeration
properties.

.. _`drm_property_create_enum.return`:

Return
------

A pointer to the newly created property on success, NULL on failure.

.. _`drm_property_create_bitmask`:

drm_property_create_bitmask
===========================

.. c:function:: struct drm_property *drm_property_create_bitmask(struct drm_device *dev, u32 flags, const char *name, const struct drm_prop_enum_list *props, int num_props, uint64_t supported_bits)

    create a new bitmask property type

    :param struct drm_device \*dev:
        drm device

    :param u32 flags:
        flags specifying the property type

    :param const char \*name:
        name of the property

    :param const struct drm_prop_enum_list \*props:
        enumeration lists with property bitflags

    :param int num_props:
        size of the \ ``props``\  array

    :param uint64_t supported_bits:
        bitmask of all supported enumeration values

.. _`drm_property_create_bitmask.description`:

Description
-----------

This creates a new bitmask drm property which can then be attached to a drm
object with \ :c:func:`drm_object_attach_property`\ . The returned property object must
be freed with \ :c:func:`drm_property_destroy`\ , which is done automatically when
calling \ :c:func:`drm_mode_config_cleanup`\ .

Compared to plain enumeration properties userspace is allowed to set any
or'ed together combination of the predefined property bitflag values

.. _`drm_property_create_bitmask.return`:

Return
------

A pointer to the newly created property on success, NULL on failure.

.. _`drm_property_create_range`:

drm_property_create_range
=========================

.. c:function:: struct drm_property *drm_property_create_range(struct drm_device *dev, u32 flags, const char *name, uint64_t min, uint64_t max)

    create a new unsigned ranged property type

    :param struct drm_device \*dev:
        drm device

    :param u32 flags:
        flags specifying the property type

    :param const char \*name:
        name of the property

    :param uint64_t min:
        minimum value of the property

    :param uint64_t max:
        maximum value of the property

.. _`drm_property_create_range.description`:

Description
-----------

This creates a new generic drm property which can then be attached to a drm
object with \ :c:func:`drm_object_attach_property`\ . The returned property object must
be freed with \ :c:func:`drm_property_destroy`\ , which is done automatically when
calling \ :c:func:`drm_mode_config_cleanup`\ .

Userspace is allowed to set any unsigned integer value in the (min, max)
range inclusive.

.. _`drm_property_create_range.return`:

Return
------

A pointer to the newly created property on success, NULL on failure.

.. _`drm_property_create_signed_range`:

drm_property_create_signed_range
================================

.. c:function:: struct drm_property *drm_property_create_signed_range(struct drm_device *dev, u32 flags, const char *name, int64_t min, int64_t max)

    create a new signed ranged property type

    :param struct drm_device \*dev:
        drm device

    :param u32 flags:
        flags specifying the property type

    :param const char \*name:
        name of the property

    :param int64_t min:
        minimum value of the property

    :param int64_t max:
        maximum value of the property

.. _`drm_property_create_signed_range.description`:

Description
-----------

This creates a new generic drm property which can then be attached to a drm
object with \ :c:func:`drm_object_attach_property`\ . The returned property object must
be freed with \ :c:func:`drm_property_destroy`\ , which is done automatically when
calling \ :c:func:`drm_mode_config_cleanup`\ .

Userspace is allowed to set any signed integer value in the (min, max)
range inclusive.

.. _`drm_property_create_signed_range.return`:

Return
------

A pointer to the newly created property on success, NULL on failure.

.. _`drm_property_create_object`:

drm_property_create_object
==========================

.. c:function:: struct drm_property *drm_property_create_object(struct drm_device *dev, u32 flags, const char *name, uint32_t type)

    create a new object property type

    :param struct drm_device \*dev:
        drm device

    :param u32 flags:
        flags specifying the property type

    :param const char \*name:
        name of the property

    :param uint32_t type:
        object type from DRM_MODE_OBJECT_* defines

.. _`drm_property_create_object.description`:

Description
-----------

This creates a new generic drm property which can then be attached to a drm
object with \ :c:func:`drm_object_attach_property`\ . The returned property object must
be freed with \ :c:func:`drm_property_destroy`\ , which is done automatically when
calling \ :c:func:`drm_mode_config_cleanup`\ .

Userspace is only allowed to set this to any property value of the given
\ ``type``\ . Only useful for atomic properties, which is enforced.

.. _`drm_property_create_object.return`:

Return
------

A pointer to the newly created property on success, NULL on failure.

.. _`drm_property_create_bool`:

drm_property_create_bool
========================

.. c:function:: struct drm_property *drm_property_create_bool(struct drm_device *dev, u32 flags, const char *name)

    create a new boolean property type

    :param struct drm_device \*dev:
        drm device

    :param u32 flags:
        flags specifying the property type

    :param const char \*name:
        name of the property

.. _`drm_property_create_bool.description`:

Description
-----------

This creates a new generic drm property which can then be attached to a drm
object with \ :c:func:`drm_object_attach_property`\ . The returned property object must
be freed with \ :c:func:`drm_property_destroy`\ , which is done automatically when
calling \ :c:func:`drm_mode_config_cleanup`\ .

This is implemented as a ranged property with only {0, 1} as valid values.

.. _`drm_property_create_bool.return`:

Return
------

A pointer to the newly created property on success, NULL on failure.

.. _`drm_property_add_enum`:

drm_property_add_enum
=====================

.. c:function:: int drm_property_add_enum(struct drm_property *property, uint64_t value, const char *name)

    add a possible value to an enumeration property

    :param struct drm_property \*property:
        enumeration property to change

    :param uint64_t value:
        value of the new enumeration

    :param const char \*name:
        symbolic name of the new enumeration

.. _`drm_property_add_enum.description`:

Description
-----------

This functions adds enumerations to a property.

It's use is deprecated, drivers should use one of the more specific helpers
to directly create the property with all enumerations already attached.

.. _`drm_property_add_enum.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_property_destroy`:

drm_property_destroy
====================

.. c:function:: void drm_property_destroy(struct drm_device *dev, struct drm_property *property)

    destroy a drm property

    :param struct drm_device \*dev:
        drm device

    :param struct drm_property \*property:
        property to destry

.. _`drm_property_destroy.description`:

Description
-----------

This function frees a property including any attached resources like
enumeration values.

.. _`drm_property_create_blob`:

drm_property_create_blob
========================

.. c:function:: struct drm_property_blob *drm_property_create_blob(struct drm_device *dev, size_t length, const void *data)

    Create new blob property

    :param struct drm_device \*dev:
        DRM device to create property for

    :param size_t length:
        Length to allocate for blob data

    :param const void \*data:
        If specified, copies data into blob

.. _`drm_property_create_blob.description`:

Description
-----------

Creates a new blob property for a specified DRM device, optionally
copying data. Note that blob properties are meant to be invariant, hence the
data must be filled out before the blob is used as the value of any property.

.. _`drm_property_create_blob.return`:

Return
------

New blob property with a single reference on success, or an ERR_PTR
value on failure.

.. _`drm_property_blob_put`:

drm_property_blob_put
=====================

.. c:function:: void drm_property_blob_put(struct drm_property_blob *blob)

    release a blob property reference

    :param struct drm_property_blob \*blob:
        DRM blob property

.. _`drm_property_blob_put.description`:

Description
-----------

Releases a reference to a blob property. May free the object.

.. _`drm_property_blob_get`:

drm_property_blob_get
=====================

.. c:function:: struct drm_property_blob *drm_property_blob_get(struct drm_property_blob *blob)

    acquire blob property reference

    :param struct drm_property_blob \*blob:
        DRM blob property

.. _`drm_property_blob_get.description`:

Description
-----------

Acquires a reference to an existing blob property. Returns \ ``blob``\ , which
allows this to be used as a shorthand in assignments.

.. _`drm_property_lookup_blob`:

drm_property_lookup_blob
========================

.. c:function:: struct drm_property_blob *drm_property_lookup_blob(struct drm_device *dev, uint32_t id)

    look up a blob property and take a reference

    :param struct drm_device \*dev:
        drm device

    :param uint32_t id:
        id of the blob property

.. _`drm_property_lookup_blob.description`:

Description
-----------

If successful, this takes an additional reference to the blob property.
callers need to make sure to eventually unreference the returned property
again, using \ :c:func:`drm_property_blob_put`\ .

.. _`drm_property_lookup_blob.return`:

Return
------

NULL on failure, pointer to the blob on success.

.. _`drm_property_replace_global_blob`:

drm_property_replace_global_blob
================================

.. c:function:: int drm_property_replace_global_blob(struct drm_device *dev, struct drm_property_blob **replace, size_t length, const void *data, struct drm_mode_object *obj_holds_id, struct drm_property *prop_holds_id)

    replace existing blob property

    :param struct drm_device \*dev:
        drm device

    :param struct drm_property_blob \*\*replace:
        location of blob property pointer to be replaced

    :param size_t length:
        length of data for new blob, or 0 for no data

    :param const void \*data:
        content for new blob, or NULL for no data

    :param struct drm_mode_object \*obj_holds_id:
        optional object for property holding blob ID

    :param struct drm_property \*prop_holds_id:
        optional property holding blob ID
        \ ``return``\  0 on success or error on failure

.. _`drm_property_replace_global_blob.description`:

Description
-----------

This function will replace a global property in the blob list, optionally
updating a property which holds the ID of that property.

If length is 0 or data is NULL, no new blob will be created, and the holding
property, if specified, will be set to 0.

Access to the replace pointer is assumed to be protected by the caller, e.g.
by holding the relevant modesetting object lock for its parent.

For example, a drm_connector has a 'PATH' property, which contains the ID
of a blob property with the value of the MST path information. Calling this
function with replace pointing to the connector's path_blob_ptr, length and
data set for the new path information, obj_holds_id set to the connector's
base object, and prop_holds_id set to the path property name, will perform
a completely atomic update. The access to path_blob_ptr is protected by the
caller holding a lock on the connector.

.. _`drm_property_replace_blob`:

drm_property_replace_blob
=========================

.. c:function:: bool drm_property_replace_blob(struct drm_property_blob **blob, struct drm_property_blob *new_blob)

    replace a blob property

    :param struct drm_property_blob \*\*blob:
        a pointer to the member blob to be replaced

    :param struct drm_property_blob \*new_blob:
        the new blob to replace with

.. _`drm_property_replace_blob.return`:

Return
------

true if the blob was in fact replaced.

.. This file was automatic generated / don't edit.

