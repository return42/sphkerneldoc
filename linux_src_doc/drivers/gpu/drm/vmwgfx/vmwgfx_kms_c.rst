.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_kms.c

.. _`vmw_kms_legacy_hotspot_clear`:

vmw_kms_legacy_hotspot_clear
============================

.. c:function:: void vmw_kms_legacy_hotspot_clear(struct vmw_private *dev_priv)

    Clear legacy hotspots

    :param dev_priv:
        Pointer to the device private struct.
    :type dev_priv: struct vmw_private \*

.. _`vmw_kms_legacy_hotspot_clear.description`:

Description
-----------

Clears all legacy hotspots.

.. _`vmw_du_plane_unpin_surf`:

vmw_du_plane_unpin_surf
=======================

.. c:function:: void vmw_du_plane_unpin_surf(struct vmw_plane_state *vps, bool unreference)

    unpins resource associated with a framebuffer surface

    :param vps:
        plane state associated with the display surface
    :type vps: struct vmw_plane_state \*

    :param unreference:
        true if we also want to unreference the display.
    :type unreference: bool

.. _`vmw_du_plane_cleanup_fb`:

vmw_du_plane_cleanup_fb
=======================

.. c:function:: void vmw_du_plane_cleanup_fb(struct drm_plane *plane, struct drm_plane_state *old_state)

    Unpins the cursor

    :param plane:
        display plane
    :type plane: struct drm_plane \*

    :param old_state:
        Contains the FB to clean up
    :type old_state: struct drm_plane_state \*

.. _`vmw_du_plane_cleanup_fb.description`:

Description
-----------

Unpins the framebuffer surface

Returns 0 on success

.. _`vmw_du_cursor_plane_prepare_fb`:

vmw_du_cursor_plane_prepare_fb
==============================

.. c:function:: int vmw_du_cursor_plane_prepare_fb(struct drm_plane *plane, struct drm_plane_state *new_state)

    Readies the cursor by referencing it

    :param plane:
        display plane
    :type plane: struct drm_plane \*

    :param new_state:
        info on the new plane state, including the FB
    :type new_state: struct drm_plane_state \*

.. _`vmw_du_cursor_plane_prepare_fb.description`:

Description
-----------

Returns 0 on success

.. _`vmw_du_primary_plane_atomic_check`:

vmw_du_primary_plane_atomic_check
=================================

.. c:function:: int vmw_du_primary_plane_atomic_check(struct drm_plane *plane, struct drm_plane_state *state)

    check if the new state is okay

    :param plane:
        display plane
    :type plane: struct drm_plane \*

    :param state:
        info on the new plane state, including the FB
    :type state: struct drm_plane_state \*

.. _`vmw_du_primary_plane_atomic_check.description`:

Description
-----------

Check if the new state is settable given the current state.  Other
than what the atomic helper checks, we care about crtc fitting
the FB and maintaining one active framebuffer.

Returns 0 on success

.. _`vmw_du_cursor_plane_atomic_check`:

vmw_du_cursor_plane_atomic_check
================================

.. c:function:: int vmw_du_cursor_plane_atomic_check(struct drm_plane *plane, struct drm_plane_state *new_state)

    check if the new state is okay

    :param plane:
        cursor plane
    :type plane: struct drm_plane \*

    :param new_state:
        *undescribed*
    :type new_state: struct drm_plane_state \*

.. _`vmw_du_cursor_plane_atomic_check.description`:

Description
-----------

This is a chance to fail if the new cursor state does not fit
our requirements.

Returns 0 on success

.. _`vmw_du_crtc_duplicate_state`:

vmw_du_crtc_duplicate_state
===========================

.. c:function:: struct drm_crtc_state *vmw_du_crtc_duplicate_state(struct drm_crtc *crtc)

    duplicate crtc state

    :param crtc:
        DRM crtc
    :type crtc: struct drm_crtc \*

.. _`vmw_du_crtc_duplicate_state.description`:

Description
-----------

Allocates and returns a copy of the crtc state (both common and
vmw-specific) for the specified crtc.

.. _`vmw_du_crtc_duplicate_state.return`:

Return
------

The newly allocated crtc state, or NULL on failure.

.. _`vmw_du_crtc_reset`:

vmw_du_crtc_reset
=================

.. c:function:: void vmw_du_crtc_reset(struct drm_crtc *crtc)

    creates a blank vmw crtc state

    :param crtc:
        DRM crtc
    :type crtc: struct drm_crtc \*

.. _`vmw_du_crtc_reset.description`:

Description
-----------

Resets the atomic state for \ ``crtc``\  by freeing the state pointer (which
might be NULL, e.g. at driver load time) and allocating a new empty state
object.

.. _`vmw_du_crtc_destroy_state`:

vmw_du_crtc_destroy_state
=========================

.. c:function:: void vmw_du_crtc_destroy_state(struct drm_crtc *crtc, struct drm_crtc_state *state)

    destroy crtc state

    :param crtc:
        DRM crtc
    :type crtc: struct drm_crtc \*

    :param state:
        state object to destroy
    :type state: struct drm_crtc_state \*

.. _`vmw_du_crtc_destroy_state.description`:

Description
-----------

Destroys the crtc state (both common and vmw-specific) for the
specified plane.

.. _`vmw_du_plane_duplicate_state`:

vmw_du_plane_duplicate_state
============================

.. c:function:: struct drm_plane_state *vmw_du_plane_duplicate_state(struct drm_plane *plane)

    duplicate plane state

    :param plane:
        drm plane
    :type plane: struct drm_plane \*

.. _`vmw_du_plane_duplicate_state.description`:

Description
-----------

Allocates and returns a copy of the plane state (both common and
vmw-specific) for the specified plane.

.. _`vmw_du_plane_duplicate_state.return`:

Return
------

The newly allocated plane state, or NULL on failure.

.. _`vmw_du_plane_reset`:

vmw_du_plane_reset
==================

.. c:function:: void vmw_du_plane_reset(struct drm_plane *plane)

    creates a blank vmw plane state

    :param plane:
        drm plane
    :type plane: struct drm_plane \*

.. _`vmw_du_plane_reset.description`:

Description
-----------

Resets the atomic state for \ ``plane``\  by freeing the state pointer (which might
be NULL, e.g. at driver load time) and allocating a new empty state object.

.. _`vmw_du_plane_destroy_state`:

vmw_du_plane_destroy_state
==========================

.. c:function:: void vmw_du_plane_destroy_state(struct drm_plane *plane, struct drm_plane_state *state)

    destroy plane state

    :param plane:
        DRM plane
    :type plane: struct drm_plane \*

    :param state:
        state object to destroy
    :type state: struct drm_plane_state \*

.. _`vmw_du_plane_destroy_state.description`:

Description
-----------

Destroys the plane state (both common and vmw-specific) for the
specified plane.

.. _`vmw_du_connector_duplicate_state`:

vmw_du_connector_duplicate_state
================================

.. c:function:: struct drm_connector_state *vmw_du_connector_duplicate_state(struct drm_connector *connector)

    duplicate connector state

    :param connector:
        DRM connector
    :type connector: struct drm_connector \*

.. _`vmw_du_connector_duplicate_state.description`:

Description
-----------

Allocates and returns a copy of the connector state (both common and
vmw-specific) for the specified connector.

.. _`vmw_du_connector_duplicate_state.return`:

Return
------

The newly allocated connector state, or NULL on failure.

.. _`vmw_du_connector_reset`:

vmw_du_connector_reset
======================

.. c:function:: void vmw_du_connector_reset(struct drm_connector *connector)

    creates a blank vmw connector state

    :param connector:
        DRM connector
    :type connector: struct drm_connector \*

.. _`vmw_du_connector_reset.description`:

Description
-----------

Resets the atomic state for \ ``connector``\  by freeing the state pointer (which
might be NULL, e.g. at driver load time) and allocating a new empty state
object.

.. _`vmw_du_connector_destroy_state`:

vmw_du_connector_destroy_state
==============================

.. c:function:: void vmw_du_connector_destroy_state(struct drm_connector *connector, struct drm_connector_state *state)

    destroy connector state

    :param connector:
        DRM connector
    :type connector: struct drm_connector \*

    :param state:
        state object to destroy
    :type state: struct drm_connector_state \*

.. _`vmw_du_connector_destroy_state.description`:

Description
-----------

Destroys the connector state (both common and vmw-specific) for the
specified plane.

.. _`vmw_kms_readback`:

vmw_kms_readback
================

.. c:function:: int vmw_kms_readback(struct vmw_private *dev_priv, struct drm_file *file_priv, struct vmw_framebuffer *vfb, struct drm_vmw_fence_rep __user *user_fence_rep, struct drm_vmw_rect *vclips, uint32_t num_clips)

    Perform a readback from the screen system to a buffer-object backed framebuffer.

    :param dev_priv:
        Pointer to the device private structure.
    :type dev_priv: struct vmw_private \*

    :param file_priv:
        Pointer to a struct drm_file identifying the caller.
        Must be set to NULL if \ ``user_fence_rep``\  is NULL.
    :type file_priv: struct drm_file \*

    :param vfb:
        Pointer to the buffer-object backed framebuffer.
    :type vfb: struct vmw_framebuffer \*

    :param user_fence_rep:
        User-space provided structure for fence information.
        Must be set to non-NULL if \ ``file_priv``\  is non-NULL.
    :type user_fence_rep: struct drm_vmw_fence_rep __user \*

    :param vclips:
        Array of clip rects.
    :type vclips: struct drm_vmw_rect \*

    :param num_clips:
        Number of clip rects in \ ``vclips``\ .
    :type num_clips: uint32_t

.. _`vmw_kms_readback.description`:

Description
-----------

Returns 0 on success, negative error code on failure. -ERESTARTSYS if
interrupted.

.. _`vmw_framebuffer_pin`:

vmw_framebuffer_pin
===================

.. c:function:: int vmw_framebuffer_pin(struct vmw_framebuffer *vfb)

    display system.

    :param vfb:
        *undescribed*
    :type vfb: struct vmw_framebuffer \*

.. _`vmw_create_bo_proxy`:

vmw_create_bo_proxy
===================

.. c:function:: int vmw_create_bo_proxy(struct drm_device *dev, const struct drm_mode_fb_cmd2 *mode_cmd, struct vmw_buffer_object *bo_mob, struct vmw_surface **srf_out)

    create a proxy surface for the buffer object

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param mode_cmd:
        parameters for the new surface
    :type mode_cmd: const struct drm_mode_fb_cmd2 \*

    :param bo_mob:
        MOB backing the buffer object
    :type bo_mob: struct vmw_buffer_object \*

    :param srf_out:
        newly created surface
    :type srf_out: struct vmw_surface \*\*

.. _`vmw_create_bo_proxy.description`:

Description
-----------

When the content FB is a buffer object, we create a surface as a proxy to the
same buffer.  This way we can do a surface copy rather than a surface DMA.
This is a more efficient approach

.. _`vmw_create_bo_proxy.return`:

Return
------

0 on success, error code otherwise

.. _`vmw_kms_srf_ok`:

vmw_kms_srf_ok
==============

.. c:function:: bool vmw_kms_srf_ok(struct vmw_private *dev_priv, uint32_t width, uint32_t height)

    check if a surface can be created

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

    :param width:
        requested width
    :type width: uint32_t

    :param height:
        requested height
    :type height: uint32_t

.. _`vmw_kms_srf_ok.description`:

Description
-----------

Surfaces need to be less than texture size

.. _`vmw_kms_new_framebuffer`:

vmw_kms_new_framebuffer
=======================

.. c:function:: struct vmw_framebuffer *vmw_kms_new_framebuffer(struct vmw_private *dev_priv, struct vmw_buffer_object *bo, struct vmw_surface *surface, bool only_2d, const struct drm_mode_fb_cmd2 *mode_cmd)

    Create a new framebuffer.

    :param dev_priv:
        Pointer to device private struct.
    :type dev_priv: struct vmw_private \*

    :param bo:
        Pointer to buffer object to wrap the kms framebuffer around.
        Either \ ``bo``\  or \ ``surface``\  must be NULL.
    :type bo: struct vmw_buffer_object \*

    :param surface:
        Pointer to a surface to wrap the kms framebuffer around.
        Either \ ``bo``\  or \ ``surface``\  must be NULL.
    :type surface: struct vmw_surface \*

    :param only_2d:
        No presents will occur to this buffer object based framebuffer.
        This helps the code to do some important optimizations.
    :type only_2d: bool

    :param mode_cmd:
        Frame-buffer metadata.
    :type mode_cmd: const struct drm_mode_fb_cmd2 \*

.. _`vmw_kms_check_display_memory`:

vmw_kms_check_display_memory
============================

.. c:function:: int vmw_kms_check_display_memory(struct drm_device *dev, uint32_t num_rects, struct drm_rect *rects)

    Validates display memory required for a topology

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param num_rects:
        number of drm_rect in rects
    :type num_rects: uint32_t

    :param rects:
        array of drm_rect representing the topology to validate indexed by
        crtc index.
    :type rects: struct drm_rect \*

.. _`vmw_kms_check_display_memory.return`:

Return
------

0 on success otherwise negative error code

.. _`vmw_kms_check_topology`:

vmw_kms_check_topology
======================

.. c:function:: int vmw_kms_check_topology(struct drm_device *dev, struct drm_atomic_state *state)

    Validates topology in drm_atomic_state

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param state:
        the driver state object
    :type state: struct drm_atomic_state \*

.. _`vmw_kms_check_topology.return`:

Return
------

0 on success otherwise negative error code

.. _`vmw_kms_atomic_check_modeset`:

vmw_kms_atomic_check_modeset
============================

.. c:function:: int vmw_kms_atomic_check_modeset(struct drm_device *dev, struct drm_atomic_state *state)

    validate state object for modeset changes

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param state:
        the driver state object
    :type state: struct drm_atomic_state \*

.. _`vmw_kms_atomic_check_modeset.description`:

Description
-----------

This is a simple wrapper around \ :c:func:`drm_atomic_helper_check_modeset`\  for
us to assign a value to mode->crtc_clock so that
\ :c:func:`drm_calc_timestamping_constants`\  won't throw an error message

.. _`vmw_kms_atomic_check_modeset.return`:

Return
------

Zero for success or -errno

.. _`vmw_get_vblank_counter`:

vmw_get_vblank_counter
======================

.. c:function:: u32 vmw_get_vblank_counter(struct drm_device *dev, unsigned int pipe)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param pipe:
        *undescribed*
    :type pipe: unsigned int

.. _`vmw_enable_vblank`:

vmw_enable_vblank
=================

.. c:function:: int vmw_enable_vblank(struct drm_device *dev, unsigned int pipe)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param pipe:
        *undescribed*
    :type pipe: unsigned int

.. _`vmw_disable_vblank`:

vmw_disable_vblank
==================

.. c:function:: void vmw_disable_vblank(struct drm_device *dev, unsigned int pipe)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param pipe:
        *undescribed*
    :type pipe: unsigned int

.. _`vmw_du_update_layout`:

vmw_du_update_layout
====================

.. c:function:: int vmw_du_update_layout(struct vmw_private *dev_priv, unsigned int num_rects, struct drm_rect *rects)

    Update the display unit with topology from resolution plugin and generate DRM uevent

    :param dev_priv:
        device private
    :type dev_priv: struct vmw_private \*

    :param num_rects:
        number of drm_rect in rects
    :type num_rects: unsigned int

    :param rects:
        toplogy to update
    :type rects: struct drm_rect \*

.. _`vmw_guess_mode_timing`:

vmw_guess_mode_timing
=====================

.. c:function:: void vmw_guess_mode_timing(struct drm_display_mode *mode)

    Provide fake timings for a 60Hz vrefresh mode.

    :param mode:
        *undescribed*
    :type mode: struct drm_display_mode \*

.. _`vmw_guess_mode_timing.description`:

Description
-----------

\ ``mode``\  - Pointer to a struct drm_display_mode with hdisplay and vdisplay
members filled in.

.. _`vmw_du_connector_atomic_set_property`:

vmw_du_connector_atomic_set_property
====================================

.. c:function:: int vmw_du_connector_atomic_set_property(struct drm_connector *connector, struct drm_connector_state *state, struct drm_property *property, uint64_t val)

    Atomic version of get property

    :param connector:
        *undescribed*
    :type connector: struct drm_connector \*

    :param state:
        *undescribed*
    :type state: struct drm_connector_state \*

    :param property:
        *undescribed*
    :type property: struct drm_property \*

    :param val:
        *undescribed*
    :type val: uint64_t

.. _`vmw_du_connector_atomic_set_property.description`:

Description
-----------

\ ``crtc``\  - crtc the property is associated with

.. _`vmw_du_connector_atomic_set_property.return`:

Return
------

Zero on success, negative errno on failure.

.. _`vmw_du_connector_atomic_get_property`:

vmw_du_connector_atomic_get_property
====================================

.. c:function:: int vmw_du_connector_atomic_get_property(struct drm_connector *connector, const struct drm_connector_state *state, struct drm_property *property, uint64_t *val)

    Atomic version of get property

    :param connector:
        *undescribed*
    :type connector: struct drm_connector \*

    :param state:
        *undescribed*
    :type state: const struct drm_connector_state \*

    :param property:
        *undescribed*
    :type property: struct drm_property \*

    :param val:
        *undescribed*
    :type val: uint64_t \*

.. _`vmw_du_connector_atomic_get_property.description`:

Description
-----------

\ ``connector``\  - connector the property is associated with

.. _`vmw_du_connector_atomic_get_property.return`:

Return
------

Zero on success, negative errno on failure.

.. _`vmw_kms_update_layout_ioctl`:

vmw_kms_update_layout_ioctl
===========================

.. c:function:: int vmw_kms_update_layout_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    Handler for DRM_VMW_UPDATE_LAYOUT ioctl

    :param dev:
        drm device for the ioctl
    :type dev: struct drm_device \*

    :param data:
        data pointer for the ioctl
    :type data: void \*

    :param file_priv:
        drm file for the ioctl call
    :type file_priv: struct drm_file \*

.. _`vmw_kms_update_layout_ioctl.description`:

Description
-----------

Update preferred topology of display unit as per ioctl request. The topology
is expressed as array of drm_vmw_rect.
e.g.
[0 0 640 480] [640 0 800 600] [0 480 640 480]

.. _`vmw_kms_update_layout_ioctl.note`:

NOTE
----

The x and y offset (upper left) in drm_vmw_rect cannot be less than 0. Beside
device limit on topology, x + w and y + h (lower right) cannot be greater
than INT_MAX. So topology beyond these limits will return with error.

.. _`vmw_kms_update_layout_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. _`vmw_kms_helper_dirty`:

vmw_kms_helper_dirty
====================

.. c:function:: int vmw_kms_helper_dirty(struct vmw_private *dev_priv, struct vmw_framebuffer *framebuffer, const struct drm_clip_rect *clips, const struct drm_vmw_rect *vclips, s32 dest_x, s32 dest_y, int num_clips, int increment, struct vmw_kms_dirty *dirty)

    Helper to build commands and perform actions based on a set of cliprects and a set of display units.

    :param dev_priv:
        Pointer to a device private structure.
    :type dev_priv: struct vmw_private \*

    :param framebuffer:
        Pointer to the framebuffer on which to perform the actions.
    :type framebuffer: struct vmw_framebuffer \*

    :param clips:
        A set of struct drm_clip_rect. Either this os \ ``vclips``\  must be NULL.
        Cliprects are given in framebuffer coordinates.
    :type clips: const struct drm_clip_rect \*

    :param vclips:
        A set of struct drm_vmw_rect cliprects. Either this or \ ``clips``\  must
        be NULL. Cliprects are given in source coordinates.
    :type vclips: const struct drm_vmw_rect \*

    :param dest_x:
        X coordinate offset for the crtc / destination clip rects.
    :type dest_x: s32

    :param dest_y:
        Y coordinate offset for the crtc / destination clip rects.
    :type dest_y: s32

    :param num_clips:
        Number of cliprects in the \ ``clips``\  or \ ``vclips``\  array.
    :type num_clips: int

    :param increment:
        Integer with which to increment the clip counter when looping.
        Used to skip a predetermined number of clip rects.
    :type increment: int

    :param dirty:
        Closure structure. See the description of struct vmw_kms_dirty.
    :type dirty: struct vmw_kms_dirty \*

.. _`vmw_kms_helper_validation_finish`:

vmw_kms_helper_validation_finish
================================

.. c:function:: void vmw_kms_helper_validation_finish(struct vmw_private *dev_priv, struct drm_file *file_priv, struct vmw_validation_context *ctx, struct vmw_fence_obj **out_fence, struct drm_vmw_fence_rep __user *user_fence_rep)

    Helper for post KMS command submission cleanup and fencing

    :param dev_priv:
        Pointer to the device-private struct
    :type dev_priv: struct vmw_private \*

    :param file_priv:
        Pointer identifying the client when user-space fencing is used
    :type file_priv: struct drm_file \*

    :param ctx:
        Pointer to the validation context
    :type ctx: struct vmw_validation_context \*

    :param out_fence:
        If non-NULL, returned refcounted fence-pointer
    :type out_fence: struct vmw_fence_obj \*\*

    :param user_fence_rep:
        If non-NULL, pointer to user-space address area
        in which to copy user-space fence info
    :type user_fence_rep: struct drm_vmw_fence_rep __user \*

.. _`vmw_kms_update_proxy`:

vmw_kms_update_proxy
====================

.. c:function:: int vmw_kms_update_proxy(struct vmw_resource *res, const struct drm_clip_rect *clips, unsigned num_clips, int increment)

    Helper function to update a proxy surface from its backing MOB.

    :param res:
        Pointer to the surface resource
    :type res: struct vmw_resource \*

    :param clips:
        Clip rects in framebuffer (surface) space.
    :type clips: const struct drm_clip_rect \*

    :param num_clips:
        Number of clips in \ ``clips``\ .
    :type num_clips: unsigned

    :param increment:
        Integer with which to increment the clip counter when looping.
        Used to skip a predetermined number of clip rects.
    :type increment: int

.. _`vmw_kms_update_proxy.description`:

Description
-----------

This function makes sure the proxy surface is updated from its backing MOB
using the region given by \ ``clips``\ . The surface resource \ ``res``\  and its backing
MOB needs to be reserved and validated on call.

.. _`vmw_kms_del_active`:

vmw_kms_del_active
==================

.. c:function:: void vmw_kms_del_active(struct vmw_private *dev_priv, struct vmw_display_unit *du)

    unregister a crtc binding to the implicit framebuffer

    :param dev_priv:
        Pointer to a device private struct.
    :type dev_priv: struct vmw_private \*

    :param du:
        The display unit of the crtc.
    :type du: struct vmw_display_unit \*

.. _`vmw_kms_add_active`:

vmw_kms_add_active
==================

.. c:function:: void vmw_kms_add_active(struct vmw_private *dev_priv, struct vmw_display_unit *du, struct vmw_framebuffer *vfb)

    register a crtc binding to an implicit framebuffer

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

    :param du:
        The display unit of the crtc.
    :type du: struct vmw_display_unit \*

    :param vfb:
        The implicit framebuffer
    :type vfb: struct vmw_framebuffer \*

.. _`vmw_kms_add_active.description`:

Description
-----------

Registers a binding to an implicit framebuffer.

.. _`vmw_kms_crtc_flippable`:

vmw_kms_crtc_flippable
======================

.. c:function:: bool vmw_kms_crtc_flippable(struct vmw_private *dev_priv, struct drm_crtc *crtc)

    Check whether we can page-flip a crtc.

    :param dev_priv:
        Pointer to device-private struct.
    :type dev_priv: struct vmw_private \*

    :param crtc:
        The crtc we want to flip.
    :type crtc: struct drm_crtc \*

.. _`vmw_kms_crtc_flippable.description`:

Description
-----------

Returns true or false depending whether it's OK to flip this crtc
based on the criterion that we must not have more than one implicit
frame-buffer at any one time.

.. _`vmw_kms_update_implicit_fb`:

vmw_kms_update_implicit_fb
==========================

.. c:function:: void vmw_kms_update_implicit_fb(struct vmw_private *dev_priv, struct drm_crtc *crtc)

    Update the implicit fb.

    :param dev_priv:
        Pointer to device-private struct.
    :type dev_priv: struct vmw_private \*

    :param crtc:
        The crtc the new implicit frame-buffer is bound to.
    :type crtc: struct drm_crtc \*

.. _`vmw_kms_create_implicit_placement_property`:

vmw_kms_create_implicit_placement_property
==========================================

.. c:function:: void vmw_kms_create_implicit_placement_property(struct vmw_private *dev_priv, bool immutable)

    Set up the implicit placement property.

    :param dev_priv:
        Pointer to a device private struct.
    :type dev_priv: struct vmw_private \*

    :param immutable:
        Whether the property is immutable.
    :type immutable: bool

.. _`vmw_kms_create_implicit_placement_property.description`:

Description
-----------

Sets up the implicit placement property unless it's already set up.

.. _`vmw_kms_set_config`:

vmw_kms_set_config
==================

.. c:function:: int vmw_kms_set_config(struct drm_mode_set *set, struct drm_modeset_acquire_ctx *ctx)

    Wrapper around drm_atomic_helper_set_config

    :param set:
        The configuration to set.
    :type set: struct drm_mode_set \*

    :param ctx:
        *undescribed*
    :type ctx: struct drm_modeset_acquire_ctx \*

.. _`vmw_kms_set_config.description`:

Description
-----------

The vmwgfx Xorg driver doesn't assign the mode::type member, which
when drm_mode_set_crtcinfo is called as part of the configuration setting
causes it to return incorrect crtc dimensions causing severe problems in
the vmwgfx modesetting. So explicitly clear that member before calling
into drm_atomic_helper_set_config.

.. _`vmw_kms_suspend`:

vmw_kms_suspend
===============

.. c:function:: int vmw_kms_suspend(struct drm_device *dev)

    Save modesetting state and turn modesetting off.

    :param dev:
        Pointer to the drm device
    :type dev: struct drm_device \*

.. _`vmw_kms_suspend.return`:

Return
------

0 on success. Negative error code on failure.

.. _`vmw_kms_resume`:

vmw_kms_resume
==============

.. c:function:: int vmw_kms_resume(struct drm_device *dev)

    Re-enable modesetting and restore state

    :param dev:
        Pointer to the drm device
    :type dev: struct drm_device \*

.. _`vmw_kms_resume.return`:

Return
------

0 on success. Negative error code on failure.

State is resumed from a previous \ :c:func:`vmw_kms_suspend`\ . It's illegal
to call this function without a previous \ :c:func:`vmw_kms_suspend`\ .

.. _`vmw_kms_lost_device`:

vmw_kms_lost_device
===================

.. c:function:: void vmw_kms_lost_device(struct drm_device *dev)

    Notify kms that modesetting capabilities will be lost

    :param dev:
        Pointer to the drm device
    :type dev: struct drm_device \*

.. This file was automatic generated / don't edit.

