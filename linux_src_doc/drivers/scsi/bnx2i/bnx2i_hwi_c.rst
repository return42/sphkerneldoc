.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/bnx2i/bnx2i_hwi.c

.. _`bnx2i_get_cid_num`:

bnx2i_get_cid_num
=================

.. c:function:: u32 bnx2i_get_cid_num(struct bnx2i_endpoint *ep)

    get cid from ep

    :param struct bnx2i_endpoint \*ep:
        endpoint pointer

.. _`bnx2i_get_cid_num.description`:

Description
-----------

Only applicable to 57710 family of devices

.. _`bnx2i_adjust_qp_size`:

bnx2i_adjust_qp_size
====================

.. c:function:: void bnx2i_adjust_qp_size(struct bnx2i_hba *hba)

    Adjust SQ/RQ/CQ size for 57710 device type

    :param struct bnx2i_hba \*hba:
        Adapter for which adjustments is to be made

.. _`bnx2i_adjust_qp_size.description`:

Description
-----------

Only applicable to 57710 family of devices

.. _`bnx2i_get_link_state`:

bnx2i_get_link_state
====================

.. c:function:: void bnx2i_get_link_state(struct bnx2i_hba *hba)

    get network interface link state

    :param struct bnx2i_hba \*hba:
        adapter instance pointer

.. _`bnx2i_get_link_state.description`:

Description
-----------

updates adapter structure flag based on netdev state

.. _`bnx2i_iscsi_license_error`:

bnx2i_iscsi_license_error
=========================

.. c:function:: void bnx2i_iscsi_license_error(struct bnx2i_hba *hba, u32 error_code)

    displays iscsi license related error message

    :param struct bnx2i_hba \*hba:
        adapter instance pointer

    :param u32 error_code:
        error classification

.. _`bnx2i_iscsi_license_error.description`:

Description
-----------

Puts out an error log when driver is unable to offload iscsi connection
due to license restrictions

.. _`bnx2i_arm_cq_event_coalescing`:

bnx2i_arm_cq_event_coalescing
=============================

.. c:function:: int bnx2i_arm_cq_event_coalescing(struct bnx2i_endpoint *ep, u8 action)

    arms CQ to enable EQ notification

    :param struct bnx2i_endpoint \*ep:
        endpoint (transport identifier) structure

    :param u8 action:
        action, ARM or DISARM. For now only ARM_CQE is used

.. _`bnx2i_arm_cq_event_coalescing.description`:

Description
-----------

Arm'ing CQ will enable chip to generate global EQ events inorder to interrupt
the driver. EQ event is generated CQ index is hit or at least 1 CQ is
outstanding and on chip timer expires

.. _`bnx2i_get_rq_buf`:

bnx2i_get_rq_buf
================

.. c:function:: void bnx2i_get_rq_buf(struct bnx2i_conn *bnx2i_conn, char *ptr, int len)

    copy RQ buffer contents to driver buffer

    :param struct bnx2i_conn \*bnx2i_conn:
        *undescribed*

    :param char \*ptr:
        driver buffer to which RQ buffer contents is to
        be copied

    :param int len:
        length of valid data inside RQ buf

.. _`bnx2i_get_rq_buf.description`:

Description
-----------

Copies RQ buffer contents from shared (DMA'able) memory region to
driver buffer. RQ is used to DMA unsolicitated iscsi pdu's and
scsi sense info

.. _`bnx2i_put_rq_buf`:

bnx2i_put_rq_buf
================

.. c:function:: void bnx2i_put_rq_buf(struct bnx2i_conn *bnx2i_conn, int count)

    Replenish RQ buffer, if required ring on chip doorbell

    :param struct bnx2i_conn \*bnx2i_conn:
        *undescribed*

    :param int count:
        number of RQ buffer being posted to chip

.. _`bnx2i_put_rq_buf.description`:

Description
-----------

No need to ring hardware doorbell for 57710 family of devices

.. _`bnx2i_ring_sq_dbell`:

bnx2i_ring_sq_dbell
===================

.. c:function:: void bnx2i_ring_sq_dbell(struct bnx2i_conn *bnx2i_conn, int count)

    Ring SQ doorbell to wake-up the processing engine

    :param struct bnx2i_conn \*bnx2i_conn:
        *undescribed*

    :param int count:
        number of SQ WQEs to post

.. _`bnx2i_ring_sq_dbell.description`:

Description
-----------

SQ DB is updated in host memory and TX Doorbell is rung for 57710 family
of devices. For 5706/5708/5709 new SQ WQE count is written into the
doorbell register

.. _`bnx2i_ring_dbell_update_sq_params`:

bnx2i_ring_dbell_update_sq_params
=================================

.. c:function:: void bnx2i_ring_dbell_update_sq_params(struct bnx2i_conn *bnx2i_conn, int count)

    update SQ driver parameters

    :param struct bnx2i_conn \*bnx2i_conn:
        *undescribed*

    :param int count:
        number of SQ WQEs to post

.. _`bnx2i_ring_dbell_update_sq_params.description`:

Description
-----------

this routine will update SQ driver parameters and ring the doorbell

.. _`bnx2i_send_iscsi_login`:

bnx2i_send_iscsi_login
======================

.. c:function:: int bnx2i_send_iscsi_login(struct bnx2i_conn *bnx2i_conn, struct iscsi_task *task)

    post iSCSI login request MP WQE to hardware

    :param struct bnx2i_conn \*bnx2i_conn:
        *undescribed*

    :param struct iscsi_task \*task:
        *undescribed*

.. _`bnx2i_send_iscsi_login.description`:

Description
-----------

prepare and post an iSCSI Login request WQE to CNIC firmware

.. _`bnx2i_send_iscsi_tmf`:

bnx2i_send_iscsi_tmf
====================

.. c:function:: int bnx2i_send_iscsi_tmf(struct bnx2i_conn *bnx2i_conn, struct iscsi_task *mtask)

    post iSCSI task management request MP WQE to hardware

    :param struct bnx2i_conn \*bnx2i_conn:
        *undescribed*

    :param struct iscsi_task \*mtask:
        driver command structure which is requesting
        a WQE to sent to chip for further processing

.. _`bnx2i_send_iscsi_tmf.description`:

Description
-----------

prepare and post an iSCSI Login request WQE to CNIC firmware

.. _`bnx2i_send_iscsi_text`:

bnx2i_send_iscsi_text
=====================

.. c:function:: int bnx2i_send_iscsi_text(struct bnx2i_conn *bnx2i_conn, struct iscsi_task *mtask)

    post iSCSI text WQE to hardware

    :param struct bnx2i_conn \*bnx2i_conn:
        *undescribed*

    :param struct iscsi_task \*mtask:
        driver command structure which is requesting
        a WQE to sent to chip for further processing

.. _`bnx2i_send_iscsi_text.description`:

Description
-----------

prepare and post an iSCSI Text request WQE to CNIC firmware

.. _`bnx2i_send_iscsi_scsicmd`:

bnx2i_send_iscsi_scsicmd
========================

.. c:function:: int bnx2i_send_iscsi_scsicmd(struct bnx2i_conn *bnx2i_conn, struct bnx2i_cmd *cmd)

    post iSCSI scsicmd request WQE to hardware

    :param struct bnx2i_conn \*bnx2i_conn:
        *undescribed*

    :param struct bnx2i_cmd \*cmd:
        driver command structure which is requesting
        a WQE to sent to chip for further processing

.. _`bnx2i_send_iscsi_scsicmd.description`:

Description
-----------

prepare and post an iSCSI SCSI-CMD request WQE to CNIC firmware

.. _`bnx2i_send_iscsi_nopout`:

bnx2i_send_iscsi_nopout
=======================

.. c:function:: int bnx2i_send_iscsi_nopout(struct bnx2i_conn *bnx2i_conn, struct iscsi_task *task, char *datap, int data_len, int unsol)

    post iSCSI NOPOUT request WQE to hardware

    :param struct bnx2i_conn \*bnx2i_conn:
        *undescribed*

    :param struct iscsi_task \*task:
        *undescribed*

    :param char \*datap:
        payload buffer pointer

    :param int data_len:
        payload data length

    :param int unsol:
        indicated whether nopout pdu is unsolicited pdu or
        in response to target's NOPIN w/ TTT != FFFFFFFF

.. _`bnx2i_send_iscsi_nopout.description`:

Description
-----------

prepare and post a nopout request WQE to CNIC firmware

.. _`bnx2i_send_iscsi_logout`:

bnx2i_send_iscsi_logout
=======================

.. c:function:: int bnx2i_send_iscsi_logout(struct bnx2i_conn *bnx2i_conn, struct iscsi_task *task)

    post iSCSI logout request WQE to hardware

    :param struct bnx2i_conn \*bnx2i_conn:
        *undescribed*

    :param struct iscsi_task \*task:
        *undescribed*

.. _`bnx2i_send_iscsi_logout.description`:

Description
-----------

prepare and post logout request WQE to CNIC firmware

.. _`bnx2i_update_iscsi_conn`:

bnx2i_update_iscsi_conn
=======================

.. c:function:: void bnx2i_update_iscsi_conn(struct iscsi_conn *conn)

    post iSCSI logout request WQE to hardware

    :param struct iscsi_conn \*conn:
        iscsi connection which requires iscsi parameter update

.. _`bnx2i_update_iscsi_conn.description`:

Description
-----------

sends down iSCSI Conn Update request to move iSCSI conn to FFP

.. _`bnx2i_ep_ofld_timer`:

bnx2i_ep_ofld_timer
===================

.. c:function:: void bnx2i_ep_ofld_timer(unsigned long data)

    post iSCSI logout request WQE to hardware

    :param unsigned long data:
        endpoint (transport handle) structure pointer

.. _`bnx2i_ep_ofld_timer.description`:

Description
-----------

routine to handle connection offload/destroy request timeout

.. _`bnx2i_send_cmd_cleanup_req`:

bnx2i_send_cmd_cleanup_req
==========================

.. c:function:: void bnx2i_send_cmd_cleanup_req(struct bnx2i_hba *hba, struct bnx2i_cmd *cmd)

    send iscsi cmd context clean-up request

    :param struct bnx2i_hba \*hba:
        adapter structure pointer

    :param struct bnx2i_cmd \*cmd:
        driver command structure which is requesting
        a WQE to sent to chip for further processing

.. _`bnx2i_send_cmd_cleanup_req.description`:

Description
-----------

prepares and posts CONN_OFLD_REQ1/2 KWQE

.. _`bnx2i_send_conn_destroy`:

bnx2i_send_conn_destroy
=======================

.. c:function:: int bnx2i_send_conn_destroy(struct bnx2i_hba *hba, struct bnx2i_endpoint *ep)

    initiates iscsi connection teardown process

    :param struct bnx2i_hba \*hba:
        adapter structure pointer

    :param struct bnx2i_endpoint \*ep:
        endpoint (transport identifier) structure

.. _`bnx2i_send_conn_destroy.description`:

Description
-----------

this routine prepares and posts CONN_OFLD_REQ1/2 KWQE to initiate
iscsi connection context clean-up process

.. _`bnx2i_570x_send_conn_ofld_req`:

bnx2i_570x_send_conn_ofld_req
=============================

.. c:function:: int bnx2i_570x_send_conn_ofld_req(struct bnx2i_hba *hba, struct bnx2i_endpoint *ep)

    initiates iscsi conn context setup process

    :param struct bnx2i_hba \*hba:
        adapter structure pointer

    :param struct bnx2i_endpoint \*ep:
        endpoint (transport identifier) structure

.. _`bnx2i_570x_send_conn_ofld_req.description`:

Description
-----------

5706/5708/5709 specific - prepares and posts CONN_OFLD_REQ1/2 KWQE

.. _`bnx2i_5771x_send_conn_ofld_req`:

bnx2i_5771x_send_conn_ofld_req
==============================

.. c:function:: int bnx2i_5771x_send_conn_ofld_req(struct bnx2i_hba *hba, struct bnx2i_endpoint *ep)

    initiates iscsi connection context creation

    :param struct bnx2i_hba \*hba:
        adapter structure pointer

    :param struct bnx2i_endpoint \*ep:
        endpoint (transport identifier) structure

.. _`bnx2i_5771x_send_conn_ofld_req.description`:

Description
-----------

57710 specific - prepares and posts CONN_OFLD_REQ1/2 KWQE

.. _`bnx2i_send_conn_ofld_req`:

bnx2i_send_conn_ofld_req
========================

.. c:function:: int bnx2i_send_conn_ofld_req(struct bnx2i_hba *hba, struct bnx2i_endpoint *ep)

    initiates iscsi connection context setup process

    :param struct bnx2i_hba \*hba:
        adapter structure pointer

    :param struct bnx2i_endpoint \*ep:
        endpoint (transport identifier) structure

.. _`bnx2i_send_conn_ofld_req.description`:

Description
-----------

this routine prepares and posts CONN_OFLD_REQ1/2 KWQE

.. _`setup_qp_page_tables`:

setup_qp_page_tables
====================

.. c:function:: void setup_qp_page_tables(struct bnx2i_endpoint *ep)

    iscsi QP page table setup function

    :param struct bnx2i_endpoint \*ep:
        endpoint (transport identifier) structure

.. _`setup_qp_page_tables.description`:

Description
-----------

Sets up page tables for SQ/RQ/CQ, 1G/sec (5706/5708/5709) devices requires
64-bit address in big endian format. Whereas 10G/sec (57710) requires
PT in little endian format

.. _`bnx2i_alloc_qp_resc`:

bnx2i_alloc_qp_resc
===================

.. c:function:: int bnx2i_alloc_qp_resc(struct bnx2i_hba *hba, struct bnx2i_endpoint *ep)

    allocates required resources for QP.

    :param struct bnx2i_hba \*hba:
        adapter structure pointer

    :param struct bnx2i_endpoint \*ep:
        endpoint (transport identifier) structure

.. _`bnx2i_alloc_qp_resc.description`:

Description
-----------

Allocate QP (transport layer for iSCSI connection) resources, DMA'able
memory for SQ/RQ/CQ and page tables. EP structure elements such
as producer/consumer indexes/pointers, queue sizes and page table
contents are setup

.. _`bnx2i_free_qp_resc`:

bnx2i_free_qp_resc
==================

.. c:function:: void bnx2i_free_qp_resc(struct bnx2i_hba *hba, struct bnx2i_endpoint *ep)

    free memory resources held by QP

    :param struct bnx2i_hba \*hba:
        adapter structure pointer

    :param struct bnx2i_endpoint \*ep:
        endpoint (transport identifier) structure

.. _`bnx2i_free_qp_resc.description`:

Description
-----------

Free QP resources - SQ/RQ/CQ memory and page tables.

.. _`bnx2i_send_fw_iscsi_init_msg`:

bnx2i_send_fw_iscsi_init_msg
============================

.. c:function:: int bnx2i_send_fw_iscsi_init_msg(struct bnx2i_hba *hba)

    initiates initial handshake with iscsi f/w

    :param struct bnx2i_hba \*hba:
        adapter structure pointer

.. _`bnx2i_send_fw_iscsi_init_msg.description`:

Description
-----------

Send down iscsi_init KWQEs which initiates the initial handshake with the f/w
This results in iSCSi support validation and on-chip context manager
initialization.  Firmware completes this handshake with a CQE carrying
the result of iscsi support validation. Parameter carried by
iscsi init request determines the number of offloaded connection and
tolerance level for iscsi protocol violation this hba/chip can support

.. _`bnx2i_process_scsi_cmd_resp`:

bnx2i_process_scsi_cmd_resp
===========================

.. c:function:: int bnx2i_process_scsi_cmd_resp(struct iscsi_session *session, struct bnx2i_conn *bnx2i_conn, struct cqe *cqe)

    this function handles scsi cmd completion.

    :param struct iscsi_session \*session:
        iscsi session

    :param struct bnx2i_conn \*bnx2i_conn:
        bnx2i connection

    :param struct cqe \*cqe:
        pointer to newly DMA'ed CQE entry for processing

.. _`bnx2i_process_scsi_cmd_resp.description`:

Description
-----------

process SCSI CMD Response CQE & complete the request to SCSI-ML

.. _`bnx2i_process_login_resp`:

bnx2i_process_login_resp
========================

.. c:function:: int bnx2i_process_login_resp(struct iscsi_session *session, struct bnx2i_conn *bnx2i_conn, struct cqe *cqe)

    this function handles iscsi login response

    :param struct iscsi_session \*session:
        iscsi session pointer

    :param struct bnx2i_conn \*bnx2i_conn:
        iscsi connection pointer

    :param struct cqe \*cqe:
        pointer to newly DMA'ed CQE entry for processing

.. _`bnx2i_process_login_resp.description`:

Description
-----------

process Login Response CQE & complete it to open-iscsi user daemon

.. _`bnx2i_process_text_resp`:

bnx2i_process_text_resp
=======================

.. c:function:: int bnx2i_process_text_resp(struct iscsi_session *session, struct bnx2i_conn *bnx2i_conn, struct cqe *cqe)

    this function handles iscsi text response

    :param struct iscsi_session \*session:
        iscsi session pointer

    :param struct bnx2i_conn \*bnx2i_conn:
        iscsi connection pointer

    :param struct cqe \*cqe:
        pointer to newly DMA'ed CQE entry for processing

.. _`bnx2i_process_text_resp.description`:

Description
-----------

process iSCSI Text Response CQE&  complete it to open-iscsi user daemon

.. _`bnx2i_process_tmf_resp`:

bnx2i_process_tmf_resp
======================

.. c:function:: int bnx2i_process_tmf_resp(struct iscsi_session *session, struct bnx2i_conn *bnx2i_conn, struct cqe *cqe)

    this function handles iscsi TMF response

    :param struct iscsi_session \*session:
        iscsi session pointer

    :param struct bnx2i_conn \*bnx2i_conn:
        iscsi connection pointer

    :param struct cqe \*cqe:
        pointer to newly DMA'ed CQE entry for processing

.. _`bnx2i_process_tmf_resp.description`:

Description
-----------

process iSCSI TMF Response CQE and wake up the driver eh thread.

.. _`bnx2i_process_logout_resp`:

bnx2i_process_logout_resp
=========================

.. c:function:: int bnx2i_process_logout_resp(struct iscsi_session *session, struct bnx2i_conn *bnx2i_conn, struct cqe *cqe)

    this function handles iscsi logout response

    :param struct iscsi_session \*session:
        iscsi session pointer

    :param struct bnx2i_conn \*bnx2i_conn:
        iscsi connection pointer

    :param struct cqe \*cqe:
        pointer to newly DMA'ed CQE entry for processing

.. _`bnx2i_process_logout_resp.description`:

Description
-----------

process iSCSI Logout Response CQE & make function call to
notify the user daemon.

.. _`bnx2i_process_nopin_local_cmpl`:

bnx2i_process_nopin_local_cmpl
==============================

.. c:function:: void bnx2i_process_nopin_local_cmpl(struct iscsi_session *session, struct bnx2i_conn *bnx2i_conn, struct cqe *cqe)

    this function handles iscsi nopin CQE

    :param struct iscsi_session \*session:
        iscsi session pointer

    :param struct bnx2i_conn \*bnx2i_conn:
        iscsi connection pointer

    :param struct cqe \*cqe:
        pointer to newly DMA'ed CQE entry for processing

.. _`bnx2i_process_nopin_local_cmpl.description`:

Description
-----------

process iSCSI NOPIN local completion CQE, frees IIT and command structures

.. _`bnx2i_unsol_pdu_adjust_rq`:

bnx2i_unsol_pdu_adjust_rq
=========================

.. c:function:: void bnx2i_unsol_pdu_adjust_rq(struct bnx2i_conn *bnx2i_conn)

    makes adjustments to RQ after unsol pdu is recvd

    :param struct bnx2i_conn \*bnx2i_conn:
        *undescribed*

.. _`bnx2i_unsol_pdu_adjust_rq.description`:

Description
-----------

Firmware advances RQ producer index for every unsolicited PDU even if
payload data length is '0'. This function makes corresponding
adjustments on the driver side to match this f/w behavior

.. _`bnx2i_process_nopin_mesg`:

bnx2i_process_nopin_mesg
========================

.. c:function:: int bnx2i_process_nopin_mesg(struct iscsi_session *session, struct bnx2i_conn *bnx2i_conn, struct cqe *cqe)

    this function handles iscsi nopin CQE

    :param struct iscsi_session \*session:
        iscsi session pointer

    :param struct bnx2i_conn \*bnx2i_conn:
        iscsi connection pointer

    :param struct cqe \*cqe:
        pointer to newly DMA'ed CQE entry for processing

.. _`bnx2i_process_nopin_mesg.description`:

Description
-----------

process iSCSI target's proactive iSCSI NOPIN request

.. _`bnx2i_process_async_mesg`:

bnx2i_process_async_mesg
========================

.. c:function:: void bnx2i_process_async_mesg(struct iscsi_session *session, struct bnx2i_conn *bnx2i_conn, struct cqe *cqe)

    this function handles iscsi async message

    :param struct iscsi_session \*session:
        iscsi session pointer

    :param struct bnx2i_conn \*bnx2i_conn:
        iscsi connection pointer

    :param struct cqe \*cqe:
        pointer to newly DMA'ed CQE entry for processing

.. _`bnx2i_process_async_mesg.description`:

Description
-----------

process iSCSI ASYNC Message

.. _`bnx2i_process_reject_mesg`:

bnx2i_process_reject_mesg
=========================

.. c:function:: void bnx2i_process_reject_mesg(struct iscsi_session *session, struct bnx2i_conn *bnx2i_conn, struct cqe *cqe)

    process iscsi reject pdu

    :param struct iscsi_session \*session:
        iscsi session pointer

    :param struct bnx2i_conn \*bnx2i_conn:
        iscsi connection pointer

    :param struct cqe \*cqe:
        pointer to newly DMA'ed CQE entry for processing

.. _`bnx2i_process_reject_mesg.description`:

Description
-----------

process iSCSI REJECT message

.. _`bnx2i_process_cmd_cleanup_resp`:

bnx2i_process_cmd_cleanup_resp
==============================

.. c:function:: void bnx2i_process_cmd_cleanup_resp(struct iscsi_session *session, struct bnx2i_conn *bnx2i_conn, struct cqe *cqe)

    process scsi command clean-up completion

    :param struct iscsi_session \*session:
        iscsi session pointer

    :param struct bnx2i_conn \*bnx2i_conn:
        iscsi connection pointer

    :param struct cqe \*cqe:
        pointer to newly DMA'ed CQE entry for processing

.. _`bnx2i_process_cmd_cleanup_resp.description`:

Description
-----------

process command cleanup response CQE during conn shutdown or error recovery

.. _`bnx2i_percpu_io_thread`:

bnx2i_percpu_io_thread
======================

.. c:function:: int bnx2i_percpu_io_thread(void *arg)

    thread per cpu for ios

    :param void \*arg:
        ptr to bnx2i_percpu_info structure

.. _`bnx2i_queue_scsi_cmd_resp`:

bnx2i_queue_scsi_cmd_resp
=========================

.. c:function:: int bnx2i_queue_scsi_cmd_resp(struct iscsi_session *session, struct bnx2i_conn *bnx2i_conn, struct bnx2i_nop_in_msg *cqe)

    queue cmd completion to the percpu thread

    :param struct iscsi_session \*session:
        *undescribed*

    :param struct bnx2i_conn \*bnx2i_conn:
        bnx2i connection

    :param struct bnx2i_nop_in_msg \*cqe:
        *undescribed*

.. _`bnx2i_queue_scsi_cmd_resp.description`:

Description
-----------

this function is called by generic KCQ handler to queue all pending cmd
completion CQEs

The implementation is to queue the cmd response based on the
last recorded command for the given connection.  The
cpu_id gets recorded upon task_xmit.  No out-of-order completion!

.. _`bnx2i_process_new_cqes`:

bnx2i_process_new_cqes
======================

.. c:function:: int bnx2i_process_new_cqes(struct bnx2i_conn *bnx2i_conn)

    process newly DMA'ed CQE's

    :param struct bnx2i_conn \*bnx2i_conn:
        bnx2i connection

.. _`bnx2i_process_new_cqes.description`:

Description
-----------

this function is called by generic KCQ handler to process all pending CQE's

.. _`bnx2i_fastpath_notification`:

bnx2i_fastpath_notification
===========================

.. c:function:: void bnx2i_fastpath_notification(struct bnx2i_hba *hba, struct iscsi_kcqe *new_cqe_kcqe)

    process global event queue (KCQ)

    :param struct bnx2i_hba \*hba:
        adapter structure pointer

    :param struct iscsi_kcqe \*new_cqe_kcqe:
        pointer to newly DMA'ed KCQE entry

.. _`bnx2i_fastpath_notification.description`:

Description
-----------

Fast path event notification handler, KCQ entry carries context id
of the connection that has 1 or more pending CQ entries

.. _`bnx2i_process_update_conn_cmpl`:

bnx2i_process_update_conn_cmpl
==============================

.. c:function:: void bnx2i_process_update_conn_cmpl(struct bnx2i_hba *hba, struct iscsi_kcqe *update_kcqe)

    process iscsi conn update completion KCQE

    :param struct bnx2i_hba \*hba:
        adapter structure pointer

    :param struct iscsi_kcqe \*update_kcqe:
        kcqe pointer

.. _`bnx2i_process_update_conn_cmpl.description`:

Description
-----------

CONN_UPDATE completion handler, this completes iSCSI connection FFP migration

.. _`bnx2i_recovery_que_add_conn`:

bnx2i_recovery_que_add_conn
===========================

.. c:function:: void bnx2i_recovery_que_add_conn(struct bnx2i_hba *hba, struct bnx2i_conn *bnx2i_conn)

    add connection to recovery queue

    :param struct bnx2i_hba \*hba:
        adapter structure pointer

    :param struct bnx2i_conn \*bnx2i_conn:
        iscsi connection

.. _`bnx2i_recovery_que_add_conn.description`:

Description
-----------

Add connection to recovery queue and schedule adapter eh worker

.. _`bnx2i_process_tcp_error`:

bnx2i_process_tcp_error
=======================

.. c:function:: void bnx2i_process_tcp_error(struct bnx2i_hba *hba, struct iscsi_kcqe *tcp_err)

    process error notification on a given connection

    :param struct bnx2i_hba \*hba:
        adapter structure pointer

    :param struct iscsi_kcqe \*tcp_err:
        tcp error kcqe pointer

.. _`bnx2i_process_tcp_error.description`:

Description
-----------

handles tcp level error notifications from FW.

.. _`bnx2i_process_iscsi_error`:

bnx2i_process_iscsi_error
=========================

.. c:function:: void bnx2i_process_iscsi_error(struct bnx2i_hba *hba, struct iscsi_kcqe *iscsi_err)

    process error notification on a given connection

    :param struct bnx2i_hba \*hba:
        adapter structure pointer

    :param struct iscsi_kcqe \*iscsi_err:
        iscsi error kcqe pointer

.. _`bnx2i_process_iscsi_error.description`:

Description
-----------

handles iscsi error notifications from the FW. Firmware based in initial
handshake classifies iscsi protocol / TCP rfc violation into either
warning or error indications. If indication is of "Error" type, driver
will initiate session recovery for that connection/session. For
"Warning" type indication, driver will put out a system log message
(there will be only one message for each type for the life of the
session, this is to avoid un-necessarily overloading the system)

.. _`bnx2i_process_conn_destroy_cmpl`:

bnx2i_process_conn_destroy_cmpl
===============================

.. c:function:: void bnx2i_process_conn_destroy_cmpl(struct bnx2i_hba *hba, struct iscsi_kcqe *conn_destroy)

    process iscsi conn destroy completion

    :param struct bnx2i_hba \*hba:
        adapter structure pointer

    :param struct iscsi_kcqe \*conn_destroy:
        conn destroy kcqe pointer

.. _`bnx2i_process_conn_destroy_cmpl.description`:

Description
-----------

handles connection destroy completion request.

.. _`bnx2i_process_ofld_cmpl`:

bnx2i_process_ofld_cmpl
=======================

.. c:function:: void bnx2i_process_ofld_cmpl(struct bnx2i_hba *hba, struct iscsi_kcqe *ofld_kcqe)

    process initial iscsi conn offload completion

    :param struct bnx2i_hba \*hba:
        adapter structure pointer

    :param struct iscsi_kcqe \*ofld_kcqe:
        conn offload kcqe pointer

.. _`bnx2i_process_ofld_cmpl.description`:

Description
-----------

handles initial connection offload completion, \ :c:func:`ep_connect`\  thread is
woken-up to continue with LLP connect process

.. _`bnx2i_indicate_kcqe`:

bnx2i_indicate_kcqe
===================

.. c:function:: void bnx2i_indicate_kcqe(void *context, struct kcqe  *kcqe, u32 num_cqe)

    process iscsi conn update completion KCQE

    :param void \*context:
        *undescribed*

    :param struct kcqe  \*kcqe:
        *undescribed*

    :param u32 num_cqe:
        *undescribed*

.. _`bnx2i_indicate_kcqe.description`:

Description
-----------

Generic KCQ event handler/dispatcher

.. _`bnx2i_indicate_netevent`:

bnx2i_indicate_netevent
=======================

.. c:function:: void bnx2i_indicate_netevent(void *context, unsigned long event, u16 vlan_id)

    Generic netdev event handler

    :param void \*context:
        adapter structure pointer

    :param unsigned long event:
        event type

    :param u16 vlan_id:
        vlans id - associated vlan id with this event

.. _`bnx2i_indicate_netevent.description`:

Description
-----------

Handles four netdev events, NETDEV_UP, NETDEV_DOWN,
NETDEV_GOING_DOWN and NETDEV_CHANGE

.. _`bnx2i_cm_connect_cmpl`:

bnx2i_cm_connect_cmpl
=====================

.. c:function:: void bnx2i_cm_connect_cmpl(struct cnic_sock *cm_sk)

    process iscsi conn establishment completion

    :param struct cnic_sock \*cm_sk:
        cnic sock structure pointer

.. _`bnx2i_cm_connect_cmpl.description`:

Description
-----------

function callback exported via bnx2i - cnic driver interface to
indicate completion of option-2 TCP connect request.

.. _`bnx2i_cm_close_cmpl`:

bnx2i_cm_close_cmpl
===================

.. c:function:: void bnx2i_cm_close_cmpl(struct cnic_sock *cm_sk)

    process tcp conn close completion

    :param struct cnic_sock \*cm_sk:
        cnic sock structure pointer

.. _`bnx2i_cm_close_cmpl.description`:

Description
-----------

function callback exported via bnx2i - cnic driver interface to
indicate completion of option-2 graceful TCP connect shutdown

.. _`bnx2i_cm_abort_cmpl`:

bnx2i_cm_abort_cmpl
===================

.. c:function:: void bnx2i_cm_abort_cmpl(struct cnic_sock *cm_sk)

    process abortive tcp conn teardown completion

    :param struct cnic_sock \*cm_sk:
        cnic sock structure pointer

.. _`bnx2i_cm_abort_cmpl.description`:

Description
-----------

function callback exported via bnx2i - cnic driver interface to
indicate completion of option-2 abortive TCP connect termination

.. _`bnx2i_cm_remote_close`:

bnx2i_cm_remote_close
=====================

.. c:function:: void bnx2i_cm_remote_close(struct cnic_sock *cm_sk)

    process received TCP FIN

    :param struct cnic_sock \*cm_sk:
        *undescribed*

.. _`bnx2i_cm_remote_close.description`:

Description
-----------

function callback exported via bnx2i - cnic driver interface to indicate
async TCP events such as FIN

.. _`bnx2i_cm_remote_abort`:

bnx2i_cm_remote_abort
=====================

.. c:function:: void bnx2i_cm_remote_abort(struct cnic_sock *cm_sk)

    process TCP RST and start conn cleanup

    :param struct cnic_sock \*cm_sk:
        *undescribed*

.. _`bnx2i_cm_remote_abort.description`:

Description
-----------

function callback exported via bnx2i - cnic driver interface to
indicate async TCP events (RST) sent by the peer.

.. _`bnx2i_map_ep_dbell_regs`:

bnx2i_map_ep_dbell_regs
=======================

.. c:function:: int bnx2i_map_ep_dbell_regs(struct bnx2i_endpoint *ep)

    map connection doorbell registers

    :param struct bnx2i_endpoint \*ep:
        bnx2i endpoint

.. _`bnx2i_map_ep_dbell_regs.description`:

Description
-----------

maps connection's SQ and RQ doorbell registers, 5706/5708/5709 hosts these
register in BAR #0. Whereas in 57710 these register are accessed by
mapping BAR #1

.. This file was automatic generated / don't edit.

