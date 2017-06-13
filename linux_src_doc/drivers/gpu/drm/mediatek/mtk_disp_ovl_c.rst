.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/mediatek/mtk_disp_ovl.c

.. _`mtk_disp_ovl`:

struct mtk_disp_ovl
===================

.. c:type:: struct mtk_disp_ovl

    DISP_OVL driver structure \ ``ddp_comp``\  - structure containing type enum and hardware resources \ ``crtc``\  - associated crtc to report vblank events to

.. _`mtk_disp_ovl.definition`:

Definition
----------

.. code-block:: c

    struct mtk_disp_ovl {
        struct mtk_ddp_comp ddp_comp;
        struct drm_crtc *crtc;
        const struct mtk_disp_ovl_data *data;
    }

.. _`mtk_disp_ovl.members`:

Members
-------

ddp_comp
    *undescribed*

crtc
    *undescribed*

data
    *undescribed*

.. This file was automatic generated / don't edit.

