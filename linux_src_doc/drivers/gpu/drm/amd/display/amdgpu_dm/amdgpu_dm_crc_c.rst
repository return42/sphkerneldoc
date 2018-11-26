.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/amdgpu_dm/amdgpu_dm_crc.c

.. _`amdgpu_dm_crtc_handle_crc_irq`:

amdgpu_dm_crtc_handle_crc_irq
=============================

.. c:function:: void amdgpu_dm_crtc_handle_crc_irq(struct drm_crtc *crtc)

    Report to DRM the CRC on given CRTC.

    :param crtc:
        DRM CRTC object.
    :type crtc: struct drm_crtc \*

.. _`amdgpu_dm_crtc_handle_crc_irq.description`:

Description
-----------

This function should be called at the end of a vblank, when the fb has been
fully processed through the pipe.

.. This file was automatic generated / don't edit.

