.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_connector.c

.. _`drm_connector_get_cmdline_mode`:

drm_connector_get_cmdline_mode
==============================

.. c:function:: void drm_connector_get_cmdline_mode(struct drm_connector *connector)

    reads the user's cmdline mode

    :param struct drm_connector \*connector:
        connector to quwery

.. _`drm_connector_get_cmdline_mode.description`:

Description
-----------

The kernel supports per-connector configuration of its consoles through
use of the video= parameter. This function parses that option and
extracts the user's specified mode (or enable/disable status) for a
particular connector. This is typically only used during the early fbdev
setup.

.. _`drm_connector_init`:

drm_connector_init
==================

.. c:function:: int drm_connector_init(struct drm_device *dev, struct drm_connector *connector, const struct drm_connector_funcs *funcs, int connector_type)

    Init a preallocated connector

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_connector \*connector:
        the connector to init

    :param const struct drm_connector_funcs \*funcs:
        callbacks for this connector

    :param int connector_type:
        user visible type of the connector

.. _`drm_connector_init.description`:

Description
-----------

Initialises a preallocated connector. Connectors should be
subclassed as part of driver connector objects.

.. _`drm_connector_init.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_mode_connector_attach_encoder`:

drm_mode_connector_attach_encoder
=================================

.. c:function:: int drm_mode_connector_attach_encoder(struct drm_connector *connector, struct drm_encoder *encoder)

    attach a connector to an encoder

    :param struct drm_connector \*connector:
        connector to attach

    :param struct drm_encoder \*encoder:
        encoder to attach \ ``connector``\  to

.. _`drm_mode_connector_attach_encoder.description`:

Description
-----------

This function links up a connector to an encoder. Note that the routing
restrictions between encoders and crtcs are exposed to userspace through the
possible_clones and possible_crtcs bitmasks.

.. _`drm_mode_connector_attach_encoder.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_connector_cleanup`:

drm_connector_cleanup
=====================

.. c:function:: void drm_connector_cleanup(struct drm_connector *connector)

    cleans up an initialised connector

    :param struct drm_connector \*connector:
        connector to cleanup

.. _`drm_connector_cleanup.description`:

Description
-----------

Cleans up the connector but doesn't free the object.

.. _`drm_connector_register`:

drm_connector_register
======================

.. c:function:: int drm_connector_register(struct drm_connector *connector)

    register a connector

    :param struct drm_connector \*connector:
        the connector to register

.. _`drm_connector_register.description`:

Description
-----------

Register userspace interfaces for a connector

.. _`drm_connector_register.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_connector_unregister`:

drm_connector_unregister
========================

.. c:function:: void drm_connector_unregister(struct drm_connector *connector)

    unregister a connector

    :param struct drm_connector \*connector:
        the connector to unregister

.. _`drm_connector_unregister.description`:

Description
-----------

Unregister userspace interfaces for a connector

.. _`drm_get_connector_status_name`:

drm_get_connector_status_name
=============================

.. c:function:: const char *drm_get_connector_status_name(enum drm_connector_status status)

    return a string for connector status

    :param enum drm_connector_status status:
        connector status to compute name of

.. _`drm_get_connector_status_name.description`:

Description
-----------

In contrast to the other drm_get_*_name functions this one here returns a
const pointer and hence is threadsafe.

.. _`drm_get_subpixel_order_name`:

drm_get_subpixel_order_name
===========================

.. c:function:: const char *drm_get_subpixel_order_name(enum subpixel_order order)

    return a string for a given subpixel enum

    :param enum subpixel_order order:
        enum of subpixel_order

.. _`drm_get_subpixel_order_name.description`:

Description
-----------

Note you could abuse this and return something out of bounds, but that
would be a caller error.  No unscrubbed user data should make it here.

.. _`drm_display_info_set_bus_formats`:

drm_display_info_set_bus_formats
================================

.. c:function:: int drm_display_info_set_bus_formats(struct drm_display_info *info, const u32 *formats, unsigned int num_formats)

    set the supported bus formats

    :param struct drm_display_info \*info:
        display info to store bus formats in

    :param const u32 \*formats:
        array containing the supported bus formats

    :param unsigned int num_formats:
        the number of entries in the fmts array

.. _`drm_display_info_set_bus_formats.description`:

Description
-----------

Store the supported bus formats in display info structure.
See MEDIA_BUS_FMT_* definitions in include/uapi/linux/media-bus-format.h for
a full list of available formats.

.. _`drm_mode_create_dvi_i_properties`:

drm_mode_create_dvi_i_properties
================================

.. c:function:: int drm_mode_create_dvi_i_properties(struct drm_device *dev)

    create DVI-I specific connector properties

    :param struct drm_device \*dev:
        DRM device

.. _`drm_mode_create_dvi_i_properties.description`:

Description
-----------

Called by a driver the first time a DVI-I connector is made.

.. _`drm_mode_create_tv_properties`:

drm_mode_create_tv_properties
=============================

.. c:function:: int drm_mode_create_tv_properties(struct drm_device *dev, unsigned int num_modes, const char * const modes[])

    create TV specific connector properties

    :param struct drm_device \*dev:
        DRM device

    :param unsigned int num_modes:
        number of different TV formats (modes) supported

    :param const char \* const modes:
        array of pointers to strings containing name of each format

.. _`drm_mode_create_tv_properties.description`:

Description
-----------

Called by a driver's TV initialization routine, this function creates
the TV specific connector properties for a given device.  Caller is
responsible for allocating a list of format names and passing them to
this routine.

.. _`drm_mode_create_scaling_mode_property`:

drm_mode_create_scaling_mode_property
=====================================

.. c:function:: int drm_mode_create_scaling_mode_property(struct drm_device *dev)

    create scaling mode property

    :param struct drm_device \*dev:
        DRM device

.. _`drm_mode_create_scaling_mode_property.description`:

Description
-----------

Called by a driver the first time it's needed, must be attached to desired
connectors.

.. _`drm_mode_create_aspect_ratio_property`:

drm_mode_create_aspect_ratio_property
=====================================

.. c:function:: int drm_mode_create_aspect_ratio_property(struct drm_device *dev)

    create aspect ratio property

    :param struct drm_device \*dev:
        DRM device

.. _`drm_mode_create_aspect_ratio_property.description`:

Description
-----------

Called by a driver the first time it's needed, must be attached to desired
connectors.

.. _`drm_mode_create_aspect_ratio_property.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_create_suggested_offset_properties`:

drm_mode_create_suggested_offset_properties
===========================================

.. c:function:: int drm_mode_create_suggested_offset_properties(struct drm_device *dev)

    create suggests offset properties

    :param struct drm_device \*dev:
        DRM device

.. _`drm_mode_create_suggested_offset_properties.description`:

Description
-----------

Create the the suggested x/y offset property for connectors.

.. _`drm_mode_connector_set_path_property`:

drm_mode_connector_set_path_property
====================================

.. c:function:: int drm_mode_connector_set_path_property(struct drm_connector *connector, const char *path)

    set tile property on connector

    :param struct drm_connector \*connector:
        connector to set property on.

    :param const char \*path:
        path to use for property; must not be NULL.

.. _`drm_mode_connector_set_path_property.description`:

Description
-----------

This creates a property to expose to userspace to specify a
connector path. This is mainly used for DisplayPort MST where
connectors have a topology and we want to allow userspace to give
them more meaningful names.

.. _`drm_mode_connector_set_path_property.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_connector_set_tile_property`:

drm_mode_connector_set_tile_property
====================================

.. c:function:: int drm_mode_connector_set_tile_property(struct drm_connector *connector)

    set tile property on connector

    :param struct drm_connector \*connector:
        connector to set property on.

.. _`drm_mode_connector_set_tile_property.description`:

Description
-----------

This looks up the tile information for a connector, and creates a
property for userspace to parse if it exists. The property is of
the form of 8 integers using ':' as a separator.

.. _`drm_mode_connector_set_tile_property.return`:

Return
------

Zero on success, errno on failure.

.. _`drm_mode_connector_update_edid_property`:

drm_mode_connector_update_edid_property
=======================================

.. c:function:: int drm_mode_connector_update_edid_property(struct drm_connector *connector, const struct edid *edid)

    update the edid property of a connector

    :param struct drm_connector \*connector:
        drm connector

    :param const struct edid \*edid:
        new value of the edid property

.. _`drm_mode_connector_update_edid_property.description`:

Description
-----------

This function creates a new blob modeset object and assigns its id to the
connector's edid property.

.. _`drm_mode_connector_update_edid_property.return`:

Return
------

Zero on success, negative errno on failure.

.. This file was automatic generated / don't edit.

