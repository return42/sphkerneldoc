.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/vboxvideo/vbox_main.c

.. _`vbox_framebuffer_dirty_rectangles`:

vbox_framebuffer_dirty_rectangles
=================================

.. c:function:: void vbox_framebuffer_dirty_rectangles(struct drm_framebuffer *fb, struct drm_clip_rect *rects, unsigned int num_rects)

    VBVA first, as this is normally disabled after a change of master in case the new master does not send dirty rectangle information (is this even allowed?)

    :param struct drm_framebuffer \*fb:
        *undescribed*

    :param struct drm_clip_rect \*rects:
        *undescribed*

    :param unsigned int num_rects:
        *undescribed*

.. _`vbox_hw_init`:

vbox_hw_init
============

.. c:function:: int vbox_hw_init(struct vbox_private *vbox)

    to the memory manager.

    :param struct vbox_private \*vbox:
        *undescribed*

.. This file was automatic generated / don't edit.

