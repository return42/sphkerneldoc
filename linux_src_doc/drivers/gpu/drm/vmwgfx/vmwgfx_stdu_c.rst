.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_stdu.c

.. _`vmw_stdu_dirty`:

struct vmw_stdu_dirty
=====================

.. c:type:: struct vmw_stdu_dirty

    closure structure for the update functions

.. _`vmw_stdu_dirty.definition`:

Definition
----------

.. code-block:: c

    struct vmw_stdu_dirty {
        struct vmw_kms_dirty base;
        SVGA3dTransferType transfer;
        s32 left, right, top, bottom;
        s32 fb_left, fb_top;
        u32 pitch;
        union {
            struct vmw_buffer_object *buf;
            u32 sid;
        } ;
    }

.. _`vmw_stdu_dirty.members`:

Members
-------

base
    The base type we derive from. Used by \ :c:func:`vmw_kms_helper_dirty`\ .

transfer
    Transfer direction for DMA command.

left
    Left side of bounding box.

right
    Right side of bounding box.

top
    Top side of bounding box.

bottom
    Bottom side of bounding box.

fb_left
    Left side of the framebuffer/content bounding box

fb_top
    Top of the framebuffer/content bounding box

pitch
    *undescribed*

{unnamed_union}
    anonymous

buf
    buffer object when DMA-ing between buffer and screen targets.

sid
    Surface ID when copying between surface and screen targets.

.. _`vmw_screen_target_display_unit`:

struct vmw_screen_target_display_unit
=====================================

.. c:type:: struct vmw_screen_target_display_unit


.. _`vmw_screen_target_display_unit.definition`:

Definition
----------

.. code-block:: c

    struct vmw_screen_target_display_unit {
        struct vmw_display_unit base;
        const struct vmw_surface *display_srf;
        enum stdu_content_type content_fb_type;
        s32 display_width, display_height;
        bool defined;
        unsigned int cpp;
    }

.. _`vmw_screen_target_display_unit.members`:

Members
-------

base
    VMW specific DU structure

display_srf
    surface to be displayed.  The dimension of this will always
    match the display mode.  If the display mode matches
    content_vfbs dimensions, then this is a pointer into the
    corresponding field in content_vfbs.  If not, then this
    is a separate buffer to which content_vfbs will blit to.

content_fb_type
    *undescribed*

display_width
    *undescribed*

display_height
    *undescribed*

defined
    true if the current display unit has been initialized

cpp
    *undescribed*

.. _`vmw_stdu_crtc_destroy`:

vmw_stdu_crtc_destroy
=====================

.. c:function:: void vmw_stdu_crtc_destroy(struct drm_crtc *crtc)

    cleans up the STDU

    :param crtc:
        used to get a reference to the containing STDU
    :type crtc: struct drm_crtc \*

.. _`vmw_stdu_define_st`:

vmw_stdu_define_st
==================

.. c:function:: int vmw_stdu_define_st(struct vmw_private *dev_priv, struct vmw_screen_target_display_unit *stdu, struct drm_display_mode *mode, int crtc_x, int crtc_y)

    Defines a Screen Target

    :param dev_priv:
        VMW DRM device
    :type dev_priv: struct vmw_private \*

    :param stdu:
        display unit to create a Screen Target for
    :type stdu: struct vmw_screen_target_display_unit \*

    :param mode:
        The mode to set.
    :type mode: struct drm_display_mode \*

    :param crtc_x:
        X coordinate of screen target relative to framebuffer origin.
    :type crtc_x: int

    :param crtc_y:
        Y coordinate of screen target relative to framebuffer origin.
    :type crtc_y: int

.. _`vmw_stdu_define_st.description`:

Description
-----------

Creates a STDU that we can used later.  This function is called whenever the
framebuffer size changes.

.. _`vmw_stdu_define_st.return`:

Return
------

0 on success, error code on failure

.. _`vmw_stdu_bind_st`:

vmw_stdu_bind_st
================

.. c:function:: int vmw_stdu_bind_st(struct vmw_private *dev_priv, struct vmw_screen_target_display_unit *stdu, const struct vmw_resource *res)

    Binds a surface to a Screen Target

    :param dev_priv:
        VMW DRM device
    :type dev_priv: struct vmw_private \*

    :param stdu:
        display unit affected
    :type stdu: struct vmw_screen_target_display_unit \*

    :param res:
        Buffer to bind to the screen target.  Set to NULL to blank screen.
    :type res: const struct vmw_resource \*

.. _`vmw_stdu_bind_st.description`:

Description
-----------

Binding a surface to a Screen Target the same as flipping

.. _`vmw_stdu_populate_update`:

vmw_stdu_populate_update
========================

.. c:function:: void vmw_stdu_populate_update(void *cmd, int unit, s32 left, s32 right, s32 top, s32 bottom)

    populate an UPDATE_GB_SCREENTARGET command with a bounding box.

    :param cmd:
        Pointer to command stream.
    :type cmd: void \*

    :param unit:
        Screen target unit.
    :type unit: int

    :param left:
        Left side of bounding box.
    :type left: s32

    :param right:
        Right side of bounding box.
    :type right: s32

    :param top:
        Top side of bounding box.
    :type top: s32

    :param bottom:
        Bottom side of bounding box.
    :type bottom: s32

.. _`vmw_stdu_update_st`:

vmw_stdu_update_st
==================

.. c:function:: int vmw_stdu_update_st(struct vmw_private *dev_priv, struct vmw_screen_target_display_unit *stdu)

    Full update of a Screen Target

    :param dev_priv:
        VMW DRM device
    :type dev_priv: struct vmw_private \*

    :param stdu:
        display unit affected
    :type stdu: struct vmw_screen_target_display_unit \*

.. _`vmw_stdu_update_st.description`:

Description
-----------

This function needs to be called whenever the content of a screen
target has changed completely. Typically as a result of a backing
surface change.

.. _`vmw_stdu_update_st.return`:

Return
------

0 on success, error code on failure

.. _`vmw_stdu_destroy_st`:

vmw_stdu_destroy_st
===================

.. c:function:: int vmw_stdu_destroy_st(struct vmw_private *dev_priv, struct vmw_screen_target_display_unit *stdu)

    Destroy a Screen Target

    :param dev_priv:
        VMW DRM device
    :type dev_priv: struct vmw_private \*

    :param stdu:
        display unit to destroy
    :type stdu: struct vmw_screen_target_display_unit \*

.. _`vmw_stdu_crtc_mode_set_nofb`:

vmw_stdu_crtc_mode_set_nofb
===========================

.. c:function:: void vmw_stdu_crtc_mode_set_nofb(struct drm_crtc *crtc)

    Updates screen target size

    :param crtc:
        CRTC associated with the screen target
    :type crtc: struct drm_crtc \*

.. _`vmw_stdu_crtc_mode_set_nofb.description`:

Description
-----------

This function defines/destroys a screen target

.. _`vmw_stdu_crtc_page_flip`:

vmw_stdu_crtc_page_flip
=======================

.. c:function:: int vmw_stdu_crtc_page_flip(struct drm_crtc *crtc, struct drm_framebuffer *new_fb, struct drm_pending_vblank_event *event, uint32_t flags, struct drm_modeset_acquire_ctx *ctx)

    Binds a buffer to a screen target

    :param crtc:
        CRTC to attach FB to
    :type crtc: struct drm_crtc \*

    :param new_fb:
        *undescribed*
    :type new_fb: struct drm_framebuffer \*

    :param event:
        Event to be posted. This event should've been alloced
        using k[mz]alloc, and should've been completely initialized.
    :type event: struct drm_pending_vblank_event \*

    :param flags:
        *undescribed*
    :type flags: uint32_t

    :param ctx:
        *undescribed*
    :type ctx: struct drm_modeset_acquire_ctx \*

.. _`vmw_stdu_crtc_page_flip.description`:

Description
-----------

If the STDU uses the same display and content buffers, i.e. a true flip,
this function will replace the existing display buffer with the new content
buffer.

If the STDU uses different display and content buffers, i.e. a blit, then
only the content buffer will be updated.

.. _`vmw_stdu_crtc_page_flip.return`:

Return
------

0 on success, error code on failure

.. _`vmw_stdu_bo_clip`:

vmw_stdu_bo_clip
================

.. c:function:: void vmw_stdu_bo_clip(struct vmw_kms_dirty *dirty)

    Callback to encode a suface DMA command cliprect

    :param dirty:
        The closure structure.
    :type dirty: struct vmw_kms_dirty \*

.. _`vmw_stdu_bo_clip.description`:

Description
-----------

Encodes a surface DMA command cliprect and updates the bounding box
for the DMA.

.. _`vmw_stdu_bo_fifo_commit`:

vmw_stdu_bo_fifo_commit
=======================

.. c:function:: void vmw_stdu_bo_fifo_commit(struct vmw_kms_dirty *dirty)

    Callback to fill in and submit a DMA command.

    :param dirty:
        The closure structure.
    :type dirty: struct vmw_kms_dirty \*

.. _`vmw_stdu_bo_fifo_commit.description`:

Description
-----------

Fills in the missing fields in a DMA command, and optionally encodes
a screen target update command, depending on transfer direction.

.. _`vmw_stdu_bo_cpu_clip`:

vmw_stdu_bo_cpu_clip
====================

.. c:function:: void vmw_stdu_bo_cpu_clip(struct vmw_kms_dirty *dirty)

    Callback to encode a CPU blit

    :param dirty:
        The closure structure.
    :type dirty: struct vmw_kms_dirty \*

.. _`vmw_stdu_bo_cpu_clip.description`:

Description
-----------

This function calculates the bounding box for all the incoming clips.

.. _`vmw_stdu_bo_cpu_commit`:

vmw_stdu_bo_cpu_commit
======================

.. c:function:: void vmw_stdu_bo_cpu_commit(struct vmw_kms_dirty *dirty)

    Callback to do a CPU blit from buffer object

    :param dirty:
        The closure structure.
    :type dirty: struct vmw_kms_dirty \*

.. _`vmw_stdu_bo_cpu_commit.description`:

Description
-----------

For the special case when we cannot create a proxy surface in a
2D VM, we have to do a CPU blit ourselves.

.. _`vmw_kms_stdu_dma`:

vmw_kms_stdu_dma
================

.. c:function:: int vmw_kms_stdu_dma(struct vmw_private *dev_priv, struct drm_file *file_priv, struct vmw_framebuffer *vfb, struct drm_vmw_fence_rep __user *user_fence_rep, struct drm_clip_rect *clips, struct drm_vmw_rect *vclips, uint32_t num_clips, int increment, bool to_surface, bool interruptible, struct drm_crtc *crtc)

    Perform a DMA transfer between a buffer-object backed framebuffer and the screen target system.

    :param dev_priv:
        Pointer to the device private structure.
    :type dev_priv: struct vmw_private \*

    :param file_priv:
        Pointer to a struct drm-file identifying the caller. May be
        set to NULL, but then \ ``user_fence_rep``\  must also be set to NULL.
    :type file_priv: struct drm_file \*

    :param vfb:
        Pointer to the buffer-object backed framebuffer.
    :type vfb: struct vmw_framebuffer \*

    :param user_fence_rep:
        *undescribed*
    :type user_fence_rep: struct drm_vmw_fence_rep __user \*

    :param clips:
        Array of clip rects. Either \ ``clips``\  or \ ``vclips``\  must be NULL.
    :type clips: struct drm_clip_rect \*

    :param vclips:
        Alternate array of clip rects. Either \ ``clips``\  or \ ``vclips``\  must
        be NULL.
    :type vclips: struct drm_vmw_rect \*

    :param num_clips:
        Number of clip rects in \ ``clips``\  or \ ``vclips``\ .
    :type num_clips: uint32_t

    :param increment:
        Increment to use when looping over \ ``clips``\  or \ ``vclips``\ .
    :type increment: int

    :param to_surface:
        Whether to DMA to the screen target system as opposed to
        from the screen target system.
    :type to_surface: bool

    :param interruptible:
        Whether to perform waits interruptible if possible.
    :type interruptible: bool

    :param crtc:
        If crtc is passed, perform stdu dma on that crtc only.
    :type crtc: struct drm_crtc \*

.. _`vmw_kms_stdu_dma.description`:

Description
-----------

If DMA-ing till the screen target system, the function will also notify
the screen target system that a bounding box of the cliprects has been
updated.
Returns 0 on success, negative error code on failure. -ERESTARTSYS if
interrupted.

.. _`vmw_kms_stdu_surface_clip`:

vmw_kms_stdu_surface_clip
=========================

.. c:function:: void vmw_kms_stdu_surface_clip(struct vmw_kms_dirty *dirty)

    Callback to encode a surface copy command cliprect

    :param dirty:
        The closure structure.
    :type dirty: struct vmw_kms_dirty \*

.. _`vmw_kms_stdu_surface_clip.description`:

Description
-----------

Encodes a surface copy command cliprect and updates the bounding box
for the copy.

.. _`vmw_kms_stdu_surface_fifo_commit`:

vmw_kms_stdu_surface_fifo_commit
================================

.. c:function:: void vmw_kms_stdu_surface_fifo_commit(struct vmw_kms_dirty *dirty)

    Callback to fill in and submit a surface copy command.

    :param dirty:
        The closure structure.
    :type dirty: struct vmw_kms_dirty \*

.. _`vmw_kms_stdu_surface_fifo_commit.description`:

Description
-----------

Fills in the missing fields in a surface copy command, and encodes a screen
target update command.

.. _`vmw_kms_stdu_surface_dirty`:

vmw_kms_stdu_surface_dirty
==========================

.. c:function:: int vmw_kms_stdu_surface_dirty(struct vmw_private *dev_priv, struct vmw_framebuffer *framebuffer, struct drm_clip_rect *clips, struct drm_vmw_rect *vclips, struct vmw_resource *srf, s32 dest_x, s32 dest_y, unsigned num_clips, int inc, struct vmw_fence_obj **out_fence, struct drm_crtc *crtc)

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

.. _`vmw_kms_stdu_surface_dirty.description`:

Description
-----------

Returns 0 on success, negative error code on failure. -ERESTARTSYS if
interrupted.

.. _`vmw_stdu_encoder_destroy`:

vmw_stdu_encoder_destroy
========================

.. c:function:: void vmw_stdu_encoder_destroy(struct drm_encoder *encoder)

    cleans up the STDU

    :param encoder:
        used the get the containing STDU
    :type encoder: struct drm_encoder \*

.. _`vmw_stdu_encoder_destroy.description`:

Description
-----------

vmwgfx cleans up crtc/encoder/connector all at the same time so technically
this can be a no-op.  Nevertheless, it doesn't hurt of have this in case
the common KMS code changes and somehow \ :c:func:`vmw_stdu_crtc_destroy`\  doesn't
get called.

.. _`vmw_stdu_connector_destroy`:

vmw_stdu_connector_destroy
==========================

.. c:function:: void vmw_stdu_connector_destroy(struct drm_connector *connector)

    cleans up the STDU

    :param connector:
        used to get the containing STDU
    :type connector: struct drm_connector \*

.. _`vmw_stdu_connector_destroy.description`:

Description
-----------

vmwgfx cleans up crtc/encoder/connector all at the same time so technically
this can be a no-op.  Nevertheless, it doesn't hurt of have this in case
the common KMS code changes and somehow \ :c:func:`vmw_stdu_crtc_destroy`\  doesn't
get called.

.. _`vmw_stdu_primary_plane_cleanup_fb`:

vmw_stdu_primary_plane_cleanup_fb
=================================

.. c:function:: void vmw_stdu_primary_plane_cleanup_fb(struct drm_plane *plane, struct drm_plane_state *old_state)

    Unpins the display surface

    :param plane:
        display plane
    :type plane: struct drm_plane \*

    :param old_state:
        Contains the FB to clean up
    :type old_state: struct drm_plane_state \*

.. _`vmw_stdu_primary_plane_cleanup_fb.description`:

Description
-----------

Unpins the display surface

Returns 0 on success

.. _`vmw_stdu_primary_plane_prepare_fb`:

vmw_stdu_primary_plane_prepare_fb
=================================

.. c:function:: int vmw_stdu_primary_plane_prepare_fb(struct drm_plane *plane, struct drm_plane_state *new_state)

    Readies the display surface

    :param plane:
        display plane
    :type plane: struct drm_plane \*

    :param new_state:
        info on the new plane state, including the FB
    :type new_state: struct drm_plane_state \*

.. _`vmw_stdu_primary_plane_prepare_fb.description`:

Description
-----------

This function allocates a new display surface if the content is
backed by a buffer object.  The display surface is pinned here, and it'll
be unpinned in .cleanup_fb()

Returns 0 on success

.. _`vmw_stdu_primary_plane_atomic_update`:

vmw_stdu_primary_plane_atomic_update
====================================

.. c:function:: void vmw_stdu_primary_plane_atomic_update(struct drm_plane *plane, struct drm_plane_state *old_state)

    formally switches STDU to new plane

    :param plane:
        display plane
    :type plane: struct drm_plane \*

    :param old_state:
        Only used to get crtc info
    :type old_state: struct drm_plane_state \*

.. _`vmw_stdu_primary_plane_atomic_update.description`:

Description
-----------

Formally update stdu->display_srf to the new plane, and bind the new
plane STDU.  This function is called during the commit phase when
all the preparation have been done and all the configurations have
been checked.

.. _`vmw_stdu_init`:

vmw_stdu_init
=============

.. c:function:: int vmw_stdu_init(struct vmw_private *dev_priv, unsigned unit)

    Sets up a Screen Target Display Unit

    :param dev_priv:
        VMW DRM device
    :type dev_priv: struct vmw_private \*

    :param unit:
        unit number range from 0 to VMWGFX_NUM_DISPLAY_UNITS
    :type unit: unsigned

.. _`vmw_stdu_init.description`:

Description
-----------

This function is called once per CRTC, and allocates one Screen Target
display unit to represent that CRTC.  Since the SVGA device does not separate
out encoder and connector, they are represented as part of the STDU as well.

.. _`vmw_stdu_destroy`:

vmw_stdu_destroy
================

.. c:function:: void vmw_stdu_destroy(struct vmw_screen_target_display_unit *stdu)

    Cleans up a vmw_screen_target_display_unit

    :param stdu:
        Screen Target Display Unit to be destroyed
    :type stdu: struct vmw_screen_target_display_unit \*

.. _`vmw_stdu_destroy.description`:

Description
-----------

Clean up after vmw_stdu_init

.. _`vmw_kms_stdu_init_display`:

vmw_kms_stdu_init_display
=========================

.. c:function:: int vmw_kms_stdu_init_display(struct vmw_private *dev_priv)

    Initializes a Screen Target based display

    :param dev_priv:
        VMW DRM device
    :type dev_priv: struct vmw_private \*

.. _`vmw_kms_stdu_init_display.description`:

Description
-----------

This function initialize a Screen Target based display device.  It checks
the capability bits to make sure the underlying hardware can support
screen targets, and then creates the maximum number of CRTCs, a.k.a Display
Units, as supported by the display hardware.

.. _`vmw_kms_stdu_init_display.return`:

Return
------

0 on success, error code otherwise

.. This file was automatic generated / don't edit.

