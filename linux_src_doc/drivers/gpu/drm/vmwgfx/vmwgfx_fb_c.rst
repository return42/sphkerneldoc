.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_fb.c

.. _`vmw_fb_dirty_flush`:

vmw_fb_dirty_flush
==================

.. c:function:: void vmw_fb_dirty_flush(struct work_struct *work)

    flush dirty regions to the kms framebuffer

    :param struct work_struct \*work:
        The struct work_struct associated with this task.

.. _`vmw_fb_dirty_flush.description`:

Description
-----------

This function flushes the dirty regions of the vmalloc framebuffer to the
kms framebuffer, and if the kms framebuffer is visible, also updated the
corresponding displays. Note that this function runs even if the kms
framebuffer is not bound to a crtc and thus not visible, but it's turned
off during hibernation using the par->dirty.active bool.

.. This file was automatic generated / don't edit.

