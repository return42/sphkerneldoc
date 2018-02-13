.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_modeset_helper.c

.. _`aux-kms-helpers`:

aux kms helpers
===============

This helper library contains various one-off functions which don't really fit
anywhere else in the DRM modeset helper library.

.. _`drm_helper_move_panel_connectors_to_head`:

drm_helper_move_panel_connectors_to_head
========================================

.. c:function:: void drm_helper_move_panel_connectors_to_head(struct drm_device *dev)

    move panels to the front in the connector list

    :param struct drm_device \*dev:
        drm device to operate on

.. _`drm_helper_move_panel_connectors_to_head.description`:

Description
-----------

Some userspace presumes that the first connected connector is the main
display, where it's supposed to display e.g. the login screen. For
laptops, this should be the main panel. Use this function to sort all
(eDP/LVDS/DSI) panels to the front of the connector list, instead of
painstakingly trying to initialize them in the right order.

.. _`drm_helper_mode_fill_fb_struct`:

drm_helper_mode_fill_fb_struct
==============================

.. c:function:: void drm_helper_mode_fill_fb_struct(struct drm_device *dev, struct drm_framebuffer *fb, const struct drm_mode_fb_cmd2 *mode_cmd)

    fill out framebuffer metadata

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_framebuffer \*fb:
        drm_framebuffer object to fill out

    :param const struct drm_mode_fb_cmd2 \*mode_cmd:
        metadata from the userspace fb creation request

.. _`drm_helper_mode_fill_fb_struct.description`:

Description
-----------

This helper can be used in a drivers fb_create callback to pre-fill the fb's
metadata fields.

.. _`drm_crtc_init`:

drm_crtc_init
=============

.. c:function:: int drm_crtc_init(struct drm_device *dev, struct drm_crtc *crtc, const struct drm_crtc_funcs *funcs)

    Legacy CRTC initialization function

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_crtc \*crtc:
        CRTC object to init

    :param const struct drm_crtc_funcs \*funcs:
        callbacks for the new CRTC

.. _`drm_crtc_init.description`:

Description
-----------

Initialize a CRTC object with a default helper-provided primary plane and no
cursor plane.

.. _`drm_crtc_init.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_mode_config_helper_suspend`:

drm_mode_config_helper_suspend
==============================

.. c:function:: int drm_mode_config_helper_suspend(struct drm_device *dev)

    Modeset suspend helper

    :param struct drm_device \*dev:
        DRM device

.. _`drm_mode_config_helper_suspend.description`:

Description
-----------

This helper function takes care of suspending the modeset side. It disables
output polling if initialized, suspends fbdev if used and finally calls
\ :c:func:`drm_atomic_helper_suspend`\ .
If suspending fails, fbdev and polling is re-enabled.

.. _`drm_mode_config_helper_suspend.return`:

Return
------

Zero on success, negative error code on error.

.. _`drm_mode_config_helper_suspend.see-also`:

See also
--------

\ :c:func:`drm_kms_helper_poll_disable`\  and \ :c:func:`drm_fb_helper_set_suspend_unlocked`\ .

.. _`drm_mode_config_helper_resume`:

drm_mode_config_helper_resume
=============================

.. c:function:: int drm_mode_config_helper_resume(struct drm_device *dev)

    Modeset resume helper

    :param struct drm_device \*dev:
        DRM device

.. _`drm_mode_config_helper_resume.description`:

Description
-----------

This helper function takes care of resuming the modeset side. It calls
\ :c:func:`drm_atomic_helper_resume`\ , resumes fbdev if used and enables output polling
if initiaized.

.. _`drm_mode_config_helper_resume.return`:

Return
------

Zero on success, negative error code on error.

.. _`drm_mode_config_helper_resume.see-also`:

See also
--------

\ :c:func:`drm_fb_helper_set_suspend_unlocked`\  and \ :c:func:`drm_kms_helper_poll_enable`\ .

.. This file was automatic generated / don't edit.

