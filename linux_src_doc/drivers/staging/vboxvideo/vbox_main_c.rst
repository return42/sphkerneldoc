.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/vboxvideo/vbox_main.c

.. _`vbox_framebuffer_dirty_rectangles`:

vbox_framebuffer_dirty_rectangles
=================================

.. c:function:: void vbox_framebuffer_dirty_rectangles(struct drm_framebuffer *fb, struct drm_clip_rect *rects, unsigned int num_rects)

    VBVA first, as this is normally disabled after a change of master in case the new master does not send dirty rectangle information (is this even allowed?)

    :param fb:
        *undescribed*
    :type fb: struct drm_framebuffer \*

    :param rects:
        *undescribed*
    :type rects: struct drm_clip_rect \*

    :param num_rects:
        *undescribed*
    :type num_rects: unsigned int

.. _`vbox_hw_init`:

vbox_hw_init
============

.. c:function:: int vbox_hw_init(struct vbox_private *vbox)

    to the memory manager.

    :param vbox:
        *undescribed*
    :type vbox: struct vbox_private \*

.. This file was automatic generated / don't edit.

