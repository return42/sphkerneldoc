.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/mtk-vcodec/venc/venc_h264_if.c

.. _`venc_h264_vpu_work_buf`:

enum venc_h264_vpu_work_buf
===========================

.. c:type:: enum venc_h264_vpu_work_buf

    h264 encoder buffer index

.. _`venc_h264_vpu_work_buf.definition`:

Definition
----------

.. code-block:: c

    enum venc_h264_vpu_work_buf {
        VENC_H264_VPU_WORK_BUF_RC_INFO,
        VENC_H264_VPU_WORK_BUF_RC_CODE,
        VENC_H264_VPU_WORK_BUF_REC_LUMA,
        VENC_H264_VPU_WORK_BUF_REC_CHROMA,
        VENC_H264_VPU_WORK_BUF_REF_LUMA,
        VENC_H264_VPU_WORK_BUF_REF_CHROMA,
        VENC_H264_VPU_WORK_BUF_MV_INFO_1,
        VENC_H264_VPU_WORK_BUF_MV_INFO_2,
        VENC_H264_VPU_WORK_BUF_SKIP_FRAME,
        VENC_H264_VPU_WORK_BUF_MAX
    };

.. _`venc_h264_vpu_work_buf.constants`:

Constants
---------

VENC_H264_VPU_WORK_BUF_RC_INFO
    *undescribed*

VENC_H264_VPU_WORK_BUF_RC_CODE
    *undescribed*

VENC_H264_VPU_WORK_BUF_REC_LUMA
    *undescribed*

VENC_H264_VPU_WORK_BUF_REC_CHROMA
    *undescribed*

VENC_H264_VPU_WORK_BUF_REF_LUMA
    *undescribed*

VENC_H264_VPU_WORK_BUF_REF_CHROMA
    *undescribed*

VENC_H264_VPU_WORK_BUF_MV_INFO_1
    *undescribed*

VENC_H264_VPU_WORK_BUF_MV_INFO_2
    *undescribed*

VENC_H264_VPU_WORK_BUF_SKIP_FRAME
    *undescribed*

VENC_H264_VPU_WORK_BUF_MAX
    *undescribed*

.. _`venc_h264_bs_mode`:

enum venc_h264_bs_mode
======================

.. c:type:: enum venc_h264_bs_mode

    for bs_mode argument in h264_enc_vpu_encode

.. _`venc_h264_bs_mode.definition`:

Definition
----------

.. code-block:: c

    enum venc_h264_bs_mode {
        H264_BS_MODE_SPS,
        H264_BS_MODE_PPS,
        H264_BS_MODE_FRAME
    };

.. _`venc_h264_bs_mode.constants`:

Constants
---------

H264_BS_MODE_SPS
    *undescribed*

H264_BS_MODE_PPS
    *undescribed*

H264_BS_MODE_FRAME
    *undescribed*

.. This file was automatic generated / don't edit.

