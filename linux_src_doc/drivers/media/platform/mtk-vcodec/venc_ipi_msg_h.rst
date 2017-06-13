.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/mtk-vcodec/venc_ipi_msg.h

.. _`venc_ipi_msg_id`:

enum venc_ipi_msg_id
====================

.. c:type:: enum venc_ipi_msg_id

    message id between AP and VPU (ipi stands for inter-processor interrupt)

.. _`venc_ipi_msg_id.definition`:

Definition
----------

.. code-block:: c

    enum venc_ipi_msg_id {
        AP_IPIMSG_ENC_INIT,
        AP_IPIMSG_ENC_SET_PARAM,
        AP_IPIMSG_ENC_ENCODE,
        AP_IPIMSG_ENC_DEINIT,
        VPU_IPIMSG_ENC_INIT_DONE,
        VPU_IPIMSG_ENC_SET_PARAM_DONE,
        VPU_IPIMSG_ENC_ENCODE_DONE,
        VPU_IPIMSG_ENC_DEINIT_DONE
    };

.. _`venc_ipi_msg_id.constants`:

Constants
---------

AP_IPIMSG_ENC_INIT
    *undescribed*

AP_IPIMSG_ENC_SET_PARAM
    *undescribed*

AP_IPIMSG_ENC_ENCODE
    *undescribed*

AP_IPIMSG_ENC_DEINIT
    *undescribed*

VPU_IPIMSG_ENC_INIT_DONE
    *undescribed*

VPU_IPIMSG_ENC_SET_PARAM_DONE
    *undescribed*

VPU_IPIMSG_ENC_ENCODE_DONE
    *undescribed*

VPU_IPIMSG_ENC_DEINIT_DONE
    *undescribed*

.. _`venc_ap_ipi_msg_init`:

struct venc_ap_ipi_msg_init
===========================

.. c:type:: struct venc_ap_ipi_msg_init

    AP to VPU init cmd structure

.. _`venc_ap_ipi_msg_init.definition`:

Definition
----------

.. code-block:: c

    struct venc_ap_ipi_msg_init {
        uint32_t msg_id;
        uint32_t reserved;
        uint64_t venc_inst;
    }

.. _`venc_ap_ipi_msg_init.members`:

Members
-------

msg_id
    message id (AP_IPIMSG_XXX_ENC_INIT)

reserved
    reserved for future use. vpu is running in 32bit. Without
    this reserved field, if kernel run in 64bit. this struct size
    will be different between kernel and vpu

venc_inst
    AP encoder instance
    (struct venc_vp8_inst/venc_h264_inst \*)

.. _`venc_ap_ipi_msg_set_param`:

struct venc_ap_ipi_msg_set_param
================================

.. c:type:: struct venc_ap_ipi_msg_set_param

    AP to VPU set_param cmd structure

.. _`venc_ap_ipi_msg_set_param.definition`:

Definition
----------

.. code-block:: c

    struct venc_ap_ipi_msg_set_param {
        uint32_t msg_id;
        uint32_t vpu_inst_addr;
        uint32_t param_id;
        uint32_t data_item;
        uint32_t data;
    }

.. _`venc_ap_ipi_msg_set_param.members`:

Members
-------

msg_id
    message id (AP_IPIMSG_XXX_ENC_SET_PARAM)

vpu_inst_addr
    VPU encoder instance addr
    (struct venc_vp8_vsi/venc_h264_vsi \*)

param_id
    parameter id (venc_set_param_type)

data_item
    number of items in the data array

data
    data array to store the set parameters

.. _`venc_ap_ipi_msg_enc`:

struct venc_ap_ipi_msg_enc
==========================

.. c:type:: struct venc_ap_ipi_msg_enc

    AP to VPU enc cmd structure

.. _`venc_ap_ipi_msg_enc.definition`:

Definition
----------

.. code-block:: c

    struct venc_ap_ipi_msg_enc {
        uint32_t msg_id;
        uint32_t vpu_inst_addr;
        uint32_t bs_mode;
        uint32_t input_addr;
        uint32_t bs_addr;
        uint32_t bs_size;
    }

.. _`venc_ap_ipi_msg_enc.members`:

Members
-------

msg_id
    message id (AP_IPIMSG_XXX_ENC_ENCODE)

vpu_inst_addr
    VPU encoder instance addr
    (struct venc_vp8_vsi/venc_h264_vsi \*)

bs_mode
    bitstream mode for h264
    (H264_BS_MODE_SPS/H264_BS_MODE_PPS/H264_BS_MODE_FRAME)

input_addr
    pointer to input image buffer plane

bs_addr
    pointer to output bit stream buffer

bs_size
    bit stream buffer size

.. _`venc_ap_ipi_msg_deinit`:

struct venc_ap_ipi_msg_deinit
=============================

.. c:type:: struct venc_ap_ipi_msg_deinit

    AP to VPU deinit cmd structure

.. _`venc_ap_ipi_msg_deinit.definition`:

Definition
----------

.. code-block:: c

    struct venc_ap_ipi_msg_deinit {
        uint32_t msg_id;
        uint32_t vpu_inst_addr;
    }

.. _`venc_ap_ipi_msg_deinit.members`:

Members
-------

msg_id
    message id (AP_IPIMSG_XXX_ENC_DEINIT)

vpu_inst_addr
    VPU encoder instance addr
    (struct venc_vp8_vsi/venc_h264_vsi \*)

.. _`venc_ipi_msg_status`:

enum venc_ipi_msg_status
========================

.. c:type:: enum venc_ipi_msg_status

    VPU ack AP cmd status

.. _`venc_ipi_msg_status.definition`:

Definition
----------

.. code-block:: c

    enum venc_ipi_msg_status {
        VENC_IPI_MSG_STATUS_OK,
        VENC_IPI_MSG_STATUS_FAIL
    };

.. _`venc_ipi_msg_status.constants`:

Constants
---------

VENC_IPI_MSG_STATUS_OK
    *undescribed*

VENC_IPI_MSG_STATUS_FAIL
    *undescribed*

.. _`venc_vpu_ipi_msg_common`:

struct venc_vpu_ipi_msg_common
==============================

.. c:type:: struct venc_vpu_ipi_msg_common

    VPU ack AP cmd common structure

.. _`venc_vpu_ipi_msg_common.definition`:

Definition
----------

.. code-block:: c

    struct venc_vpu_ipi_msg_common {
        uint32_t msg_id;
        uint32_t status;
        uint64_t venc_inst;
    }

.. _`venc_vpu_ipi_msg_common.members`:

Members
-------

msg_id
    message id (VPU_IPIMSG_XXX_DONE)

status
    cmd status (venc_ipi_msg_status)

venc_inst
    AP encoder instance (struct venc_vp8_inst/venc_h264_inst \*)

.. _`venc_vpu_ipi_msg_init`:

struct venc_vpu_ipi_msg_init
============================

.. c:type:: struct venc_vpu_ipi_msg_init

    VPU ack AP init cmd structure

.. _`venc_vpu_ipi_msg_init.definition`:

Definition
----------

.. code-block:: c

    struct venc_vpu_ipi_msg_init {
        uint32_t msg_id;
        uint32_t status;
        uint64_t venc_inst;
        uint32_t vpu_inst_addr;
        uint32_t reserved;
    }

.. _`venc_vpu_ipi_msg_init.members`:

Members
-------

msg_id
    message id (VPU_IPIMSG_XXX_ENC_SET_PARAM_DONE)

status
    cmd status (venc_ipi_msg_status)

venc_inst
    AP encoder instance (struct venc_vp8_inst/venc_h264_inst \*)

vpu_inst_addr
    VPU encoder instance addr
    (struct venc_vp8_vsi/venc_h264_vsi \*)

reserved
    reserved for future use. vpu is running in 32bit. Without
    this reserved field, if kernel run in 64bit. this struct size
    will be different between kernel and vpu

.. _`venc_vpu_ipi_msg_set_param`:

struct venc_vpu_ipi_msg_set_param
=================================

.. c:type:: struct venc_vpu_ipi_msg_set_param

    VPU ack AP set_param cmd structure

.. _`venc_vpu_ipi_msg_set_param.definition`:

Definition
----------

.. code-block:: c

    struct venc_vpu_ipi_msg_set_param {
        uint32_t msg_id;
        uint32_t status;
        uint64_t venc_inst;
        uint32_t param_id;
        uint32_t data_item;
        uint32_t data;
    }

.. _`venc_vpu_ipi_msg_set_param.members`:

Members
-------

msg_id
    message id (VPU_IPIMSG_XXX_ENC_SET_PARAM_DONE)

status
    cmd status (venc_ipi_msg_status)

venc_inst
    AP encoder instance (struct venc_vp8_inst/venc_h264_inst \*)

param_id
    parameter id (venc_set_param_type)

data_item
    number of items in the data array

data
    data array to store the return result

.. _`venc_ipi_msg_enc_state`:

enum venc_ipi_msg_enc_state
===========================

.. c:type:: enum venc_ipi_msg_enc_state

    Type of encode state

.. _`venc_ipi_msg_enc_state.definition`:

Definition
----------

.. code-block:: c

    enum venc_ipi_msg_enc_state {
        VEN_IPI_MSG_ENC_STATE_FRAME,
        VEN_IPI_MSG_ENC_STATE_PART,
        VEN_IPI_MSG_ENC_STATE_SKIP,
        VEN_IPI_MSG_ENC_STATE_ERROR
    };

.. _`venc_ipi_msg_enc_state.constants`:

Constants
---------

VEN_IPI_MSG_ENC_STATE_FRAME
    *undescribed*

VEN_IPI_MSG_ENC_STATE_PART
    *undescribed*

VEN_IPI_MSG_ENC_STATE_SKIP
    *undescribed*

VEN_IPI_MSG_ENC_STATE_ERROR
    *undescribed*

.. _`venc_ipi_msg_enc_state.ven_ipi_msg_enc_state_frame`:

VEN_IPI_MSG_ENC_STATE_FRAME
---------------------------

one frame being encoded

.. _`venc_ipi_msg_enc_state.ven_ipi_msg_enc_state_part`:

VEN_IPI_MSG_ENC_STATE_PART
--------------------------

bit stream buffer full

.. _`venc_ipi_msg_enc_state.ven_ipi_msg_enc_state_skip`:

VEN_IPI_MSG_ENC_STATE_SKIP
--------------------------

encoded skip frame

.. _`venc_ipi_msg_enc_state.ven_ipi_msg_enc_state_error`:

VEN_IPI_MSG_ENC_STATE_ERROR
---------------------------

encounter error

.. _`venc_vpu_ipi_msg_enc`:

struct venc_vpu_ipi_msg_enc
===========================

.. c:type:: struct venc_vpu_ipi_msg_enc

    VPU ack AP enc cmd structure

.. _`venc_vpu_ipi_msg_enc.definition`:

Definition
----------

.. code-block:: c

    struct venc_vpu_ipi_msg_enc {
        uint32_t msg_id;
        uint32_t status;
        uint64_t venc_inst;
        uint32_t state;
        uint32_t is_key_frm;
        uint32_t bs_size;
        uint32_t reserved;
    }

.. _`venc_vpu_ipi_msg_enc.members`:

Members
-------

msg_id
    message id (VPU_IPIMSG_XXX_ENC_ENCODE_DONE)

status
    cmd status (venc_ipi_msg_status)

venc_inst
    AP encoder instance (struct venc_vp8_inst/venc_h264_inst \*)

state
    encode state (venc_ipi_msg_enc_state)

is_key_frm
    whether the encoded frame is key frame

bs_size
    encoded bitstream size

reserved
    reserved for future use. vpu is running in 32bit. Without
    this reserved field, if kernel run in 64bit. this struct size
    will be different between kernel and vpu

.. _`venc_vpu_ipi_msg_deinit`:

struct venc_vpu_ipi_msg_deinit
==============================

.. c:type:: struct venc_vpu_ipi_msg_deinit

    VPU ack AP deinit cmd structure

.. _`venc_vpu_ipi_msg_deinit.definition`:

Definition
----------

.. code-block:: c

    struct venc_vpu_ipi_msg_deinit {
        uint32_t msg_id;
        uint32_t status;
        uint64_t venc_inst;
    }

.. _`venc_vpu_ipi_msg_deinit.members`:

Members
-------

msg_id
    message id (VPU_IPIMSG_XXX_ENC_DEINIT_DONE)

status
    cmd status (venc_ipi_msg_status)

venc_inst
    AP encoder instance (struct venc_vp8_inst/venc_h264_inst \*)

.. This file was automatic generated / don't edit.

