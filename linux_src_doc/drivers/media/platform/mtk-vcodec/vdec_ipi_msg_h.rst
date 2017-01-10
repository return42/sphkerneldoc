.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/mtk-vcodec/vdec_ipi_msg.h

.. _`vdec_ipi_msgid`:

enum vdec_ipi_msgid
===================

.. c:type:: enum vdec_ipi_msgid

    message id between AP and VPU

.. _`vdec_ipi_msgid.definition`:

Definition
----------

.. code-block:: c

    enum vdec_ipi_msgid {
        AP_IPIMSG_DEC_INIT,
        AP_IPIMSG_DEC_START,
        AP_IPIMSG_DEC_END,
        AP_IPIMSG_DEC_DEINIT,
        AP_IPIMSG_DEC_RESET,
        VPU_IPIMSG_DEC_INIT_ACK,
        VPU_IPIMSG_DEC_START_ACK,
        VPU_IPIMSG_DEC_END_ACK,
        VPU_IPIMSG_DEC_DEINIT_ACK,
        VPU_IPIMSG_DEC_RESET_ACK
    };

.. _`vdec_ipi_msgid.constants`:

Constants
---------

AP_IPIMSG_DEC_INIT
    *undescribed*

AP_IPIMSG_DEC_START
    *undescribed*

AP_IPIMSG_DEC_END
    *undescribed*

AP_IPIMSG_DEC_DEINIT
    *undescribed*

AP_IPIMSG_DEC_RESET
    *undescribed*

VPU_IPIMSG_DEC_INIT_ACK
    *undescribed*

VPU_IPIMSG_DEC_START_ACK
    *undescribed*

VPU_IPIMSG_DEC_END_ACK
    *undescribed*

VPU_IPIMSG_DEC_DEINIT_ACK
    *undescribed*

VPU_IPIMSG_DEC_RESET_ACK
    *undescribed*

.. _`vdec_ap_ipi_cmd`:

struct vdec_ap_ipi_cmd
======================

.. c:type:: struct vdec_ap_ipi_cmd

    generic AP to VPU ipi command format

.. _`vdec_ap_ipi_cmd.definition`:

Definition
----------

.. code-block:: c

    struct vdec_ap_ipi_cmd {
        uint32_t msg_id;
        uint32_t vpu_inst_addr;
    }

.. _`vdec_ap_ipi_cmd.members`:

Members
-------

msg_id
    vdec_ipi_msgid

vpu_inst_addr
    VPU decoder instance address

.. _`vdec_vpu_ipi_ack`:

struct vdec_vpu_ipi_ack
=======================

.. c:type:: struct vdec_vpu_ipi_ack

    generic VPU to AP ipi command format

.. _`vdec_vpu_ipi_ack.definition`:

Definition
----------

.. code-block:: c

    struct vdec_vpu_ipi_ack {
        uint32_t msg_id;
        int32_t status;
        uint64_t ap_inst_addr;
    }

.. _`vdec_vpu_ipi_ack.members`:

Members
-------

msg_id
    vdec_ipi_msgid

status
    VPU exeuction result

ap_inst_addr
    AP video decoder instance address

.. _`vdec_ap_ipi_init`:

struct vdec_ap_ipi_init
=======================

.. c:type:: struct vdec_ap_ipi_init

    for AP_IPIMSG_DEC_INIT

.. _`vdec_ap_ipi_init.definition`:

Definition
----------

.. code-block:: c

    struct vdec_ap_ipi_init {
        uint32_t msg_id;
        uint32_t reserved;
        uint64_t ap_inst_addr;
    }

.. _`vdec_ap_ipi_init.members`:

Members
-------

msg_id
    AP_IPIMSG_DEC_INIT

reserved
    Reserved field

ap_inst_addr
    AP video decoder instance address

.. _`vdec_ap_ipi_dec_start`:

struct vdec_ap_ipi_dec_start
============================

.. c:type:: struct vdec_ap_ipi_dec_start

    for AP_IPIMSG_DEC_START

.. _`vdec_ap_ipi_dec_start.definition`:

Definition
----------

.. code-block:: c

    struct vdec_ap_ipi_dec_start {
        uint32_t msg_id;
        uint32_t vpu_inst_addr;
        uint32_t data[3];
        uint32_t reserved;
    }

.. _`vdec_ap_ipi_dec_start.members`:

Members
-------

msg_id
    AP_IPIMSG_DEC_START

vpu_inst_addr
    VPU decoder instance address

data
    Header info
    H264 decoder [0]:buf_sz [1]:nal_start
    VP8 decoder  [0]:width/height
    VP9 decoder  [0]:profile, [1][2] width/height

reserved
    Reserved field

.. _`vdec_vpu_ipi_init_ack`:

struct vdec_vpu_ipi_init_ack
============================

.. c:type:: struct vdec_vpu_ipi_init_ack

    for VPU_IPIMSG_DEC_INIT_ACK

.. _`vdec_vpu_ipi_init_ack.definition`:

Definition
----------

.. code-block:: c

    struct vdec_vpu_ipi_init_ack {
        uint32_t msg_id;
        int32_t status;
        uint64_t ap_inst_addr;
        uint32_t vpu_inst_addr;
    }

.. _`vdec_vpu_ipi_init_ack.members`:

Members
-------

msg_id
    VPU_IPIMSG_DEC_INIT_ACK

status
    VPU exeuction result

ap_inst_addr
    AP vcodec_vpu_inst instance address

vpu_inst_addr
    VPU decoder instance address

.. This file was automatic generated / don't edit.

