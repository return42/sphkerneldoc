.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/vboxvideo/vbox_mode.c

.. _`vbox_do_modeset`:

vbox_do_modeset
===============

.. c:function:: void vbox_do_modeset(struct drm_crtc *crtc, const struct drm_display_mode *mode)

    mode set and tell the host we support advanced graphics functions.

    :param struct drm_crtc \*crtc:
        *undescribed*

    :param const struct drm_display_mode \*mode:
        *undescribed*

.. _`vbox_set_edid`:

vbox_set_edid
=============

.. c:function:: void vbox_set_edid(struct drm_connector *connector, int width, int height)

    unique serial number for the virtual monitor to try to persuade Unity that different modes correspond to different monitors and it should not try to force the same resolution on them.

    :param struct drm_connector \*connector:
        *undescribed*

    :param int width:
        *undescribed*

    :param int height:
        *undescribed*

.. _`copy_cursor_image`:

copy_cursor_image
=================

.. c:function:: void copy_cursor_image(u8 *src, u8 *dst, u32 width, u32 height, size_t mask_size)

    does not support ARGB cursors.  The mask is a 1BPP bitmap with the bit set if the corresponding alpha value in the ARGB image is greater than 0xF0.

    :param u8 \*src:
        *undescribed*

    :param u8 \*dst:
        *undescribed*

    :param u32 width:
        *undescribed*

    :param u32 height:
        *undescribed*

    :param size_t mask_size:
        *undescribed*

.. This file was automatic generated / don't edit.

