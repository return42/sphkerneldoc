.. -*- coding: utf-8; mode: rst -*-

=============
gma_display.c
=============


.. _`gma_pipe_has_type`:

gma_pipe_has_type
=================

.. c:function:: bool gma_pipe_has_type (struct drm_crtc *crtc, int type)

    :param struct drm_crtc \*crtc:

        *undescribed*

    :param int type:

        *undescribed*



.. _`gma_crtc_dpms`:

gma_crtc_dpms
=============

.. c:function:: void gma_crtc_dpms (struct drm_crtc *crtc, int mode)

    :param struct drm_crtc \*crtc:

        *undescribed*

    :param int mode:

        *undescribed*



.. _`gma_crtc_dpms.description`:

Description
-----------


This code should probably grow support for turning the cursor off and back
on appropriately at the same time as we're turning the pipe off/on.



.. _`gma_crtc_save`:

gma_crtc_save
=============

.. c:function:: void gma_crtc_save (struct drm_crtc *crtc)

    :param struct drm_crtc \*crtc:

        *undescribed*



.. _`gma_crtc_restore`:

gma_crtc_restore
================

.. c:function:: void gma_crtc_restore (struct drm_crtc *crtc)

    :param struct drm_crtc \*crtc:

        *undescribed*

