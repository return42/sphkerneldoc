.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/nouveau/dispnv04/crtc.c

.. _`nv_crtc_mode_set_regs`:

nv_crtc_mode_set_regs
=====================

.. c:function:: void nv_crtc_mode_set_regs(struct drm_crtc *crtc, struct drm_display_mode *mode)

    :param struct drm_crtc \*crtc:
        *undescribed*

    :param struct drm_display_mode \*mode:
        *undescribed*

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

    :param struct drm_crtc \*crtc:
        *undescribed*

    :param struct drm_display_mode \*mode:
        *undescribed*

    :param struct drm_display_mode \*adjusted_mode:
        *undescribed*

    :param int x:
        *undescribed*

    :param int y:
        *undescribed*

    :param struct drm_framebuffer \*old_fb:
        *undescribed*

.. _`nv_crtc_mode_set.description`:

Description
-----------

The clocks, CRTCs and outputs attached to this CRTC must be off.

This shouldn't enable any clocks, CRTCs, or outputs, but they should
be easily turned on/off after this.

.. This file was automatic generated / don't edit.

