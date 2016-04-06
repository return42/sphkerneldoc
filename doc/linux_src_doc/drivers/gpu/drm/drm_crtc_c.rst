.. -*- coding: utf-8; mode: rst -*-

==========
drm_crtc.c
==========



.. _xref_drm_get_connector_status_name:

drm_get_connector_status_name
=============================

.. c:function:: const char * drm_get_connector_status_name (enum drm_connector_status status)

    return a string for connector status

    :param enum drm_connector_status status:
        connector status to compute name of



Description
-----------

In contrast to the other drm_get_*_name functions this one here returns a
const pointer and hence is threadsafe.




.. _xref_drm_get_subpixel_order_name:

drm_get_subpixel_order_name
===========================

.. c:function:: const char * drm_get_subpixel_order_name (enum subpixel_order order)

    return a string for a given subpixel enum

    :param enum subpixel_order order:
        enum of subpixel_order



Description
-----------

Note you could abuse this and return something out of bounds, but that
would be a caller error.  No unscrubbed user data should make it here.




.. _xref_drm_get_format_name:

drm_get_format_name
===================

.. c:function:: const char * drm_get_format_name (uint32_t format)

    return a string for drm fourcc format

    :param uint32_t format:
        format to compute name of



Description
-----------

Note that the buffer used by this function is globally shared and owned by
the function itself.



FIXME
-----

This isn't really multithreading safe.




.. _xref_drm_mode_object_get:

drm_mode_object_get
===================

.. c:function:: int drm_mode_object_get (struct drm_device * dev, struct drm_mode_object * obj, uint32_t obj_type)

    allocate a new modeset identifier

    :param struct drm_device * dev:
        DRM device

    :param struct drm_mode_object * obj:
        object pointer, used to generate unique ID

    :param uint32_t obj_type:
        object type



Description
-----------

Create a unique identifier based on **ptr** in **dev**'s identifier space.  Used
for tracking modes, CRTCs and connectors. Note that despite the _get postfix
modeset identifiers are _not_ reference counted. Hence don't use this for
reference counted modeset objects like framebuffers.



Returns
-------

Zero on success, error code on failure.




.. _xref_drm_mode_object_put:

drm_mode_object_put
===================

.. c:function:: void drm_mode_object_put (struct drm_device * dev, struct drm_mode_object * object)

    free a modeset identifer

    :param struct drm_device * dev:
        DRM device

    :param struct drm_mode_object * object:
        object to free



Description
-----------

Free **id** from **dev**'s unique identifier pool. Note that despite the _get
postfix modeset identifiers are _not_ reference counted. Hence don't use this
for reference counted modeset objects like framebuffers.




.. _xref_drm_mode_object_find:

drm_mode_object_find
====================

.. c:function:: struct drm_mode_object * drm_mode_object_find (struct drm_device * dev, uint32_t id, uint32_t type)

    look up a drm object with static lifetime

    :param struct drm_device * dev:
        drm device

    :param uint32_t id:
        id of the mode object

    :param uint32_t type:
        type of the mode object



Description
-----------

Note that framebuffers cannot be looked up with this functions - since those
are reference counted, they need special treatment.  Even with
DRM_MODE_OBJECT_ANY (although that will simply return NULL
rather than :c:func:`WARN_ON`).




.. _xref_drm_framebuffer_init:

drm_framebuffer_init
====================

.. c:function:: int drm_framebuffer_init (struct drm_device * dev, struct drm_framebuffer * fb, const struct drm_framebuffer_funcs * funcs)

    initialize a framebuffer

    :param struct drm_device * dev:
        DRM device

    :param struct drm_framebuffer * fb:
        framebuffer to be initialized

    :param const struct drm_framebuffer_funcs * funcs:
        ... with these functions



Description
-----------

Allocates an ID for the framebuffer's parent mode object, sets its mode
functions & device file and adds it to the master fd list.



IMPORTANT
---------

This functions publishes the fb and makes it available for concurrent access
by other users. Which means by this point the fb _must_ be fully set up -
since all the fb attributes are invariant over its lifetime, no further
locking but only correct reference counting is required.



Returns
-------

Zero on success, error code on failure.




.. _xref_drm_framebuffer_lookup:

drm_framebuffer_lookup
======================

.. c:function:: struct drm_framebuffer * drm_framebuffer_lookup (struct drm_device * dev, uint32_t id)

    look up a drm framebuffer and grab a reference

    :param struct drm_device * dev:
        drm device

    :param uint32_t id:
        id of the fb object



Description
-----------

If successful, this grabs an additional reference to the framebuffer -
callers need to make sure to eventually unreference the returned framebuffer
again, using **drm_framebuffer_unreference**.




.. _xref_drm_framebuffer_unreference:

drm_framebuffer_unreference
===========================

.. c:function:: void drm_framebuffer_unreference (struct drm_framebuffer * fb)

    unref a framebuffer

    :param struct drm_framebuffer * fb:
        framebuffer to unref



Description
-----------

This functions decrements the fb's refcount and frees it if it drops to zero.




.. _xref_drm_framebuffer_reference:

drm_framebuffer_reference
=========================

.. c:function:: void drm_framebuffer_reference (struct drm_framebuffer * fb)

    incr the fb refcnt

    :param struct drm_framebuffer * fb:
        framebuffer



Description
-----------

This functions increments the fb's refcount.




.. _xref_drm_framebuffer_unregister_private:

drm_framebuffer_unregister_private
==================================

.. c:function:: void drm_framebuffer_unregister_private (struct drm_framebuffer * fb)

    unregister a private fb from the lookup idr

    :param struct drm_framebuffer * fb:
        fb to unregister



Description
-----------

Drivers need to call this when cleaning up driver-private framebuffers, e.g.
those used for fbdev. Note that the caller must hold a reference of it's own,
i.e. the object may not be destroyed through this call (since it'll lead to a
locking inversion).




.. _xref_drm_framebuffer_cleanup:

drm_framebuffer_cleanup
=======================

.. c:function:: void drm_framebuffer_cleanup (struct drm_framebuffer * fb)

    remove a framebuffer object

    :param struct drm_framebuffer * fb:
        framebuffer to remove



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




.. _xref_drm_framebuffer_remove:

drm_framebuffer_remove
======================

.. c:function:: void drm_framebuffer_remove (struct drm_framebuffer * fb)

    remove and unreference a framebuffer object

    :param struct drm_framebuffer * fb:
        framebuffer to remove



Description
-----------

Scans all the CRTCs and planes in **dev**'s mode_config.  If they're
using **fb**, removes it, setting it to NULL. Then drops the reference to the
passed-in framebuffer. Might take the modeset locks.


Note that this function optimizes the cleanup away if the caller holds the
last reference to the framebuffer. It is also guaranteed to not take the
modeset locks in this case.




.. _xref_drm_crtc_init_with_planes:

drm_crtc_init_with_planes
=========================

.. c:function:: int drm_crtc_init_with_planes (struct drm_device * dev, struct drm_crtc * crtc, struct drm_plane * primary, struct drm_plane * cursor, const struct drm_crtc_funcs * funcs, const char * name,  ...)

    Initialise a new CRTC object with specified primary and cursor planes.

    :param struct drm_device * dev:
        DRM device

    :param struct drm_crtc * crtc:
        CRTC object to init

    :param struct drm_plane * primary:
        Primary plane for CRTC

    :param struct drm_plane * cursor:
        Cursor plane for CRTC

    :param const struct drm_crtc_funcs * funcs:
        callbacks for the new CRTC

    :param const char * name:
        printf style format string for the CRTC name, or NULL for default name

    :param ...:
        variable arguments



Description
-----------

Inits a new object created as base part of a driver crtc object.



Returns
-------

Zero on success, error code on failure.




.. _xref_drm_crtc_cleanup:

drm_crtc_cleanup
================

.. c:function:: void drm_crtc_cleanup (struct drm_crtc * crtc)

    Clean up the core crtc usage

    :param struct drm_crtc * crtc:
        CRTC to cleanup



Description
-----------

This function cleans up **crtc** and removes it from the DRM mode setting
core. Note that the function does *not* free the crtc structure itself,
this is the responsibility of the caller.




.. _xref_drm_crtc_index:

drm_crtc_index
==============

.. c:function:: unsigned int drm_crtc_index (struct drm_crtc * crtc)

    find the index of a registered CRTC

    :param struct drm_crtc * crtc:
        CRTC to find index for



Description
-----------

Given a registered CRTC, return the index of that CRTC within a DRM
device's list of CRTCs.




.. _xref_drm_display_info_set_bus_formats:

drm_display_info_set_bus_formats
================================

.. c:function:: int drm_display_info_set_bus_formats (struct drm_display_info * info, const u32 * formats, unsigned int num_formats)

    set the supported bus formats

    :param struct drm_display_info * info:
        display info to store bus formats in

    :param const u32 * formats:
        array containing the supported bus formats

    :param unsigned int num_formats:
        the number of entries in the fmts array



Description
-----------

Store the supported bus formats in display info structure.
See MEDIA_BUS_FMT_* definitions in include/uapi/linux/media-bus-format.h for
a full list of available formats.




.. _xref_drm_connector_get_cmdline_mode:

drm_connector_get_cmdline_mode
==============================

.. c:function:: void drm_connector_get_cmdline_mode (struct drm_connector * connector)

    reads the user's cmdline mode

    :param struct drm_connector * connector:
        connector to quwery



Description
-----------

The kernel supports per-connector configration of its consoles through
use of the video= parameter. This function parses that option and
extracts the user's specified mode (or enable/disable status) for a
particular connector. This is typically only used during the early fbdev
setup.




.. _xref_drm_connector_init:

drm_connector_init
==================

.. c:function:: int drm_connector_init (struct drm_device * dev, struct drm_connector * connector, const struct drm_connector_funcs * funcs, int connector_type)

    Init a preallocated connector

    :param struct drm_device * dev:
        DRM device

    :param struct drm_connector * connector:
        the connector to init

    :param const struct drm_connector_funcs * funcs:
        callbacks for this connector

    :param int connector_type:
        user visible type of the connector



Description
-----------

Initialises a preallocated connector. Connectors should be
subclassed as part of driver connector objects.



Returns
-------

Zero on success, error code on failure.




.. _xref_drm_connector_cleanup:

drm_connector_cleanup
=====================

.. c:function:: void drm_connector_cleanup (struct drm_connector * connector)

    cleans up an initialised connector

    :param struct drm_connector * connector:
        connector to cleanup



Description
-----------

Cleans up the connector but doesn't free the object.




.. _xref_drm_connector_register:

drm_connector_register
======================

.. c:function:: int drm_connector_register (struct drm_connector * connector)

    register a connector

    :param struct drm_connector * connector:
        the connector to register



Description
-----------

Register userspace interfaces for a connector



Returns
-------

Zero on success, error code on failure.




.. _xref_drm_connector_unregister:

drm_connector_unregister
========================

.. c:function:: void drm_connector_unregister (struct drm_connector * connector)

    unregister a connector

    :param struct drm_connector * connector:
        the connector to unregister



Description
-----------

Unregister userspace interfaces for a connector




.. _xref_drm_connector_unplug_all:

drm_connector_unplug_all
========================

.. c:function:: void drm_connector_unplug_all (struct drm_device * dev)

    unregister connector userspace interfaces

    :param struct drm_device * dev:
        drm device



Description
-----------

This function unregisters all connector userspace interfaces in sysfs. Should
be call when the device is disconnected, e.g. from an usb driver's
->disconnect callback.




.. _xref_drm_encoder_init:

drm_encoder_init
================

.. c:function:: int drm_encoder_init (struct drm_device * dev, struct drm_encoder * encoder, const struct drm_encoder_funcs * funcs, int encoder_type, const char * name,  ...)

    Init a preallocated encoder

    :param struct drm_device * dev:
        drm device

    :param struct drm_encoder * encoder:
        the encoder to init

    :param const struct drm_encoder_funcs * funcs:
        callbacks for this encoder

    :param int encoder_type:
        user visible type of the encoder

    :param const char * name:
        printf style format string for the encoder name, or NULL for default name

    :param ...:
        variable arguments



Description
-----------

Initialises a preallocated encoder. Encoder should be
subclassed as part of driver encoder objects.



Returns
-------

Zero on success, error code on failure.




.. _xref_drm_encoder_index:

drm_encoder_index
=================

.. c:function:: unsigned int drm_encoder_index (struct drm_encoder * encoder)

    find the index of a registered encoder

    :param struct drm_encoder * encoder:
        encoder to find index for



Description
-----------

Given a registered encoder, return the index of that encoder within a DRM
device's list of encoders.




.. _xref_drm_encoder_cleanup:

drm_encoder_cleanup
===================

.. c:function:: void drm_encoder_cleanup (struct drm_encoder * encoder)

    cleans up an initialised encoder

    :param struct drm_encoder * encoder:
        encoder to cleanup



Description
-----------

Cleans up the encoder but doesn't free the object.




.. _xref_drm_universal_plane_init:

drm_universal_plane_init
========================

.. c:function:: int drm_universal_plane_init (struct drm_device * dev, struct drm_plane * plane, unsigned long possible_crtcs, const struct drm_plane_funcs * funcs, const uint32_t * formats, unsigned int format_count, enum drm_plane_type type, const char * name,  ...)

    Initialize a new universal plane object

    :param struct drm_device * dev:
        DRM device

    :param struct drm_plane * plane:
        plane object to init

    :param unsigned long possible_crtcs:
        bitmask of possible CRTCs

    :param const struct drm_plane_funcs * funcs:
        callbacks for the new plane

    :param const uint32_t * formats:
        array of supported formats (``DRM_FORMAT_``*)

    :param unsigned int format_count:
        number of elements in **formats**

    :param enum drm_plane_type type:
        type of plane (overlay, primary, cursor)

    :param const char * name:
        printf style format string for the plane name, or NULL for default name

    :param ...:
        variable arguments



Description
-----------

Initializes a plane object of type **type**.



Returns
-------

Zero on success, error code on failure.




.. _xref_drm_plane_init:

drm_plane_init
==============

.. c:function:: int drm_plane_init (struct drm_device * dev, struct drm_plane * plane, unsigned long possible_crtcs, const struct drm_plane_funcs * funcs, const uint32_t * formats, unsigned int format_count, bool is_primary)

    Initialize a legacy plane

    :param struct drm_device * dev:
        DRM device

    :param struct drm_plane * plane:
        plane object to init

    :param unsigned long possible_crtcs:
        bitmask of possible CRTCs

    :param const struct drm_plane_funcs * funcs:
        callbacks for the new plane

    :param const uint32_t * formats:
        array of supported formats (``DRM_FORMAT_``*)

    :param unsigned int format_count:
        number of elements in **formats**

    :param bool is_primary:
        plane type (primary vs overlay)



Description
-----------

Legacy API to initialize a DRM plane.


New drivers should call :c:func:`drm_universal_plane_init` instead.



Returns
-------

Zero on success, error code on failure.




.. _xref_drm_plane_cleanup:

drm_plane_cleanup
=================

.. c:function:: void drm_plane_cleanup (struct drm_plane * plane)

    Clean up the core plane usage

    :param struct drm_plane * plane:
        plane to cleanup



Description
-----------

This function cleans up **plane** and removes it from the DRM mode setting
core. Note that the function does *not* free the plane structure itself,
this is the responsibility of the caller.




.. _xref_drm_plane_index:

drm_plane_index
===============

.. c:function:: unsigned int drm_plane_index (struct drm_plane * plane)

    find the index of a registered plane

    :param struct drm_plane * plane:
        plane to find index for



Description
-----------

Given a registered plane, return the index of that CRTC within a DRM
device's list of planes.




.. _xref_drm_plane_from_index:

drm_plane_from_index
====================

.. c:function:: struct drm_plane * drm_plane_from_index (struct drm_device * dev, int idx)

    find the registered plane at an index

    :param struct drm_device * dev:
        DRM device

    :param int idx:
        index of registered plane to find for



Description
-----------

Given a plane index, return the registered plane from DRM device's
list of planes with matching index.




.. _xref_drm_plane_force_disable:

drm_plane_force_disable
=======================

.. c:function:: void drm_plane_force_disable (struct drm_plane * plane)

    Forcibly disable a plane

    :param struct drm_plane * plane:
        plane to disable



Description
-----------

Forces the plane to be disabled.


Used when the plane's current framebuffer is destroyed,
and when restoring fbdev mode.




.. _xref_drm_mode_create_dvi_i_properties:

drm_mode_create_dvi_i_properties
================================

.. c:function:: int drm_mode_create_dvi_i_properties (struct drm_device * dev)

    create DVI-I specific connector properties

    :param struct drm_device * dev:
        DRM device



Description
-----------

Called by a driver the first time a DVI-I connector is made.




.. _xref_drm_mode_create_tv_properties:

drm_mode_create_tv_properties
=============================

.. c:function:: int drm_mode_create_tv_properties (struct drm_device * dev, unsigned int num_modes, const char *const modes[])

    create TV specific connector properties

    :param struct drm_device * dev:
        DRM device

    :param unsigned int num_modes:
        number of different TV formats (modes) supported

    :param const char *const modes[]:



Description
-----------

Called by a driver's TV initialization routine, this function creates
the TV specific connector properties for a given device.  Caller is
responsible for allocating a list of format names and passing them to
this routine.




.. _xref_drm_mode_create_scaling_mode_property:

drm_mode_create_scaling_mode_property
=====================================

.. c:function:: int drm_mode_create_scaling_mode_property (struct drm_device * dev)

    create scaling mode property

    :param struct drm_device * dev:
        DRM device



Description
-----------

Called by a driver the first time it's needed, must be attached to desired
connectors.




.. _xref_drm_mode_create_aspect_ratio_property:

drm_mode_create_aspect_ratio_property
=====================================

.. c:function:: int drm_mode_create_aspect_ratio_property (struct drm_device * dev)

    create aspect ratio property

    :param struct drm_device * dev:
        DRM device



Description
-----------

Called by a driver the first time it's needed, must be attached to desired
connectors.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_create_dirty_info_property:

drm_mode_create_dirty_info_property
===================================

.. c:function:: int drm_mode_create_dirty_info_property (struct drm_device * dev)

    create dirty property

    :param struct drm_device * dev:
        DRM device



Description
-----------

Called by a driver the first time it's needed, must be attached to desired
connectors.




.. _xref_drm_mode_create_suggested_offset_properties:

drm_mode_create_suggested_offset_properties
===========================================

.. c:function:: int drm_mode_create_suggested_offset_properties (struct drm_device * dev)

    create suggests offset properties

    :param struct drm_device * dev:
        DRM device



Description
-----------

Create the the suggested x/y offset property for connectors.




.. _xref_drm_mode_getresources:

drm_mode_getresources
=====================

.. c:function:: int drm_mode_getresources (struct drm_device * dev, void * data, struct drm_file * file_priv)

    get graphics configuration

    :param struct drm_device * dev:
        drm device for the ioctl

    :param void * data:
        data pointer for the ioctl

    :param struct drm_file * file_priv:
        drm file for the ioctl call



Description
-----------

Construct a set of configuration description structures and return
them to the user, including CRTC, connector and framebuffer configuration.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_getcrtc:

drm_mode_getcrtc
================

.. c:function:: int drm_mode_getcrtc (struct drm_device * dev, void * data, struct drm_file * file_priv)

    get CRTC configuration

    :param struct drm_device * dev:
        drm device for the ioctl

    :param void * data:
        data pointer for the ioctl

    :param struct drm_file * file_priv:
        drm file for the ioctl call



Description
-----------

Construct a CRTC configuration structure to return to the user.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_getconnector:

drm_mode_getconnector
=====================

.. c:function:: int drm_mode_getconnector (struct drm_device * dev, void * data, struct drm_file * file_priv)

    get connector configuration

    :param struct drm_device * dev:
        drm device for the ioctl

    :param void * data:
        data pointer for the ioctl

    :param struct drm_file * file_priv:
        drm file for the ioctl call



Description
-----------

Construct a connector configuration structure to return to the user.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_getencoder:

drm_mode_getencoder
===================

.. c:function:: int drm_mode_getencoder (struct drm_device * dev, void * data, struct drm_file * file_priv)

    get encoder configuration

    :param struct drm_device * dev:
        drm device for the ioctl

    :param void * data:
        data pointer for the ioctl

    :param struct drm_file * file_priv:
        drm file for the ioctl call



Description
-----------

Construct a encoder configuration structure to return to the user.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_getplane_res:

drm_mode_getplane_res
=====================

.. c:function:: int drm_mode_getplane_res (struct drm_device * dev, void * data, struct drm_file * file_priv)

    enumerate all plane resources

    :param struct drm_device * dev:
        DRM device

    :param void * data:
        ioctl data

    :param struct drm_file * file_priv:
        DRM file info



Description
-----------

Construct a list of plane ids to return to the user.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_getplane:

drm_mode_getplane
=================

.. c:function:: int drm_mode_getplane (struct drm_device * dev, void * data, struct drm_file * file_priv)

    get plane configuration

    :param struct drm_device * dev:
        DRM device

    :param void * data:
        ioctl data

    :param struct drm_file * file_priv:
        DRM file info



Description
-----------

Construct a plane configuration structure to return to the user.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_plane_check_pixel_format:

drm_plane_check_pixel_format
============================

.. c:function:: int drm_plane_check_pixel_format (const struct drm_plane * plane, u32 format)

    Check if the plane supports the pixel format

    :param const struct drm_plane * plane:
        plane to check for format support

    :param u32 format:
        the pixel format



Returns
-------

Zero of **plane** has **format** in its list of supported pixel formats, -EINVAL
otherwise.




.. _xref_drm_mode_setplane:

drm_mode_setplane
=================

.. c:function:: int drm_mode_setplane (struct drm_device * dev, void * data, struct drm_file * file_priv)

    configure a plane's configuration

    :param struct drm_device * dev:
        DRM device

    :param void * data:
        ioctl data*

    :param struct drm_file * file_priv:
        DRM file info



Description
-----------

Set plane configuration, including placement, fb, scaling, and other factors.
Or pass a NULL fb to disable (planes may be disabled without providing a
valid crtc).



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_set_config_internal:

drm_mode_set_config_internal
============================

.. c:function:: int drm_mode_set_config_internal (struct drm_mode_set * set)

    helper to call -\\\gt;set_config

    :param struct drm_mode_set * set:
        modeset config to set



Description
-----------

This is a little helper to wrap internal calls to the ->set_config driver
interface. The only thing it adds is correct refcounting dance.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_crtc_get_hv_timing:

drm_crtc_get_hv_timing
======================

.. c:function:: void drm_crtc_get_hv_timing (const struct drm_display_mode * mode, int * hdisplay, int * vdisplay)

    Fetches hdisplay/vdisplay for given mode

    :param const struct drm_display_mode * mode:
        mode to query

    :param int * hdisplay:
        hdisplay value to fill in

    :param int * vdisplay:
        vdisplay value to fill in



Description
-----------

The vdisplay value will be doubled if the specified mode is a stereo mode of
the appropriate layout.




.. _xref_drm_crtc_check_viewport:

drm_crtc_check_viewport
=======================

.. c:function:: int drm_crtc_check_viewport (const struct drm_crtc * crtc, int x, int y, const struct drm_display_mode * mode, const struct drm_framebuffer * fb)

    Checks that a framebuffer is big enough for the CRTC viewport

    :param const struct drm_crtc * crtc:
        CRTC that framebuffer will be displayed on

    :param int x:
        x panning

    :param int y:
        y panning

    :param const struct drm_display_mode * mode:
        mode that framebuffer will be displayed under

    :param const struct drm_framebuffer * fb:
        framebuffer to check size of




.. _xref_drm_mode_setcrtc:

drm_mode_setcrtc
================

.. c:function:: int drm_mode_setcrtc (struct drm_device * dev, void * data, struct drm_file * file_priv)

    set CRTC configuration

    :param struct drm_device * dev:
        drm device for the ioctl

    :param void * data:
        data pointer for the ioctl

    :param struct drm_file * file_priv:
        drm file for the ioctl call



Description
-----------

Build a new CRTC configuration based on user request.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_cursor_universal:

drm_mode_cursor_universal
=========================

.. c:function:: int drm_mode_cursor_universal (struct drm_crtc * crtc, struct drm_mode_cursor2 * req, struct drm_file * file_priv)

    translate legacy cursor ioctl call into a universal plane handler call

    :param struct drm_crtc * crtc:
        crtc to update cursor for

    :param struct drm_mode_cursor2 * req:
        data pointer for the ioctl

    :param struct drm_file * file_priv:
        drm file for the ioctl call



Description
-----------

Legacy cursor ioctl's work directly with driver buffer handles.  To
translate legacy ioctl calls into universal plane handler calls, we need to
wrap the native buffer handle in a drm_framebuffer.


Note that we assume any handle passed to the legacy ioctls was a 32-bit ARGB
buffer with a pitch of 4*width; the universal plane interface should be used
directly in cases where the hardware can support other buffer settings and
userspace wants to make use of these capabilities.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_cursor_ioctl:

drm_mode_cursor_ioctl
=====================

.. c:function:: int drm_mode_cursor_ioctl (struct drm_device * dev, void * data, struct drm_file * file_priv)

    set CRTC's cursor configuration

    :param struct drm_device * dev:
        drm device for the ioctl

    :param void * data:
        data pointer for the ioctl

    :param struct drm_file * file_priv:
        drm file for the ioctl call



Description
-----------

Set the cursor configuration based on user request.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_cursor2_ioctl:

drm_mode_cursor2_ioctl
======================

.. c:function:: int drm_mode_cursor2_ioctl (struct drm_device * dev, void * data, struct drm_file * file_priv)

    set CRTC's cursor configuration

    :param struct drm_device * dev:
        drm device for the ioctl

    :param void * data:
        data pointer for the ioctl

    :param struct drm_file * file_priv:
        drm file for the ioctl call



Description
-----------

Set the cursor configuration based on user request. This implements the 2nd
version of the cursor ioctl, which allows userspace to additionally specify
the hotspot of the pointer.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_legacy_fb_format:

drm_mode_legacy_fb_format
=========================

.. c:function:: uint32_t drm_mode_legacy_fb_format (uint32_t bpp, uint32_t depth)

    compute drm fourcc code from legacy description

    :param uint32_t bpp:
        bits per pixels

    :param uint32_t depth:
        bit depth per pixel



Description
-----------

Computes a drm fourcc pixel format code for the given **bpp**/**depth** values.
Useful in fbdev emulation code, since that deals in those values.




.. _xref_drm_mode_addfb:

drm_mode_addfb
==============

.. c:function:: int drm_mode_addfb (struct drm_device * dev, void * data, struct drm_file * file_priv)

    add an FB to the graphics configuration

    :param struct drm_device * dev:
        drm device for the ioctl

    :param void * data:
        data pointer for the ioctl

    :param struct drm_file * file_priv:
        drm file for the ioctl call



Description
-----------

Add a new FB to the specified CRTC, given a user request. This is the
original addfb ioctl which only supported RGB formats.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_addfb2:

drm_mode_addfb2
===============

.. c:function:: int drm_mode_addfb2 (struct drm_device * dev, void * data, struct drm_file * file_priv)

    add an FB to the graphics configuration

    :param struct drm_device * dev:
        drm device for the ioctl

    :param void * data:
        data pointer for the ioctl

    :param struct drm_file * file_priv:
        drm file for the ioctl call



Description
-----------

Add a new FB to the specified CRTC, given a user request with format. This is
the 2nd version of the addfb ioctl, which supports multi-planar framebuffers
and uses fourcc codes as pixel format specifiers.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_rmfb:

drm_mode_rmfb
=============

.. c:function:: int drm_mode_rmfb (struct drm_device * dev, void * data, struct drm_file * file_priv)

    remove an FB from the configuration

    :param struct drm_device * dev:
        drm device for the ioctl

    :param void * data:
        data pointer for the ioctl

    :param struct drm_file * file_priv:
        drm file for the ioctl call



Description
-----------

Remove the FB specified by the user.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_getfb:

drm_mode_getfb
==============

.. c:function:: int drm_mode_getfb (struct drm_device * dev, void * data, struct drm_file * file_priv)

    get FB info

    :param struct drm_device * dev:
        drm device for the ioctl

    :param void * data:
        data pointer for the ioctl

    :param struct drm_file * file_priv:
        drm file for the ioctl call



Description
-----------

Lookup the FB given its ID and return info about it.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_dirtyfb_ioctl:

drm_mode_dirtyfb_ioctl
======================

.. c:function:: int drm_mode_dirtyfb_ioctl (struct drm_device * dev, void * data, struct drm_file * file_priv)

    flush frontbuffer rendering on an FB

    :param struct drm_device * dev:
        drm device for the ioctl

    :param void * data:
        data pointer for the ioctl

    :param struct drm_file * file_priv:
        drm file for the ioctl call



Description
-----------

Lookup the FB and flush out the damaged area supplied by userspace as a clip
rectangle list. Generic userspace which does frontbuffer rendering must call
this ioctl to flush out the changes on manual-update display outputs, e.g.
usb display-link, mipi manual update panels or edp panel self refresh modes.


Modesetting drivers which always update the frontbuffer do not need to
implement the corresponding ->dirty framebuffer callback.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_fb_release:

drm_fb_release
==============

.. c:function:: void drm_fb_release (struct drm_file * priv)

    remove and free the FBs on this file

    :param struct drm_file * priv:
        drm file for the ioctl



Description
-----------

Destroy all the FBs associated with **filp**.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_property_create:

drm_property_create
===================

.. c:function:: struct drm_property * drm_property_create (struct drm_device * dev, int flags, const char * name, int num_values)

    create a new property type

    :param struct drm_device * dev:
        drm device

    :param int flags:
        flags specifying the property type

    :param const char * name:
        name of the property

    :param int num_values:
        number of pre-defined values



Description
-----------

This creates a new generic drm property which can then be attached to a drm
object with drm_object_attach_property. The returned property object must be
freed with drm_property_destroy.


Note that the DRM core keeps a per-device list of properties and that, if
:c:func:`drm_mode_config_cleanup` is called, it will destroy all properties created
by the driver.



Returns
-------

A pointer to the newly created property on success, NULL on failure.




.. _xref_drm_property_create_enum:

drm_property_create_enum
========================

.. c:function:: struct drm_property * drm_property_create_enum (struct drm_device * dev, int flags, const char * name, const struct drm_prop_enum_list * props, int num_values)

    create a new enumeration property type

    :param struct drm_device * dev:
        drm device

    :param int flags:
        flags specifying the property type

    :param const char * name:
        name of the property

    :param const struct drm_prop_enum_list * props:
        enumeration lists with property values

    :param int num_values:
        number of pre-defined values



Description
-----------

This creates a new generic drm property which can then be attached to a drm
object with drm_object_attach_property. The returned property object must be
freed with drm_property_destroy.


Userspace is only allowed to set one of the predefined values for enumeration
properties.



Returns
-------

A pointer to the newly created property on success, NULL on failure.




.. _xref_drm_property_create_bitmask:

drm_property_create_bitmask
===========================

.. c:function:: struct drm_property * drm_property_create_bitmask (struct drm_device * dev, int flags, const char * name, const struct drm_prop_enum_list * props, int num_props, uint64_t supported_bits)

    create a new bitmask property type

    :param struct drm_device * dev:
        drm device

    :param int flags:
        flags specifying the property type

    :param const char * name:
        name of the property

    :param const struct drm_prop_enum_list * props:
        enumeration lists with property bitflags

    :param int num_props:
        size of the **props** array

    :param uint64_t supported_bits:
        bitmask of all supported enumeration values



Description
-----------

This creates a new bitmask drm property which can then be attached to a drm
object with drm_object_attach_property. The returned property object must be
freed with drm_property_destroy.


Compared to plain enumeration properties userspace is allowed to set any
or'ed together combination of the predefined property bitflag values



Returns
-------

A pointer to the newly created property on success, NULL on failure.




.. _xref_drm_property_create_range:

drm_property_create_range
=========================

.. c:function:: struct drm_property * drm_property_create_range (struct drm_device * dev, int flags, const char * name, uint64_t min, uint64_t max)

    create a new unsigned ranged property type

    :param struct drm_device * dev:
        drm device

    :param int flags:
        flags specifying the property type

    :param const char * name:
        name of the property

    :param uint64_t min:
        minimum value of the property

    :param uint64_t max:
        maximum value of the property



Description
-----------

This creates a new generic drm property which can then be attached to a drm
object with drm_object_attach_property. The returned property object must be
freed with drm_property_destroy.


Userspace is allowed to set any unsigned integer value in the (min, max)
range inclusive.



Returns
-------

A pointer to the newly created property on success, NULL on failure.




.. _xref_drm_property_create_signed_range:

drm_property_create_signed_range
================================

.. c:function:: struct drm_property * drm_property_create_signed_range (struct drm_device * dev, int flags, const char * name, int64_t min, int64_t max)

    create a new signed ranged property type

    :param struct drm_device * dev:
        drm device

    :param int flags:
        flags specifying the property type

    :param const char * name:
        name of the property

    :param int64_t min:
        minimum value of the property

    :param int64_t max:
        maximum value of the property



Description
-----------

This creates a new generic drm property which can then be attached to a drm
object with drm_object_attach_property. The returned property object must be
freed with drm_property_destroy.


Userspace is allowed to set any signed integer value in the (min, max)
range inclusive.



Returns
-------

A pointer to the newly created property on success, NULL on failure.




.. _xref_drm_property_create_object:

drm_property_create_object
==========================

.. c:function:: struct drm_property * drm_property_create_object (struct drm_device * dev, int flags, const char * name, uint32_t type)

    create a new object property type

    :param struct drm_device * dev:
        drm device

    :param int flags:
        flags specifying the property type

    :param const char * name:
        name of the property

    :param uint32_t type:
        object type from DRM_MODE_OBJECT_* defines



Description
-----------

This creates a new generic drm property which can then be attached to a drm
object with drm_object_attach_property. The returned property object must be
freed with drm_property_destroy.


Userspace is only allowed to set this to any property value of the given
**type**. Only useful for atomic properties, which is enforced.



Returns
-------

A pointer to the newly created property on success, NULL on failure.




.. _xref_drm_property_create_bool:

drm_property_create_bool
========================

.. c:function:: struct drm_property * drm_property_create_bool (struct drm_device * dev, int flags, const char * name)

    create a new boolean property type

    :param struct drm_device * dev:
        drm device

    :param int flags:
        flags specifying the property type

    :param const char * name:
        name of the property



Description
-----------

This creates a new generic drm property which can then be attached to a drm
object with drm_object_attach_property. The returned property object must be
freed with drm_property_destroy.


This is implemented as a ranged property with only {0, 1} as valid values.



Returns
-------

A pointer to the newly created property on success, NULL on failure.




.. _xref_drm_property_add_enum:

drm_property_add_enum
=====================

.. c:function:: int drm_property_add_enum (struct drm_property * property, int index, uint64_t value, const char * name)

    add a possible value to an enumeration property

    :param struct drm_property * property:
        enumeration property to change

    :param int index:
        index of the new enumeration

    :param uint64_t value:
        value of the new enumeration

    :param const char * name:
        symbolic name of the new enumeration



Description
-----------

This functions adds enumerations to a property.


It's use is deprecated, drivers should use one of the more specific helpers
to directly create the property with all enumerations already attached.



Returns
-------

Zero on success, error code on failure.




.. _xref_drm_property_destroy:

drm_property_destroy
====================

.. c:function:: void drm_property_destroy (struct drm_device * dev, struct drm_property * property)

    destroy a drm property

    :param struct drm_device * dev:
        drm device

    :param struct drm_property * property:
        property to destry



Description
-----------

This function frees a property including any attached resources like
enumeration values.




.. _xref_drm_object_attach_property:

drm_object_attach_property
==========================

.. c:function:: void drm_object_attach_property (struct drm_mode_object * obj, struct drm_property * property, uint64_t init_val)

    attach a property to a modeset object

    :param struct drm_mode_object * obj:
        drm modeset object

    :param struct drm_property * property:
        property to attach

    :param uint64_t init_val:
        initial value of the property



Description
-----------

This attaches the given property to the modeset object with the given initial
value. Currently this function cannot fail since the properties are stored in
a statically sized array.




.. _xref_drm_object_property_set_value:

drm_object_property_set_value
=============================

.. c:function:: int drm_object_property_set_value (struct drm_mode_object * obj, struct drm_property * property, uint64_t val)

    set the value of a property

    :param struct drm_mode_object * obj:
        drm mode object to set property value for

    :param struct drm_property * property:
        property to set

    :param uint64_t val:
        value the property should be set to



Description
-----------

This functions sets a given property on a given object. This function only
changes the software state of the property, it does not call into the
driver's ->set_property callback.



Returns
-------

Zero on success, error code on failure.




.. _xref_drm_object_property_get_value:

drm_object_property_get_value
=============================

.. c:function:: int drm_object_property_get_value (struct drm_mode_object * obj, struct drm_property * property, uint64_t * val)

    retrieve the value of a property

    :param struct drm_mode_object * obj:
        drm mode object to get property value from

    :param struct drm_property * property:
        property to retrieve

    :param uint64_t * val:
        storage for the property value



Description
-----------

This function retrieves the softare state of the given property for the given
property. Since there is no driver callback to retrieve the current property
value this might be out of sync with the hardware, depending upon the driver
and property.



Returns
-------

Zero on success, error code on failure.




.. _xref_drm_mode_getproperty_ioctl:

drm_mode_getproperty_ioctl
==========================

.. c:function:: int drm_mode_getproperty_ioctl (struct drm_device * dev, void * data, struct drm_file * file_priv)

    get the property metadata

    :param struct drm_device * dev:
        DRM device

    :param void * data:
        ioctl data

    :param struct drm_file * file_priv:
        DRM file info



Description
-----------

This function retrieves the metadata for a given property, like the different
possible values for an enum property or the limits for a range property.


Blob properties are special


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_property_create_blob:

drm_property_create_blob
========================

.. c:function:: struct drm_property_blob * drm_property_create_blob (struct drm_device * dev, size_t length, const void * data)

    Create new blob property

    :param struct drm_device * dev:
        DRM device to create property for

    :param size_t length:
        Length to allocate for blob data

    :param const void * data:
        If specified, copies data into blob



Description
-----------



Creates a new blob property for a specified DRM device, optionally
copying data.



Returns
-------

New blob property with a single reference on success, or an ERR_PTR
value on failure.




.. _xref_drm_property_free_blob:

drm_property_free_blob
======================

.. c:function:: void drm_property_free_blob (struct kref * kref)

    Blob property destructor

    :param struct kref * kref:
        Reference



Description
-----------



Internal free function for blob properties; must not be used directly.




.. _xref_drm_property_unreference_blob:

drm_property_unreference_blob
=============================

.. c:function:: void drm_property_unreference_blob (struct drm_property_blob * blob)

    Unreference a blob property

    :param struct drm_property_blob * blob:
        Pointer to blob property



Description
-----------



Drop a reference on a blob property. May free the object.




.. _xref_drm_property_unreference_blob_locked:

drm_property_unreference_blob_locked
====================================

.. c:function:: void drm_property_unreference_blob_locked (struct drm_property_blob * blob)

    Unreference a blob property with blob_lock held

    :param struct drm_property_blob * blob:
        Pointer to blob property



Description
-----------



Drop a reference on a blob property. May free the object. This must be
called with blob_lock held.




.. _xref_drm_property_destroy_user_blobs:

drm_property_destroy_user_blobs
===============================

.. c:function:: void drm_property_destroy_user_blobs (struct drm_device * dev, struct drm_file * file_priv)

    destroy all blobs created by this client

    :param struct drm_device * dev:
        DRM device

    :param struct drm_file * file_priv:
        destroy all blobs owned by this file handle




.. _xref_drm_property_reference_blob:

drm_property_reference_blob
===========================

.. c:function:: struct drm_property_blob * drm_property_reference_blob (struct drm_property_blob * blob)

    Take a reference on an existing property

    :param struct drm_property_blob * blob:
        Pointer to blob property



Description
-----------



Take a new reference on an existing blob property.




.. _xref_drm_property_lookup_blob:

drm_property_lookup_blob
========================

.. c:function:: struct drm_property_blob * drm_property_lookup_blob (struct drm_device * dev, uint32_t id)

    look up a blob property and take a reference

    :param struct drm_device * dev:
        drm device

    :param uint32_t id:
        id of the blob property



Description
-----------

If successful, this takes an additional reference to the blob property.
callers need to make sure to eventually unreference the returned property
again, using **drm_property_unreference_blob**.




.. _xref_drm_property_replace_global_blob:

drm_property_replace_global_blob
================================

.. c:function:: int drm_property_replace_global_blob (struct drm_device * dev, struct drm_property_blob ** replace, size_t length, const void * data, struct drm_mode_object * obj_holds_id, struct drm_property * prop_holds_id)

    atomically replace existing blob property

    :param struct drm_device * dev:
        drm device

    :param struct drm_property_blob ** replace:
        location of blob property pointer to be replaced

    :param size_t length:
        length of data for new blob, or 0 for no data

    :param const void * data:
        content for new blob, or NULL for no data

    :param struct drm_mode_object * obj_holds_id:
        optional object for property holding blob ID

    :param struct drm_property * prop_holds_id:
        optional property holding blob ID
        **return** 0 on success or error on failure



Description
-----------

This function will atomically replace a global property in the blob list,
optionally updating a property which holds the ID of that property. It is



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




.. _xref_drm_mode_getblob_ioctl:

drm_mode_getblob_ioctl
======================

.. c:function:: int drm_mode_getblob_ioctl (struct drm_device * dev, void * data, struct drm_file * file_priv)

    get the contents of a blob property value

    :param struct drm_device * dev:
        DRM device

    :param void * data:
        ioctl data

    :param struct drm_file * file_priv:
        DRM file info



Description
-----------

This function retrieves the contents of a blob property. The value stored in
an object's blob property is just a normal modeset object id.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_createblob_ioctl:

drm_mode_createblob_ioctl
=========================

.. c:function:: int drm_mode_createblob_ioctl (struct drm_device * dev, void * data, struct drm_file * file_priv)

    create a new blob property

    :param struct drm_device * dev:
        DRM device

    :param void * data:
        ioctl data

    :param struct drm_file * file_priv:
        DRM file info



Description
-----------

This function creates a new blob property with user-defined values. In order
to give us sensible validation and checking when creating, rather than at
every potential use, we also require a type to be provided upfront.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_destroyblob_ioctl:

drm_mode_destroyblob_ioctl
==========================

.. c:function:: int drm_mode_destroyblob_ioctl (struct drm_device * dev, void * data, struct drm_file * file_priv)

    destroy a user blob property

    :param struct drm_device * dev:
        DRM device

    :param void * data:
        ioctl data

    :param struct drm_file * file_priv:
        DRM file info



Description
-----------

Destroy an existing user-defined blob property.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_connector_set_path_property:

drm_mode_connector_set_path_property
====================================

.. c:function:: int drm_mode_connector_set_path_property (struct drm_connector * connector, const char * path)

    set tile property on connector

    :param struct drm_connector * connector:
        connector to set property on.

    :param const char * path:
        path to use for property; must not be NULL.



Description
-----------

This creates a property to expose to userspace to specify a
connector path. This is mainly used for DisplayPort MST where
connectors have a topology and we want to allow userspace to give
them more meaningful names.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_connector_set_tile_property:

drm_mode_connector_set_tile_property
====================================

.. c:function:: int drm_mode_connector_set_tile_property (struct drm_connector * connector)

    set tile property on connector

    :param struct drm_connector * connector:
        connector to set property on.



Description
-----------

This looks up the tile information for a connector, and creates a
property for userspace to parse if it exists. The property is of
the form of 8 integers using ':' as a separator.



Returns
-------

Zero on success, errno on failure.




.. _xref_drm_mode_connector_update_edid_property:

drm_mode_connector_update_edid_property
=======================================

.. c:function:: int drm_mode_connector_update_edid_property (struct drm_connector * connector, const struct edid * edid)

    update the edid property of a connector

    :param struct drm_connector * connector:
        drm connector

    :param const struct edid * edid:
        new value of the edid property



Description
-----------

This function creates a new blob modeset object and assigns its id to the
connector's edid property.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_connector_property_set_ioctl:

drm_mode_connector_property_set_ioctl
=====================================

.. c:function:: int drm_mode_connector_property_set_ioctl (struct drm_device * dev, void * data, struct drm_file * file_priv)

    set the current value of a connector property

    :param struct drm_device * dev:
        DRM device

    :param void * data:
        ioctl data

    :param struct drm_file * file_priv:
        DRM file info



Description
-----------

This function sets the current value for a connectors's property. It also
calls into a driver's ->set_property callback to update the hardware state


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_plane_set_obj_prop:

drm_mode_plane_set_obj_prop
===========================

.. c:function:: int drm_mode_plane_set_obj_prop (struct drm_plane * plane, struct drm_property * property, uint64_t value)

    set the value of a property

    :param struct drm_plane * plane:
        drm plane object to set property value for

    :param struct drm_property * property:
        property to set

    :param uint64_t value:
        value the property should be set to



Description
-----------

This functions sets a given property on a given plane object. This function
calls the driver's ->set_property callback and changes the software state of
the property if the callback succeeds.



Returns
-------

Zero on success, error code on failure.




.. _xref_drm_mode_obj_get_properties_ioctl:

drm_mode_obj_get_properties_ioctl
=================================

.. c:function:: int drm_mode_obj_get_properties_ioctl (struct drm_device * dev, void * data, struct drm_file * file_priv)

    get the current value of a object's property

    :param struct drm_device * dev:
        DRM device

    :param void * data:
        ioctl data

    :param struct drm_file * file_priv:
        DRM file info



Description
-----------

This function retrieves the current value for an object's property. Compared
to the connector specific ioctl this one is extended to also work on crtc and
plane objects.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_obj_set_property_ioctl:

drm_mode_obj_set_property_ioctl
===============================

.. c:function:: int drm_mode_obj_set_property_ioctl (struct drm_device * dev, void * data, struct drm_file * file_priv)

    set the current value of an object's property

    :param struct drm_device * dev:
        DRM device

    :param void * data:
        ioctl data

    :param struct drm_file * file_priv:
        DRM file info



Description
-----------

This function sets the current value for an object's property. It also calls
into a driver's ->set_property callback to update the hardware state.
Compared to the connector specific ioctl this one is extended to also work on
crtc and plane objects.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_connector_attach_encoder:

drm_mode_connector_attach_encoder
=================================

.. c:function:: int drm_mode_connector_attach_encoder (struct drm_connector * connector, struct drm_encoder * encoder)

    attach a connector to an encoder

    :param struct drm_connector * connector:
        connector to attach

    :param struct drm_encoder * encoder:
        encoder to attach **connector** to



Description
-----------

This function links up a connector to an encoder. Note that the routing
restrictions between encoders and crtcs are exposed to userspace through the
possible_clones and possible_crtcs bitmasks.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_crtc_set_gamma_size:

drm_mode_crtc_set_gamma_size
============================

.. c:function:: int drm_mode_crtc_set_gamma_size (struct drm_crtc * crtc, int gamma_size)

    set the gamma table size

    :param struct drm_crtc * crtc:
        CRTC to set the gamma table size for

    :param int gamma_size:
        size of the gamma table



Description
-----------

Drivers which support gamma tables should set this to the supported gamma
table size when initializing the CRTC. Currently the drm core only supports a
fixed gamma table size.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_gamma_set_ioctl:

drm_mode_gamma_set_ioctl
========================

.. c:function:: int drm_mode_gamma_set_ioctl (struct drm_device * dev, void * data, struct drm_file * file_priv)

    set the gamma table

    :param struct drm_device * dev:
        DRM device

    :param void * data:
        ioctl data

    :param struct drm_file * file_priv:
        DRM file info



Description
-----------

Set the gamma table of a CRTC to the one passed in by the user. Userspace can
inquire the required gamma table size through drm_mode_gamma_get_ioctl.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_gamma_get_ioctl:

drm_mode_gamma_get_ioctl
========================

.. c:function:: int drm_mode_gamma_get_ioctl (struct drm_device * dev, void * data, struct drm_file * file_priv)

    get the gamma table

    :param struct drm_device * dev:
        DRM device

    :param void * data:
        ioctl data

    :param struct drm_file * file_priv:
        DRM file info



Description
-----------

Copy the current gamma table into the storage provided. This also provides
the gamma table size the driver expects, which can be used to size the
allocated storage.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_page_flip_ioctl:

drm_mode_page_flip_ioctl
========================

.. c:function:: int drm_mode_page_flip_ioctl (struct drm_device * dev, void * data, struct drm_file * file_priv)

    schedule an asynchronous fb update

    :param struct drm_device * dev:
        DRM device

    :param void * data:
        ioctl data

    :param struct drm_file * file_priv:
        DRM file info



Description
-----------

This schedules an asynchronous update on a given CRTC, called page flip.
Optionally a drm event is generated to signal the completion of the event.
Generic drivers cannot assume that a pageflip with changed framebuffer
properties (including driver specific metadata like tiling layout) will work,
but some drivers support e.g. pixel format changes through the pageflip
ioctl.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_config_reset:

drm_mode_config_reset
=====================

.. c:function:: void drm_mode_config_reset (struct drm_device * dev)

    call -\\\gt;reset callbacks

    :param struct drm_device * dev:
        drm device



Description
-----------

This functions calls all the crtc's, encoder's and connector's ->reset
callback. Drivers can use this in e.g. their driver load or resume code to
reset hardware and software state.




.. _xref_drm_mode_create_dumb_ioctl:

drm_mode_create_dumb_ioctl
==========================

.. c:function:: int drm_mode_create_dumb_ioctl (struct drm_device * dev, void * data, struct drm_file * file_priv)

    create a dumb backing storage buffer

    :param struct drm_device * dev:
        DRM device

    :param void * data:
        ioctl data

    :param struct drm_file * file_priv:
        DRM file info



Description
-----------

This creates a new dumb buffer in the driver's backing storage manager (GEM,
TTM or something else entirely) and returns the resulting buffer handle. This
handle can then be wrapped up into a framebuffer modeset object.


Note that userspace is not allowed to use such objects for render
acceleration - drivers must create their own private ioctls for such a use
case.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_mmap_dumb_ioctl:

drm_mode_mmap_dumb_ioctl
========================

.. c:function:: int drm_mode_mmap_dumb_ioctl (struct drm_device * dev, void * data, struct drm_file * file_priv)

    create an mmap offset for a dumb backing storage buffer

    :param struct drm_device * dev:
        DRM device

    :param void * data:
        ioctl data

    :param struct drm_file * file_priv:
        DRM file info



Description
-----------

Allocate an offset in the drm device node's address space to be able to
memory map a dumb buffer.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_mode_destroy_dumb_ioctl:

drm_mode_destroy_dumb_ioctl
===========================

.. c:function:: int drm_mode_destroy_dumb_ioctl (struct drm_device * dev, void * data, struct drm_file * file_priv)

    destroy a dumb backing strage buffer

    :param struct drm_device * dev:
        DRM device

    :param void * data:
        ioctl data

    :param struct drm_file * file_priv:
        DRM file info



Description
-----------

This destroys the userspace handle for the given dumb backing storage buffer.
Since buffer objects must be reference counted in the kernel a buffer object
won't be immediately freed if a framebuffer modeset object still uses it.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_drm_fb_get_bpp_depth:

drm_fb_get_bpp_depth
====================

.. c:function:: void drm_fb_get_bpp_depth (uint32_t format, unsigned int * depth, int * bpp)

    get the bpp/depth values for format

    :param uint32_t format:
        pixel format (DRM_FORMAT_*)

    :param unsigned int * depth:
        storage for the depth value

    :param int * bpp:
        storage for the bpp value



Description
-----------

This only supports RGB formats here for compat with code that doesn't use
pixel formats directly yet.




.. _xref_drm_format_num_planes:

drm_format_num_planes
=====================

.. c:function:: int drm_format_num_planes (uint32_t format)

    get the number of planes for format

    :param uint32_t format:
        pixel format (DRM_FORMAT_*)



Returns
-------

The number of planes used by the specified pixel format.




.. _xref_drm_format_plane_cpp:

drm_format_plane_cpp
====================

.. c:function:: int drm_format_plane_cpp (uint32_t format, int plane)

    determine the bytes per pixel value

    :param uint32_t format:
        pixel format (DRM_FORMAT_*)

    :param int plane:
        plane index



Returns
-------

The bytes per pixel value for the specified plane.




.. _xref_drm_format_horz_chroma_subsampling:

drm_format_horz_chroma_subsampling
==================================

.. c:function:: int drm_format_horz_chroma_subsampling (uint32_t format)

    get the horizontal chroma subsampling factor

    :param uint32_t format:
        pixel format (DRM_FORMAT_*)



Returns
-------

The horizontal chroma subsampling factor for the
specified pixel format.




.. _xref_drm_format_vert_chroma_subsampling:

drm_format_vert_chroma_subsampling
==================================

.. c:function:: int drm_format_vert_chroma_subsampling (uint32_t format)

    get the vertical chroma subsampling factor

    :param uint32_t format:
        pixel format (DRM_FORMAT_*)



Returns
-------

The vertical chroma subsampling factor for the
specified pixel format.




.. _xref_drm_format_plane_width:

drm_format_plane_width
======================

.. c:function:: int drm_format_plane_width (int width, uint32_t format, int plane)

    width of the plane given the first plane

    :param int width:
        width of the first plane

    :param uint32_t format:
        pixel format

    :param int plane:
        plane index



Returns
-------

The width of **plane**, given that the width of the first plane is **width**.




.. _xref_drm_format_plane_height:

drm_format_plane_height
=======================

.. c:function:: int drm_format_plane_height (int height, uint32_t format, int plane)

    height of the plane given the first plane

    :param int height:
        height of the first plane

    :param uint32_t format:
        pixel format

    :param int plane:
        plane index



Returns
-------

The height of **plane**, given that the height of the first plane is **height**.




.. _xref_drm_rotation_simplify:

drm_rotation_simplify
=====================

.. c:function:: unsigned int drm_rotation_simplify (unsigned int rotation, unsigned int supported_rotations)

    Try to simplify the rotation

    :param unsigned int rotation:
        Rotation to be simplified

    :param unsigned int supported_rotations:
        Supported rotations



Description
-----------

Attempt to simplify the rotation to a form that is supported.
Eg. if the hardware supports everything except DRM_REFLECT_X



one could call this function like this
--------------------------------------



drm_rotation_simplify(rotation, BIT(DRM_ROTATE_0) |
                      BIT(DRM_ROTATE_90) | BIT(DRM_ROTATE_180) |
                      BIT(DRM_ROTATE_270) | BIT(DRM_REFLECT_Y));


to eliminate the DRM_ROTATE_X flag. Depending on what kind of
transforms the hardware supports, this function may not
be able to produce a supported transform, so the caller should
check the result afterwards.




.. _xref_drm_mode_config_init:

drm_mode_config_init
====================

.. c:function:: void drm_mode_config_init (struct drm_device * dev)

    initialize DRM mode_configuration structure

    :param struct drm_device * dev:
        DRM device



Description
-----------

Initialize **dev**'s mode_config structure, used for tracking the graphics
configuration of **dev**.


Since this initializes the modeset locks, no locking is possible. Which is no
problem, since this should happen single threaded at init time. It is the
driver's problem to ensure this guarantee.




.. _xref_drm_mode_config_cleanup:

drm_mode_config_cleanup
=======================

.. c:function:: void drm_mode_config_cleanup (struct drm_device * dev)

    free up DRM mode_config info

    :param struct drm_device * dev:
        DRM device



Description
-----------

Free up all the connectors and CRTCs associated with this DRM device, then
free up the framebuffers and associated buffer objects.


Note that since this /should/ happen single-threaded at driver/device
teardown time, no locking is required. It's the driver's job to ensure that
this guarantee actually holds true.



FIXME
-----

cleanup any dangling user buffer objects too




.. _xref_drm_mode_put_tile_group:

drm_mode_put_tile_group
=======================

.. c:function:: void drm_mode_put_tile_group (struct drm_device * dev, struct drm_tile_group * tg)

    drop a reference to a tile group.

    :param struct drm_device * dev:
        DRM device

    :param struct drm_tile_group * tg:
        tile group to drop reference to.



Description
-----------

drop reference to tile group and free if 0.




.. _xref_drm_mode_get_tile_group:

drm_mode_get_tile_group
=======================

.. c:function:: struct drm_tile_group * drm_mode_get_tile_group (struct drm_device * dev, char topology[8])

    get a reference to an existing tile group

    :param struct drm_device * dev:
        DRM device

    :param char topology[8]:



Description
-----------

Use the unique bytes to get a reference to an existing tile group.



RETURNS
-------

tile group or NULL if not found.




.. _xref_drm_mode_create_tile_group:

drm_mode_create_tile_group
==========================

.. c:function:: struct drm_tile_group * drm_mode_create_tile_group (struct drm_device * dev, char topology[8])

    create a tile group from a displayid description

    :param struct drm_device * dev:
        DRM device

    :param char topology[8]:



Description
-----------

Create a tile group for the unique monitor, and get a unique
identifier for the tile group.



RETURNS
-------

new tile group or error.


