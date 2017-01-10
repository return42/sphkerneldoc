.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_plane.c

.. _`drm_universal_plane_init`:

drm_universal_plane_init
========================

.. c:function:: int drm_universal_plane_init(struct drm_device *dev, struct drm_plane *plane, uint32_t possible_crtcs, const struct drm_plane_funcs *funcs, const uint32_t *formats, unsigned int format_count, enum drm_plane_type type, const char *name,  ...)

    Initialize a new universal plane object

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_plane \*plane:
        plane object to init

    :param uint32_t possible_crtcs:
        bitmask of possible CRTCs

    :param const struct drm_plane_funcs \*funcs:
        callbacks for the new plane

    :param const uint32_t \*formats:
        array of supported formats (DRM_FORMAT\_\*)

    :param unsigned int format_count:
        number of elements in \ ``formats``\ 

    :param enum drm_plane_type type:
        type of plane (overlay, primary, cursor)

    :param const char \*name:
        printf style format string for the plane name, or NULL for default name

    :param ... :
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

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_plane \*plane:
        plane object to init

    :param uint32_t possible_crtcs:
        bitmask of possible CRTCs

    :param const struct drm_plane_funcs \*funcs:
        callbacks for the new plane

    :param const uint32_t \*formats:
        array of supported formats (DRM_FORMAT\_\*)

    :param unsigned int format_count:
        number of elements in \ ``formats``\ 

    :param bool is_primary:
        plane type (primary vs overlay)

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

    :param struct drm_plane \*plane:
        plane to cleanup

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

    :param struct drm_device \*dev:
        DRM device

    :param int idx:
        index of registered plane to find for

.. _`drm_plane_from_index.description`:

Description
-----------

Given a plane index, return the registered plane from DRM device's
list of planes with matching index.

.. _`drm_plane_force_disable`:

drm_plane_force_disable
=======================

.. c:function:: void drm_plane_force_disable(struct drm_plane *plane)

    Forcibly disable a plane

    :param struct drm_plane \*plane:
        plane to disable

.. _`drm_plane_force_disable.description`:

Description
-----------

Forces the plane to be disabled.

Used when the plane's current framebuffer is destroyed,
and when restoring fbdev mode.

.. _`drm_mode_plane_set_obj_prop`:

drm_mode_plane_set_obj_prop
===========================

.. c:function:: int drm_mode_plane_set_obj_prop(struct drm_plane *plane, struct drm_property *property, uint64_t value)

    set the value of a property

    :param struct drm_plane \*plane:
        drm plane object to set property value for

    :param struct drm_property \*property:
        property to set

    :param uint64_t value:
        value the property should be set to

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

