.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_plane.c

.. _`overview`:

overview
========

A plane represents an image source that can be blended with or overlayed on
top of a CRTC during the scanout process. Planes take their input data from a
\ :c:type:`struct drm_framebuffer <drm_framebuffer>`\  object. The plane itself specifies the cropping and scaling
of that image, and where it is placed on the visible are of a display
pipeline, represented by \ :c:type:`struct drm_crtc <drm_crtc>`\ . A plane can also have additional
properties that specify how the pixels are positioned and blended, like
rotation or Z-position. All these properties are stored in \ :c:type:`struct drm_plane_state <drm_plane_state>`\ .

To create a plane, a KMS drivers allocates and zeroes an instances of
\ :c:type:`struct drm_plane <drm_plane>`\  (possibly as part of a larger structure) and registers it
with a call to \ :c:func:`drm_universal_plane_init`\ .

Cursor and overlay planes are optional. All drivers should provide one
primary plane per CRTC to avoid surprising userspace too much. See enum
drm_plane_type for a more in-depth discussion of these special uapi-relevant
plane types. Special planes are associated with their CRTC by calling
\ :c:func:`drm_crtc_init_with_planes`\ .

The type of a plane is exposed in the immutable "type" enumeration property,
which has one of the following values: "Overlay", "Primary", "Cursor".

.. _`drm_universal_plane_init`:

drm_universal_plane_init
========================

.. c:function:: int drm_universal_plane_init(struct drm_device *dev, struct drm_plane *plane, uint32_t possible_crtcs, const struct drm_plane_funcs *funcs, const uint32_t *formats, unsigned int format_count, const uint64_t *format_modifiers, enum drm_plane_type type, const char *name,  ...)

    Initialize a new universal plane object

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param plane:
        plane object to init
    :type plane: struct drm_plane \*

    :param possible_crtcs:
        bitmask of possible CRTCs
    :type possible_crtcs: uint32_t

    :param funcs:
        callbacks for the new plane
    :type funcs: const struct drm_plane_funcs \*

    :param formats:
        array of supported formats (DRM_FORMAT\_\*)
    :type formats: const uint32_t \*

    :param format_count:
        number of elements in \ ``formats``\ 
    :type format_count: unsigned int

    :param format_modifiers:
        array of struct drm_format modifiers terminated by
        DRM_FORMAT_MOD_INVALID
    :type format_modifiers: const uint64_t \*

    :param type:
        type of plane (overlay, primary, cursor)
    :type type: enum drm_plane_type

    :param name:
        printf style format string for the plane name, or NULL for default name
    :type name: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`drm_universal_plane_init.description`:

Description
-----------

Initializes a plane object of type \ ``type``\ .

.. _`drm_universal_plane_init.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_plane_init`:

drm_plane_init
==============

.. c:function:: int drm_plane_init(struct drm_device *dev, struct drm_plane *plane, uint32_t possible_crtcs, const struct drm_plane_funcs *funcs, const uint32_t *formats, unsigned int format_count, bool is_primary)

    Initialize a legacy plane

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param plane:
        plane object to init
    :type plane: struct drm_plane \*

    :param possible_crtcs:
        bitmask of possible CRTCs
    :type possible_crtcs: uint32_t

    :param funcs:
        callbacks for the new plane
    :type funcs: const struct drm_plane_funcs \*

    :param formats:
        array of supported formats (DRM_FORMAT\_\*)
    :type formats: const uint32_t \*

    :param format_count:
        number of elements in \ ``formats``\ 
    :type format_count: unsigned int

    :param is_primary:
        plane type (primary vs overlay)
    :type is_primary: bool

.. _`drm_plane_init.description`:

Description
-----------

Legacy API to initialize a DRM plane.

New drivers should call \ :c:func:`drm_universal_plane_init`\  instead.

.. _`drm_plane_init.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_plane_cleanup`:

drm_plane_cleanup
=================

.. c:function:: void drm_plane_cleanup(struct drm_plane *plane)

    Clean up the core plane usage

    :param plane:
        plane to cleanup
    :type plane: struct drm_plane \*

.. _`drm_plane_cleanup.description`:

Description
-----------

This function cleans up \ ``plane``\  and removes it from the DRM mode setting
core. Note that the function does *not* free the plane structure itself,
this is the responsibility of the caller.

.. _`drm_plane_from_index`:

drm_plane_from_index
====================

.. c:function:: struct drm_plane *drm_plane_from_index(struct drm_device *dev, int idx)

    find the registered plane at an index

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param idx:
        index of registered plane to find for
    :type idx: int

.. _`drm_plane_from_index.description`:

Description
-----------

Given a plane index, return the registered plane from DRM device's
list of planes with matching index. This is the inverse of \ :c:func:`drm_plane_index`\ .

.. _`drm_plane_force_disable`:

drm_plane_force_disable
=======================

.. c:function:: void drm_plane_force_disable(struct drm_plane *plane)

    Forcibly disable a plane

    :param plane:
        plane to disable
    :type plane: struct drm_plane \*

.. _`drm_plane_force_disable.description`:

Description
-----------

Forces the plane to be disabled.

Used when the plane's current framebuffer is destroyed,
and when restoring fbdev mode.

Note that this function is not suitable for atomic drivers, since it doesn't
wire through the lock acquisition context properly and hence can't handle
retries or driver private locks. You probably want to use
\ :c:func:`drm_atomic_helper_disable_plane`\  or
\ :c:func:`drm_atomic_helper_disable_planes_on_crtc`\  instead.

.. _`drm_mode_plane_set_obj_prop`:

drm_mode_plane_set_obj_prop
===========================

.. c:function:: int drm_mode_plane_set_obj_prop(struct drm_plane *plane, struct drm_property *property, uint64_t value)

    set the value of a property

    :param plane:
        drm plane object to set property value for
    :type plane: struct drm_plane \*

    :param property:
        property to set
    :type property: struct drm_property \*

    :param value:
        value the property should be set to
    :type value: uint64_t

.. _`drm_mode_plane_set_obj_prop.description`:

Description
-----------

This functions sets a given property on a given plane object. This function
calls the driver's ->set_property callback and changes the software state of
the property if the callback succeeds.

.. _`drm_mode_plane_set_obj_prop.return`:

Return
------

Zero on success, error code on failure.

.. This file was automatic generated / don't edit.

