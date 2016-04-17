.. -*- coding: utf-8; mode: rst -*-

=============
vmwgfx_scrn.c
=============


.. _`vmw_kms_sou_surface_dirty`:

struct vmw_kms_sou_surface_dirty
================================

.. c:type:: vmw_kms_sou_surface_dirty

    Closure structure for blit surface to screen command.


.. _`vmw_kms_sou_surface_dirty.definition`:

Definition
----------

.. code-block:: c

  struct vmw_kms_sou_surface_dirty {
    struct vmw_kms_dirty base;
    s32 left;
    s32 right;
    s32 top;
    s32 bottom;
    s32 dst_x;
    s32 dst_y;
    u32 sid;
  };


.. _`vmw_kms_sou_surface_dirty.members`:

Members
-------

:``base``:
    The base type we derive from. Used by :c:func:`vmw_kms_helper_dirty`.

:``left``:
    Left side of bounding box.

:``right``:
    Right side of bounding box.

:``top``:
    Top side of bounding box.

:``bottom``:
    Bottom side of bounding box.

:``dst_x``:
    Difference between source clip rects and framebuffer coordinates.

:``dst_y``:
    Difference between source clip rects and framebuffer coordinates.

:``sid``:
    Surface id of surface to copy from.




.. _`vmw_sou_fifo_create`:

vmw_sou_fifo_create
===================

.. c:function:: int vmw_sou_fifo_create (struct vmw_private *dev_priv, struct vmw_screen_object_unit *sou, uint32_t x, uint32_t y, struct drm_display_mode *mode)

    :param struct vmw_private \*dev_priv:

        *undescribed*

    :param struct vmw_screen_object_unit \*sou:

        *undescribed*

    :param uint32_t x:

        *undescribed*

    :param uint32_t y:

        *undescribed*

    :param struct drm_display_mode \*mode:

        *undescribed*



.. _`vmw_sou_fifo_destroy`:

vmw_sou_fifo_destroy
====================

.. c:function:: int vmw_sou_fifo_destroy (struct vmw_private *dev_priv, struct vmw_screen_object_unit *sou)

    :param struct vmw_private \*dev_priv:

        *undescribed*

    :param struct vmw_screen_object_unit \*sou:

        *undescribed*



.. _`vmw_sou_backing_free`:

vmw_sou_backing_free
====================

.. c:function:: void vmw_sou_backing_free (struct vmw_private *dev_priv, struct vmw_screen_object_unit *sou)

    :param struct vmw_private \*dev_priv:

        *undescribed*

    :param struct vmw_screen_object_unit \*sou:

        *undescribed*



.. _`vmw_sou_backing_alloc`:

vmw_sou_backing_alloc
=====================

.. c:function:: int vmw_sou_backing_alloc (struct vmw_private *dev_priv, struct vmw_screen_object_unit *sou, unsigned long size)

    :param struct vmw_private \*dev_priv:

        *undescribed*

    :param struct vmw_screen_object_unit \*sou:

        *undescribed*

    :param unsigned long size:

        *undescribed*



.. _`vmw_sou_surface_fifo_commit`:

vmw_sou_surface_fifo_commit
===========================

.. c:function:: void vmw_sou_surface_fifo_commit (struct vmw_kms_dirty *dirty)

    Callback to fill in and submit a blit surface to screen command.

    :param struct vmw_kms_dirty \*dirty:
        The closure structure.



.. _`vmw_sou_surface_fifo_commit.description`:

Description
-----------

Fills in the missing fields in the command, and translates the cliprects
to match the destination bounding box encoded.



.. _`vmw_sou_surface_clip`:

vmw_sou_surface_clip
====================

.. c:function:: void vmw_sou_surface_clip (struct vmw_kms_dirty *dirty)

    Callback to encode a blit surface to screen cliprect.

    :param struct vmw_kms_dirty \*dirty:
        The closure structure



.. _`vmw_sou_surface_clip.description`:

Description
-----------

Encodes a SVGASignedRect cliprect and updates the bounding box of the
BLIT_SURFACE_TO_SCREEN command.



.. _`vmw_kms_sou_do_surface_dirty`:

vmw_kms_sou_do_surface_dirty
============================

.. c:function:: int vmw_kms_sou_do_surface_dirty (struct vmw_private *dev_priv, struct vmw_framebuffer *framebuffer, struct drm_clip_rect *clips, struct drm_vmw_rect *vclips, struct vmw_resource *srf, s32 dest_x, s32 dest_y, unsigned num_clips, int inc, struct vmw_fence_obj **out_fence)

    Dirty part of a surface backed framebuffer

    :param struct vmw_private \*dev_priv:
        Pointer to the device private structure.

    :param struct vmw_framebuffer \*framebuffer:
        Pointer to the surface-buffer backed framebuffer.

    :param struct drm_clip_rect \*clips:
        Array of clip rects. Either ``clips`` or ``vclips`` must be NULL.

    :param struct drm_vmw_rect \*vclips:
        Alternate array of clip rects. Either ``clips`` or ``vclips`` must
        be NULL.

    :param struct vmw_resource \*srf:
        Pointer to surface to blit from. If NULL, the surface attached
        to ``framebuffer`` will be used.

    :param s32 dest_x:
        X coordinate offset to align ``srf`` with framebuffer coordinates.

    :param s32 dest_y:
        Y coordinate offset to align ``srf`` with framebuffer coordinates.

    :param unsigned num_clips:
        Number of clip rects in ``clips``\ .

    :param int inc:
        Increment to use when looping over ``clips``\ .

    :param struct vmw_fence_obj \*\*out_fence:
        If non-NULL, will return a ref-counted pointer to a
        struct vmw_fence_obj. The returned fence pointer may be NULL in which
        case the device has already synchronized.



.. _`vmw_kms_sou_do_surface_dirty.description`:

Description
-----------

Returns 0 on success, negative error code on failure. -ERESTARTSYS if
interrupted.



.. _`vmw_sou_dmabuf_fifo_commit`:

vmw_sou_dmabuf_fifo_commit
==========================

.. c:function:: void vmw_sou_dmabuf_fifo_commit (struct vmw_kms_dirty *dirty)

    Callback to submit a set of readback clips.

    :param struct vmw_kms_dirty \*dirty:
        The closure structure.



.. _`vmw_sou_dmabuf_fifo_commit.description`:

Description
-----------

Commits a previously built command buffer of readback clips.



.. _`vmw_sou_dmabuf_clip`:

vmw_sou_dmabuf_clip
===================

.. c:function:: void vmw_sou_dmabuf_clip (struct vmw_kms_dirty *dirty)

    Callback to encode a readback cliprect.

    :param struct vmw_kms_dirty \*dirty:
        The closure structure



.. _`vmw_sou_dmabuf_clip.description`:

Description
-----------

Encodes a BLIT_GMRFB_TO_SCREEN cliprect.



.. _`vmw_kms_sou_do_dmabuf_dirty`:

vmw_kms_sou_do_dmabuf_dirty
===========================

.. c:function:: int vmw_kms_sou_do_dmabuf_dirty (struct vmw_private *dev_priv, struct vmw_framebuffer *framebuffer, struct drm_clip_rect *clips, struct drm_vmw_rect *vclips, unsigned num_clips, int increment, bool interruptible, struct vmw_fence_obj **out_fence)

    Dirty part of a dma-buffer backed framebuffer

    :param struct vmw_private \*dev_priv:
        Pointer to the device private structure.

    :param struct vmw_framebuffer \*framebuffer:
        Pointer to the dma-buffer backed framebuffer.

    :param struct drm_clip_rect \*clips:
        Array of clip rects.

    :param struct drm_vmw_rect \*vclips:
        Alternate array of clip rects. Either ``clips`` or ``vclips`` must
        be NULL.

    :param unsigned num_clips:
        Number of clip rects in ``clips``\ .

    :param int increment:
        Increment to use when looping over ``clips``\ .

    :param bool interruptible:
        Whether to perform waits interruptible if possible.

    :param struct vmw_fence_obj \*\*out_fence:
        If non-NULL, will return a ref-counted pointer to a
        struct vmw_fence_obj. The returned fence pointer may be NULL in which
        case the device has already synchronized.



.. _`vmw_kms_sou_do_dmabuf_dirty.description`:

Description
-----------

Returns 0 on success, negative error code on failure. -ERESTARTSYS if
interrupted.



.. _`vmw_sou_readback_fifo_commit`:

vmw_sou_readback_fifo_commit
============================

.. c:function:: void vmw_sou_readback_fifo_commit (struct vmw_kms_dirty *dirty)

    Callback to submit a set of readback clips.

    :param struct vmw_kms_dirty \*dirty:
        The closure structure.



.. _`vmw_sou_readback_fifo_commit.description`:

Description
-----------

Commits a previously built command buffer of readback clips.



.. _`vmw_sou_readback_clip`:

vmw_sou_readback_clip
=====================

.. c:function:: void vmw_sou_readback_clip (struct vmw_kms_dirty *dirty)

    Callback to encode a readback cliprect.

    :param struct vmw_kms_dirty \*dirty:
        The closure structure



.. _`vmw_sou_readback_clip.description`:

Description
-----------

Encodes a BLIT_SCREEN_TO_GMRFB cliprect.



.. _`vmw_kms_sou_readback`:

vmw_kms_sou_readback
====================

.. c:function:: int vmw_kms_sou_readback (struct vmw_private *dev_priv, struct drm_file *file_priv, struct vmw_framebuffer *vfb, struct drm_vmw_fence_rep __user *user_fence_rep, struct drm_vmw_rect *vclips, uint32_t num_clips)

    Perform a readback from the screen object system to a dma-buffer backed framebuffer.

    :param struct vmw_private \*dev_priv:
        Pointer to the device private structure.

    :param struct drm_file \*file_priv:
        Pointer to a struct drm_file identifying the caller.
        Must be set to NULL if ``user_fence_rep`` is NULL.

    :param struct vmw_framebuffer \*vfb:
        Pointer to the dma-buffer backed framebuffer.

    :param struct drm_vmw_fence_rep __user \*user_fence_rep:
        User-space provided structure for fence information.
        Must be set to non-NULL if ``file_priv`` is non-NULL.

    :param struct drm_vmw_rect \*vclips:
        Array of clip rects.

    :param uint32_t num_clips:
        Number of clip rects in ``vclips``\ .



.. _`vmw_kms_sou_readback.description`:

Description
-----------

Returns 0 on success, negative error code on failure. -ERESTARTSYS if
interrupted.

