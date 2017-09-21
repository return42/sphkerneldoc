.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/mediatek/mtk_disp_color.c

.. _`mtk_disp_color`:

struct mtk_disp_color
=====================

.. c:type:: struct mtk_disp_color

    DISP_COLOR driver structure \ ``ddp_comp``\  - structure containing type enum and hardware resources \ ``crtc``\  - associated crtc to report irq events to

.. _`mtk_disp_color.definition`:

Definition
----------

.. code-block:: c

    struct mtk_disp_color {
        struct mtk_ddp_comp ddp_comp;
        struct drm_crtc *crtc;
        const struct mtk_disp_color_data *data;
    }

.. _`mtk_disp_color.members`:

Members
-------

ddp_comp
    *undescribed*

crtc
    *undescribed*

data
    *undescribed*

.. This file was automatic generated / don't edit.

