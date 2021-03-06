.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/lpfc/lpfc_nvmet.c

.. _`lpfc_nvmet_xmt_ls_rsp_cmp`:

lpfc_nvmet_xmt_ls_rsp_cmp
=========================

.. c:function:: void lpfc_nvmet_xmt_ls_rsp_cmp(struct lpfc_hba *phba, struct lpfc_iocbq *cmdwqe, struct lpfc_wcqe_complete *wcqe)

    Completion handler for LS Response

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

    :param cmdwqe:
        Pointer to driver command WQE object.
    :type cmdwqe: struct lpfc_iocbq \*

    :param wcqe:
        Pointer to driver response CQE object.
    :type wcqe: struct lpfc_wcqe_complete \*

.. _`lpfc_nvmet_xmt_ls_rsp_cmp.description`:

Description
-----------

The function is called from SLI ring event handler with no
lock held. This function is the completion handler for NVME LS commands
The function frees memory resources used for the NVME commands.

.. _`lpfc_nvmet_ctxbuf_post`:

lpfc_nvmet_ctxbuf_post
======================

.. c:function:: void lpfc_nvmet_ctxbuf_post(struct lpfc_hba *phba, struct lpfc_nvmet_ctxbuf *ctx_buf)

    Repost a NVMET RQ DMA buffer and clean up context

    :param phba:
        HBA buffer is associated with
    :type phba: struct lpfc_hba \*

    :param ctx_buf:
        *undescribed*
    :type ctx_buf: struct lpfc_nvmet_ctxbuf \*

.. _`lpfc_nvmet_ctxbuf_post.description`:

Description
-----------

Frees the given DMA buffer in the appropriate way given by
reposting it to its associated RQ so it can be reused.

.. _`lpfc_nvmet_ctxbuf_post.notes`:

Notes
-----

Takes phba->hbalock.  Can be called with or without other locks held.

.. _`lpfc_nvmet_ctxbuf_post.return`:

Return
------

None

.. _`lpfc_nvmet_xmt_fcp_op_cmp`:

lpfc_nvmet_xmt_fcp_op_cmp
=========================

.. c:function:: void lpfc_nvmet_xmt_fcp_op_cmp(struct lpfc_hba *phba, struct lpfc_iocbq *cmdwqe, struct lpfc_wcqe_complete *wcqe)

    Completion handler for FCP Response

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

    :param cmdwqe:
        Pointer to driver command WQE object.
    :type cmdwqe: struct lpfc_iocbq \*

    :param wcqe:
        Pointer to driver response CQE object.
    :type wcqe: struct lpfc_wcqe_complete \*

.. _`lpfc_nvmet_xmt_fcp_op_cmp.description`:

Description
-----------

The function is called from SLI ring event handler with no
lock held. This function is the completion handler for NVME FCP commands
The function frees memory resources used for the NVME commands.

.. _`lpfc_sli4_nvmet_xri_aborted`:

lpfc_sli4_nvmet_xri_aborted
===========================

.. c:function:: void lpfc_sli4_nvmet_xri_aborted(struct lpfc_hba *phba, struct sli4_wcqe_xri_aborted *axri)

    Fast-path process of nvmet xri abort

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param axri:
        pointer to the nvmet xri abort wcqe structure.
    :type axri: struct sli4_wcqe_xri_aborted \*

.. _`lpfc_sli4_nvmet_xri_aborted.description`:

Description
-----------

This routine is invoked by the worker thread to process a SLI4 fast-path
NVMET aborted xri.

.. _`lpfc_nvmet_unsol_ls_buffer`:

lpfc_nvmet_unsol_ls_buffer
==========================

.. c:function:: void lpfc_nvmet_unsol_ls_buffer(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, struct hbq_dmabuf *nvmebuf)

    Process an unsolicited event data buffer

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param pring:
        pointer to a SLI ring.
    :type pring: struct lpfc_sli_ring \*

    :param nvmebuf:
        pointer to lpfc nvme command HBQ data structure.
    :type nvmebuf: struct hbq_dmabuf \*

.. _`lpfc_nvmet_unsol_ls_buffer.description`:

Description
-----------

This routine is used for processing the WQE associated with a unsolicited
event. It first determines whether there is an existing ndlp that matches
the DID from the unsolicited WQE. If not, it will create a new one with
the DID from the unsolicited WQE. The ELS command from the unsolicited
WQE is then used to invoke the proper routine and to set up proper state
of the discovery state machine.

.. _`lpfc_nvmet_unsol_fcp_buffer`:

lpfc_nvmet_unsol_fcp_buffer
===========================

.. c:function:: void lpfc_nvmet_unsol_fcp_buffer(struct lpfc_hba *phba, uint32_t idx, struct rqb_dmabuf *nvmebuf, uint64_t isr_timestamp)

    Process an unsolicited event data buffer

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param idx:
        relative index of MRQ vector
    :type idx: uint32_t

    :param nvmebuf:
        pointer to lpfc nvme command HBQ data structure.
    :type nvmebuf: struct rqb_dmabuf \*

    :param isr_timestamp:
        *undescribed*
    :type isr_timestamp: uint64_t

.. _`lpfc_nvmet_unsol_fcp_buffer.description`:

Description
-----------

This routine is used for processing the WQE associated with a unsolicited
event. It first determines whether there is an existing ndlp that matches
the DID from the unsolicited WQE. If not, it will create a new one with
the DID from the unsolicited WQE. The ELS command from the unsolicited
WQE is then used to invoke the proper routine and to set up proper state
of the discovery state machine.

.. _`lpfc_nvmet_unsol_ls_event`:

lpfc_nvmet_unsol_ls_event
=========================

.. c:function:: void lpfc_nvmet_unsol_ls_event(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, struct lpfc_iocbq *piocb)

    Process an unsolicited event from an nvme nport

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param pring:
        pointer to a SLI ring.
    :type pring: struct lpfc_sli_ring \*

    :param piocb:
        *undescribed*
    :type piocb: struct lpfc_iocbq \*

.. _`lpfc_nvmet_unsol_ls_event.description`:

Description
-----------

This routine is used to process an unsolicited event received from a SLI
(Service Level Interface) ring. The actual processing of the data buffer
associated with the unsolicited event is done by invoking the routine
\ :c:func:`lpfc_nvmet_unsol_ls_buffer`\  after properly set up the buffer from the
SLI RQ on which the unsolicited event was received.

.. _`lpfc_nvmet_unsol_fcp_event`:

lpfc_nvmet_unsol_fcp_event
==========================

.. c:function:: void lpfc_nvmet_unsol_fcp_event(struct lpfc_hba *phba, uint32_t idx, struct rqb_dmabuf *nvmebuf, uint64_t isr_timestamp)

    Process an unsolicited event from an nvme nport

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param idx:
        relative index of MRQ vector
    :type idx: uint32_t

    :param nvmebuf:
        pointer to received nvme data structure.
    :type nvmebuf: struct rqb_dmabuf \*

    :param isr_timestamp:
        *undescribed*
    :type isr_timestamp: uint64_t

.. _`lpfc_nvmet_unsol_fcp_event.description`:

Description
-----------

This routine is used to process an unsolicited event received from a SLI
(Service Level Interface) ring. The actual processing of the data buffer
associated with the unsolicited event is done by invoking the routine
\ :c:func:`lpfc_nvmet_unsol_fcp_buffer`\  after properly set up the buffer from the
SLI RQ on which the unsolicited event was received.

.. _`lpfc_nvmet_prep_ls_wqe`:

lpfc_nvmet_prep_ls_wqe
======================

.. c:function:: struct lpfc_iocbq *lpfc_nvmet_prep_ls_wqe(struct lpfc_hba *phba, struct lpfc_nvmet_rcv_ctx *ctxp, dma_addr_t rspbuf, uint16_t rspsize)

    Allocate and prepare a lpfc wqe data structure

    :param phba:
        pointer to a host N_Port data structure.
    :type phba: struct lpfc_hba \*

    :param ctxp:
        Context info for NVME LS Request
    :type ctxp: struct lpfc_nvmet_rcv_ctx \*

    :param rspbuf:
        DMA buffer of NVME command.
    :type rspbuf: dma_addr_t

    :param rspsize:
        size of the NVME command.
    :type rspsize: uint16_t

.. _`lpfc_nvmet_prep_ls_wqe.description`:

Description
-----------

This routine is used for allocating a lpfc-WQE data structure from
the driver lpfc-WQE free-list and prepare the WQE with the parameters
passed into the routine for discovery state machine to issue an Extended
Link Service (NVME) commands. It is a generic lpfc-WQE allocation
and preparation routine that is used by all the discovery state machine
routines and the NVME command-specific fields will be later set up by
the individual discovery machine routines after calling this routine
allocating and preparing a generic WQE data structure. It fills in the
Buffer Descriptor Entries (BDEs), allocates buffers for both command
payload and response payload (if expected). The reference count on the
ndlp is incremented by 1 and the reference to the ndlp is put into
context1 of the WQE data structure for this WQE to hold the ndlp
reference for the command's callback function to access later.

Return code
Pointer to the newly allocated/prepared nvme wqe data structure
NULL - when nvme wqe data structure allocation/preparation failed

.. _`lpfc_nvmet_sol_fcp_abort_cmp`:

lpfc_nvmet_sol_fcp_abort_cmp
============================

.. c:function:: void lpfc_nvmet_sol_fcp_abort_cmp(struct lpfc_hba *phba, struct lpfc_iocbq *cmdwqe, struct lpfc_wcqe_complete *wcqe)

    Completion handler for ABTS

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

    :param cmdwqe:
        Pointer to driver command WQE object.
    :type cmdwqe: struct lpfc_iocbq \*

    :param wcqe:
        Pointer to driver response CQE object.
    :type wcqe: struct lpfc_wcqe_complete \*

.. _`lpfc_nvmet_sol_fcp_abort_cmp.description`:

Description
-----------

The function is called from SLI ring event handler with no
lock held. This function is the completion handler for NVME ABTS for FCP cmds
The function frees memory resources used for the NVME commands.

.. _`lpfc_nvmet_unsol_fcp_abort_cmp`:

lpfc_nvmet_unsol_fcp_abort_cmp
==============================

.. c:function:: void lpfc_nvmet_unsol_fcp_abort_cmp(struct lpfc_hba *phba, struct lpfc_iocbq *cmdwqe, struct lpfc_wcqe_complete *wcqe)

    Completion handler for ABTS

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

    :param cmdwqe:
        Pointer to driver command WQE object.
    :type cmdwqe: struct lpfc_iocbq \*

    :param wcqe:
        Pointer to driver response CQE object.
    :type wcqe: struct lpfc_wcqe_complete \*

.. _`lpfc_nvmet_unsol_fcp_abort_cmp.description`:

Description
-----------

The function is called from SLI ring event handler with no
lock held. This function is the completion handler for NVME ABTS for FCP cmds
The function frees memory resources used for the NVME commands.

.. _`lpfc_nvmet_xmt_ls_abort_cmp`:

lpfc_nvmet_xmt_ls_abort_cmp
===========================

.. c:function:: void lpfc_nvmet_xmt_ls_abort_cmp(struct lpfc_hba *phba, struct lpfc_iocbq *cmdwqe, struct lpfc_wcqe_complete *wcqe)

    Completion handler for ABTS

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

    :param cmdwqe:
        Pointer to driver command WQE object.
    :type cmdwqe: struct lpfc_iocbq \*

    :param wcqe:
        Pointer to driver response CQE object.
    :type wcqe: struct lpfc_wcqe_complete \*

.. _`lpfc_nvmet_xmt_ls_abort_cmp.description`:

Description
-----------

The function is called from SLI ring event handler with no
lock held. This function is the completion handler for NVME ABTS for LS cmds
The function frees memory resources used for the NVME commands.

.. This file was automatic generated / don't edit.

