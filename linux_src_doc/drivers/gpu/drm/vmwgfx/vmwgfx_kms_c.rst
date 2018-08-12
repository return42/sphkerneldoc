.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_kms.c

.. _`vmw_kms_legacy_hotspot_clear`:

vmw_kms_legacy_hotspot_clear
============================

.. c:function:: void vmw_kms_legacy_hotspot_clear(struct vmw_private *dev_priv)

    Clear legacy hotspots

    :param struct vmw_private \*dev_priv:
        Pointer to the device private struct.

.. _`vmw_kms_legacy_hotspot_clear.description`:

Description
-----------

Clears all legacy hotspots.

.. _`vmw_du_plane_unpin_surf`:

vmw_du_plane_unpin_surf
=======================

.. c:function:: void vmw_du_plane_unpin_surf(struct vmw_plane_state *vps, bool unreference)

    unpins resource associated with a framebuffer surface

    :param struct vmw_plane_state \*vps:
        plane state associated with the display surface

    :param bool unreference:
        true if we also want to unreference the display.

.. _`vmw_du_plane_cleanup_fb`:

vmw_du_plane_cleanup_fb
=======================

.. c:function:: void vmw_du_plane_cleanup_fb(struct drm_plane *plane, struct drm_plane_state *old_state)

    Unpins the cursor

    :param struct drm_plane \*plane:
        display plane

    :param struct drm_plane_state \*old_state:
        Contains the FB to clean up

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

    :param struct drm_plane \*plane:
        display plane

    :param struct drm_plane_state \*new_state:
        info on the new plane state, including the FB

.. _`vmw_du_cursor_plane_prepare_fb.description`:

Description
-----------

Returns 0 on success

.. _`vmw_du_primary_plane_atomic_check`:

vmw_du_primary_plane_atomic_check
=================================

.. c:function:: int vmw_du_primary_plane_atomic_check(struct drm_plane *plane, struct drm_plane_state *state)

    check if the new state is okay

    :param struct drm_plane \*plane:
        display plane

    :param struct drm_plane_state \*state:
        info on the new plane state, including the FB

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

    :param struct drm_plane \*plane:
        cursor plane

    :param struct drm_plane_state \*new_state:
        *undescribed*

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

    :param struct drm_crtc \*crtc:
        DRM crtc

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

    :param struct drm_crtc \*crtc:
        DRM crtc

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

    :param struct drm_crtc \*crtc:
        DRM crtc

    :param struct drm_crtc_state \*state:
        state object to destroy

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

    :param struct drm_plane \*plane:
        drm plane

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

    :param struct drm_plane \*plane:
        drm plane

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

    :param struct drm_plane \*plane:
        DRM plane

    :param struct drm_plane_state \*state:
        state object to destroy

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

    :param struct drm_connector \*connector:
        DRM connector

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

    :param struct drm_connector \*connector:
        DRM connector

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

    :param struct drm_connector \*connector:
        DRM connector

    :param struct drm_connector_state \*state:
        state object to destroy

.. _`vmw_du_connector_destroy_state.description`:

Description
-----------

Destroys the connector state (both common and vmw-specific) for the
specified plane.

.. _`vmw_kms_readback`:

vmw_kms_readback
================

.. c:function:: int vmw_kms_readback(struct vmw_private *dev_priv, struct drm_file *file_priv, struct vmw_framebuffer *vfb, struct drm_vmw_fence_rep __user *user_fence_rep, struct drm_vmw_rect *vclips, uint32_t num_clips)

    Perform a readback from the screen system to a dma-buffer backed framebuffer.

    :param struct vmw_private \*dev_priv:
        Pointer to the device private structure.

    :param struct drm_file \*file_priv:
        Pointer to a struct drm_file identifying the caller.
        Must be set to NULL if \ ``user_fence_rep``\  is NULL.

    :param struct vmw_framebuffer \*vfb:
        Pointer to the dma-buffer backed framebuffer.

    :param struct drm_vmw_fence_rep __user \*user_fence_rep:
        User-space provided structure for fence information.
        Must be set to non-NULL if \ ``file_priv``\  is non-NULL.

    :param struct drm_vmw_rect \*vclips:
        Array of clip rects.

    :param uint32_t num_clips:
        Number of clip rects in \ ``vclips``\ .

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

    :param struct vmw_framebuffer \*vfb:
        *undescribed*

.. _`vmw_create_dmabuf_proxy`:

vmw_create_dmabuf_proxy
=======================

.. c:function:: int vmw_create_dmabuf_proxy(struct drm_device *dev, const struct drm_mode_fb_cmd2 *mode_cmd, struct vmw_dma_buffer *dmabuf_mob, struct vmw_surface **srf_out)

    create a proxy surface for the DMA buf

    :param struct drm_device \*dev:
        DRM device

    :param const struct drm_mode_fb_cmd2 \*mode_cmd:
        parameters for the new surface

    :param struct vmw_dma_buffer \*dmabuf_mob:
        MOB backing the DMA buf

    :param struct vmw_surface \*\*srf_out:
        newly created surface

.. _`vmw_create_dmabuf_proxy.description`:

Description
-----------

When the content FB is a DMA buf, we create a surface as a proxy to the
same buffer.  This way we can do a surface copy rather than a surface DMA.
This is a more efficient approach

.. _`vmw_create_dmabuf_proxy.return`:

Return
------

0 on success, error code otherwise

.. _`vmw_kms_srf_ok`:

vmw_kms_srf_ok
==============

.. c:function:: bool vmw_kms_srf_ok(struct vmw_private *dev_priv, uint32_t width, uint32_t height)

    check if a surface can be created

    :param struct vmw_private \*dev_priv:
        *undescribed*

    :param uint32_t width:
        requested width

    :param uint32_t height:
        requested height

.. _`vmw_kms_srf_ok.description`:

Description
-----------

Surfaces need to be less than texture size

.. _`vmw_kms_new_framebuffer`:

vmw_kms_new_framebuffer
=======================

.. c:function:: struct vmw_framebuffer *vmw_kms_new_framebuffer(struct vmw_private *dev_priv, struct vmw_dma_buffer *dmabuf, struct vmw_surface *surface, bool only_2d, const struct drm_mode_fb_cmd2 *mode_cmd)

    Create a new framebuffer.

    :param struct vmw_private \*dev_priv:
        Pointer to device private struct.

    :param struct vmw_dma_buffer \*dmabuf:
        Pointer to dma buffer to wrap the kms framebuffer around.
        Either \ ``dmabuf``\  or \ ``surface``\  must be NULL.

    :param struct vmw_surface \*surface:
        Pointer to a surface to wrap the kms framebuffer around.
        Either \ ``dmabuf``\  or \ ``surface``\  must be NULL.

    :param bool only_2d:
        No presents will occur to this dma buffer based framebuffer. This
        Helps the code to do some important optimizations.

    :param const struct drm_mode_fb_cmd2 \*mode_cmd:
        Frame-buffer metadata.

.. _`vmw_kms_atomic_check_modeset`:

vmw_kms_atomic_check_modeset
============================

.. c:function:: int vmw_kms_atomic_check_modeset(struct drm_device *dev, struct drm_atomic_state *state)

    validate state object for modeset changes

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_atomic_state \*state:
        the driver state object

.. _`vmw_kms_atomic_check_modeset.description`:

Description
-----------

This is a simple wrapper around \ :c:func:`drm_atomic_helper_check_modeset`\  for
us to assign a value to mode->crtc_clock so that
\ :c:func:`drm_calc_timestamping_constants`\  won't throw an error message

RETURNS
Zero for success or -errno

.. _`vmw_get_vblank_counter`:

vmw_get_vblank_counter
======================

.. c:function:: u32 vmw_get_vblank_counter(struct drm_device *dev, unsigned int pipe)

    :param struct drm_device \*dev:
        *undescribed*

    :param unsigned int pipe:
        *undescribed*

.. _`vmw_enable_vblank`:

vmw_enable_vblank
=================

.. c:function:: int vmw_enable_vblank(struct drm_device *dev, unsigned int pipe)

    :param struct drm_device \*dev:
        *undescribed*

    :param unsigned int pipe:
        *undescribed*

.. _`vmw_disable_vblank`:

vmw_disable_vblank
==================

.. c:function:: void vmw_disable_vblank(struct drm_device *dev, unsigned int pipe)

    :param struct drm_device \*dev:
        *undescribed*

    :param unsigned int pipe:
        *undescribed*

.. _`vmw_guess_mode_timing`:

vmw_guess_mode_timing
=====================

.. c:function:: void vmw_guess_mode_timing(struct drm_display_mode *mode)

    Provide fake timings for a 60Hz vrefresh mode.

    :param struct drm_display_mode \*mode:
        *undescribed*

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

    :param struct drm_connector \*connector:
        *undescribed*

    :param struct drm_connector_state \*state:
        *undescribed*

    :param struct drm_property \*property:
        *undescribed*

    :param uint64_t val:
        *undescribed*

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

    :param struct drm_connector \*connector:
        *undescribed*

    :param const struct drm_connector_state \*state:
        *undescribed*

    :param struct drm_property \*property:
        *undescribed*

    :param uint64_t \*val:
        *undescribed*

.. _`vmw_du_connector_atomic_get_property.description`:

Description
-----------

\ ``connector``\  - connector the property is associated with

.. _`vmw_du_connector_atomic_get_property.return`:

Return
------

Zero on success, negative errno on failure.

.. _`vmw_kms_helper_dirty`:

vmw_kms_helper_dirty
====================

.. c:function:: int vmw_kms_helper_dirty(struct vmw_private *dev_priv, struct vmw_framebuffer *framebuffer, const struct drm_clip_rect *clips, const struct drm_vmw_rect *vclips, s32 dest_x, s32 dest_y, int num_clips, int increment, struct vmw_kms_dirty *dirty)

    Helper to build commands and perform actions based on a set of cliprects and a set of display units.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private structure.

    :param struct vmw_framebuffer \*framebuffer:
        Pointer to the framebuffer on which to perform the actions.

    :param const struct drm_clip_rect \*clips:
        A set of struct drm_clip_rect. Either this os \ ``vclips``\  must be NULL.
        Cliprects are given in framebuffer coordinates.

    :param const struct drm_vmw_rect \*vclips:
        A set of struct drm_vmw_rect cliprects. Either this or \ ``clips``\  must
        be NULL. Cliprects are given in source coordinates.

    :param s32 dest_x:
        X coordinate offset for the crtc / destination clip rects.

    :param s32 dest_y:
        Y coordinate offset for the crtc / destination clip rects.

    :param int num_clips:
        Number of cliprects in the \ ``clips``\  or \ ``vclips``\  array.

    :param int increment:
        Integer with which to increment the clip counter when looping.
        Used to skip a predetermined number of clip rects.

    :param struct vmw_kms_dirty \*dirty:
        Closure structure. See the description of struct vmw_kms_dirty.

.. _`vmw_kms_helper_buffer_prepare`:

vmw_kms_helper_buffer_prepare
=============================

.. c:function:: int vmw_kms_helper_buffer_prepare(struct vmw_private *dev_priv, struct vmw_dma_buffer *buf, bool interruptible, bool validate_as_mob, bool for_cpu_blit)

    Reserve and validate a buffer object before command submission.

    :param struct vmw_private \*dev_priv:
        *undescribed*

    :param struct vmw_dma_buffer \*buf:
        The buffer object

    :param bool interruptible:
        Whether to perform waits as interruptible.

    :param bool validate_as_mob:
        Whether the buffer should be validated as a MOB. If false,
        The buffer will be validated as a GMR. Already pinned buffers will not be
        validated.

    :param bool for_cpu_blit:
        *undescribed*

.. _`vmw_kms_helper_buffer_prepare.description`:

Description
-----------

\ ``dev_priv``\ . Pointer to a device private structure.

Returns 0 on success, negative error code on failure, -ERESTARTSYS if
interrupted by a signal.

.. _`vmw_kms_helper_buffer_revert`:

vmw_kms_helper_buffer_revert
============================

.. c:function:: void vmw_kms_helper_buffer_revert(struct vmw_dma_buffer *buf)

    Undo the actions of vmw_kms_helper_buffer_prepare.

    :param struct vmw_dma_buffer \*buf:
        *undescribed*

.. _`vmw_kms_helper_buffer_revert.description`:

Description
-----------

Helper to be used if an error forces the caller to undo the actions of
vmw_kms_helper_buffer_prepare.

.. _`vmw_kms_helper_buffer_finish`:

vmw_kms_helper_buffer_finish
============================

.. c:function:: void vmw_kms_helper_buffer_finish(struct vmw_private *dev_priv, struct drm_file *file_priv, struct vmw_dma_buffer *buf, struct vmw_fence_obj **out_fence, struct drm_vmw_fence_rep __user *user_fence_rep)

    Unreserve and fence a buffer object after kms command submission.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private structure.

    :param struct drm_file \*file_priv:
        Pointer to a struct drm_file representing the caller's
        connection. Must be set to NULL if \ ``user_fence_rep``\  is NULL, and conversely
        if non-NULL, \ ``user_fence_rep``\  must be non-NULL.

    :param struct vmw_dma_buffer \*buf:
        The buffer object.

    :param struct vmw_fence_obj \*\*out_fence:
        Optional pointer to a fence pointer. If non-NULL, a
        ref-counted fence pointer is returned here.

    :param struct drm_vmw_fence_rep __user \*user_fence_rep:
        Optional pointer to a user-space provided struct
        drm_vmw_fence_rep. If provided, \ ``file_priv``\  must also be provided and the
        function copies fence data to user-space in a fail-safe manner.

.. _`vmw_kms_helper_resource_revert`:

vmw_kms_helper_resource_revert
==============================

.. c:function:: void vmw_kms_helper_resource_revert(struct vmw_validation_ctx *ctx)

    Undo the actions of vmw_kms_helper_resource_prepare.

    :param struct vmw_validation_ctx \*ctx:
        *undescribed*

.. _`vmw_kms_helper_resource_revert.description`:

Description
-----------

Helper to be used if an error forces the caller to undo the actions of
vmw_kms_helper_resource_prepare.

.. _`vmw_kms_helper_resource_prepare`:

vmw_kms_helper_resource_prepare
===============================

.. c:function:: int vmw_kms_helper_resource_prepare(struct vmw_resource *res, bool interruptible, struct vmw_validation_ctx *ctx)

    Reserve and validate a resource before command submission.

    :param struct vmw_resource \*res:
        Pointer to the resource. Typically a surface.

    :param bool interruptible:
        Whether to perform waits as interruptible.

    :param struct vmw_validation_ctx \*ctx:
        *undescribed*

.. _`vmw_kms_helper_resource_prepare.description`:

Description
-----------

Reserves and validates also the backup buffer if a guest-backed resource.
Returns 0 on success, negative error code on failure. -ERESTARTSYS if
interrupted by a signal.

.. _`vmw_kms_helper_resource_finish`:

vmw_kms_helper_resource_finish
==============================

.. c:function:: void vmw_kms_helper_resource_finish(struct vmw_validation_ctx *ctx, struct vmw_fence_obj **out_fence)

    Unreserve and fence a resource after kms command submission.

    :param struct vmw_validation_ctx \*ctx:
        *undescribed*

    :param struct vmw_fence_obj \*\*out_fence:
        Optional pointer to a fence pointer. If non-NULL, a
        ref-counted fence pointer is returned here.

.. _`vmw_kms_update_proxy`:

vmw_kms_update_proxy
====================

.. c:function:: int vmw_kms_update_proxy(struct vmw_resource *res, const struct drm_clip_rect *clips, unsigned num_clips, int increment)

    Helper function to update a proxy surface from its backing MOB.

    :param struct vmw_resource \*res:
        Pointer to the surface resource

    :param const struct drm_clip_rect \*clips:
        Clip rects in framebuffer (surface) space.

    :param unsigned num_clips:
        Number of clips in \ ``clips``\ .

    :param int increment:
        Integer with which to increment the clip counter when looping.
        Used to skip a predetermined number of clip rects.

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

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_display_unit \*du:
        The display unit of the crtc.

.. _`vmw_kms_add_active`:

vmw_kms_add_active
==================

.. c:function:: void vmw_kms_add_active(struct vmw_private *dev_priv, struct vmw_display_unit *du, struct vmw_framebuffer *vfb)

    register a crtc binding to an implicit framebuffer

    :param struct vmw_private \*dev_priv:
        *undescribed*

    :param struct vmw_display_unit \*du:
        The display unit of the crtc.

    :param struct vmw_framebuffer \*vfb:
        The implicit framebuffer

.. _`vmw_kms_add_active.description`:

Description
-----------

Registers a binding to an implicit framebuffer.

.. _`vmw_kms_crtc_flippable`:

vmw_kms_crtc_flippable
======================

.. c:function:: bool vmw_kms_crtc_flippable(struct vmw_private *dev_priv, struct drm_crtc *crtc)

    Check whether we can page-flip a crtc.

    :param struct vmw_private \*dev_priv:
        Pointer to device-private struct.

    :param struct drm_crtc \*crtc:
        The crtc we want to flip.

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

    :param struct vmw_private \*dev_priv:
        Pointer to device-private struct.

    :param struct drm_crtc \*crtc:
        The crtc the new implicit frame-buffer is bound to.

.. _`vmw_kms_create_implicit_placement_property`:

vmw_kms_create_implicit_placement_property
==========================================

.. c:function:: void vmw_kms_create_implicit_placement_property(struct vmw_private *dev_priv, bool immutable)

    Set up the implicit placement property.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param bool immutable:
        Whether the property is immutable.

.. _`vmw_kms_create_implicit_placement_property.description`:

Description
-----------

Sets up the implicit placement property unless it's already set up.

.. _`vmw_kms_set_config`:

vmw_kms_set_config
==================

.. c:function:: int vmw_kms_set_config(struct drm_mode_set *set, struct drm_modeset_acquire_ctx *ctx)

    Wrapper around drm_atomic_helper_set_config

    :param struct drm_mode_set \*set:
        The configuration to set.

    :param struct drm_modeset_acquire_ctx \*ctx:
        *undescribed*

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

    :param struct drm_device \*dev:
        Pointer to the drm device

.. _`vmw_kms_suspend.return`:

Return
------

0 on success. Negative error code on failure.

.. _`vmw_kms_resume`:

vmw_kms_resume
==============

.. c:function:: int vmw_kms_resume(struct drm_device *dev)

    Re-enable modesetting and restore state

    :param struct drm_device \*dev:
        Pointer to the drm device

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

    :param struct drm_device \*dev:
        Pointer to the drm device

.. This file was automatic generated / don't edit.

