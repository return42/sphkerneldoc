.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/bnx2fc/bnx2fc_hwi.c

.. _`bnx2fc_send_fw_fcoe_init_msg`:

bnx2fc_send_fw_fcoe_init_msg
============================

.. c:function:: int bnx2fc_send_fw_fcoe_init_msg(struct bnx2fc_hba *hba)

    initiates initial handshake with FCoE f/w

    :param hba:
        adapter structure pointer
    :type hba: struct bnx2fc_hba \*

.. _`bnx2fc_send_fw_fcoe_init_msg.description`:

Description
-----------

Send down FCoE firmware init KWQEs which initiates the initial handshake
with the f/w.

.. _`bnx2fc_send_session_ofld_req`:

bnx2fc_send_session_ofld_req
============================

.. c:function:: int bnx2fc_send_session_ofld_req(struct fcoe_port *port, struct bnx2fc_rport *tgt)

    initiates FCoE Session offload process

    :param port:
        port structure pointer
    :type port: struct fcoe_port \*

    :param tgt:
        bnx2fc_rport structure pointer
    :type tgt: struct bnx2fc_rport \*

.. _`bnx2fc_send_session_enable_req`:

bnx2fc_send_session_enable_req
==============================

.. c:function:: int bnx2fc_send_session_enable_req(struct fcoe_port *port, struct bnx2fc_rport *tgt)

    initiates FCoE Session enablement

    :param port:
        port structure pointer
    :type port: struct fcoe_port \*

    :param tgt:
        bnx2fc_rport structure pointer
    :type tgt: struct bnx2fc_rport \*

.. _`bnx2fc_send_session_disable_req`:

bnx2fc_send_session_disable_req
===============================

.. c:function:: int bnx2fc_send_session_disable_req(struct fcoe_port *port, struct bnx2fc_rport *tgt)

    initiates FCoE Session disable

    :param port:
        port structure pointer
    :type port: struct fcoe_port \*

    :param tgt:
        bnx2fc_rport structure pointer
    :type tgt: struct bnx2fc_rport \*

.. _`bnx2fc_send_session_destroy_req`:

bnx2fc_send_session_destroy_req
===============================

.. c:function:: int bnx2fc_send_session_destroy_req(struct bnx2fc_hba *hba, struct bnx2fc_rport *tgt)

    initiates FCoE Session destroy

    :param hba:
        *undescribed*
    :type hba: struct bnx2fc_hba \*

    :param tgt:
        bnx2fc_rport structure pointer
    :type tgt: struct bnx2fc_rport \*

.. _`bnx2fc_fastpath_notification`:

bnx2fc_fastpath_notification
============================

.. c:function:: void bnx2fc_fastpath_notification(struct bnx2fc_hba *hba, struct fcoe_kcqe *new_cqe_kcqe)

    process global event queue (KCQ)

    :param hba:
        adapter structure pointer
    :type hba: struct bnx2fc_hba \*

    :param new_cqe_kcqe:
        pointer to newly DMA'd KCQ entry
    :type new_cqe_kcqe: struct fcoe_kcqe \*

.. _`bnx2fc_fastpath_notification.description`:

Description
-----------

Fast path event notification handler

.. _`bnx2fc_process_ofld_cmpl`:

bnx2fc_process_ofld_cmpl
========================

.. c:function:: void bnx2fc_process_ofld_cmpl(struct bnx2fc_hba *hba, struct fcoe_kcqe *ofld_kcqe)

    process FCoE session offload completion

    :param hba:
        adapter structure pointer
    :type hba: struct bnx2fc_hba \*

    :param ofld_kcqe:
        connection offload kcqe pointer
    :type ofld_kcqe: struct fcoe_kcqe \*

.. _`bnx2fc_process_ofld_cmpl.description`:

Description
-----------

handle session offload completion, enable the session if offload is
successful.

.. _`bnx2fc_process_enable_conn_cmpl`:

bnx2fc_process_enable_conn_cmpl
===============================

.. c:function:: void bnx2fc_process_enable_conn_cmpl(struct bnx2fc_hba *hba, struct fcoe_kcqe *ofld_kcqe)

    process FCoE session enable completion

    :param hba:
        adapter structure pointer
    :type hba: struct bnx2fc_hba \*

    :param ofld_kcqe:
        connection offload kcqe pointer
    :type ofld_kcqe: struct fcoe_kcqe \*

.. _`bnx2fc_process_enable_conn_cmpl.description`:

Description
-----------

handle session enable completion, mark the rport as ready

.. _`bnx2fc_indicate_kcqe`:

bnx2fc_indicate_kcqe
====================

.. c:function:: void bnx2fc_indicate_kcqe(void *context, struct kcqe  *kcq, u32 num_cqe)

    process KCQE

    :param context:
        *undescribed*
    :type context: void \*

    :param kcq:
        *undescribed*
    :type kcq: struct kcqe  \*

    :param num_cqe:
        Number of completion queue elements
    :type num_cqe: u32

.. _`bnx2fc_indicate_kcqe.description`:

Description
-----------

Generic KCQ event handler

.. _`bnx2fc_setup_task_ctx`:

bnx2fc_setup_task_ctx
=====================

.. c:function:: int bnx2fc_setup_task_ctx(struct bnx2fc_hba *hba)

    allocate and map task context

    :param hba:
        pointer to adapter structure
    :type hba: struct bnx2fc_hba \*

.. _`bnx2fc_setup_task_ctx.description`:

Description
-----------

allocate memory for task context, and associated BD table to be used
by firmware

.. _`bnx2fc_setup_fw_resc`:

bnx2fc_setup_fw_resc
====================

.. c:function:: int bnx2fc_setup_fw_resc(struct bnx2fc_hba *hba)

    Allocate and map hash table and dummy buffer

    :param hba:
        Pointer to adapter structure
    :type hba: struct bnx2fc_hba \*

.. This file was automatic generated / don't edit.

