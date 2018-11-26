.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/gma500/gma_display.c

.. _`gma_pipe_has_type`:

gma_pipe_has_type
=================

.. c:function:: bool gma_pipe_has_type(struct drm_crtc *crtc, int type)

    :param crtc:
        *undescribed*
    :type crtc: struct drm_crtc \*

    :param type:
        *undescribed*
    :type type: int

.. _`gma_crtc_dpms`:

gma_crtc_dpms
=============

.. c:function:: void gma_crtc_dpms(struct drm_crtc *crtc, int mode)

    :param crtc:
        *undescribed*
    :type crtc: struct drm_crtc \*

    :param mode:
        *undescribed*
    :type mode: int

.. _`gma_crtc_dpms.description`:

Description
-----------

This code should probably grow support for turning the cursor off and back
on appropriately at the same time as we're turning the pipe off/on.

.. _`gma_crtc_save`:

gma_crtc_save
=============

.. c:function:: void gma_crtc_save(struct drm_crtc *crtc)

    :param crtc:
        *undescribed*
    :type crtc: struct drm_crtc \*

.. _`gma_crtc_restore`:

gma_crtc_restore
================

.. c:function:: void gma_crtc_restore(struct drm_crtc *crtc)

    :param crtc:
        *undescribed*
    :type crtc: struct drm_crtc \*

.. This file was automatic generated / don't edit.

