.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_kms.h

.. _`vmw_kms_dirty`:

struct vmw_kms_dirty
====================

.. c:type:: struct vmw_kms_dirty

    closure structure for the vmw_kms_helper_dirty function.

.. _`vmw_kms_dirty.definition`:

Definition
----------

.. code-block:: c

    struct vmw_kms_dirty {
        void (* fifo_commit) (struct vmw_kms_dirty *);
        void (* clip) (struct vmw_kms_dirty *);
        size_t fifo_reserve_size;
        struct vmw_private *dev_priv;
        struct vmw_display_unit *unit;
        void *cmd;
        u32 num_hits;
        s32 fb_x;
        s32 fb_y;
        s32 unit_x1;
        s32 unit_y1;
        s32 unit_x2;
        s32 unit_y2;
    }

.. _`vmw_kms_dirty.members`:

Members
-------

fifo_commit
    Callback that is called once for each display unit after
    all clip rects. This function must commit the fifo space reserved by the
    helper. Set up by the caller.

clip
    Callback that is called for each cliprect on each display unit.
    Set up by the caller.

fifo_reserve_size
    Fifo size that the helper should try to allocat for
    each display unit. Set up by the caller.

dev_priv
    Pointer to the device private. Set up by the helper.

unit
    The current display unit. Set up by the helper before a call to \ ``clip``\ .

cmd
    The allocated fifo space. Set up by the helper before the first \ ``clip``\ 
    call.

num_hits
    Number of clip rect commands for this display unit.
    Cleared by the helper before the first \ ``clip``\  call. Updated by the \ ``clip``\ 
    callback.

fb_x
    Clip rect left side in framebuffer coordinates.

fb_y
    Clip rect right side in framebuffer coordinates.

unit_x1
    Clip rect left side in crtc coordinates.

unit_y1
    Clip rect top side in crtc coordinates.

unit_x2
    Clip rect right side in crtc coordinates.

unit_y2
    Clip rect bottom side in crtc coordinates.

.. _`vmw_kms_dirty.description`:

Description
-----------

The clip rect coordinates are updated by the helper for each \ ``clip``\  call.
Note that this may be derived from if more info needs to be passed between
helper caller and helper callbacks.

.. This file was automatic generated / don't edit.

