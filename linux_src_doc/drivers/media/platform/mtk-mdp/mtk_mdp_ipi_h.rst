.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/mtk-mdp/mtk_mdp_ipi.h

.. _`mdp_ipi_init`:

struct mdp_ipi_init
===================

.. c:type:: struct mdp_ipi_init

    for AP_MDP_INIT

.. _`mdp_ipi_init.definition`:

Definition
----------

.. code-block:: c

    struct mdp_ipi_init {
        uint32_t msg_id;
        uint32_t ipi_id;
        uint64_t ap_inst;
    }

.. _`mdp_ipi_init.members`:

Members
-------

msg_id
    AP_MDP_INIT

ipi_id
    IPI_MDP

ap_inst
    AP mtk_mdp_vpu address

.. _`mdp_ipi_comm`:

struct mdp_ipi_comm
===================

.. c:type:: struct mdp_ipi_comm

    for AP_MDP_PROCESS, AP_MDP_DEINIT

.. _`mdp_ipi_comm.definition`:

Definition
----------

.. code-block:: c

    struct mdp_ipi_comm {
        uint32_t msg_id;
        uint32_t ipi_id;
        uint64_t ap_inst;
        uint32_t vpu_inst_addr;
    }

.. _`mdp_ipi_comm.members`:

Members
-------

msg_id
    AP_MDP_PROCESS, AP_MDP_DEINIT

ipi_id
    IPI_MDP

ap_inst
    AP mtk_mdp_vpu address

vpu_inst_addr
    VPU MDP instance address

.. _`mdp_ipi_comm_ack`:

struct mdp_ipi_comm_ack
=======================

.. c:type:: struct mdp_ipi_comm_ack

    for VPU_MDP_DEINIT_ACK, VPU_MDP_PROCESS_ACK

.. _`mdp_ipi_comm_ack.definition`:

Definition
----------

.. code-block:: c

    struct mdp_ipi_comm_ack {
        uint32_t msg_id;
        uint32_t ipi_id;
        uint64_t ap_inst;
        uint32_t vpu_inst_addr;
        int32_t status;
    }

.. _`mdp_ipi_comm_ack.members`:

Members
-------

msg_id
    VPU_MDP_DEINIT_ACK, VPU_MDP_PROCESS_ACK

ipi_id
    IPI_MDP

ap_inst
    AP mtk_mdp_vpu address

vpu_inst_addr
    VPU MDP instance address

status
    VPU exeuction result

.. _`mdp_config`:

struct mdp_config
=================

.. c:type:: struct mdp_config

    configured for source/destination image

.. _`mdp_config.definition`:

Definition
----------

.. code-block:: c

    struct mdp_config {
        int32_t x;
        int32_t y;
        int32_t w;
        int32_t h;
        int32_t w_stride;
        int32_t h_stride;
        int32_t crop_x;
        int32_t crop_y;
        int32_t crop_w;
        int32_t crop_h;
        int32_t format;
    }

.. _`mdp_config.members`:

Members
-------

x
    left

y
    top

w
    width

h
    height

w_stride
    bytes in horizontal

h_stride
    bytes in vertical

crop_x
    cropped left

crop_y
    cropped top

crop_w
    cropped width

crop_h
    cropped height

format
    color format

.. This file was automatic generated / don't edit.

