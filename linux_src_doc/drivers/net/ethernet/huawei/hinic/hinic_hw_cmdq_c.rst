.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/huawei/hinic/hinic_hw_cmdq.c

.. _`hinic_alloc_cmdq_buf`:

hinic_alloc_cmdq_buf
====================

.. c:function:: int hinic_alloc_cmdq_buf(struct hinic_cmdqs *cmdqs, struct hinic_cmdq_buf *cmdq_buf)

    alloc buffer for sending command

    :param cmdqs:
        the cmdqs
    :type cmdqs: struct hinic_cmdqs \*

    :param cmdq_buf:
        the buffer returned in this struct
    :type cmdq_buf: struct hinic_cmdq_buf \*

.. _`hinic_alloc_cmdq_buf.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_free_cmdq_buf`:

hinic_free_cmdq_buf
===================

.. c:function:: void hinic_free_cmdq_buf(struct hinic_cmdqs *cmdqs, struct hinic_cmdq_buf *cmdq_buf)

    free buffer

    :param cmdqs:
        the cmdqs
    :type cmdqs: struct hinic_cmdqs \*

    :param cmdq_buf:
        the buffer to free that is in this struct
    :type cmdq_buf: struct hinic_cmdq_buf \*

.. _`hinic_cmdq_direct_resp`:

hinic_cmdq_direct_resp
======================

.. c:function:: int hinic_cmdq_direct_resp(struct hinic_cmdqs *cmdqs, enum hinic_mod_type mod, u8 cmd, struct hinic_cmdq_buf *buf_in, u64 *resp)

    send command with direct data as resp

    :param cmdqs:
        the cmdqs
    :type cmdqs: struct hinic_cmdqs \*

    :param mod:
        module on the card that will handle the command
    :type mod: enum hinic_mod_type

    :param cmd:
        the command
    :type cmd: u8

    :param buf_in:
        the buffer for the command
    :type buf_in: struct hinic_cmdq_buf \*

    :param resp:
        the response to return
    :type resp: u64 \*

.. _`hinic_cmdq_direct_resp.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_set_arm_bit`:

hinic_set_arm_bit
=================

.. c:function:: int hinic_set_arm_bit(struct hinic_cmdqs *cmdqs, enum hinic_set_arm_qtype q_type, u32 q_id)

    set arm bit for enable interrupt again

    :param cmdqs:
        the cmdqs
    :type cmdqs: struct hinic_cmdqs \*

    :param q_type:
        type of queue to set the arm bit for
    :type q_type: enum hinic_set_arm_qtype

    :param q_id:
        the queue number
    :type q_id: u32

.. _`hinic_set_arm_bit.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`cmdq_arm_ceq_handler`:

cmdq_arm_ceq_handler
====================

.. c:function:: int cmdq_arm_ceq_handler(struct hinic_cmdq *cmdq, struct hinic_cmdq_wqe *wqe)

    cmdq completion event handler for arm command

    :param cmdq:
        the cmdq of the arm command
    :type cmdq: struct hinic_cmdq \*

    :param wqe:
        the wqe of the arm command
    :type wqe: struct hinic_cmdq_wqe \*

.. _`cmdq_arm_ceq_handler.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`cmdq_sync_cmd_handler`:

cmdq_sync_cmd_handler
=====================

.. c:function:: void cmdq_sync_cmd_handler(struct hinic_cmdq *cmdq, u16 cons_idx, int errcode)

    cmdq completion event handler for sync command

    :param cmdq:
        the cmdq of the command
    :type cmdq: struct hinic_cmdq \*

    :param cons_idx:
        the consumer index to update the error code for
    :type cons_idx: u16

    :param errcode:
        the error code
    :type errcode: int

.. _`cmdq_ceq_handler`:

cmdq_ceq_handler
================

.. c:function:: void cmdq_ceq_handler(void *handle, u32 ceqe_data)

    cmdq completion event handler

    :param handle:
        private data for the handler(cmdqs)
    :type handle: void \*

    :param ceqe_data:
        ceq element data
    :type ceqe_data: u32

.. _`cmdq_init_queue_ctxt`:

cmdq_init_queue_ctxt
====================

.. c:function:: void cmdq_init_queue_ctxt(struct hinic_cmdq_ctxt *cmdq_ctxt, struct hinic_cmdq *cmdq, struct hinic_cmdq_pages *cmdq_pages)

    init the queue ctxt of a cmdq

    :param cmdq_ctxt:
        cmdq ctxt to initialize
    :type cmdq_ctxt: struct hinic_cmdq_ctxt \*

    :param cmdq:
        the cmdq
    :type cmdq: struct hinic_cmdq \*

    :param cmdq_pages:
        the memory of the queue
    :type cmdq_pages: struct hinic_cmdq_pages \*

.. _`init_cmdq`:

init_cmdq
=========

.. c:function:: int init_cmdq(struct hinic_cmdq *cmdq, struct hinic_wq *wq, enum hinic_cmdq_type q_type, void __iomem *db_area)

    initialize cmdq

    :param cmdq:
        the cmdq
    :type cmdq: struct hinic_cmdq \*

    :param wq:
        the wq attaced to the cmdq
    :type wq: struct hinic_wq \*

    :param q_type:
        the cmdq type of the cmdq
    :type q_type: enum hinic_cmdq_type

    :param db_area:
        doorbell area for the cmdq
    :type db_area: void __iomem \*

.. _`init_cmdq.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`free_cmdq`:

free_cmdq
=========

.. c:function:: void free_cmdq(struct hinic_cmdq *cmdq)

    Free cmdq

    :param cmdq:
        the cmdq to free
    :type cmdq: struct hinic_cmdq \*

.. _`init_cmdqs_ctxt`:

init_cmdqs_ctxt
===============

.. c:function:: int init_cmdqs_ctxt(struct hinic_hwdev *hwdev, struct hinic_cmdqs *cmdqs, void __iomem **db_area)

    write the cmdq ctxt to HW after init all cmdq

    :param hwdev:
        the NIC HW device
    :type hwdev: struct hinic_hwdev \*

    :param cmdqs:
        cmdqs to write the ctxts for
        \ :c:type:`struct db_area <db_area>`\ : db_area for all the cmdqs
    :type cmdqs: struct hinic_cmdqs \*

    :param db_area:
        *undescribed*
    :type db_area: void __iomem \*\*

.. _`init_cmdqs_ctxt.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_init_cmdqs`:

hinic_init_cmdqs
================

.. c:function:: int hinic_init_cmdqs(struct hinic_cmdqs *cmdqs, struct hinic_hwif *hwif, void __iomem **db_area)

    init all cmdqs

    :param cmdqs:
        cmdqs to init
    :type cmdqs: struct hinic_cmdqs \*

    :param hwif:
        HW interface for accessing cmdqs
    :type hwif: struct hinic_hwif \*

    :param db_area:
        doorbell areas for all the cmdqs
    :type db_area: void __iomem \*\*

.. _`hinic_init_cmdqs.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_free_cmdqs`:

hinic_free_cmdqs
================

.. c:function:: void hinic_free_cmdqs(struct hinic_cmdqs *cmdqs)

    free all cmdqs

    :param cmdqs:
        cmdqs to free
    :type cmdqs: struct hinic_cmdqs \*

.. This file was automatic generated / don't edit.

