.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_connector.c

.. _`overview`:

overview
========

In DRM connectors are the general abstraction for display sinks, and include
als fixed panels or anything else that can display pixels in some form. As
opposed to all other KMS objects representing hardware (like CRTC, encoder or
plane abstractions) connectors can be hotplugged and unplugged at runtime.
Hence they are reference-counted using \ :c:func:`drm_connector_get`\  and
\ :c:func:`drm_connector_put`\ .

KMS driver must create, initialize, register and attach at a \ :c:type:`struct struct <struct>`\ 
drm_connector for each such sink. The instance is created as other KMS
objects and initialized by setting the following fields. The connector is
initialized with a call to \ :c:func:`drm_connector_init`\  with a pointer to the
\ :c:type:`struct drm_connector_funcs <drm_connector_funcs>`\  and a connector type, and then exposed to
userspace with a call to \ :c:func:`drm_connector_register`\ .

Connectors must be attached to an encoder to be used. For devices that map
connectors to encoders 1:1, the connector should be attached at
initialization time with a call to \ :c:func:`drm_mode_connector_attach_encoder`\ . The
driver must also set the \ :c:type:`drm_connector.encoder <drm_connector>`\  field to point to the
attached encoder.

For connectors which are not fixed (like built-in panels) the driver needs to
support hotplug notifications. The simplest way to do that is by using the
probe helpers, see \ :c:func:`drm_kms_helper_poll_init`\  for connectors which don't have
hardware support for hotplug interrupts. Connectors with hardware hotplug
support can instead use e.g. \ :c:func:`drm_helper_hpd_irq_event`\ .

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

.. _`drm_get_connector_force_name`:

drm_get_connector_force_name
============================

.. c:function:: const char *drm_get_connector_force_name(enum drm_connector_force force)

    return a string for connector force

    :param enum drm_connector_force force:
        connector force to get name of

.. _`drm_get_connector_force_name.return`:

Return
------

const pointer to name.

.. _`drm_connector_list_iter_begin`:

drm_connector_list_iter_begin
=============================

.. c:function:: void drm_connector_list_iter_begin(struct drm_device *dev, struct drm_connector_list_iter *iter)

    initialize a connector_list iterator

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_connector_list_iter \*iter:
        connector_list iterator

.. _`drm_connector_list_iter_begin.description`:

Description
-----------

Sets \ ``iter``\  up to walk the \ :c:type:`drm_mode_config.connector_list <drm_mode_config>`\  of \ ``dev``\ . \ ``iter``\ 
must always be cleaned up again by calling \ :c:func:`drm_connector_list_iter_end`\ .
Iteration itself happens using \ :c:func:`drm_connector_list_iter_next`\  or
\ :c:func:`drm_for_each_connector_iter`\ .

.. _`drm_connector_list_iter_next`:

drm_connector_list_iter_next
============================

.. c:function:: struct drm_connector *drm_connector_list_iter_next(struct drm_connector_list_iter *iter)

    return next connector

    :param struct drm_connector_list_iter \*iter:
        connectr_list iterator

.. _`drm_connector_list_iter_next.description`:

Description
-----------

Returns the next connector for \ ``iter``\ , or NULL when the list walk has
completed.

.. _`drm_connector_list_iter_end`:

drm_connector_list_iter_end
===========================

.. c:function:: void drm_connector_list_iter_end(struct drm_connector_list_iter *iter)

    tear down a connector_list iterator

    :param struct drm_connector_list_iter \*iter:
        connector_list iterator

.. _`drm_connector_list_iter_end.description`:

Description
-----------

Tears down \ ``iter``\  and releases any resources (like \ :c:type:`struct drm_connector <drm_connector>`\  references)
acquired while walking the list. This must always be called, both when the
iteration completes fully or when it was aborted without walking the entire
list.

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

.. _`standard-connector-properties`:

standard connector properties
=============================

DRM connectors have a few standardized properties:

EDID:
     Blob property which contains the current EDID read from the sink. This
     is useful to parse sink identification information like vendor, model
     and serial. Drivers should update this property by calling
     \ :c:func:`drm_mode_connector_update_edid_property`\ , usually after having parsed
     the EDID using \ :c:func:`drm_add_edid_modes`\ . Userspace cannot change this
     property.
DPMS:
     Legacy property for setting the power state of the connector. For atomic
     drivers this is only provided for backwards compatibility with existing
     drivers, it remaps to controlling the "ACTIVE" property on the CRTC the
     connector is linked to. Drivers should never set this property directly,
     it is handled by the DRM core by calling the \ :c:type:`drm_connector_funcs.dpms <drm_connector_funcs>`\ 
     callback. For atomic drivers the remapping to the "ACTIVE" property is
     implemented in the DRM core.  This is the only standard connector
     property that userspace can change.

     Note that this property cannot be set through the MODE_ATOMIC ioctl,
     userspace must use "ACTIVE" on the CRTC instead.

     WARNING:

     For userspace also running on legacy drivers the "DPMS" semantics are a
     lot more complicated. First, userspace cannot rely on the "DPMS" value
     returned by the GETCONNECTOR actually reflecting reality, because many
     drivers fail to update it. For atomic drivers this is taken care of in
     \ :c:func:`drm_atomic_helper_update_legacy_modeset_state`\ .

     The second issue is that the DPMS state is only well-defined when the
     connector is connected to a CRTC. In atomic the DRM core enforces that
     "ACTIVE" is off in such a case, no such checks exists for "DPMS".

     Finally, when enabling an output using the legacy SETCONFIG ioctl then
     "DPMS" is forced to ON. But see above, that might not be reflected in
     the software value on legacy drivers.

     Summarizing: Only set "DPMS" when the connector is known to be enabled,
     assume that a successful SETCONFIG call also sets "DPMS" to on, and
     never read back the value of "DPMS" because it can be incorrect.
PATH:
     Connector path property to identify how this sink is physically
     connected. Used by DP MST. This should be set by calling
     \ :c:func:`drm_mode_connector_set_path_property`\ , in the case of DP MST with the
     path property the MST manager created. Userspace cannot change this
     property.
TILE:
     Connector tile group property to indicate how a set of DRM connector
     compose together into one logical screen. This is used by both high-res
     external screens (often only using a single cable, but exposing multiple
     DP MST sinks), or high-res integrated panels (like dual-link DSI) which
     are not gen-locked. Note that for tiled panels which are genlocked, like
     dual-link LVDS or dual-link DSI, the driver should try to not expose the
     tiling and virtualize both \ :c:type:`struct drm_crtc <drm_crtc>`\  and \ :c:type:`struct drm_plane <drm_plane>`\  if needed. Drivers
     should update this value using \ :c:func:`drm_mode_connector_set_tile_property`\ .
     Userspace cannot change this property.
link-status:
     Connector link-status property to indicate the status of link. The
     default value of link-status is "GOOD". If something fails during or
     after modeset, the kernel driver may set this to "BAD" and issue a
     hotplug uevent. Drivers should update this value using
     \ :c:func:`drm_mode_connector_set_link_status_property`\ .
non_desktop:
     Indicates the output should be ignored for purposes of displaying a
     standard desktop environment or console. This is most likely because
     the output device is not rectilinear.
Content Protection:
     This property is used by userspace to request the kernel protect future
     content communicated over the link. When requested, kernel will apply
     the appropriate means of protection (most often HDCP), and use the
     property to tell userspace the protection is active.

     Drivers can set this up by calling
     \ :c:func:`drm_connector_attach_content_protection_property`\  on initialization.

     The value of this property can be one of the following:

     DRM_MODE_CONTENT_PROTECTION_UNDESIRED = 0
             The link is not protected, content is transmitted in the clear.
     DRM_MODE_CONTENT_PROTECTION_DESIRED = 1
             Userspace has requested content protection, but the link is not
             currently protected. When in this state, kernel should enable
             Content Protection as soon as possible.
     DRM_MODE_CONTENT_PROTECTION_ENABLED = 2
             Userspace has requested content protection, and the link is
             protected. Only the driver can set the property to this value.
             If userspace attempts to set to ENABLED, kernel will return
             -EINVAL.

     A few guidelines:

     - DESIRED state should be preserved until userspace de-asserts it by
       setting the property to UNDESIRED. This means ENABLED should only
       transition to UNDESIRED when the user explicitly requests it.
     - If the state is DESIRED, kernel should attempt to re-authenticate the
       link whenever possible. This includes across disable/enable, dpms,
       hotplug, downstream device changes, link status failures, etc..
     - Userspace is responsible for polling the property to determine when
       the value transitions from ENABLED to DESIRED. This signifies the link
       is no longer protected and userspace should take appropriate action
       (whatever that might be).

Connectors also have one standardized atomic property:

CRTC_ID:
     Mode object ID of the \ :c:type:`struct drm_crtc <drm_crtc>`\  this connector should be connected to.

Connectors for LCD panels may also have one standardized property:

panel orientation:
     On some devices the LCD panel is mounted in the casing in such a way
     that the up/top side of the panel does not match with the top side of
     the device. Userspace can use this property to check for this.
     Note that input coordinates from touchscreens (input devices with
     INPUT_PROP_DIRECT) will still map 1:1 to the actual LCD panel
     coordinates, so if userspace rotates the picture to adjust for
     the orientation it must also apply the same transformation to the
     touchscreen input coordinates. This property is initialized by calling
     \ :c:func:`drm_connector_init_panel_orientation_property`\ .

scaling mode:
     This property defines how a non-native mode is upscaled to the native
     mode of an LCD panel:

     None:
             No upscaling happens, scaling is left to the panel. Not all
             drivers expose this mode.
     Full:
             The output is upscaled to the full resolution of the panel,
             ignoring the aspect ratio.
     Center:
             No upscaling happens, the output is centered within the native
             resolution the panel.
     Full aspect:
             The output is upscaled to maximize either the width or height
             while retaining the aspect ratio.

     This property should be set up by calling
     \ :c:func:`drm_connector_attach_scaling_mode_property`\ . Note that drivers
     can also expose this property to external outputs, in which case they
     must support "None", which should be the default (since external screens
     have a built-in scaler).

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

.. c:function:: int drm_mode_create_tv_properties(struct drm_device *dev, unsigned int num_modes, const char * const modes)

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

Atomic drivers should use \ :c:func:`drm_connector_attach_scaling_mode_property`\ 
instead to correctly assign \ :c:type:`drm_connector_state.picture_aspect_ratio <drm_connector_state>`\ 
in the atomic state.

.. _`drm_connector_attach_scaling_mode_property`:

drm_connector_attach_scaling_mode_property
==========================================

.. c:function:: int drm_connector_attach_scaling_mode_property(struct drm_connector *connector, u32 scaling_mode_mask)

    attach atomic scaling mode property

    :param struct drm_connector \*connector:
        connector to attach scaling mode property on.

    :param u32 scaling_mode_mask:
        or'ed mask of BIT(%DRM_MODE_SCALE_\*).

.. _`drm_connector_attach_scaling_mode_property.description`:

Description
-----------

This is used to add support for scaling mode to atomic drivers.
The scaling mode will be set to \ :c:type:`drm_connector_state.picture_aspect_ratio <drm_connector_state>`\ 
and can be used from \ :c:type:`drm_connector_helper_funcs->atomic_check <drm_connector_helper_funcs>`\  for validation.

This is the atomic version of \ :c:func:`drm_mode_create_scaling_mode_property`\ .

.. _`drm_connector_attach_scaling_mode_property.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_connector_attach_content_protection_property`:

drm_connector_attach_content_protection_property
================================================

.. c:function:: int drm_connector_attach_content_protection_property(struct drm_connector *connector)

    attach content protection property

    :param struct drm_connector \*connector:
        connector to attach CP property on.

.. _`drm_connector_attach_content_protection_property.description`:

Description
-----------

This is used to add support for content protection on select connectors.
Content Protection is intentionally vague to allow for different underlying
technologies, however it is most implemented by HDCP.

The content protection will be set to \ :c:type:`drm_connector_state.content_protection <drm_connector_state>`\ 

.. _`drm_connector_attach_content_protection_property.return`:

Return
------

Zero on success, negative errno on failure.

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

.. _`drm_mode_connector_set_link_status_property`:

drm_mode_connector_set_link_status_property
===========================================

.. c:function:: void drm_mode_connector_set_link_status_property(struct drm_connector *connector, uint64_t link_status)

    Set link status property of a connector

    :param struct drm_connector \*connector:
        drm connector

    :param uint64_t link_status:
        new value of link status property (0: Good, 1: Bad)

.. _`drm_mode_connector_set_link_status_property.description`:

Description
-----------

In usual working scenario, this link status property will always be set to
"GOOD". If something fails during or after a mode set, the kernel driver
may set this link status property to "BAD". The caller then needs to send a
hotplug uevent for userspace to re-check the valid modes through
GET_CONNECTOR_IOCTL and retry modeset.

.. _`drm_mode_connector_set_link_status_property.note`:

Note
----

Drivers cannot rely on userspace to support this property and
issue a modeset. As such, they may choose to handle issues (like
re-training a link) without userspace's intervention.

The reason for adding this property is to handle link training failures, but
it is not limited to DP or link training. For example, if we implement
asynchronous setcrtc, this property can be used to report any failures in that.

.. _`drm_connector_init_panel_orientation_property`:

drm_connector_init_panel_orientation_property
=============================================

.. c:function:: int drm_connector_init_panel_orientation_property(struct drm_connector *connector, int width, int height)

    initialize the connecters panel_orientation property

    :param struct drm_connector \*connector:
        connector for which to init the panel-orientation property.

    :param int width:
        width in pixels of the panel, used for panel quirk detection

    :param int height:
        height in pixels of the panel, used for panel quirk detection

.. _`drm_connector_init_panel_orientation_property.description`:

Description
-----------

This function should only be called for built-in panels, after setting
connector->display_info.panel_orientation first (if known).

This function will check for platform specific (e.g. DMI based) quirks
overriding display_info.panel_orientation first, then if panel_orientation
is not DRM_MODE_PANEL_ORIENTATION_UNKNOWN it will attach the
"panel orientation" property to the connector.

.. _`drm_connector_init_panel_orientation_property.return`:

Return
------

Zero on success, negative errno on failure.

.. _`tile-group`:

Tile group
==========

Tile groups are used to represent tiled monitors with a unique integer
identifier. Tiled monitors using DisplayID v1.3 have a unique 8-byte handle,
we store this in a tile group, so we have a common identifier for all tiles
in a monitor group. The property is called "TILE". Drivers can manage tile
groups using \ :c:func:`drm_mode_create_tile_group`\ , \ :c:func:`drm_mode_put_tile_group`\  and
\ :c:func:`drm_mode_get_tile_group`\ . But this is only needed for internal panels where
the tile group information is exposed through a non-standard way.

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

.. c:function:: struct drm_tile_group *drm_mode_get_tile_group(struct drm_device *dev, char topology)

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

.. c:function:: struct drm_tile_group *drm_mode_create_tile_group(struct drm_device *dev, char topology)

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

.. This file was automatic generated / don't edit.

