.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/lpfc/lpfc_bsg.c

.. _`lpfc_bsg_send_mgmt_cmd_cmp`:

lpfc_bsg_send_mgmt_cmd_cmp
==========================

.. c:function:: void lpfc_bsg_send_mgmt_cmd_cmp(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocbq, struct lpfc_iocbq *rspiocbq)

    lpfc_bsg_send_mgmt_cmd's completion handler

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*cmdiocbq:
        Pointer to command iocb.

    :param struct lpfc_iocbq \*rspiocbq:
        Pointer to response iocb.

.. _`lpfc_bsg_send_mgmt_cmd_cmp.description`:

Description
-----------

This function is the completion handler for iocbs issued using
lpfc_bsg_send_mgmt_cmd function. This function is called by the
ring event handler function without any lock held. This function
can be called from both worker thread context and interrupt
context. This function also can be called from another thread which
cleans up the SLI layer objects.
This function copies the contents of the response iocb to the
response iocb memory object provided by the caller of
lpfc_sli_issue_iocb_wait and then wakes up the thread which
sleeps for the iocb completion.

.. _`lpfc_bsg_send_mgmt_cmd`:

lpfc_bsg_send_mgmt_cmd
======================

.. c:function:: int lpfc_bsg_send_mgmt_cmd(struct bsg_job *job)

    send a CT command from a bsg request

    :param struct bsg_job \*job:
        fc_bsg_job to handle

.. _`lpfc_bsg_rport_els_cmp`:

lpfc_bsg_rport_els_cmp
======================

.. c:function:: void lpfc_bsg_rport_els_cmp(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocbq, struct lpfc_iocbq *rspiocbq)

    lpfc_bsg_rport_els's completion handler

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*cmdiocbq:
        Pointer to command iocb.

    :param struct lpfc_iocbq \*rspiocbq:
        Pointer to response iocb.

.. _`lpfc_bsg_rport_els_cmp.description`:

Description
-----------

This function is the completion handler for iocbs issued using
lpfc_bsg_rport_els_cmp function. This function is called by the
ring event handler function without any lock held. This function
can be called from both worker thread context and interrupt
context. This function also can be called from other thread which
cleans up the SLI layer objects.
This function copies the contents of the response iocb to the
response iocb memory object provided by the caller of
lpfc_sli_issue_iocb_wait and then wakes up the thread which
sleeps for the iocb completion.

.. _`lpfc_bsg_rport_els`:

lpfc_bsg_rport_els
==================

.. c:function:: int lpfc_bsg_rport_els(struct bsg_job *job)

    send an ELS command from a bsg request

    :param struct bsg_job \*job:
        fc_bsg_job to handle

.. _`lpfc_bsg_event_free`:

lpfc_bsg_event_free
===================

.. c:function:: void lpfc_bsg_event_free(struct kref *kref)

    frees an allocated event structure

    :param struct kref \*kref:
        Pointer to a kref.

.. _`lpfc_bsg_event_free.description`:

Description
-----------

Called from kref_put. Back cast the kref into an event structure address.
Free any events to get, delete associated nodes, free any events to see,
free any data then free the event itself.

.. _`lpfc_bsg_event_ref`:

lpfc_bsg_event_ref
==================

.. c:function:: void lpfc_bsg_event_ref(struct lpfc_bsg_event *evt)

    increments the kref for an event

    :param struct lpfc_bsg_event \*evt:
        Pointer to an event structure.

.. _`lpfc_bsg_event_unref`:

lpfc_bsg_event_unref
====================

.. c:function:: void lpfc_bsg_event_unref(struct lpfc_bsg_event *evt)

    Uses kref_put to free an event structure

    :param struct lpfc_bsg_event \*evt:
        Pointer to an event structure.

.. _`lpfc_bsg_event_new`:

lpfc_bsg_event_new
==================

.. c:function:: struct lpfc_bsg_event *lpfc_bsg_event_new(uint32_t ev_mask, int ev_reg_id, uint32_t ev_req_id)

    allocate and initialize a event structure

    :param uint32_t ev_mask:
        Mask of events.

    :param int ev_reg_id:
        Event reg id.

    :param uint32_t ev_req_id:
        Event request id.

.. _`diag_cmd_data_free`:

diag_cmd_data_free
==================

.. c:function:: int diag_cmd_data_free(struct lpfc_hba *phba, struct lpfc_dmabufext *mlist)

    Frees an lpfc dma buffer extension

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_dmabufext \*mlist:
        Pointer to an lpfc dma buffer extension.

.. _`lpfc_bsg_ct_unsol_event`:

lpfc_bsg_ct_unsol_event
=======================

.. c:function:: int lpfc_bsg_ct_unsol_event(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, struct lpfc_iocbq *piocbq)

    process an unsolicited CT command

    :param struct lpfc_hba \*phba:
        *undescribed*

    :param struct lpfc_sli_ring \*pring:
        *undescribed*

    :param struct lpfc_iocbq \*piocbq:
        *undescribed*

.. _`lpfc_bsg_ct_unsol_event.description`:

Description
-----------

This function is called when an unsolicited CT command is received.  It
forwards the event to any processes registered to receive CT events.

.. _`lpfc_bsg_ct_unsol_abort`:

lpfc_bsg_ct_unsol_abort
=======================

.. c:function:: int lpfc_bsg_ct_unsol_abort(struct lpfc_hba *phba, struct hbq_dmabuf *dmabuf)

    handler ct abort to management plane

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct hbq_dmabuf \*dmabuf:
        pointer to a dmabuf that describes the FC sequence

.. _`lpfc_bsg_ct_unsol_abort.description`:

Description
-----------

This function handles abort to the CT command toward management plane
for SLI4 port.

If the pending context of a CT command to management plane present, clears
such context and returns 1 for handled; otherwise, it returns 0 indicating
no context exists.

.. _`lpfc_bsg_hba_set_event`:

lpfc_bsg_hba_set_event
======================

.. c:function:: int lpfc_bsg_hba_set_event(struct bsg_job *job)

    process a SET_EVENT bsg vendor command

    :param struct bsg_job \*job:
        SET_EVENT fc_bsg_job

.. _`lpfc_bsg_hba_get_event`:

lpfc_bsg_hba_get_event
======================

.. c:function:: int lpfc_bsg_hba_get_event(struct bsg_job *job)

    process a GET_EVENT bsg vendor command

    :param struct bsg_job \*job:
        GET_EVENT fc_bsg_job

.. _`lpfc_issue_ct_rsp_cmp`:

lpfc_issue_ct_rsp_cmp
=====================

.. c:function:: void lpfc_issue_ct_rsp_cmp(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocbq, struct lpfc_iocbq *rspiocbq)

    lpfc_issue_ct_rsp's completion handler

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*cmdiocbq:
        Pointer to command iocb.

    :param struct lpfc_iocbq \*rspiocbq:
        Pointer to response iocb.

.. _`lpfc_issue_ct_rsp_cmp.description`:

Description
-----------

This function is the completion handler for iocbs issued using
lpfc_issue_ct_rsp_cmp function. This function is called by the
ring event handler function without any lock held. This function
can be called from both worker thread context and interrupt
context. This function also can be called from other thread which
cleans up the SLI layer objects.
This function copy the contents of the response iocb to the
response iocb memory object provided by the caller of
lpfc_sli_issue_iocb_wait and then wakes up the thread which
sleeps for the iocb completion.

.. _`lpfc_issue_ct_rsp`:

lpfc_issue_ct_rsp
=================

.. c:function:: int lpfc_issue_ct_rsp(struct lpfc_hba *phba, struct bsg_job *job, uint32_t tag, struct lpfc_dmabuf *cmp, struct lpfc_dmabuf *bmp, int num_entry)

    issue a ct response

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct bsg_job \*job:
        Pointer to the job object.

    :param uint32_t tag:
        tag index value into the ports context exchange array.

    :param struct lpfc_dmabuf \*cmp:
        *undescribed*

    :param struct lpfc_dmabuf \*bmp:
        Pointer to a dma buffer descriptor.

    :param int num_entry:
        Number of enties in the bde.

.. _`lpfc_bsg_send_mgmt_rsp`:

lpfc_bsg_send_mgmt_rsp
======================

.. c:function:: int lpfc_bsg_send_mgmt_rsp(struct bsg_job *job)

    process a SEND_MGMT_RESP bsg vendor command

    :param struct bsg_job \*job:
        SEND_MGMT_RESP fc_bsg_job

.. _`lpfc_bsg_diag_mode_enter`:

lpfc_bsg_diag_mode_enter
========================

.. c:function:: int lpfc_bsg_diag_mode_enter(struct lpfc_hba *phba)

    process preparing into device diag loopback mode

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_bsg_diag_mode_enter.description`:

Description
-----------

This function is responsible for preparing driver for diag loopback
on device.

.. _`lpfc_bsg_diag_mode_exit`:

lpfc_bsg_diag_mode_exit
=======================

.. c:function:: void lpfc_bsg_diag_mode_exit(struct lpfc_hba *phba)

    exit process from device diag loopback mode

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_bsg_diag_mode_exit.description`:

Description
-----------

This function is responsible for driver exit processing of setting up
diag loopback mode on device.

.. _`lpfc_sli3_bsg_diag_loopback_mode`:

lpfc_sli3_bsg_diag_loopback_mode
================================

.. c:function:: int lpfc_sli3_bsg_diag_loopback_mode(struct lpfc_hba *phba, struct bsg_job *job)

    process an sli3 bsg vendor command

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct bsg_job \*job:
        LPFC_BSG_VENDOR_DIAG_MODE

.. _`lpfc_sli3_bsg_diag_loopback_mode.description`:

Description
-----------

This function is responsible for placing an sli3  port into diagnostic
loopback mode in order to perform a diagnostic loopback test.
All new scsi requests are blocked, a small delay is used to allow the
scsi requests to complete then the link is brought down. If the link is
is placed in loopback mode then scsi requests are again allowed
so the scsi mid-layer doesn't give up on the port.
All of this is done in-line.

.. _`lpfc_sli4_bsg_set_link_diag_state`:

lpfc_sli4_bsg_set_link_diag_state
=================================

.. c:function:: int lpfc_sli4_bsg_set_link_diag_state(struct lpfc_hba *phba, uint32_t diag)

    set sli4 link diag state

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint32_t diag:
        Flag for set link to diag or nomral operation state.

.. _`lpfc_sli4_bsg_set_link_diag_state.description`:

Description
-----------

This function is responsible for issuing a sli4 mailbox command for setting
link to either diag state or normal operation state.

.. _`lpfc_sli4_bsg_set_internal_loopback`:

lpfc_sli4_bsg_set_internal_loopback
===================================

.. c:function:: int lpfc_sli4_bsg_set_internal_loopback(struct lpfc_hba *phba)

    set sli4 internal loopback diagnostic

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli4_bsg_set_internal_loopback.description`:

Description
-----------

This function is responsible for issuing a sli4 mailbox command for setting
up internal loopback diagnostic.

.. _`lpfc_sli4_diag_fcport_reg_setup`:

lpfc_sli4_diag_fcport_reg_setup
===============================

.. c:function:: int lpfc_sli4_diag_fcport_reg_setup(struct lpfc_hba *phba)

    setup port registrations for diagnostic

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli4_diag_fcport_reg_setup.description`:

Description
-----------

This function set up SLI4 FC port registrations for diagnostic run, which
includes all the rpis, vfi, and also vpi.

.. _`lpfc_sli4_bsg_diag_loopback_mode`:

lpfc_sli4_bsg_diag_loopback_mode
================================

.. c:function:: int lpfc_sli4_bsg_diag_loopback_mode(struct lpfc_hba *phba, struct bsg_job *job)

    process an sli4 bsg vendor command

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct bsg_job \*job:
        LPFC_BSG_VENDOR_DIAG_MODE

.. _`lpfc_sli4_bsg_diag_loopback_mode.description`:

Description
-----------

This function is responsible for placing an sli4 port into diagnostic
loopback mode in order to perform a diagnostic loopback test.

.. _`lpfc_bsg_diag_loopback_mode`:

lpfc_bsg_diag_loopback_mode
===========================

.. c:function:: int lpfc_bsg_diag_loopback_mode(struct bsg_job *job)

    bsg vendor command for diag loopback mode

    :param struct bsg_job \*job:
        LPFC_BSG_VENDOR_DIAG_MODE

.. _`lpfc_bsg_diag_loopback_mode.description`:

Description
-----------

This function is responsible for responding to check and dispatch bsg diag
command from the user to proper driver action routines.

.. _`lpfc_sli4_bsg_diag_mode_end`:

lpfc_sli4_bsg_diag_mode_end
===========================

.. c:function:: int lpfc_sli4_bsg_diag_mode_end(struct bsg_job *job)

    sli4 bsg vendor command for ending diag mode

    :param struct bsg_job \*job:
        LPFC_BSG_VENDOR_DIAG_MODE_END

.. _`lpfc_sli4_bsg_diag_mode_end.description`:

Description
-----------

This function is responsible for responding to check and dispatch bsg diag
command from the user to proper driver action routines.

.. _`lpfc_sli4_bsg_link_diag_test`:

lpfc_sli4_bsg_link_diag_test
============================

.. c:function:: int lpfc_sli4_bsg_link_diag_test(struct bsg_job *job)

    sli4 bsg vendor command for diag link test

    :param struct bsg_job \*job:
        LPFC_BSG_VENDOR_DIAG_LINK_TEST

.. _`lpfc_sli4_bsg_link_diag_test.description`:

Description
-----------

This function is to perform SLI4 diag link test request from the user
applicaiton.

.. _`lpfcdiag_loop_self_reg`:

lpfcdiag_loop_self_reg
======================

.. c:function:: int lpfcdiag_loop_self_reg(struct lpfc_hba *phba, uint16_t *rpi)

    obtains a remote port login id

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object

    :param uint16_t \*rpi:
        Pointer to a remote port login id

.. _`lpfcdiag_loop_self_reg.description`:

Description
-----------

This function obtains a remote port login id so the diag loopback test
can send and receive its own unsolicited CT command.

.. _`lpfcdiag_loop_self_unreg`:

lpfcdiag_loop_self_unreg
========================

.. c:function:: int lpfcdiag_loop_self_unreg(struct lpfc_hba *phba, uint16_t rpi)

    unregs from the rpi

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object

    :param uint16_t rpi:
        Remote port login id

.. _`lpfcdiag_loop_self_unreg.description`:

Description
-----------

This function unregisters the rpi obtained in lpfcdiag_loop_self_reg

.. _`lpfcdiag_loop_get_xri`:

lpfcdiag_loop_get_xri
=====================

.. c:function:: int lpfcdiag_loop_get_xri(struct lpfc_hba *phba, uint16_t rpi, uint16_t *txxri, uint16_t *rxxri)

    obtains the transmit and receive ids

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object

    :param uint16_t rpi:
        Remote port login id

    :param uint16_t \*txxri:
        Pointer to transmit exchange id

    :param uint16_t \*rxxri:
        Pointer to response exchabge id

.. _`lpfcdiag_loop_get_xri.description`:

Description
-----------

This function obtains the transmit and receive ids required to send
an unsolicited ct command with a payload. A special lpfc FsType and CmdRsp
flags are used to the unsolicted response handler is able to process
the ct command sent on the same port.

.. _`lpfc_bsg_dma_page_alloc`:

lpfc_bsg_dma_page_alloc
=======================

.. c:function:: struct lpfc_dmabuf *lpfc_bsg_dma_page_alloc(struct lpfc_hba *phba)

    allocate a bsg mbox page sized dma buffers

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object

.. _`lpfc_bsg_dma_page_alloc.description`:

Description
-----------

This function allocates BSG_MBOX_SIZE (4KB) page size dma buffer and
returns the pointer to the buffer.

.. _`lpfc_bsg_dma_page_free`:

lpfc_bsg_dma_page_free
======================

.. c:function:: void lpfc_bsg_dma_page_free(struct lpfc_hba *phba, struct lpfc_dmabuf *dmabuf)

    free a bsg mbox page sized dma buffer

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_dmabuf \*dmabuf:
        Pointer to the bsg mbox page sized dma buffer descriptor.

.. _`lpfc_bsg_dma_page_free.description`:

Description
-----------

This routine just simply frees a dma buffer and its associated buffer
descriptor referred by \ ``dmabuf``\ .

.. _`lpfc_bsg_dma_page_list_free`:

lpfc_bsg_dma_page_list_free
===========================

.. c:function:: void lpfc_bsg_dma_page_list_free(struct lpfc_hba *phba, struct list_head *dmabuf_list)

    free a list of bsg mbox page sized dma buffers

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct list_head \*dmabuf_list:
        Pointer to a list of bsg mbox page sized dma buffer descs.

.. _`lpfc_bsg_dma_page_list_free.description`:

Description
-----------

This routine just simply frees all dma buffers and their associated buffer
descriptors referred by \ ``dmabuf_list``\ .

.. _`diag_cmd_data_alloc`:

diag_cmd_data_alloc
===================

.. c:function:: struct lpfc_dmabufext *diag_cmd_data_alloc(struct lpfc_hba *phba, struct ulp_bde64 *bpl, uint32_t size, int nocopydata)

    fills in a bde struct with dma buffers

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object

    :param struct ulp_bde64 \*bpl:
        Pointer to 64 bit bde structure

    :param uint32_t size:
        Number of bytes to process

    :param int nocopydata:
        Flag to copy user data into the allocated buffer

.. _`diag_cmd_data_alloc.description`:

Description
-----------

This function allocates page size buffers and populates an lpfc_dmabufext.
If allowed the user data pointed to with indataptr is copied into the kernel
memory. The chained list of page size buffers is returned.

.. _`lpfcdiag_loop_post_rxbufs`:

lpfcdiag_loop_post_rxbufs
=========================

.. c:function:: int lpfcdiag_loop_post_rxbufs(struct lpfc_hba *phba, uint16_t rxxri, size_t len)

    post the receive buffers for an unsol CT cmd

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object

    :param uint16_t rxxri:
        Receive exchange id

    :param size_t len:
        Number of data bytes

.. _`lpfcdiag_loop_post_rxbufs.description`:

Description
-----------

This function allocates and posts a data buffer of sufficient size to receive
an unsolicted CT command.

.. _`lpfc_bsg_diag_loopback_run`:

lpfc_bsg_diag_loopback_run
==========================

.. c:function:: int lpfc_bsg_diag_loopback_run(struct bsg_job *job)

    run loopback on a port by issue ct cmd to itself

    :param struct bsg_job \*job:
        LPFC_BSG_VENDOR_DIAG_TEST fc_bsg_job

.. _`lpfc_bsg_diag_loopback_run.description`:

Description
-----------

This function receives a user data buffer to be transmitted and received on
the same port, the link must be up and in loopback mode prior
to being called.
1. A kernel buffer is allocated to copy the user data into.
2. The port registers with "itself".
3. The transmit and receive exchange ids are obtained.
4. The receive exchange id is posted.
5. A new els loopback event is created.
6. The command and response iocbs are allocated.
7. The cmd iocb FsType is set to elx loopback and the CmdRsp to looppback.

This function is meant to be called n times while the port is in loopback
so it is the apps responsibility to issue a reset to take the port out
of loopback mode.

.. _`lpfc_bsg_get_dfc_rev`:

lpfc_bsg_get_dfc_rev
====================

.. c:function:: int lpfc_bsg_get_dfc_rev(struct bsg_job *job)

    process a GET_DFC_REV bsg vendor command

    :param struct bsg_job \*job:
        GET_DFC_REV fc_bsg_job

.. _`lpfc_bsg_issue_mbox_cmpl`:

lpfc_bsg_issue_mbox_cmpl
========================

.. c:function:: void lpfc_bsg_issue_mbox_cmpl(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmboxq)

    lpfc_bsg_issue_mbox mbox completion handler

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param LPFC_MBOXQ_t \*pmboxq:
        Pointer to mailbox command.

.. _`lpfc_bsg_issue_mbox_cmpl.description`:

Description
-----------

This is completion handler function for mailbox commands issued from
lpfc_bsg_issue_mbox function. This function is called by the
mailbox event handler function with no lock held. This function
will wake up thread waiting on the wait queue pointed by context1
of the mailbox.

.. _`lpfc_bsg_check_cmd_access`:

lpfc_bsg_check_cmd_access
=========================

.. c:function:: int lpfc_bsg_check_cmd_access(struct lpfc_hba *phba, MAILBOX_t *mb, struct lpfc_vport *vport)

    test for a supported mailbox command

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param MAILBOX_t \*mb:
        Pointer to a mailbox object.

    :param struct lpfc_vport \*vport:
        Pointer to a vport object.

.. _`lpfc_bsg_check_cmd_access.description`:

Description
-----------

Some commands require the port to be offline, some may not be called from
the application.

.. _`lpfc_bsg_mbox_ext_session_reset`:

lpfc_bsg_mbox_ext_session_reset
===============================

.. c:function:: void lpfc_bsg_mbox_ext_session_reset(struct lpfc_hba *phba)

    clean up context of multi-buffer mbox session

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_bsg_mbox_ext_session_reset.description`:

Description
-----------

This is routine clean up and reset BSG handling of multi-buffer mbox
command session.

.. _`lpfc_bsg_issue_mbox_ext_handle_job`:

lpfc_bsg_issue_mbox_ext_handle_job
==================================

.. c:function:: struct bsg_job *lpfc_bsg_issue_mbox_ext_handle_job(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmboxq)

    job handler for multi-buffer mbox cmpl

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param LPFC_MBOXQ_t \*pmboxq:
        Pointer to mailbox command.

.. _`lpfc_bsg_issue_mbox_ext_handle_job.description`:

Description
-----------

This is routine handles BSG job for mailbox commands completions with
multiple external buffers.

.. _`lpfc_bsg_issue_read_mbox_ext_cmpl`:

lpfc_bsg_issue_read_mbox_ext_cmpl
=================================

.. c:function:: void lpfc_bsg_issue_read_mbox_ext_cmpl(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmboxq)

    compl handler for multi-buffer read mbox

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param LPFC_MBOXQ_t \*pmboxq:
        Pointer to mailbox command.

.. _`lpfc_bsg_issue_read_mbox_ext_cmpl.description`:

Description
-----------

This is completion handler function for mailbox read commands with multiple
external buffers.

.. _`lpfc_bsg_issue_write_mbox_ext_cmpl`:

lpfc_bsg_issue_write_mbox_ext_cmpl
==================================

.. c:function:: void lpfc_bsg_issue_write_mbox_ext_cmpl(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmboxq)

    cmpl handler for multi-buffer write mbox

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param LPFC_MBOXQ_t \*pmboxq:
        Pointer to mailbox command.

.. _`lpfc_bsg_issue_write_mbox_ext_cmpl.description`:

Description
-----------

This is completion handler function for mailbox write commands with multiple
external buffers.

.. _`lpfc_bsg_sli_cfg_read_cmd_ext`:

lpfc_bsg_sli_cfg_read_cmd_ext
=============================

.. c:function:: int lpfc_bsg_sli_cfg_read_cmd_ext(struct lpfc_hba *phba, struct bsg_job *job, enum nemb_type nemb_tp, struct lpfc_dmabuf *dmabuf)

    sli_config non-embedded mailbox cmd read

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct bsg_job \*job:
        *undescribed*

    :param enum nemb_type nemb_tp:
        Enumerate of non-embedded mailbox command type.

    :param struct lpfc_dmabuf \*dmabuf:
        *undescribed*

.. _`lpfc_bsg_sli_cfg_read_cmd_ext.description`:

Description
-----------

This routine performs SLI_CONFIG (0x9B) read mailbox command operation with
non-embedded external bufffers.

.. _`lpfc_bsg_sli_cfg_write_cmd_ext`:

lpfc_bsg_sli_cfg_write_cmd_ext
==============================

.. c:function:: int lpfc_bsg_sli_cfg_write_cmd_ext(struct lpfc_hba *phba, struct bsg_job *job, enum nemb_type nemb_tp, struct lpfc_dmabuf *dmabuf)

    sli_config non-embedded mailbox cmd write

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct bsg_job \*job:
        *undescribed*

    :param enum nemb_type nemb_tp:
        *undescribed*

    :param struct lpfc_dmabuf \*dmabuf:
        *undescribed*

.. _`lpfc_bsg_sli_cfg_write_cmd_ext.description`:

Description
-----------

This routine performs SLI_CONFIG (0x9B) write mailbox command operation with
non-embedded external bufffers.

.. _`lpfc_bsg_handle_sli_cfg_mbox`:

lpfc_bsg_handle_sli_cfg_mbox
============================

.. c:function:: int lpfc_bsg_handle_sli_cfg_mbox(struct lpfc_hba *phba, struct bsg_job *job, struct lpfc_dmabuf *dmabuf)

    handle sli-cfg mailbox cmd with ext buffer

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct bsg_job \*job:
        *undescribed*

    :param struct lpfc_dmabuf \*dmabuf:
        *undescribed*

.. _`lpfc_bsg_handle_sli_cfg_mbox.description`:

Description
-----------

This routine handles SLI_CONFIG (0x9B) mailbox command with non-embedded
external bufffers, including both 0x9B with non-embedded MSEs and 0x9B
with embedded sussystem 0x1 and opcodes with external HBDs.

.. _`lpfc_bsg_mbox_ext_abort`:

lpfc_bsg_mbox_ext_abort
=======================

.. c:function:: void lpfc_bsg_mbox_ext_abort(struct lpfc_hba *phba)

    request to abort mbox command with ext buffers

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_bsg_mbox_ext_abort.description`:

Description
-----------

This routine is for requesting to abort a pass-through mailbox command with
multiple external buffers due to error condition.

.. _`lpfc_bsg_read_ebuf_get`:

lpfc_bsg_read_ebuf_get
======================

.. c:function:: int lpfc_bsg_read_ebuf_get(struct lpfc_hba *phba, struct bsg_job *job)

    get the next mailbox read external buffer

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct bsg_job \*job:
        *undescribed*

.. _`lpfc_bsg_read_ebuf_get.description`:

Description
-----------

This routine extracts the next mailbox read external buffer back to
user space through BSG.

.. _`lpfc_bsg_write_ebuf_set`:

lpfc_bsg_write_ebuf_set
=======================

.. c:function:: int lpfc_bsg_write_ebuf_set(struct lpfc_hba *phba, struct bsg_job *job, struct lpfc_dmabuf *dmabuf)

    set the next mailbox write external buffer

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct bsg_job \*job:
        *undescribed*

    :param struct lpfc_dmabuf \*dmabuf:
        Pointer to a DMA buffer descriptor.

.. _`lpfc_bsg_write_ebuf_set.description`:

Description
-----------

This routine sets up the next mailbox read external buffer obtained
from user space through BSG.

.. _`lpfc_bsg_handle_sli_cfg_ebuf`:

lpfc_bsg_handle_sli_cfg_ebuf
============================

.. c:function:: int lpfc_bsg_handle_sli_cfg_ebuf(struct lpfc_hba *phba, struct bsg_job *job, struct lpfc_dmabuf *dmabuf)

    handle ext buffer with sli-cfg mailbox cmd

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct bsg_job \*job:
        *undescribed*

    :param struct lpfc_dmabuf \*dmabuf:
        *undescribed*

.. _`lpfc_bsg_handle_sli_cfg_ebuf.description`:

Description
-----------

This routine handles the external buffer with SLI_CONFIG (0x9B) mailbox
command with multiple non-embedded external buffers.

.. _`lpfc_bsg_handle_sli_cfg_ext`:

lpfc_bsg_handle_sli_cfg_ext
===========================

.. c:function:: int lpfc_bsg_handle_sli_cfg_ext(struct lpfc_hba *phba, struct bsg_job *job, struct lpfc_dmabuf *dmabuf)

    handle sli-cfg mailbox with external buffer

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct bsg_job \*job:
        *undescribed*

    :param struct lpfc_dmabuf \*dmabuf:
        *undescribed*

.. _`lpfc_bsg_handle_sli_cfg_ext.description`:

Description
-----------

This routine checkes and handles non-embedded multi-buffer SLI_CONFIG
(0x9B) mailbox commands and external buffers.

.. _`lpfc_bsg_issue_mbox`:

lpfc_bsg_issue_mbox
===================

.. c:function:: int lpfc_bsg_issue_mbox(struct lpfc_hba *phba, struct bsg_job *job, struct lpfc_vport *vport)

    issues a mailbox command on behalf of an app

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct bsg_job \*job:
        *undescribed*

    :param struct lpfc_vport \*vport:
        Pointer to a vport object.

.. _`lpfc_bsg_issue_mbox.description`:

Description
-----------

Allocate a tracking object, mailbox command memory, get a mailbox
from the mailbox pool, copy the caller mailbox command.

If offline and the sli is active we need to poll for the command (port is
being reset) and com-plete the job, otherwise issue the mailbox command and
let our completion handler finish the command.

.. _`lpfc_bsg_mbox_cmd`:

lpfc_bsg_mbox_cmd
=================

.. c:function:: int lpfc_bsg_mbox_cmd(struct bsg_job *job)

    process an fc bsg LPFC_BSG_VENDOR_MBOX command

    :param struct bsg_job \*job:
        MBOX fc_bsg_job for LPFC_BSG_VENDOR_MBOX.

.. _`lpfc_bsg_menlo_cmd_cmp`:

lpfc_bsg_menlo_cmd_cmp
======================

.. c:function:: void lpfc_bsg_menlo_cmd_cmp(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocbq, struct lpfc_iocbq *rspiocbq)

    lpfc_menlo_cmd completion handler

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*cmdiocbq:
        Pointer to command iocb.

    :param struct lpfc_iocbq \*rspiocbq:
        Pointer to response iocb.

.. _`lpfc_bsg_menlo_cmd_cmp.description`:

Description
-----------

This function is the completion handler for iocbs issued using
lpfc_menlo_cmd function. This function is called by the
ring event handler function without any lock held. This function
can be called from both worker thread context and interrupt
context. This function also can be called from another thread which
cleans up the SLI layer objects.
This function copies the contents of the response iocb to the
response iocb memory object provided by the caller of
lpfc_sli_issue_iocb_wait and then wakes up the thread which
sleeps for the iocb completion.

.. _`lpfc_menlo_cmd`:

lpfc_menlo_cmd
==============

.. c:function:: int lpfc_menlo_cmd(struct bsg_job *job)

    send an ioctl for menlo hardware

    :param struct bsg_job \*job:
        fc_bsg_job to handle

.. _`lpfc_menlo_cmd.description`:

Description
-----------

This function issues a gen request 64 CR ioctl for all menlo cmd requests,
all the command completions will return the xri for the command.
For menlo data requests a gen request 64 CX is used to continue the exchange
supplied in the menlo request header xri field.

.. _`lpfc_bsg_hst_vendor`:

lpfc_bsg_hst_vendor
===================

.. c:function:: int lpfc_bsg_hst_vendor(struct bsg_job *job)

    process a vendor-specific fc_bsg_job

    :param struct bsg_job \*job:
        fc_bsg_job to handle

.. _`lpfc_bsg_request`:

lpfc_bsg_request
================

.. c:function:: int lpfc_bsg_request(struct bsg_job *job)

    handle a bsg request from the FC transport

    :param struct bsg_job \*job:
        fc_bsg_job to handle

.. _`lpfc_bsg_timeout`:

lpfc_bsg_timeout
================

.. c:function:: int lpfc_bsg_timeout(struct bsg_job *job)

    handle timeout of a bsg request from the FC transport

    :param struct bsg_job \*job:
        fc_bsg_job that has timed out

.. _`lpfc_bsg_timeout.description`:

Description
-----------

This function just aborts the job's IOCB.  The aborted IOCB will return to
the waiting function which will handle passing the error back to userspace

.. This file was automatic generated / don't edit.

