.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/mediatek/mtk_drm_crtc.c

.. _`mtk_drm_crtc`:

struct mtk_drm_crtc
===================

.. c:type:: struct mtk_drm_crtc

    MediaTek specific crtc structure.

.. _`mtk_drm_crtc.definition`:

Definition
----------

.. code-block:: c

    struct mtk_drm_crtc {
        struct drm_crtc base;
        bool enabled;
        bool pending_needs_vblank;
        struct drm_pending_vblank_event *event;
        struct mtk_drm_plane planes[OVL_LAYER_NR];
        bool pending_planes;
        void __iomem *config_regs;
        struct mtk_disp_mutex *mutex;
        unsigned int ddp_comp_nr;
        struct mtk_ddp_comp **ddp_comp;
    }

.. _`mtk_drm_crtc.members`:

Members
-------

base
    crtc object.

enabled
    records whether crtc_enable succeeded

pending_needs_vblank
    *undescribed*

event
    *undescribed*

planes
    array of 4 mtk_drm_plane structures, one for each overlay plane

pending_planes
    whether any plane has pending changes to be applied

config_regs
    memory mapped mmsys configuration register space

mutex
    handle to one of the ten disp_mutex streams

ddp_comp_nr
    number of components in ddp_comp

ddp_comp
    array of pointers the mtk_ddp_comp structures used by this crtc

.. This file was automatic generated / don't edit.

