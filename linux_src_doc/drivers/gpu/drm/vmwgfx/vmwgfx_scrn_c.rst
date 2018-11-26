.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_scrn.c

.. _`vmw_kms_sou_surface_dirty`:

struct vmw_kms_sou_surface_dirty
================================

.. c:type:: struct vmw_kms_sou_surface_dirty

    Closure structure for blit surface to screen command.

.. _`vmw_kms_sou_surface_dirty.definition`:

Definition
----------

.. code-block:: c

    struct vmw_kms_sou_surface_dirty {
        struct vmw_kms_dirty base;
        s32 left, right, top, bottom;
        s32 dst_x, dst_y;
        u32 sid;
    }

.. _`vmw_kms_sou_surface_dirty.members`:

Members
-------

base
    The base type we derive from. Used by \ :c:func:`vmw_kms_helper_dirty`\ .

left
    Left side of bounding box.

right
    Right side of bounding box.

top
    Top side of bounding box.

bottom
    Bottom side of bounding box.

dst_x
    Difference between source clip rects and framebuffer coordinates.

dst_y
    Difference between source clip rects and framebuffer coordinates.

sid
    Surface id of surface to copy from.

.. _`vmw_sou_fifo_create`:

vmw_sou_fifo_create
===================

.. c:function:: int vmw_sou_fifo_create(struct vmw_private *dev_priv, struct vmw_screen_object_unit *sou, int x, int y, struct drm_display_mode *mode)

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

    :param sou:
        *undescribed*
    :type sou: struct vmw_screen_object_unit \*

    :param x:
        *undescribed*
    :type x: int

    :param y:
        *undescribed*
    :type y: int

    :param mode:
        *undescribed*
    :type mode: struct drm_display_mode \*

.. _`vmw_sou_fifo_destroy`:

vmw_sou_fifo_destroy
====================

.. c:function:: int vmw_sou_fifo_destroy(struct vmw_private *dev_priv, struct vmw_screen_object_unit *sou)

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

    :param sou:
        *undescribed*
    :type sou: struct vmw_screen_object_unit \*

.. _`vmw_sou_crtc_mode_set_nofb`:

vmw_sou_crtc_mode_set_nofb
==========================

.. c:function:: void vmw_sou_crtc_mode_set_nofb(struct drm_crtc *crtc)

    Create new screen

    :param crtc:
        CRTC associated with the new screen
    :type crtc: struct drm_crtc \*

.. _`vmw_sou_crtc_mode_set_nofb.description`:

Description
-----------

This function creates/destroys a screen.  This function cannot fail, so if
somehow we run into a failure, just do the best we can to get out.

.. _`vmw_sou_crtc_helper_prepare`:

vmw_sou_crtc_helper_prepare
===========================

.. c:function:: void vmw_sou_crtc_helper_prepare(struct drm_crtc *crtc)

    Noop

    :param crtc:
        CRTC associated with the new screen
    :type crtc: struct drm_crtc \*

.. _`vmw_sou_crtc_helper_prepare.description`:

Description
-----------

Prepares the CRTC for a mode set, but we don't need to do anything here.

.. _`vmw_sou_crtc_atomic_enable`:

vmw_sou_crtc_atomic_enable
==========================

.. c:function:: void vmw_sou_crtc_atomic_enable(struct drm_crtc *crtc, struct drm_crtc_state *old_state)

    Noop

    :param crtc:
        CRTC associated with the new screen
    :type crtc: struct drm_crtc \*

    :param old_state:
        *undescribed*
    :type old_state: struct drm_crtc_state \*

.. _`vmw_sou_crtc_atomic_enable.description`:

Description
-----------

This is called after a mode set has been completed.

.. _`vmw_sou_crtc_atomic_disable`:

vmw_sou_crtc_atomic_disable
===========================

.. c:function:: void vmw_sou_crtc_atomic_disable(struct drm_crtc *crtc, struct drm_crtc_state *old_state)

    Turns off CRTC

    :param crtc:
        CRTC to be turned off
    :type crtc: struct drm_crtc \*

    :param old_state:
        *undescribed*
    :type old_state: struct drm_crtc_state \*

.. _`vmw_sou_primary_plane_cleanup_fb`:

vmw_sou_primary_plane_cleanup_fb
================================

.. c:function:: void vmw_sou_primary_plane_cleanup_fb(struct drm_plane *plane, struct drm_plane_state *old_state)

    Frees sou backing buffer

    :param plane:
        display plane
    :type plane: struct drm_plane \*

    :param old_state:
        Contains the FB to clean up
    :type old_state: struct drm_plane_state \*

.. _`vmw_sou_primary_plane_cleanup_fb.description`:

Description
-----------

Unpins the display surface

Returns 0 on success

.. _`vmw_sou_primary_plane_prepare_fb`:

vmw_sou_primary_plane_prepare_fb
================================

.. c:function:: int vmw_sou_primary_plane_prepare_fb(struct drm_plane *plane, struct drm_plane_state *new_state)

    allocate backing buffer

    :param plane:
        display plane
    :type plane: struct drm_plane \*

    :param new_state:
        info on the new plane state, including the FB
    :type new_state: struct drm_plane_state \*

.. _`vmw_sou_primary_plane_prepare_fb.description`:

Description
-----------

The SOU backing buffer is our equivalent of the display plane.

Returns 0 on success

.. _`vmw_sou_surface_fifo_commit`:

vmw_sou_surface_fifo_commit
===========================

.. c:function:: void vmw_sou_surface_fifo_commit(struct vmw_kms_dirty *dirty)

    Callback to fill in and submit a blit surface to screen command.

    :param dirty:
        The closure structure.
    :type dirty: struct vmw_kms_dirty \*

.. _`vmw_sou_surface_fifo_commit.description`:

Description
-----------

Fills in the missing fields in the command, and translates the cliprects
to match the destination bounding box encoded.

.. _`vmw_sou_surface_clip`:

vmw_sou_surface_clip
====================

.. c:function:: void vmw_sou_surface_clip(struct vmw_kms_dirty *dirty)

    Callback to encode a blit surface to screen cliprect.

    :param dirty:
        The closure structure
    :type dirty: struct vmw_kms_dirty \*

.. _`vmw_sou_surface_clip.description`:

Description
-----------

Encodes a SVGASignedRect cliprect and updates the bounding box of the
BLIT_SURFACE_TO_SCREEN command.

.. _`vmw_kms_sou_do_surface_dirty`:

vmw_kms_sou_do_surface_dirty
============================

.. c:function:: int vmw_kms_sou_do_surface_dirty(struct vmw_private *dev_priv, struct vmw_framebuffer *framebuffer, struct drm_clip_rect *clips, struct drm_vmw_rect *vclips, struct vmw_resource *srf, s32 dest_x, s32 dest_y, unsigned num_clips, int inc, struct vmw_fence_obj **out_fence, struct drm_crtc *crtc)

    Dirty part of a surface backed framebuffer

    :param dev_priv:
        Pointer to the device private structure.
    :type dev_priv: struct vmw_private \*

    :param framebuffer:
        Pointer to the surface-buffer backed framebuffer.
    :type framebuffer: struct vmw_framebuffer \*

    :param clips:
        Array of clip rects. Either \ ``clips``\  or \ ``vclips``\  must be NULL.
    :type clips: struct drm_clip_rect \*

    :param vclips:
        Alternate array of clip rects. Either \ ``clips``\  or \ ``vclips``\  must
        be NULL.
    :type vclips: struct drm_vmw_rect \*

    :param srf:
        Pointer to surface to blit from. If NULL, the surface attached
        to \ ``framebuffer``\  will be used.
    :type srf: struct vmw_resource \*

    :param dest_x:
        X coordinate offset to align \ ``srf``\  with framebuffer coordinates.
    :type dest_x: s32

    :param dest_y:
        Y coordinate offset to align \ ``srf``\  with framebuffer coordinates.
    :type dest_y: s32

    :param num_clips:
        Number of clip rects in \ ``clips``\ .
    :type num_clips: unsigned

    :param inc:
        Increment to use when looping over \ ``clips``\ .
    :type inc: int

    :param out_fence:
        If non-NULL, will return a ref-counted pointer to a
        struct vmw_fence_obj. The returned fence pointer may be NULL in which
        case the device has already synchronized.
    :type out_fence: struct vmw_fence_obj \*\*

    :param crtc:
        If crtc is passed, perform surface dirty on that crtc only.
    :type crtc: struct drm_crtc \*

.. _`vmw_kms_sou_do_surface_dirty.description`:

Description
-----------

Returns 0 on success, negative error code on failure. -ERESTARTSYS if
interrupted.

.. _`vmw_sou_bo_fifo_commit`:

vmw_sou_bo_fifo_commit
======================

.. c:function:: void vmw_sou_bo_fifo_commit(struct vmw_kms_dirty *dirty)

    Callback to submit a set of readback clips.

    :param dirty:
        The closure structure.
    :type dirty: struct vmw_kms_dirty \*

.. _`vmw_sou_bo_fifo_commit.description`:

Description
-----------

Commits a previously built command buffer of readback clips.

.. _`vmw_sou_bo_clip`:

vmw_sou_bo_clip
===============

.. c:function:: void vmw_sou_bo_clip(struct vmw_kms_dirty *dirty)

    Callback to encode a readback cliprect.

    :param dirty:
        The closure structure
    :type dirty: struct vmw_kms_dirty \*

.. _`vmw_sou_bo_clip.description`:

Description
-----------

Encodes a BLIT_GMRFB_TO_SCREEN cliprect.

.. _`vmw_kms_sou_do_bo_dirty`:

vmw_kms_sou_do_bo_dirty
=======================

.. c:function:: int vmw_kms_sou_do_bo_dirty(struct vmw_private *dev_priv, struct vmw_framebuffer *framebuffer, struct drm_clip_rect *clips, struct drm_vmw_rect *vclips, unsigned num_clips, int increment, bool interruptible, struct vmw_fence_obj **out_fence, struct drm_crtc *crtc)

    Dirty part of a buffer-object backed framebuffer

    :param dev_priv:
        Pointer to the device private structure.
    :type dev_priv: struct vmw_private \*

    :param framebuffer:
        Pointer to the buffer-object backed framebuffer.
    :type framebuffer: struct vmw_framebuffer \*

    :param clips:
        Array of clip rects.
    :type clips: struct drm_clip_rect \*

    :param vclips:
        Alternate array of clip rects. Either \ ``clips``\  or \ ``vclips``\  must
        be NULL.
    :type vclips: struct drm_vmw_rect \*

    :param num_clips:
        Number of clip rects in \ ``clips``\ .
    :type num_clips: unsigned

    :param increment:
        Increment to use when looping over \ ``clips``\ .
    :type increment: int

    :param interruptible:
        Whether to perform waits interruptible if possible.
    :type interruptible: bool

    :param out_fence:
        If non-NULL, will return a ref-counted pointer to a
        struct vmw_fence_obj. The returned fence pointer may be NULL in which
        case the device has already synchronized.
    :type out_fence: struct vmw_fence_obj \*\*

    :param crtc:
        If crtc is passed, perform bo dirty on that crtc only.
    :type crtc: struct drm_crtc \*

.. _`vmw_kms_sou_do_bo_dirty.description`:

Description
-----------

Returns 0 on success, negative error code on failure. -ERESTARTSYS if
interrupted.

.. _`vmw_sou_readback_fifo_commit`:

vmw_sou_readback_fifo_commit
============================

.. c:function:: void vmw_sou_readback_fifo_commit(struct vmw_kms_dirty *dirty)

    Callback to submit a set of readback clips.

    :param dirty:
        The closure structure.
    :type dirty: struct vmw_kms_dirty \*

.. _`vmw_sou_readback_fifo_commit.description`:

Description
-----------

Commits a previously built command buffer of readback clips.

.. _`vmw_sou_readback_clip`:

vmw_sou_readback_clip
=====================

.. c:function:: void vmw_sou_readback_clip(struct vmw_kms_dirty *dirty)

    Callback to encode a readback cliprect.

    :param dirty:
        The closure structure
    :type dirty: struct vmw_kms_dirty \*

.. _`vmw_sou_readback_clip.description`:

Description
-----------

Encodes a BLIT_SCREEN_TO_GMRFB cliprect.

.. _`vmw_kms_sou_readback`:

vmw_kms_sou_readback
====================

.. c:function:: int vmw_kms_sou_readback(struct vmw_private *dev_priv, struct drm_file *file_priv, struct vmw_framebuffer *vfb, struct drm_vmw_fence_rep __user *user_fence_rep, struct drm_vmw_rect *vclips, uint32_t num_clips, struct drm_crtc *crtc)

    Perform a readback from the screen object system to a buffer-object backed framebuffer.

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

    :param crtc:
        If crtc is passed, readback on that crtc only.
    :type crtc: struct drm_crtc \*

.. _`vmw_kms_sou_readback.description`:

Description
-----------

Returns 0 on success, negative error code on failure. -ERESTARTSYS if
interrupted.

.. This file was automatic generated / don't edit.

