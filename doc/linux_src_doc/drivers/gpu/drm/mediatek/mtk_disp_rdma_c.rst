.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/mediatek/mtk_disp_rdma.c

.. _`mtk_disp_rdma`:

struct mtk_disp_rdma
====================

.. c:type:: struct mtk_disp_rdma

    DISP_RDMA driver structure \ ``ddp_comp``\  - structure containing type enum and hardware resources \ ``crtc``\  - associated crtc to report irq events to

.. _`mtk_disp_rdma.definition`:

Definition
----------

.. code-block:: c

    struct mtk_disp_rdma {
        struct mtk_ddp_comp ddp_comp;
        struct drm_crtc *crtc;
    }

.. _`mtk_disp_rdma.members`:

Members
-------

ddp_comp
    *undescribed*

crtc
    *undescribed*

.. This file was automatic generated / don't edit.

