.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/nouveau/dispnv04/crtc.c

.. _`nv_crtc_mode_set_regs`:

nv_crtc_mode_set_regs
=====================

.. c:function:: void nv_crtc_mode_set_regs(struct drm_crtc *crtc, struct drm_display_mode *mode)

    :param crtc:
        *undescribed*
    :type crtc: struct drm_crtc \*

    :param mode:
        *undescribed*
    :type mode: struct drm_display_mode \*

.. _`nv_crtc_mode_set_regs.description`:

Description
-----------

The clocks, CRTCs and outputs attached to this CRTC must be off.

This shouldn't enable any clocks, CRTCs, or outputs, but they should
be easily turned on/off after this.

.. _`nv_crtc_mode_set`:

nv_crtc_mode_set
================

.. c:function:: int nv_crtc_mode_set(struct drm_crtc *crtc, struct drm_display_mode *mode, struct drm_display_mode *adjusted_mode, int x, int y, struct drm_framebuffer *old_fb)

    :param crtc:
        *undescribed*
    :type crtc: struct drm_crtc \*

    :param mode:
        *undescribed*
    :type mode: struct drm_display_mode \*

    :param adjusted_mode:
        *undescribed*
    :type adjusted_mode: struct drm_display_mode \*

    :param x:
        *undescribed*
    :type x: int

    :param y:
        *undescribed*
    :type y: int

    :param old_fb:
        *undescribed*
    :type old_fb: struct drm_framebuffer \*

.. _`nv_crtc_mode_set.description`:

Description
-----------

The clocks, CRTCs and outputs attached to this CRTC must be off.

This shouldn't enable any clocks, CRTCs, or outputs, but they should
be easily turned on/off after this.

.. This file was automatic generated / don't edit.

