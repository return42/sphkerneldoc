.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_cursor.c

.. _`radeon_cursor_reset`:

radeon_cursor_reset
===================

.. c:function:: void radeon_cursor_reset(struct drm_crtc *crtc)

    Re-set the current cursor, if any.

    :param struct drm_crtc \*crtc:
        drm crtc

.. _`radeon_cursor_reset.description`:

Description
-----------

If the CRTC passed in currently has a cursor assigned, this function
makes sure it's visible.

.. This file was automatic generated / don't edit.

