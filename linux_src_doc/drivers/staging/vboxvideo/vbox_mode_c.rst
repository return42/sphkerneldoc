.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/vboxvideo/vbox_mode.c

.. _`vbox_do_modeset`:

vbox_do_modeset
===============

.. c:function:: void vbox_do_modeset(struct drm_crtc *crtc)

    mode set and tell the host we support advanced graphics functions.

    :param crtc:
        *undescribed*
    :type crtc: struct drm_crtc \*

.. _`copy_cursor_image`:

copy_cursor_image
=================

.. c:function:: void copy_cursor_image(u8 *src, u8 *dst, u32 width, u32 height, size_t mask_size)

    does not support ARGB cursors.  The mask is a 1BPP bitmap with the bit set if the corresponding alpha value in the ARGB image is greater than 0xF0.

    :param src:
        *undescribed*
    :type src: u8 \*

    :param dst:
        *undescribed*
    :type dst: u8 \*

    :param width:
        *undescribed*
    :type width: u32

    :param height:
        *undescribed*
    :type height: u32

    :param mask_size:
        *undescribed*
    :type mask_size: size_t

.. _`vbox_set_edid`:

vbox_set_edid
=============

.. c:function:: void vbox_set_edid(struct drm_connector *connector, int width, int height)

    unique serial number for the virtual monitor to try to persuade Unity that different modes correspond to different monitors and it should not try to force the same resolution on them.

    :param connector:
        *undescribed*
    :type connector: struct drm_connector \*

    :param width:
        *undescribed*
    :type width: int

    :param height:
        *undescribed*
    :type height: int

.. This file was automatic generated / don't edit.

