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
        s32 left;
        s32 right;
        s32 top;
        s32 bottom;
        u32 pitch;
        union {unnamed_union};
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

pitch
    *undescribed*

{unnamed_union}
    anonymous


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
        struct vmw_surface *display_srf;
        enum stdu_content_type content_fb_type;
        bool defined;
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

defined
    true if the current display unit has been initialized

.. _`vmw_stdu_unpin_display`:

vmw_stdu_unpin_display
======================

.. c:function:: void vmw_stdu_unpin_display(struct vmw_screen_target_display_unit *stdu)

    unpins the resource associated with display surface

    :param struct vmw_screen_target_display_unit \*stdu:
        contains the display surface

.. _`vmw_stdu_unpin_display.description`:

Description
-----------

If the display surface was privatedly allocated by
\ :c:func:`vmw_surface_gb_priv_define`\  and not registered as a framebuffer, then it
won't be automatically cleaned up when all the framebuffers are freed.  As
such, we have to explicitly call \ :c:func:`vmw_resource_unreference`\  to get it freed.

.. _`vmw_stdu_crtc_destroy`:

vmw_stdu_crtc_destroy
=====================

.. c:function:: void vmw_stdu_crtc_destroy(struct drm_crtc *crtc)

    cleans up the STDU

    :param struct drm_crtc \*crtc:
        used to get a reference to the containing STDU

.. _`vmw_stdu_define_st`:

vmw_stdu_define_st
==================

.. c:function:: int vmw_stdu_define_st(struct vmw_private *dev_priv, struct vmw_screen_target_display_unit *stdu, struct drm_display_mode *mode, int crtc_x, int crtc_y)

    Defines a Screen Target

    :param struct vmw_private \*dev_priv:
        VMW DRM device

    :param struct vmw_screen_target_display_unit \*stdu:
        display unit to create a Screen Target for

    :param struct drm_display_mode \*mode:
        The mode to set.

    :param int crtc_x:
        X coordinate of screen target relative to framebuffer origin.

    :param int crtc_y:
        Y coordinate of screen target relative to framebuffer origin.

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

.. c:function:: int vmw_stdu_bind_st(struct vmw_private *dev_priv, struct vmw_screen_target_display_unit *stdu, struct vmw_resource *res)

    Binds a surface to a Screen Target

    :param struct vmw_private \*dev_priv:
        VMW DRM device

    :param struct vmw_screen_target_display_unit \*stdu:
        display unit affected

    :param struct vmw_resource \*res:
        Buffer to bind to the screen target.  Set to NULL to blank screen.

.. _`vmw_stdu_bind_st.description`:

Description
-----------

Binding a surface to a Screen Target the same as flipping

.. _`vmw_stdu_populate_update`:

vmw_stdu_populate_update
========================

.. c:function:: void vmw_stdu_populate_update(void *cmd, int unit, s32 left, s32 right, s32 top, s32 bottom)

    populate an UPDATE_GB_SCREENTARGET command with a bounding box.

    :param void \*cmd:
        Pointer to command stream.

    :param int unit:
        Screen target unit.

    :param s32 left:
        Left side of bounding box.

    :param s32 right:
        Right side of bounding box.

    :param s32 top:
        Top side of bounding box.

    :param s32 bottom:
        Bottom side of bounding box.

.. _`vmw_stdu_update_st`:

vmw_stdu_update_st
==================

.. c:function:: int vmw_stdu_update_st(struct vmw_private *dev_priv, struct vmw_screen_target_display_unit *stdu)

    Full update of a Screen Target

    :param struct vmw_private \*dev_priv:
        VMW DRM device

    :param struct vmw_screen_target_display_unit \*stdu:
        display unit affected

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

    :param struct vmw_private \*dev_priv:
        VMW DRM device

    :param struct vmw_screen_target_display_unit \*stdu:
        display unit to destroy

.. _`vmw_stdu_bind_fb`:

vmw_stdu_bind_fb
================

.. c:function:: int vmw_stdu_bind_fb(struct vmw_private *dev_priv, struct drm_crtc *crtc, struct drm_display_mode *mode, struct drm_framebuffer *new_fb)

    Bind an fb to a defined screen target

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct drm_crtc \*crtc:
        The crtc holding the screen target.

    :param struct drm_display_mode \*mode:
        The mode currently used by the screen target. Must be non-NULL.

    :param struct drm_framebuffer \*new_fb:
        The new framebuffer to bind. Must be non-NULL.

.. _`vmw_stdu_bind_fb.return`:

Return
------

0 on success, error code on failure.

.. _`vmw_stdu_crtc_set_config`:

vmw_stdu_crtc_set_config
========================

.. c:function:: int vmw_stdu_crtc_set_config(struct drm_mode_set *set)

    Sets a mode

    :param struct drm_mode_set \*set:
        mode parameters

.. _`vmw_stdu_crtc_set_config.description`:

Description
-----------

This function is the device-specific portion of the DRM CRTC mode set.
For the SVGA device, we do this by defining a Screen Target, binding a
GB Surface to that target, and finally update the screen target.

.. _`vmw_stdu_crtc_set_config.return`:

Return
------

0 on success, error code otherwise

.. _`vmw_stdu_crtc_page_flip`:

vmw_stdu_crtc_page_flip
=======================

.. c:function:: int vmw_stdu_crtc_page_flip(struct drm_crtc *crtc, struct drm_framebuffer *new_fb, struct drm_pending_vblank_event *event, uint32_t flags)

    Binds a buffer to a screen target

    :param struct drm_crtc \*crtc:
        CRTC to attach FB to

    :param struct drm_framebuffer \*new_fb:
        *undescribed*

    :param struct drm_pending_vblank_event \*event:
        Event to be posted. This event should've been alloced
        using k[mz]alloc, and should've been completely initialized.

    :param uint32_t flags:
        *undescribed*

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

.. _`vmw_stdu_dmabuf_clip`:

vmw_stdu_dmabuf_clip
====================

.. c:function:: void vmw_stdu_dmabuf_clip(struct vmw_kms_dirty *dirty)

    Callback to encode a suface DMA command cliprect

    :param struct vmw_kms_dirty \*dirty:
        The closure structure.

.. _`vmw_stdu_dmabuf_clip.description`:

Description
-----------

Encodes a surface DMA command cliprect and updates the bounding box
for the DMA.

.. _`vmw_stdu_dmabuf_fifo_commit`:

vmw_stdu_dmabuf_fifo_commit
===========================

.. c:function:: void vmw_stdu_dmabuf_fifo_commit(struct vmw_kms_dirty *dirty)

    Callback to fill in and submit a DMA command.

    :param struct vmw_kms_dirty \*dirty:
        The closure structure.

.. _`vmw_stdu_dmabuf_fifo_commit.description`:

Description
-----------

Fills in the missing fields in a DMA command, and optionally encodes
a screen target update command, depending on transfer direction.

.. _`vmw_kms_stdu_dma`:

vmw_kms_stdu_dma
================

.. c:function:: int vmw_kms_stdu_dma(struct vmw_private *dev_priv, struct drm_file *file_priv, struct vmw_framebuffer *vfb, struct drm_vmw_fence_rep __user *user_fence_rep, struct drm_clip_rect *clips, struct drm_vmw_rect *vclips, uint32_t num_clips, int increment, bool to_surface, bool interruptible)

    Perform a DMA transfer between a dma-buffer backed framebuffer and the screen target system.

    :param struct vmw_private \*dev_priv:
        Pointer to the device private structure.

    :param struct drm_file \*file_priv:
        Pointer to a struct drm-file identifying the caller. May be
        set to NULL, but then \ ``user_fence_rep``\  must also be set to NULL.

    :param struct vmw_framebuffer \*vfb:
        Pointer to the dma-buffer backed framebuffer.

    :param struct drm_vmw_fence_rep __user \*user_fence_rep:
        *undescribed*

    :param struct drm_clip_rect \*clips:
        Array of clip rects. Either \ ``clips``\  or \ ``vclips``\  must be NULL.

    :param struct drm_vmw_rect \*vclips:
        Alternate array of clip rects. Either \ ``clips``\  or \ ``vclips``\  must
        be NULL.

    :param uint32_t num_clips:
        Number of clip rects in \ ``clips``\  or \ ``vclips``\ .

    :param int increment:
        Increment to use when looping over \ ``clips``\  or \ ``vclips``\ .

    :param bool to_surface:
        Whether to DMA to the screen target system as opposed to
        from the screen target system.

    :param bool interruptible:
        Whether to perform waits interruptible if possible.

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

    :param struct vmw_kms_dirty \*dirty:
        The closure structure.

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

    :param struct vmw_kms_dirty \*dirty:
        The closure structure.

.. _`vmw_kms_stdu_surface_fifo_commit.description`:

Description
-----------

Fills in the missing fields in a surface copy command, and encodes a screen
target update command.

.. _`vmw_kms_stdu_surface_dirty`:

vmw_kms_stdu_surface_dirty
==========================

.. c:function:: int vmw_kms_stdu_surface_dirty(struct vmw_private *dev_priv, struct vmw_framebuffer *framebuffer, struct drm_clip_rect *clips, struct drm_vmw_rect *vclips, struct vmw_resource *srf, s32 dest_x, s32 dest_y, unsigned num_clips, int inc, struct vmw_fence_obj **out_fence)

    Dirty part of a surface backed framebuffer

    :param struct vmw_private \*dev_priv:
        Pointer to the device private structure.

    :param struct vmw_framebuffer \*framebuffer:
        Pointer to the surface-buffer backed framebuffer.

    :param struct drm_clip_rect \*clips:
        Array of clip rects. Either \ ``clips``\  or \ ``vclips``\  must be NULL.

    :param struct drm_vmw_rect \*vclips:
        Alternate array of clip rects. Either \ ``clips``\  or \ ``vclips``\  must
        be NULL.

    :param struct vmw_resource \*srf:
        Pointer to surface to blit from. If NULL, the surface attached
        to \ ``framebuffer``\  will be used.

    :param s32 dest_x:
        X coordinate offset to align \ ``srf``\  with framebuffer coordinates.

    :param s32 dest_y:
        Y coordinate offset to align \ ``srf``\  with framebuffer coordinates.

    :param unsigned num_clips:
        Number of clip rects in \ ``clips``\ .

    :param int inc:
        Increment to use when looping over \ ``clips``\ .

    :param struct vmw_fence_obj \*\*out_fence:
        If non-NULL, will return a ref-counted pointer to a
        struct vmw_fence_obj. The returned fence pointer may be NULL in which
        case the device has already synchronized.

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

    :param struct drm_encoder \*encoder:
        used the get the containing STDU

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

    :param struct drm_connector \*connector:
        used to get the containing STDU

.. _`vmw_stdu_connector_destroy.description`:

Description
-----------

vmwgfx cleans up crtc/encoder/connector all at the same time so technically
this can be a no-op.  Nevertheless, it doesn't hurt of have this in case
the common KMS code changes and somehow \ :c:func:`vmw_stdu_crtc_destroy`\  doesn't
get called.

.. _`vmw_stdu_init`:

vmw_stdu_init
=============

.. c:function:: int vmw_stdu_init(struct vmw_private *dev_priv, unsigned unit)

    Sets up a Screen Target Display Unit

    :param struct vmw_private \*dev_priv:
        VMW DRM device

    :param unsigned unit:
        unit number range from 0 to VMWGFX_NUM_DISPLAY_UNITS

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

    :param struct vmw_screen_target_display_unit \*stdu:
        Screen Target Display Unit to be destroyed

.. _`vmw_stdu_destroy.description`:

Description
-----------

Clean up after vmw_stdu_init

.. _`vmw_kms_stdu_init_display`:

vmw_kms_stdu_init_display
=========================

.. c:function:: int vmw_kms_stdu_init_display(struct vmw_private *dev_priv)

    Initializes a Screen Target based display

    :param struct vmw_private \*dev_priv:
        VMW DRM device

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

.. _`vmw_kms_stdu_close_display`:

vmw_kms_stdu_close_display
==========================

.. c:function:: int vmw_kms_stdu_close_display(struct vmw_private *dev_priv)

    Cleans up after vmw_kms_stdu_init_display

    :param struct vmw_private \*dev_priv:
        VMW DRM device

.. _`vmw_kms_stdu_close_display.description`:

Description
-----------

Frees up any resources allocated by vmw_kms_stdu_init_display

.. _`vmw_kms_stdu_close_display.return`:

Return
------

0 on success

.. This file was automatic generated / don't edit.

