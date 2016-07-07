.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_crtc.c

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

In contrast to the other drm_get\_\*\_name functions this one here returns a
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

.. _`drm_mode_object_get`:

drm_mode_object_get
===================

.. c:function:: int drm_mode_object_get(struct drm_device *dev, struct drm_mode_object *obj, uint32_t obj_type)

    allocate a new modeset identifier

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_mode_object \*obj:
        object pointer, used to generate unique ID

    :param uint32_t obj_type:
        object type

.. _`drm_mode_object_get.description`:

Description
-----------

Create a unique identifier based on \ ``ptr``\  in \ ``dev``\ 's identifier space.  Used
for tracking modes, CRTCs and connectors. Note that despite the \_get postfix
modeset identifiers are \_not\_ reference counted. Hence don't use this for
reference counted modeset objects like framebuffers.

.. _`drm_mode_object_get.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_mode_object_unregister`:

drm_mode_object_unregister
==========================

.. c:function:: void drm_mode_object_unregister(struct drm_device *dev, struct drm_mode_object *object)

    free a modeset identifer

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_mode_object \*object:
        object to free

.. _`drm_mode_object_unregister.description`:

Description
-----------

Free \ ``id``\  from \ ``dev``\ 's unique identifier pool.
This function can be called multiple times, and guards against
multiple removals.
These modeset identifiers are \_not\_ reference counted. Hence don't use this
for reference counted modeset objects like framebuffers.

.. _`drm_mode_object_find`:

drm_mode_object_find
====================

.. c:function:: struct drm_mode_object *drm_mode_object_find(struct drm_device *dev, uint32_t id, uint32_t type)

    look up a drm object with static lifetime

    :param struct drm_device \*dev:
        drm device

    :param uint32_t id:
        id of the mode object

    :param uint32_t type:
        type of the mode object

.. _`drm_mode_object_find.description`:

Description
-----------

This function is used to look up a modeset object. It will acquire a
reference for reference counted objects. This reference must be dropped again
by callind \ :c:func:`drm_mode_object_unreference`\ .

.. _`drm_mode_object_unreference`:

drm_mode_object_unreference
===========================

.. c:function:: void drm_mode_object_unreference(struct drm_mode_object *obj)

    decr the object refcnt

    :param struct drm_mode_object \*obj:
        mode_object

.. _`drm_mode_object_unreference.description`:

Description
-----------

This functions decrements the object's refcount if it is a refcounted modeset
object. It is a no-op on any other object. This is used to drop references
acquired with \ :c:func:`drm_mode_object_reference`\ .

.. _`drm_mode_object_reference`:

drm_mode_object_reference
=========================

.. c:function:: void drm_mode_object_reference(struct drm_mode_object *obj)

    incr the object refcnt

    :param struct drm_mode_object \*obj:
        mode_object

.. _`drm_mode_object_reference.description`:

Description
-----------

This functions increments the object's refcount if it is a refcounted modeset
object. It is a no-op on any other object. References should be dropped again
by calling \ :c:func:`drm_mode_object_unreference`\ .

.. _`drm_framebuffer_init`:

drm_framebuffer_init
====================

.. c:function:: int drm_framebuffer_init(struct drm_device *dev, struct drm_framebuffer *fb, const struct drm_framebuffer_funcs *funcs)

    initialize a framebuffer

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_framebuffer \*fb:
        framebuffer to be initialized

    :param const struct drm_framebuffer_funcs \*funcs:
        ... with these functions

.. _`drm_framebuffer_init.description`:

Description
-----------

Allocates an ID for the framebuffer's parent mode object, sets its mode
functions & device file and adds it to the master fd list.

.. _`drm_framebuffer_init.important`:

IMPORTANT
---------

This functions publishes the fb and makes it available for concurrent access
by other users. Which means by this point the fb \_must\_ be fully set up -
since all the fb attributes are invariant over its lifetime, no further
locking but only correct reference counting is required.

.. _`drm_framebuffer_init.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_framebuffer_lookup`:

drm_framebuffer_lookup
======================

.. c:function:: struct drm_framebuffer *drm_framebuffer_lookup(struct drm_device *dev, uint32_t id)

    look up a drm framebuffer and grab a reference

    :param struct drm_device \*dev:
        drm device

    :param uint32_t id:
        id of the fb object

.. _`drm_framebuffer_lookup.description`:

Description
-----------

If successful, this grabs an additional reference to the framebuffer -
callers need to make sure to eventually unreference the returned framebuffer
again, using \ ``drm_framebuffer_unreference``\ .

.. _`drm_framebuffer_unregister_private`:

drm_framebuffer_unregister_private
==================================

.. c:function:: void drm_framebuffer_unregister_private(struct drm_framebuffer *fb)

    unregister a private fb from the lookup idr

    :param struct drm_framebuffer \*fb:
        fb to unregister

.. _`drm_framebuffer_unregister_private.description`:

Description
-----------

Drivers need to call this when cleaning up driver-private framebuffers, e.g.
those used for fbdev. Note that the caller must hold a reference of it's own,
i.e. the object may not be destroyed through this call (since it'll lead to a
locking inversion).

.. _`drm_framebuffer_cleanup`:

drm_framebuffer_cleanup
=======================

.. c:function:: void drm_framebuffer_cleanup(struct drm_framebuffer *fb)

    remove a framebuffer object

    :param struct drm_framebuffer \*fb:
        framebuffer to remove

.. _`drm_framebuffer_cleanup.description`:

Description
-----------

Cleanup framebuffer. This function is intended to be used from the drivers
->destroy callback. It can also be used to clean up driver private
framebuffers embedded into a larger structure.

Note that this function does not remove the fb from active usuage - if it is
still used anywhere, hilarity can ensue since userspace could call getfb on
the id and get back -EINVAL. Obviously no concern at driver unload time.

Also, the framebuffer will not be removed from the lookup idr - for
user-created framebuffers this will happen in in the rmfb ioctl. For
driver-private objects (e.g. for fbdev) drivers need to explicitly call
drm_framebuffer_unregister_private.

.. _`drm_framebuffer_remove`:

drm_framebuffer_remove
======================

.. c:function:: void drm_framebuffer_remove(struct drm_framebuffer *fb)

    remove and unreference a framebuffer object

    :param struct drm_framebuffer \*fb:
        framebuffer to remove

.. _`drm_framebuffer_remove.description`:

Description
-----------

Scans all the CRTCs and planes in \ ``dev``\ 's mode_config.  If they're
using \ ``fb``\ , removes it, setting it to NULL. Then drops the reference to the
passed-in framebuffer. Might take the modeset locks.

Note that this function optimizes the cleanup away if the caller holds the
last reference to the framebuffer. It is also guaranteed to not take the
modeset locks in this case.

.. _`drm_crtc_init_with_planes`:

drm_crtc_init_with_planes
=========================

.. c:function:: int drm_crtc_init_with_planes(struct drm_device *dev, struct drm_crtc *crtc, struct drm_plane *primary, struct drm_plane *cursor, const struct drm_crtc_funcs *funcs, const char *name,  ...)

    Initialise a new CRTC object with specified primary and cursor planes.

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_crtc \*crtc:
        CRTC object to init

    :param struct drm_plane \*primary:
        Primary plane for CRTC

    :param struct drm_plane \*cursor:
        Cursor plane for CRTC

    :param const struct drm_crtc_funcs \*funcs:
        callbacks for the new CRTC

    :param const char \*name:
        printf style format string for the CRTC name, or NULL for default name

    :param ... :
        variable arguments

.. _`drm_crtc_init_with_planes.description`:

Description
-----------

Inits a new object created as base part of a driver crtc object.

.. _`drm_crtc_init_with_planes.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_crtc_cleanup`:

drm_crtc_cleanup
================

.. c:function:: void drm_crtc_cleanup(struct drm_crtc *crtc)

    Clean up the core crtc usage

    :param struct drm_crtc \*crtc:
        CRTC to cleanup

.. _`drm_crtc_cleanup.description`:

Description
-----------

This function cleans up \ ``crtc``\  and removes it from the DRM mode setting
core. Note that the function does \*not\* free the crtc structure itself,
this is the responsibility of the caller.

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
See MEDIA_BUS_FMT\_\* definitions in include/uapi/linux/media-bus-format.h for
a full list of available formats.

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

The kernel supports per-connector configration of its consoles through
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

.. _`drm_connector_register_all`:

drm_connector_register_all
==========================

.. c:function:: int drm_connector_register_all(struct drm_device *dev)

    register all connectors

    :param struct drm_device \*dev:
        drm device

.. _`drm_connector_register_all.description`:

Description
-----------

This function registers all connectors in sysfs and other places so that
userspace can start to access them. \ :c:func:`drm_connector_register_all`\  is called
automatically from \ :c:func:`drm_dev_register`\  to complete the device registration,
if they don't call \ :c:func:`drm_connector_register`\  on each connector individually.

When a device is unplugged and should be removed from userspace access,
call \ :c:func:`drm_connector_unregister_all`\ , which is the inverse of this
function.

.. _`drm_connector_register_all.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_connector_unregister_all`:

drm_connector_unregister_all
============================

.. c:function:: void drm_connector_unregister_all(struct drm_device *dev)

    unregister connector userspace interfaces

    :param struct drm_device \*dev:
        drm device

.. _`drm_connector_unregister_all.description`:

Description
-----------

This functions unregisters all connectors from sysfs and other places so
that userspace can no longer access them. Drivers should call this as the
first step tearing down the device instace, or when the underlying
physical device disappeared (e.g. USB unplug), right before calling
\ :c:func:`drm_dev_unregister`\ .

.. _`drm_encoder_init`:

drm_encoder_init
================

.. c:function:: int drm_encoder_init(struct drm_device *dev, struct drm_encoder *encoder, const struct drm_encoder_funcs *funcs, int encoder_type, const char *name,  ...)

    Init a preallocated encoder

    :param struct drm_device \*dev:
        drm device

    :param struct drm_encoder \*encoder:
        the encoder to init

    :param const struct drm_encoder_funcs \*funcs:
        callbacks for this encoder

    :param int encoder_type:
        user visible type of the encoder

    :param const char \*name:
        printf style format string for the encoder name, or NULL for default name

    :param ... :
        variable arguments

.. _`drm_encoder_init.description`:

Description
-----------

Initialises a preallocated encoder. Encoder should be
subclassed as part of driver encoder objects.

.. _`drm_encoder_init.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_encoder_cleanup`:

drm_encoder_cleanup
===================

.. c:function:: void drm_encoder_cleanup(struct drm_encoder *encoder)

    cleans up an initialised encoder

    :param struct drm_encoder \*encoder:
        encoder to cleanup

.. _`drm_encoder_cleanup.description`:

Description
-----------

Cleans up the encoder but doesn't free the object.

.. _`drm_universal_plane_init`:

drm_universal_plane_init
========================

.. c:function:: int drm_universal_plane_init(struct drm_device *dev, struct drm_plane *plane, unsigned long possible_crtcs, const struct drm_plane_funcs *funcs, const uint32_t *formats, unsigned int format_count, enum drm_plane_type type, const char *name,  ...)

    Initialize a new universal plane object

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_plane \*plane:
        plane object to init

    :param unsigned long possible_crtcs:
        bitmask of possible CRTCs

    :param const struct drm_plane_funcs \*funcs:
        callbacks for the new plane

    :param const uint32_t \*formats:
        array of supported formats (\ ``DRM_FORMAT``\ \_\*)

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

.. c:function:: int drm_plane_init(struct drm_device *dev, struct drm_plane *plane, unsigned long possible_crtcs, const struct drm_plane_funcs *funcs, const uint32_t *formats, unsigned int format_count, bool is_primary)

    Initialize a legacy plane

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_plane \*plane:
        plane object to init

    :param unsigned long possible_crtcs:
        bitmask of possible CRTCs

    :param const struct drm_plane_funcs \*funcs:
        callbacks for the new plane

    :param const uint32_t \*formats:
        array of supported formats (\ ``DRM_FORMAT``\ \_\*)

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
core. Note that the function does \*not\* free the plane structure itself,
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

.. _`drm_mode_create_dirty_info_property`:

drm_mode_create_dirty_info_property
===================================

.. c:function:: int drm_mode_create_dirty_info_property(struct drm_device *dev)

    create dirty property

    :param struct drm_device \*dev:
        DRM device

.. _`drm_mode_create_dirty_info_property.description`:

Description
-----------

Called by a driver the first time it's needed, must be attached to desired
connectors.

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

.. _`drm_mode_getresources`:

drm_mode_getresources
=====================

.. c:function:: int drm_mode_getresources(struct drm_device *dev, void *data, struct drm_file *file_priv)

    get graphics configuration

    :param struct drm_device \*dev:
        drm device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

.. _`drm_mode_getresources.description`:

Description
-----------

Construct a set of configuration description structures and return
them to the user, including CRTC, connector and framebuffer configuration.

Called by the user via ioctl.

.. _`drm_mode_getresources.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_getcrtc`:

drm_mode_getcrtc
================

.. c:function:: int drm_mode_getcrtc(struct drm_device *dev, void *data, struct drm_file *file_priv)

    get CRTC configuration

    :param struct drm_device \*dev:
        drm device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

.. _`drm_mode_getcrtc.description`:

Description
-----------

Construct a CRTC configuration structure to return to the user.

Called by the user via ioctl.

.. _`drm_mode_getcrtc.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_getconnector`:

drm_mode_getconnector
=====================

.. c:function:: int drm_mode_getconnector(struct drm_device *dev, void *data, struct drm_file *file_priv)

    get connector configuration

    :param struct drm_device \*dev:
        drm device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

.. _`drm_mode_getconnector.description`:

Description
-----------

Construct a connector configuration structure to return to the user.

Called by the user via ioctl.

.. _`drm_mode_getconnector.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_getencoder`:

drm_mode_getencoder
===================

.. c:function:: int drm_mode_getencoder(struct drm_device *dev, void *data, struct drm_file *file_priv)

    get encoder configuration

    :param struct drm_device \*dev:
        drm device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

.. _`drm_mode_getencoder.description`:

Description
-----------

Construct a encoder configuration structure to return to the user.

Called by the user via ioctl.

.. _`drm_mode_getencoder.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_getplane_res`:

drm_mode_getplane_res
=====================

.. c:function:: int drm_mode_getplane_res(struct drm_device *dev, void *data, struct drm_file *file_priv)

    enumerate all plane resources

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        DRM file info

.. _`drm_mode_getplane_res.description`:

Description
-----------

Construct a list of plane ids to return to the user.

Called by the user via ioctl.

.. _`drm_mode_getplane_res.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_getplane`:

drm_mode_getplane
=================

.. c:function:: int drm_mode_getplane(struct drm_device *dev, void *data, struct drm_file *file_priv)

    get plane configuration

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        DRM file info

.. _`drm_mode_getplane.description`:

Description
-----------

Construct a plane configuration structure to return to the user.

Called by the user via ioctl.

.. _`drm_mode_getplane.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_plane_check_pixel_format`:

drm_plane_check_pixel_format
============================

.. c:function:: int drm_plane_check_pixel_format(const struct drm_plane *plane, u32 format)

    Check if the plane supports the pixel format

    :param const struct drm_plane \*plane:
        plane to check for format support

    :param u32 format:
        the pixel format

.. _`drm_plane_check_pixel_format.return`:

Return
------

Zero of \ ``plane``\  has \ ``format``\  in its list of supported pixel formats, -EINVAL
otherwise.

.. _`drm_mode_setplane`:

drm_mode_setplane
=================

.. c:function:: int drm_mode_setplane(struct drm_device *dev, void *data, struct drm_file *file_priv)

    configure a plane's configuration

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl data\*

    :param struct drm_file \*file_priv:
        DRM file info

.. _`drm_mode_setplane.description`:

Description
-----------

Set plane configuration, including placement, fb, scaling, and other factors.
Or pass a NULL fb to disable (planes may be disabled without providing a
valid crtc).

.. _`drm_mode_setplane.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_set_config_internal`:

drm_mode_set_config_internal
============================

.. c:function:: int drm_mode_set_config_internal(struct drm_mode_set *set)

    helper to call ->set_config

    :param struct drm_mode_set \*set:
        modeset config to set

.. _`drm_mode_set_config_internal.description`:

Description
-----------

This is a little helper to wrap internal calls to the ->set_config driver
interface. The only thing it adds is correct refcounting dance.

.. _`drm_mode_set_config_internal.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_crtc_get_hv_timing`:

drm_crtc_get_hv_timing
======================

.. c:function:: void drm_crtc_get_hv_timing(const struct drm_display_mode *mode, int *hdisplay, int *vdisplay)

    Fetches hdisplay/vdisplay for given mode

    :param const struct drm_display_mode \*mode:
        mode to query

    :param int \*hdisplay:
        hdisplay value to fill in

    :param int \*vdisplay:
        vdisplay value to fill in

.. _`drm_crtc_get_hv_timing.description`:

Description
-----------

The vdisplay value will be doubled if the specified mode is a stereo mode of
the appropriate layout.

.. _`drm_crtc_check_viewport`:

drm_crtc_check_viewport
=======================

.. c:function:: int drm_crtc_check_viewport(const struct drm_crtc *crtc, int x, int y, const struct drm_display_mode *mode, const struct drm_framebuffer *fb)

    Checks that a framebuffer is big enough for the CRTC viewport

    :param const struct drm_crtc \*crtc:
        CRTC that framebuffer will be displayed on

    :param int x:
        x panning

    :param int y:
        y panning

    :param const struct drm_display_mode \*mode:
        mode that framebuffer will be displayed under

    :param const struct drm_framebuffer \*fb:
        framebuffer to check size of

.. _`drm_mode_setcrtc`:

drm_mode_setcrtc
================

.. c:function:: int drm_mode_setcrtc(struct drm_device *dev, void *data, struct drm_file *file_priv)

    set CRTC configuration

    :param struct drm_device \*dev:
        drm device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

.. _`drm_mode_setcrtc.description`:

Description
-----------

Build a new CRTC configuration based on user request.

Called by the user via ioctl.

.. _`drm_mode_setcrtc.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_cursor_universal`:

drm_mode_cursor_universal
=========================

.. c:function:: int drm_mode_cursor_universal(struct drm_crtc *crtc, struct drm_mode_cursor2 *req, struct drm_file *file_priv)

    translate legacy cursor ioctl call into a universal plane handler call

    :param struct drm_crtc \*crtc:
        crtc to update cursor for

    :param struct drm_mode_cursor2 \*req:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

.. _`drm_mode_cursor_universal.description`:

Description
-----------

Legacy cursor ioctl's work directly with driver buffer handles.  To
translate legacy ioctl calls into universal plane handler calls, we need to
wrap the native buffer handle in a drm_framebuffer.

Note that we assume any handle passed to the legacy ioctls was a 32-bit ARGB
buffer with a pitch of 4\*width; the universal plane interface should be used
directly in cases where the hardware can support other buffer settings and
userspace wants to make use of these capabilities.

.. _`drm_mode_cursor_universal.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_cursor_ioctl`:

drm_mode_cursor_ioctl
=====================

.. c:function:: int drm_mode_cursor_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    set CRTC's cursor configuration

    :param struct drm_device \*dev:
        drm device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

.. _`drm_mode_cursor_ioctl.description`:

Description
-----------

Set the cursor configuration based on user request.

Called by the user via ioctl.

.. _`drm_mode_cursor_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_cursor2_ioctl`:

drm_mode_cursor2_ioctl
======================

.. c:function:: int drm_mode_cursor2_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    set CRTC's cursor configuration

    :param struct drm_device \*dev:
        drm device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

.. _`drm_mode_cursor2_ioctl.description`:

Description
-----------

Set the cursor configuration based on user request. This implements the 2nd
version of the cursor ioctl, which allows userspace to additionally specify
the hotspot of the pointer.

Called by the user via ioctl.

.. _`drm_mode_cursor2_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_legacy_fb_format`:

drm_mode_legacy_fb_format
=========================

.. c:function:: uint32_t drm_mode_legacy_fb_format(uint32_t bpp, uint32_t depth)

    compute drm fourcc code from legacy description

    :param uint32_t bpp:
        bits per pixels

    :param uint32_t depth:
        bit depth per pixel

.. _`drm_mode_legacy_fb_format.description`:

Description
-----------

Computes a drm fourcc pixel format code for the given \ ``bpp``\ /\ ``depth``\  values.
Useful in fbdev emulation code, since that deals in those values.

.. _`drm_mode_addfb`:

drm_mode_addfb
==============

.. c:function:: int drm_mode_addfb(struct drm_device *dev, void *data, struct drm_file *file_priv)

    add an FB to the graphics configuration

    :param struct drm_device \*dev:
        drm device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

.. _`drm_mode_addfb.description`:

Description
-----------

Add a new FB to the specified CRTC, given a user request. This is the
original addfb ioctl which only supported RGB formats.

Called by the user via ioctl.

.. _`drm_mode_addfb.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_addfb2`:

drm_mode_addfb2
===============

.. c:function:: int drm_mode_addfb2(struct drm_device *dev, void *data, struct drm_file *file_priv)

    add an FB to the graphics configuration

    :param struct drm_device \*dev:
        drm device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

.. _`drm_mode_addfb2.description`:

Description
-----------

Add a new FB to the specified CRTC, given a user request with format. This is
the 2nd version of the addfb ioctl, which supports multi-planar framebuffers
and uses fourcc codes as pixel format specifiers.

Called by the user via ioctl.

.. _`drm_mode_addfb2.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_rmfb`:

drm_mode_rmfb
=============

.. c:function:: int drm_mode_rmfb(struct drm_device *dev, void *data, struct drm_file *file_priv)

    remove an FB from the configuration

    :param struct drm_device \*dev:
        drm device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

.. _`drm_mode_rmfb.description`:

Description
-----------

Remove the FB specified by the user.

Called by the user via ioctl.

.. _`drm_mode_rmfb.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_getfb`:

drm_mode_getfb
==============

.. c:function:: int drm_mode_getfb(struct drm_device *dev, void *data, struct drm_file *file_priv)

    get FB info

    :param struct drm_device \*dev:
        drm device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

.. _`drm_mode_getfb.description`:

Description
-----------

Lookup the FB given its ID and return info about it.

Called by the user via ioctl.

.. _`drm_mode_getfb.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_dirtyfb_ioctl`:

drm_mode_dirtyfb_ioctl
======================

.. c:function:: int drm_mode_dirtyfb_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    flush frontbuffer rendering on an FB

    :param struct drm_device \*dev:
        drm device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

.. _`drm_mode_dirtyfb_ioctl.description`:

Description
-----------

Lookup the FB and flush out the damaged area supplied by userspace as a clip
rectangle list. Generic userspace which does frontbuffer rendering must call
this ioctl to flush out the changes on manual-update display outputs, e.g.
usb display-link, mipi manual update panels or edp panel self refresh modes.

Modesetting drivers which always update the frontbuffer do not need to
implement the corresponding ->dirty framebuffer callback.

Called by the user via ioctl.

.. _`drm_mode_dirtyfb_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_fb_release`:

drm_fb_release
==============

.. c:function:: void drm_fb_release(struct drm_file *priv)

    remove and free the FBs on this file

    :param struct drm_file \*priv:
        drm file for the ioctl

.. _`drm_fb_release.description`:

Description
-----------

Destroy all the FBs associated with \ ``filp``\ .

Called by the user via ioctl.

.. _`drm_fb_release.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_property_create`:

drm_property_create
===================

.. c:function:: struct drm_property *drm_property_create(struct drm_device *dev, int flags, const char *name, int num_values)

    create a new property type

    :param struct drm_device \*dev:
        drm device

    :param int flags:
        flags specifying the property type

    :param const char \*name:
        name of the property

    :param int num_values:
        number of pre-defined values

.. _`drm_property_create.description`:

Description
-----------

This creates a new generic drm property which can then be attached to a drm
object with drm_object_attach_property. The returned property object must be
freed with drm_property_destroy.

Note that the DRM core keeps a per-device list of properties and that, if
\ :c:func:`drm_mode_config_cleanup`\  is called, it will destroy all properties created
by the driver.

.. _`drm_property_create.return`:

Return
------

A pointer to the newly created property on success, NULL on failure.

.. _`drm_property_create_enum`:

drm_property_create_enum
========================

.. c:function:: struct drm_property *drm_property_create_enum(struct drm_device *dev, int flags, const char *name, const struct drm_prop_enum_list *props, int num_values)

    create a new enumeration property type

    :param struct drm_device \*dev:
        drm device

    :param int flags:
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
object with drm_object_attach_property. The returned property object must be
freed with drm_property_destroy.

Userspace is only allowed to set one of the predefined values for enumeration
properties.

.. _`drm_property_create_enum.return`:

Return
------

A pointer to the newly created property on success, NULL on failure.

.. _`drm_property_create_bitmask`:

drm_property_create_bitmask
===========================

.. c:function:: struct drm_property *drm_property_create_bitmask(struct drm_device *dev, int flags, const char *name, const struct drm_prop_enum_list *props, int num_props, uint64_t supported_bits)

    create a new bitmask property type

    :param struct drm_device \*dev:
        drm device

    :param int flags:
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
object with drm_object_attach_property. The returned property object must be
freed with drm_property_destroy.

Compared to plain enumeration properties userspace is allowed to set any
or'ed together combination of the predefined property bitflag values

.. _`drm_property_create_bitmask.return`:

Return
------

A pointer to the newly created property on success, NULL on failure.

.. _`drm_property_create_range`:

drm_property_create_range
=========================

.. c:function:: struct drm_property *drm_property_create_range(struct drm_device *dev, int flags, const char *name, uint64_t min, uint64_t max)

    create a new unsigned ranged property type

    :param struct drm_device \*dev:
        drm device

    :param int flags:
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
object with drm_object_attach_property. The returned property object must be
freed with drm_property_destroy.

Userspace is allowed to set any unsigned integer value in the (min, max)
range inclusive.

.. _`drm_property_create_range.return`:

Return
------

A pointer to the newly created property on success, NULL on failure.

.. _`drm_property_create_signed_range`:

drm_property_create_signed_range
================================

.. c:function:: struct drm_property *drm_property_create_signed_range(struct drm_device *dev, int flags, const char *name, int64_t min, int64_t max)

    create a new signed ranged property type

    :param struct drm_device \*dev:
        drm device

    :param int flags:
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
object with drm_object_attach_property. The returned property object must be
freed with drm_property_destroy.

Userspace is allowed to set any signed integer value in the (min, max)
range inclusive.

.. _`drm_property_create_signed_range.return`:

Return
------

A pointer to the newly created property on success, NULL on failure.

.. _`drm_property_create_object`:

drm_property_create_object
==========================

.. c:function:: struct drm_property *drm_property_create_object(struct drm_device *dev, int flags, const char *name, uint32_t type)

    create a new object property type

    :param struct drm_device \*dev:
        drm device

    :param int flags:
        flags specifying the property type

    :param const char \*name:
        name of the property

    :param uint32_t type:
        object type from DRM_MODE_OBJECT\_\* defines

.. _`drm_property_create_object.description`:

Description
-----------

This creates a new generic drm property which can then be attached to a drm
object with drm_object_attach_property. The returned property object must be
freed with drm_property_destroy.

Userspace is only allowed to set this to any property value of the given
\ ``type``\ . Only useful for atomic properties, which is enforced.

.. _`drm_property_create_object.return`:

Return
------

A pointer to the newly created property on success, NULL on failure.

.. _`drm_property_create_bool`:

drm_property_create_bool
========================

.. c:function:: struct drm_property *drm_property_create_bool(struct drm_device *dev, int flags, const char *name)

    create a new boolean property type

    :param struct drm_device \*dev:
        drm device

    :param int flags:
        flags specifying the property type

    :param const char \*name:
        name of the property

.. _`drm_property_create_bool.description`:

Description
-----------

This creates a new generic drm property which can then be attached to a drm
object with drm_object_attach_property. The returned property object must be
freed with drm_property_destroy.

This is implemented as a ranged property with only {0, 1} as valid values.

.. _`drm_property_create_bool.return`:

Return
------

A pointer to the newly created property on success, NULL on failure.

.. _`drm_property_add_enum`:

drm_property_add_enum
=====================

.. c:function:: int drm_property_add_enum(struct drm_property *property, int index, uint64_t value, const char *name)

    add a possible value to an enumeration property

    :param struct drm_property \*property:
        enumeration property to change

    :param int index:
        index of the new enumeration

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

.. _`drm_object_attach_property`:

drm_object_attach_property
==========================

.. c:function:: void drm_object_attach_property(struct drm_mode_object *obj, struct drm_property *property, uint64_t init_val)

    attach a property to a modeset object

    :param struct drm_mode_object \*obj:
        drm modeset object

    :param struct drm_property \*property:
        property to attach

    :param uint64_t init_val:
        initial value of the property

.. _`drm_object_attach_property.description`:

Description
-----------

This attaches the given property to the modeset object with the given initial
value. Currently this function cannot fail since the properties are stored in
a statically sized array.

.. _`drm_object_property_set_value`:

drm_object_property_set_value
=============================

.. c:function:: int drm_object_property_set_value(struct drm_mode_object *obj, struct drm_property *property, uint64_t val)

    set the value of a property

    :param struct drm_mode_object \*obj:
        drm mode object to set property value for

    :param struct drm_property \*property:
        property to set

    :param uint64_t val:
        value the property should be set to

.. _`drm_object_property_set_value.description`:

Description
-----------

This functions sets a given property on a given object. This function only
changes the software state of the property, it does not call into the
driver's ->set_property callback.

.. _`drm_object_property_set_value.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_object_property_get_value`:

drm_object_property_get_value
=============================

.. c:function:: int drm_object_property_get_value(struct drm_mode_object *obj, struct drm_property *property, uint64_t *val)

    retrieve the value of a property

    :param struct drm_mode_object \*obj:
        drm mode object to get property value from

    :param struct drm_property \*property:
        property to retrieve

    :param uint64_t \*val:
        storage for the property value

.. _`drm_object_property_get_value.description`:

Description
-----------

This function retrieves the softare state of the given property for the given
property. Since there is no driver callback to retrieve the current property
value this might be out of sync with the hardware, depending upon the driver
and property.

.. _`drm_object_property_get_value.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_mode_getproperty_ioctl`:

drm_mode_getproperty_ioctl
==========================

.. c:function:: int drm_mode_getproperty_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    get the property metadata

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        DRM file info

.. _`drm_mode_getproperty_ioctl.description`:

Description
-----------

This function retrieves the metadata for a given property, like the different
possible values for an enum property or the limits for a range property.

Blob properties are special

Called by the user via ioctl.

.. _`drm_mode_getproperty_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

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
copying data.

.. _`drm_property_create_blob.return`:

Return
------

New blob property with a single reference on success, or an ERR_PTR
value on failure.

.. _`drm_property_unreference_blob`:

drm_property_unreference_blob
=============================

.. c:function:: void drm_property_unreference_blob(struct drm_property_blob *blob)

    Unreference a blob property

    :param struct drm_property_blob \*blob:
        Pointer to blob property

.. _`drm_property_unreference_blob.description`:

Description
-----------

Drop a reference on a blob property. May free the object.

.. _`drm_property_destroy_user_blobs`:

drm_property_destroy_user_blobs
===============================

.. c:function:: void drm_property_destroy_user_blobs(struct drm_device *dev, struct drm_file *file_priv)

    destroy all blobs created by this client

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_file \*file_priv:
        destroy all blobs owned by this file handle

.. _`drm_property_reference_blob`:

drm_property_reference_blob
===========================

.. c:function:: struct drm_property_blob *drm_property_reference_blob(struct drm_property_blob *blob)

    Take a reference on an existing property

    :param struct drm_property_blob \*blob:
        Pointer to blob property

.. _`drm_property_reference_blob.description`:

Description
-----------

Take a new reference on an existing blob property.

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
again, using \ ``drm_property_unreference_blob``\ .

.. _`drm_property_replace_global_blob`:

drm_property_replace_global_blob
================================

.. c:function:: int drm_property_replace_global_blob(struct drm_device *dev, struct drm_property_blob **replace, size_t length, const void *data, struct drm_mode_object *obj_holds_id, struct drm_property *prop_holds_id)

    atomically replace existing blob property

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

This function will atomically replace a global property in the blob list,
optionally updating a property which holds the ID of that property. It is

.. _`drm_property_replace_global_blob.guaranteed-to-be-atomic`:

guaranteed to be atomic
-----------------------

no caller will be allowed to see intermediate
results, and either the entire operation will succeed and clean up the
previous property, or it will fail and the state will be unchanged.

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

.. _`drm_mode_getblob_ioctl`:

drm_mode_getblob_ioctl
======================

.. c:function:: int drm_mode_getblob_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    get the contents of a blob property value

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        DRM file info

.. _`drm_mode_getblob_ioctl.description`:

Description
-----------

This function retrieves the contents of a blob property. The value stored in
an object's blob property is just a normal modeset object id.

Called by the user via ioctl.

.. _`drm_mode_getblob_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_createblob_ioctl`:

drm_mode_createblob_ioctl
=========================

.. c:function:: int drm_mode_createblob_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    create a new blob property

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        DRM file info

.. _`drm_mode_createblob_ioctl.description`:

Description
-----------

This function creates a new blob property with user-defined values. In order
to give us sensible validation and checking when creating, rather than at
every potential use, we also require a type to be provided upfront.

Called by the user via ioctl.

.. _`drm_mode_createblob_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_destroyblob_ioctl`:

drm_mode_destroyblob_ioctl
==========================

.. c:function:: int drm_mode_destroyblob_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    destroy a user blob property

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        DRM file info

.. _`drm_mode_destroyblob_ioctl.description`:

Description
-----------

Destroy an existing user-defined blob property.

Called by the user via ioctl.

.. _`drm_mode_destroyblob_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

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

.. _`drm_mode_connector_property_set_ioctl`:

drm_mode_connector_property_set_ioctl
=====================================

.. c:function:: int drm_mode_connector_property_set_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    set the current value of a connector property

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        DRM file info

.. _`drm_mode_connector_property_set_ioctl.description`:

Description
-----------

This function sets the current value for a connectors's property. It also
calls into a driver's ->set_property callback to update the hardware state

Called by the user via ioctl.

.. _`drm_mode_connector_property_set_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

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

.. _`drm_mode_obj_get_properties_ioctl`:

drm_mode_obj_get_properties_ioctl
=================================

.. c:function:: int drm_mode_obj_get_properties_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    get the current value of a object's property

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        DRM file info

.. _`drm_mode_obj_get_properties_ioctl.description`:

Description
-----------

This function retrieves the current value for an object's property. Compared
to the connector specific ioctl this one is extended to also work on crtc and
plane objects.

Called by the user via ioctl.

.. _`drm_mode_obj_get_properties_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_obj_set_property_ioctl`:

drm_mode_obj_set_property_ioctl
===============================

.. c:function:: int drm_mode_obj_set_property_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    set the current value of an object's property

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        DRM file info

.. _`drm_mode_obj_set_property_ioctl.description`:

Description
-----------

This function sets the current value for an object's property. It also calls
into a driver's ->set_property callback to update the hardware state.
Compared to the connector specific ioctl this one is extended to also work on
crtc and plane objects.

Called by the user via ioctl.

.. _`drm_mode_obj_set_property_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

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

.. _`drm_mode_crtc_set_gamma_size`:

drm_mode_crtc_set_gamma_size
============================

.. c:function:: int drm_mode_crtc_set_gamma_size(struct drm_crtc *crtc, int gamma_size)

    set the gamma table size

    :param struct drm_crtc \*crtc:
        CRTC to set the gamma table size for

    :param int gamma_size:
        size of the gamma table

.. _`drm_mode_crtc_set_gamma_size.description`:

Description
-----------

Drivers which support gamma tables should set this to the supported gamma
table size when initializing the CRTC. Currently the drm core only supports a
fixed gamma table size.

.. _`drm_mode_crtc_set_gamma_size.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_gamma_set_ioctl`:

drm_mode_gamma_set_ioctl
========================

.. c:function:: int drm_mode_gamma_set_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    set the gamma table

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        DRM file info

.. _`drm_mode_gamma_set_ioctl.description`:

Description
-----------

Set the gamma table of a CRTC to the one passed in by the user. Userspace can
inquire the required gamma table size through drm_mode_gamma_get_ioctl.

Called by the user via ioctl.

.. _`drm_mode_gamma_set_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_gamma_get_ioctl`:

drm_mode_gamma_get_ioctl
========================

.. c:function:: int drm_mode_gamma_get_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    get the gamma table

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        DRM file info

.. _`drm_mode_gamma_get_ioctl.description`:

Description
-----------

Copy the current gamma table into the storage provided. This also provides
the gamma table size the driver expects, which can be used to size the
allocated storage.

Called by the user via ioctl.

.. _`drm_mode_gamma_get_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_page_flip_ioctl`:

drm_mode_page_flip_ioctl
========================

.. c:function:: int drm_mode_page_flip_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    schedule an asynchronous fb update

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        DRM file info

.. _`drm_mode_page_flip_ioctl.description`:

Description
-----------

This schedules an asynchronous update on a given CRTC, called page flip.
Optionally a drm event is generated to signal the completion of the event.
Generic drivers cannot assume that a pageflip with changed framebuffer
properties (including driver specific metadata like tiling layout) will work,
but some drivers support e.g. pixel format changes through the pageflip
ioctl.

Called by the user via ioctl.

.. _`drm_mode_page_flip_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_config_reset`:

drm_mode_config_reset
=====================

.. c:function:: void drm_mode_config_reset(struct drm_device *dev)

    call ->reset callbacks

    :param struct drm_device \*dev:
        drm device

.. _`drm_mode_config_reset.description`:

Description
-----------

This functions calls all the crtc's, encoder's and connector's ->reset
callback. Drivers can use this in e.g. their driver load or resume code to
reset hardware and software state.

.. _`drm_mode_create_dumb_ioctl`:

drm_mode_create_dumb_ioctl
==========================

.. c:function:: int drm_mode_create_dumb_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    create a dumb backing storage buffer

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        DRM file info

.. _`drm_mode_create_dumb_ioctl.description`:

Description
-----------

This creates a new dumb buffer in the driver's backing storage manager (GEM,
TTM or something else entirely) and returns the resulting buffer handle. This
handle can then be wrapped up into a framebuffer modeset object.

Note that userspace is not allowed to use such objects for render
acceleration - drivers must create their own private ioctls for such a use
case.

Called by the user via ioctl.

.. _`drm_mode_create_dumb_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_mmap_dumb_ioctl`:

drm_mode_mmap_dumb_ioctl
========================

.. c:function:: int drm_mode_mmap_dumb_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    create an mmap offset for a dumb backing storage buffer

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        DRM file info

.. _`drm_mode_mmap_dumb_ioctl.description`:

Description
-----------

Allocate an offset in the drm device node's address space to be able to
memory map a dumb buffer.

Called by the user via ioctl.

.. _`drm_mode_mmap_dumb_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_destroy_dumb_ioctl`:

drm_mode_destroy_dumb_ioctl
===========================

.. c:function:: int drm_mode_destroy_dumb_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    destroy a dumb backing strage buffer

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        DRM file info

.. _`drm_mode_destroy_dumb_ioctl.description`:

Description
-----------

This destroys the userspace handle for the given dumb backing storage buffer.
Since buffer objects must be reference counted in the kernel a buffer object
won't be immediately freed if a framebuffer modeset object still uses it.

Called by the user via ioctl.

.. _`drm_mode_destroy_dumb_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_rotation_simplify`:

drm_rotation_simplify
=====================

.. c:function:: unsigned int drm_rotation_simplify(unsigned int rotation, unsigned int supported_rotations)

    Try to simplify the rotation

    :param unsigned int rotation:
        Rotation to be simplified

    :param unsigned int supported_rotations:
        Supported rotations

.. _`drm_rotation_simplify.description`:

Description
-----------

Attempt to simplify the rotation to a form that is supported.
Eg. if the hardware supports everything except DRM_REFLECT_X

.. _`drm_rotation_simplify.one-could-call-this-function-like-this`:

one could call this function like this
--------------------------------------


drm_rotation_simplify(rotation, BIT(DRM_ROTATE_0) \|
BIT(DRM_ROTATE_90) \| BIT(DRM_ROTATE_180) \|
BIT(DRM_ROTATE_270) \| BIT(DRM_REFLECT_Y));

to eliminate the DRM_ROTATE_X flag. Depending on what kind of
transforms the hardware supports, this function may not
be able to produce a supported transform, so the caller should
check the result afterwards.

.. _`drm_mode_config_init`:

drm_mode_config_init
====================

.. c:function:: void drm_mode_config_init(struct drm_device *dev)

    initialize DRM mode_configuration structure

    :param struct drm_device \*dev:
        DRM device

.. _`drm_mode_config_init.description`:

Description
-----------

Initialize \ ``dev``\ 's mode_config structure, used for tracking the graphics
configuration of \ ``dev``\ .

Since this initializes the modeset locks, no locking is possible. Which is no
problem, since this should happen single threaded at init time. It is the
driver's problem to ensure this guarantee.

.. _`drm_mode_config_cleanup`:

drm_mode_config_cleanup
=======================

.. c:function:: void drm_mode_config_cleanup(struct drm_device *dev)

    free up DRM mode_config info

    :param struct drm_device \*dev:
        DRM device

.. _`drm_mode_config_cleanup.description`:

Description
-----------

Free up all the connectors and CRTCs associated with this DRM device, then
free up the framebuffers and associated buffer objects.

Note that since this /should/ happen single-threaded at driver/device
teardown time, no locking is required. It's the driver's job to ensure that
this guarantee actually holds true.

.. _`drm_mode_config_cleanup.fixme`:

FIXME
-----

cleanup any dangling user buffer objects too

.. _`drm_mode_put_tile_group`:

drm_mode_put_tile_group
=======================

.. c:function:: void drm_mode_put_tile_group(struct drm_device *dev, struct drm_tile_group *tg)

    drop a reference to a tile group.

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_tile_group \*tg:
        tile group to drop reference to.

.. _`drm_mode_put_tile_group.description`:

Description
-----------

drop reference to tile group and free if 0.

.. _`drm_mode_get_tile_group`:

drm_mode_get_tile_group
=======================

.. c:function:: struct drm_tile_group *drm_mode_get_tile_group(struct drm_device *dev, char topology[8])

    get a reference to an existing tile group

    :param struct drm_device \*dev:
        DRM device

    :param char topology:
        8-bytes unique per monitor.

.. _`drm_mode_get_tile_group.description`:

Description
-----------

Use the unique bytes to get a reference to an existing tile group.

.. _`drm_mode_get_tile_group.return`:

Return
------

tile group or NULL if not found.

.. _`drm_mode_create_tile_group`:

drm_mode_create_tile_group
==========================

.. c:function:: struct drm_tile_group *drm_mode_create_tile_group(struct drm_device *dev, char topology[8])

    create a tile group from a displayid description

    :param struct drm_device \*dev:
        DRM device

    :param char topology:
        8-bytes unique per monitor.

.. _`drm_mode_create_tile_group.description`:

Description
-----------

Create a tile group for the unique monitor, and get a unique
identifier for the tile group.

.. _`drm_mode_create_tile_group.return`:

Return
------

new tile group or error.

.. _`drm_crtc_enable_color_mgmt`:

drm_crtc_enable_color_mgmt
==========================

.. c:function:: void drm_crtc_enable_color_mgmt(struct drm_crtc *crtc, uint degamma_lut_size, bool has_ctm, uint gamma_lut_size)

    enable color management properties

    :param struct drm_crtc \*crtc:
        DRM CRTC

    :param uint degamma_lut_size:
        the size of the degamma lut (before CSC)

    :param bool has_ctm:
        whether to attach ctm_property for CSC matrix

    :param uint gamma_lut_size:
        the size of the gamma lut (after CSC)

.. _`drm_crtc_enable_color_mgmt.description`:

Description
-----------

This function lets the driver enable the color correction
properties on a CRTC. This includes 3 degamma, csc and gamma
properties that userspace can set and 2 size properties to inform
the userspace of the lut sizes. Each of the properties are
optional. The gamma and degamma properties are only attached if
their size is not 0 and ctm_property is only attached if has_ctm is
true.

.. This file was automatic generated / don't edit.

