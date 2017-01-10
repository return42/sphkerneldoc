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

@mode - Pointer to a struct drm_display_mode with hdisplay and vdisplay
members filled in.

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

.. c:function:: int vmw_kms_helper_buffer_prepare(struct vmw_private *dev_priv, struct vmw_dma_buffer *buf, bool interruptible, bool validate_as_mob)

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

.. _`vmw_kms_helper_buffer_prepare.description`:

Description
-----------

@dev_priv. Pointer to a device private structure.

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

.. c:function:: void vmw_kms_helper_resource_revert(struct vmw_resource *res)

    Undo the actions of vmw_kms_helper_resource_prepare.

    :param struct vmw_resource \*res:
        Pointer to the resource. Typically a surface.

.. _`vmw_kms_helper_resource_revert.description`:

Description
-----------

Helper to be used if an error forces the caller to undo the actions of
vmw_kms_helper_resource_prepare.

.. _`vmw_kms_helper_resource_prepare`:

vmw_kms_helper_resource_prepare
===============================

.. c:function:: int vmw_kms_helper_resource_prepare(struct vmw_resource *res, bool interruptible)

    Reserve and validate a resource before command submission.

    :param struct vmw_resource \*res:
        Pointer to the resource. Typically a surface.

    :param bool interruptible:
        Whether to perform waits as interruptible.

.. _`vmw_kms_helper_resource_prepare.description`:

Description
-----------

Reserves and validates also the backup buffer if a guest-backed resource.
Returns 0 on success, negative error code on failure. -ERESTARTSYS if
interrupted by a signal.

.. _`vmw_kms_helper_resource_finish`:

vmw_kms_helper_resource_finish
==============================

.. c:function:: void vmw_kms_helper_resource_finish(struct vmw_resource *res, struct vmw_fence_obj **out_fence)

    Unreserve and fence a resource after kms command submission.

    :param struct vmw_resource \*res:
        Pointer to the resource. Typically a surface.

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

.. This file was automatic generated / don't edit.

