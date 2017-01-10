.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/mtk-vcodec/vdec_vpu_if.h

.. _`vdec_vpu_inst`:

struct vdec_vpu_inst
====================

.. c:type:: struct vdec_vpu_inst

    VPU instance for video codec

.. _`vdec_vpu_inst.definition`:

Definition
----------

.. code-block:: c

    struct vdec_vpu_inst {
        enum ipi_id id;
        void *vsi;
        int32_t failure;
        uint32_t inst_addr;
        unsigned int signaled;
        struct mtk_vcodec_ctx *ctx;
        struct platform_device *dev;
        wait_queue_head_t wq;
        ipi_handler_t handler;
    }

.. _`vdec_vpu_inst.members`:

Members
-------

id
    *undescribed*

vsi
    driver structure allocated by VPU side and shared to AP side
    for control and info share

failure
    VPU execution result status, 0: success, others: fail

inst_addr
    VPU decoder instance address

signaled
    1 - Host has received ack message from VPU, 0 - not received

ctx
    context for v4l2 layer integration

dev
    platform device of VPU

wq
    wait queue to wait VPU message ack

handler
    ipi handler for each decoder

.. _`vpu_dec_init`:

vpu_dec_init
============

.. c:function:: int vpu_dec_init(struct vdec_vpu_inst *vpu)

    init decoder instance and allocate required resource in VPU.

    :param struct vdec_vpu_inst \*vpu:
        instance for vdec_vpu_inst

.. _`vpu_dec_start`:

vpu_dec_start
=============

.. c:function:: int vpu_dec_start(struct vdec_vpu_inst *vpu, uint32_t *data, unsigned int len)

    start decoding, basically the function will be invoked once every frame.

    :param struct vdec_vpu_inst \*vpu:
        instance for vdec_vpu_inst

    :param uint32_t \*data:
        meta data to pass bitstream info to VPU decoder

    :param unsigned int len:
        meta data length

.. _`vpu_dec_end`:

vpu_dec_end
===========

.. c:function:: int vpu_dec_end(struct vdec_vpu_inst *vpu)

    end decoding, basically the function will be invoked once when HW decoding done interrupt received successfully. The decoder in VPU will continute to do referene frame management and check if there is a new decoded frame available to display.

    :param struct vdec_vpu_inst \*vpu:
        instance for vdec_vpu_inst

.. _`vpu_dec_deinit`:

vpu_dec_deinit
==============

.. c:function:: int vpu_dec_deinit(struct vdec_vpu_inst *vpu)

    deinit decoder instance and resource freed in VPU.

    :param struct vdec_vpu_inst \*vpu:
        instance for vdec_vpu_inst

.. _`vpu_dec_reset`:

vpu_dec_reset
=============

.. c:function:: int vpu_dec_reset(struct vdec_vpu_inst *vpu)

    reset decoder, use for flush decoder when end of stream or seek. Remainig non displayed frame will be pushed to display.

    :param struct vdec_vpu_inst \*vpu:
        instance for vdec_vpu_inst

.. _`vpu_dec_ipi_handler`:

vpu_dec_ipi_handler
===================

.. c:function:: void vpu_dec_ipi_handler(void *data, unsigned int len, void *priv)

    Handler for VPU ipi message.

    :param void \*data:
        ipi message

    :param unsigned int len:
        length of ipi message

    :param void \*priv:
        callback private data which is passed by decoder when register.

.. This file was automatic generated / don't edit.

