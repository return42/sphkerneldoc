.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/huawei/hinic/hinic_hw_cmdq.c

.. _`hinic_alloc_cmdq_buf`:

hinic_alloc_cmdq_buf
====================

.. c:function:: int hinic_alloc_cmdq_buf(struct hinic_cmdqs *cmdqs, struct hinic_cmdq_buf *cmdq_buf)

    alloc buffer for sending command

    :param struct hinic_cmdqs \*cmdqs:
        the cmdqs

    :param struct hinic_cmdq_buf \*cmdq_buf:
        the buffer returned in this struct

.. _`hinic_alloc_cmdq_buf.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_free_cmdq_buf`:

hinic_free_cmdq_buf
===================

.. c:function:: void hinic_free_cmdq_buf(struct hinic_cmdqs *cmdqs, struct hinic_cmdq_buf *cmdq_buf)

    free buffer

    :param struct hinic_cmdqs \*cmdqs:
        the cmdqs

    :param struct hinic_cmdq_buf \*cmdq_buf:
        the buffer to free that is in this struct

.. _`hinic_cmdq_direct_resp`:

hinic_cmdq_direct_resp
======================

.. c:function:: int hinic_cmdq_direct_resp(struct hinic_cmdqs *cmdqs, enum hinic_mod_type mod, u8 cmd, struct hinic_cmdq_buf *buf_in, u64 *resp)

    send command with direct data as resp

    :param struct hinic_cmdqs \*cmdqs:
        the cmdqs

    :param enum hinic_mod_type mod:
        module on the card that will handle the command

    :param u8 cmd:
        the command

    :param struct hinic_cmdq_buf \*buf_in:
        the buffer for the command

    :param u64 \*resp:
        the response to return

.. _`hinic_cmdq_direct_resp.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_set_arm_bit`:

hinic_set_arm_bit
=================

.. c:function:: int hinic_set_arm_bit(struct hinic_cmdqs *cmdqs, enum hinic_set_arm_qtype q_type, u32 q_id)

    set arm bit for enable interrupt again

    :param struct hinic_cmdqs \*cmdqs:
        the cmdqs

    :param enum hinic_set_arm_qtype q_type:
        type of queue to set the arm bit for

    :param u32 q_id:
        the queue number

.. _`hinic_set_arm_bit.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`cmdq_arm_ceq_handler`:

cmdq_arm_ceq_handler
====================

.. c:function:: int cmdq_arm_ceq_handler(struct hinic_cmdq *cmdq, struct hinic_cmdq_wqe *wqe)

    cmdq completion event handler for arm command

    :param struct hinic_cmdq \*cmdq:
        the cmdq of the arm command

    :param struct hinic_cmdq_wqe \*wqe:
        the wqe of the arm command

.. _`cmdq_arm_ceq_handler.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`cmdq_sync_cmd_handler`:

cmdq_sync_cmd_handler
=====================

.. c:function:: void cmdq_sync_cmd_handler(struct hinic_cmdq *cmdq, u16 cons_idx, int errcode)

    cmdq completion event handler for sync command

    :param struct hinic_cmdq \*cmdq:
        the cmdq of the command

    :param u16 cons_idx:
        the consumer index to update the error code for

    :param int errcode:
        the error code

.. _`cmdq_ceq_handler`:

cmdq_ceq_handler
================

.. c:function:: void cmdq_ceq_handler(void *handle, u32 ceqe_data)

    cmdq completion event handler

    :param void \*handle:
        private data for the handler(cmdqs)

    :param u32 ceqe_data:
        ceq element data

.. _`cmdq_init_queue_ctxt`:

cmdq_init_queue_ctxt
====================

.. c:function:: void cmdq_init_queue_ctxt(struct hinic_cmdq_ctxt *cmdq_ctxt, struct hinic_cmdq *cmdq, struct hinic_cmdq_pages *cmdq_pages)

    init the queue ctxt of a cmdq

    :param struct hinic_cmdq_ctxt \*cmdq_ctxt:
        cmdq ctxt to initialize

    :param struct hinic_cmdq \*cmdq:
        the cmdq

    :param struct hinic_cmdq_pages \*cmdq_pages:
        the memory of the queue

.. _`init_cmdq`:

init_cmdq
=========

.. c:function:: int init_cmdq(struct hinic_cmdq *cmdq, struct hinic_wq *wq, enum hinic_cmdq_type q_type, void __iomem *db_area)

    initialize cmdq

    :param struct hinic_cmdq \*cmdq:
        the cmdq

    :param struct hinic_wq \*wq:
        the wq attaced to the cmdq

    :param enum hinic_cmdq_type q_type:
        the cmdq type of the cmdq

    :param void __iomem \*db_area:
        doorbell area for the cmdq

.. _`init_cmdq.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`free_cmdq`:

free_cmdq
=========

.. c:function:: void free_cmdq(struct hinic_cmdq *cmdq)

    Free cmdq

    :param struct hinic_cmdq \*cmdq:
        the cmdq to free

.. _`init_cmdqs_ctxt`:

init_cmdqs_ctxt
===============

.. c:function:: int init_cmdqs_ctxt(struct hinic_hwdev *hwdev, struct hinic_cmdqs *cmdqs, void __iomem **db_area)

    write the cmdq ctxt to HW after init all cmdq

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device

    :param struct hinic_cmdqs \*cmdqs:
        cmdqs to write the ctxts for
        \ :c:type:`struct db_area <db_area>`\ : db_area for all the cmdqs

    :param void __iomem \*\*db_area:
        *undescribed*

.. _`init_cmdqs_ctxt.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_init_cmdqs`:

hinic_init_cmdqs
================

.. c:function:: int hinic_init_cmdqs(struct hinic_cmdqs *cmdqs, struct hinic_hwif *hwif, void __iomem **db_area)

    init all cmdqs

    :param struct hinic_cmdqs \*cmdqs:
        cmdqs to init

    :param struct hinic_hwif \*hwif:
        HW interface for accessing cmdqs

    :param void __iomem \*\*db_area:
        doorbell areas for all the cmdqs

.. _`hinic_init_cmdqs.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_free_cmdqs`:

hinic_free_cmdqs
================

.. c:function:: void hinic_free_cmdqs(struct hinic_cmdqs *cmdqs)

    free all cmdqs

    :param struct hinic_cmdqs \*cmdqs:
        cmdqs to free

.. This file was automatic generated / don't edit.

