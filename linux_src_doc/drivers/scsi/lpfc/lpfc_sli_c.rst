.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/lpfc/lpfc_sli.c

.. _`lpfc_sli4_wq_put`:

lpfc_sli4_wq_put
================

.. c:function:: int lpfc_sli4_wq_put(struct lpfc_queue *q, union lpfc_wqe *wqe)

    Put a Work Queue Entry on an Work Queue

    :param struct lpfc_queue \*q:
        The Work Queue to operate on.

    :param union lpfc_wqe \*wqe:
        The work Queue Entry to put on the Work queue.

.. _`lpfc_sli4_wq_put.description`:

Description
-----------

This routine will copy the contents of \ ``wqe``\  to the next available entry on
the \ ``q``\ . This function will then ring the Work Queue Doorbell to signal the
HBA to start processing the Work Queue Entry. This function returns 0 if
successful. If no entries are available on \ ``q``\  then this function will return
-ENOMEM.
The caller is expected to hold the hbalock when calling this routine.

.. _`lpfc_sli4_wq_release`:

lpfc_sli4_wq_release
====================

.. c:function:: uint32_t lpfc_sli4_wq_release(struct lpfc_queue *q, uint32_t index)

    Updates internal hba index for WQ

    :param struct lpfc_queue \*q:
        The Work Queue to operate on.

    :param uint32_t index:
        The index to advance the hba index to.

.. _`lpfc_sli4_wq_release.description`:

Description
-----------

This routine will update the HBA index of a queue to reflect consumption of
Work Queue Entries by the HBA. When the HBA indicates that it has consumed
an entry the host calls this function to update the queue's internal
pointers. This routine returns the number of entries that were consumed by
the HBA.

.. _`lpfc_sli4_mq_put`:

lpfc_sli4_mq_put
================

.. c:function:: uint32_t lpfc_sli4_mq_put(struct lpfc_queue *q, struct lpfc_mqe *mqe)

    Put a Mailbox Queue Entry on an Mailbox Queue

    :param struct lpfc_queue \*q:
        The Mailbox Queue to operate on.

    :param struct lpfc_mqe \*mqe:
        *undescribed*

.. _`lpfc_sli4_mq_put.description`:

Description
-----------

This routine will copy the contents of \ ``mqe``\  to the next available entry on
the \ ``q``\ . This function will then ring the Work Queue Doorbell to signal the
HBA to start processing the Work Queue Entry. This function returns 0 if
successful. If no entries are available on \ ``q``\  then this function will return
-ENOMEM.
The caller is expected to hold the hbalock when calling this routine.

.. _`lpfc_sli4_mq_release`:

lpfc_sli4_mq_release
====================

.. c:function:: uint32_t lpfc_sli4_mq_release(struct lpfc_queue *q)

    Updates internal hba index for MQ

    :param struct lpfc_queue \*q:
        The Mailbox Queue to operate on.

.. _`lpfc_sli4_mq_release.description`:

Description
-----------

This routine will update the HBA index of a queue to reflect consumption of
a Mailbox Queue Entry by the HBA. When the HBA indicates that it has consumed
an entry the host calls this function to update the queue's internal
pointers. This routine returns the number of entries that were consumed by
the HBA.

.. _`lpfc_sli4_eq_get`:

lpfc_sli4_eq_get
================

.. c:function:: struct lpfc_eqe *lpfc_sli4_eq_get(struct lpfc_queue *q)

    Gets the next valid EQE from a EQ

    :param struct lpfc_queue \*q:
        The Event Queue to get the first valid EQE from

.. _`lpfc_sli4_eq_get.description`:

Description
-----------

This routine will get the first valid Event Queue Entry from \ ``q``\ , update
the queue's internal hba index, and return the EQE. If no valid EQEs are in
the Queue (no more work to do), or the Queue is full of EQEs that have been
processed, but not popped back to the HBA then this routine will return NULL.

.. _`lpfc_sli4_eq_clr_intr`:

lpfc_sli4_eq_clr_intr
=====================

.. c:function:: void lpfc_sli4_eq_clr_intr(struct lpfc_queue *q)

    Turn off interrupts from this EQ

    :param struct lpfc_queue \*q:
        The Event Queue to disable interrupts

.. _`lpfc_sli4_eq_release`:

lpfc_sli4_eq_release
====================

.. c:function:: uint32_t lpfc_sli4_eq_release(struct lpfc_queue *q, bool arm)

    Indicates the host has finished processing an EQ

    :param struct lpfc_queue \*q:
        The Event Queue that the host has completed processing for.

    :param bool arm:
        Indicates whether the host wants to arms this CQ.

.. _`lpfc_sli4_eq_release.description`:

Description
-----------

This routine will mark all Event Queue Entries on \ ``q``\ , from the last
known completed entry to the last entry that was processed, as completed
by clearing the valid bit for each completion queue entry. Then it will
notify the HBA, by ringing the doorbell, that the EQEs have been processed.
The internal host index in the \ ``q``\  will be updated by this routine to indicate
that the host has finished processing the entries. The \ ``arm``\  parameter
indicates that the queue should be rearmed when ringing the doorbell.

This function will return the number of EQEs that were popped.

.. _`lpfc_sli4_cq_get`:

lpfc_sli4_cq_get
================

.. c:function:: struct lpfc_cqe *lpfc_sli4_cq_get(struct lpfc_queue *q)

    Gets the next valid CQE from a CQ

    :param struct lpfc_queue \*q:
        The Completion Queue to get the first valid CQE from

.. _`lpfc_sli4_cq_get.description`:

Description
-----------

This routine will get the first valid Completion Queue Entry from \ ``q``\ , update
the queue's internal hba index, and return the CQE. If no valid CQEs are in
the Queue (no more work to do), or the Queue is full of CQEs that have been
processed, but not popped back to the HBA then this routine will return NULL.

.. _`lpfc_sli4_cq_release`:

lpfc_sli4_cq_release
====================

.. c:function:: uint32_t lpfc_sli4_cq_release(struct lpfc_queue *q, bool arm)

    Indicates the host has finished processing a CQ

    :param struct lpfc_queue \*q:
        The Completion Queue that the host has completed processing for.

    :param bool arm:
        Indicates whether the host wants to arms this CQ.

.. _`lpfc_sli4_cq_release.description`:

Description
-----------

This routine will mark all Completion queue entries on \ ``q``\ , from the last
known completed entry to the last entry that was processed, as completed
by clearing the valid bit for each completion queue entry. Then it will
notify the HBA, by ringing the doorbell, that the CQEs have been processed.
The internal host index in the \ ``q``\  will be updated by this routine to indicate
that the host has finished processing the entries. The \ ``arm``\  parameter
indicates that the queue should be rearmed when ringing the doorbell.

This function will return the number of CQEs that were released.

.. _`lpfc_sli4_rq_put`:

lpfc_sli4_rq_put
================

.. c:function:: int lpfc_sli4_rq_put(struct lpfc_queue *hq, struct lpfc_queue *dq, struct lpfc_rqe *hrqe, struct lpfc_rqe *drqe)

    Put a Receive Buffer Queue Entry on a Receive Queue

    :param struct lpfc_queue \*hq:
        *undescribed*

    :param struct lpfc_queue \*dq:
        *undescribed*

    :param struct lpfc_rqe \*hrqe:
        *undescribed*

    :param struct lpfc_rqe \*drqe:
        *undescribed*

.. _`lpfc_sli4_rq_put.description`:

Description
-----------

This routine will copy the contents of \ ``wqe``\  to the next available entry on
the \ ``q``\ . This function will then ring the Receive Queue Doorbell to signal the
HBA to start processing the Receive Queue Entry. This function returns the
index that the rqe was copied to if successful. If no entries are available
on \ ``q``\  then this function will return -ENOMEM.
The caller is expected to hold the hbalock when calling this routine.

.. _`lpfc_sli4_rq_release`:

lpfc_sli4_rq_release
====================

.. c:function:: uint32_t lpfc_sli4_rq_release(struct lpfc_queue *hq, struct lpfc_queue *dq)

    Updates internal hba index for RQ

    :param struct lpfc_queue \*hq:
        *undescribed*

    :param struct lpfc_queue \*dq:
        *undescribed*

.. _`lpfc_sli4_rq_release.description`:

Description
-----------

This routine will update the HBA index of a queue to reflect consumption of
one Receive Queue Entry by the HBA. When the HBA indicates that it has
consumed an entry the host calls this function to update the queue's
internal pointers. This routine returns the number of entries that were
consumed by the HBA.

.. _`lpfc_cmd_iocb`:

lpfc_cmd_iocb
=============

.. c:function:: IOCB_t *lpfc_cmd_iocb(struct lpfc_hba *phba, struct lpfc_sli_ring *pring)

    Get next command iocb entry in the ring

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

.. _`lpfc_cmd_iocb.description`:

Description
-----------

This function returns pointer to next command iocb entry
in the command ring. The caller must hold hbalock to prevent
other threads consume the next command iocb.
SLI-2/SLI-3 provide different sized iocbs.

.. _`lpfc_resp_iocb`:

lpfc_resp_iocb
==============

.. c:function:: IOCB_t *lpfc_resp_iocb(struct lpfc_hba *phba, struct lpfc_sli_ring *pring)

    Get next response iocb entry in the ring

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

.. _`lpfc_resp_iocb.description`:

Description
-----------

This function returns pointer to next response iocb entry
in the response ring. The caller must hold hbalock to make sure
that no other thread consume the next response iocb.
SLI-2/SLI-3 provide different sized iocbs.

.. _`__lpfc_sli_get_iocbq`:

\__lpfc_sli_get_iocbq
=====================

.. c:function:: struct lpfc_iocbq *__lpfc_sli_get_iocbq(struct lpfc_hba *phba)

    Allocates an iocb object from iocb pool

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`__lpfc_sli_get_iocbq.description`:

Description
-----------

This function is called with hbalock held. This function
allocates a new driver iocb object from the iocb pool. If the
allocation is successful, it returns pointer to the newly
allocated iocb object else it returns NULL.

.. _`__lpfc_clear_active_sglq`:

\__lpfc_clear_active_sglq
=========================

.. c:function:: struct lpfc_sglq *__lpfc_clear_active_sglq(struct lpfc_hba *phba, uint16_t xritag)

    Remove the active sglq for this XRI.

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint16_t xritag:
        XRI value.

.. _`__lpfc_clear_active_sglq.description`:

Description
-----------

This function clears the sglq pointer from the array of acive
sglq's. The xritag that is passed in is used to index into the
array. Before the xritag can be used it needs to be adjusted
by subtracting the xribase.

Returns sglq ponter = success, NULL = Failure.

.. _`__lpfc_get_active_sglq`:

\__lpfc_get_active_sglq
=======================

.. c:function:: struct lpfc_sglq *__lpfc_get_active_sglq(struct lpfc_hba *phba, uint16_t xritag)

    Get the active sglq for this XRI.

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint16_t xritag:
        XRI value.

.. _`__lpfc_get_active_sglq.description`:

Description
-----------

This function returns the sglq pointer from the array of acive
sglq's. The xritag that is passed in is used to index into the
array. Before the xritag can be used it needs to be adjusted
by subtracting the xribase.

Returns sglq ponter = success, NULL = Failure.

.. _`lpfc_clr_rrq_active`:

lpfc_clr_rrq_active
===================

.. c:function:: void lpfc_clr_rrq_active(struct lpfc_hba *phba, uint16_t xritag, struct lpfc_node_rrq *rrq)

    Clears RRQ active bit in xri_bitmap.

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint16_t xritag:
        xri used in this exchange.

    :param struct lpfc_node_rrq \*rrq:
        The RRQ to be cleared.

.. _`lpfc_handle_rrq_active`:

lpfc_handle_rrq_active
======================

.. c:function:: void lpfc_handle_rrq_active(struct lpfc_hba *phba)

    Checks if RRQ has waithed RATOV.

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_handle_rrq_active.description`:

Description
-----------

This function is called with hbalock held. This function
Checks if stop_time (ratov from setting rrq active) has
been reached, if it has and the send_rrq flag is set then
it will call lpfc_send_rrq. If the send_rrq flag is not set
then it will just call the routine to clear the rrq and
free the rrq resource.
The timer is set to the next rrq that is going to expire before
leaving the routine.

.. _`lpfc_get_active_rrq`:

lpfc_get_active_rrq
===================

.. c:function:: struct lpfc_node_rrq *lpfc_get_active_rrq(struct lpfc_vport *vport, uint16_t xri, uint32_t did)

    Get the active RRQ for this exchange.

    :param struct lpfc_vport \*vport:
        Pointer to vport context object.

    :param uint16_t xri:
        The xri used in the exchange.

    :param uint32_t did:
        The targets DID for this exchange.

.. _`lpfc_get_active_rrq.description`:

Description
-----------

returns NULL = rrq not found in the phba->active_rrq_list.
rrq = rrq for this xri and target.

.. _`lpfc_cleanup_vports_rrqs`:

lpfc_cleanup_vports_rrqs
========================

.. c:function:: void lpfc_cleanup_vports_rrqs(struct lpfc_vport *vport, struct lpfc_nodelist *ndlp)

    Remove and clear the active RRQ for this vport.

    :param struct lpfc_vport \*vport:
        Pointer to vport context object.

    :param struct lpfc_nodelist \*ndlp:
        Pointer to the lpfc_node_list structure.
        If ndlp is NULL Remove all active RRQs for this vport from the
        phba->active_rrq_list and clear the rrq.
        If ndlp is not NULL then only remove rrqs for this vport & this ndlp.

.. _`lpfc_test_rrq_active`:

lpfc_test_rrq_active
====================

.. c:function:: int lpfc_test_rrq_active(struct lpfc_hba *phba, struct lpfc_nodelist *ndlp, uint16_t xritag)

    Test RRQ bit in xri_bitmap.

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_nodelist \*ndlp:
        Targets nodelist pointer for this exchange.
        \ ``xritag``\  the xri in the bitmap to test.

    :param uint16_t xritag:
        *undescribed*

.. _`lpfc_test_rrq_active.description`:

Description
-----------

This function is called with hbalock held. This function
returns 0 = rrq not active for this xri
1 = rrq is valid for this xri.

.. _`lpfc_set_rrq_active`:

lpfc_set_rrq_active
===================

.. c:function:: int lpfc_set_rrq_active(struct lpfc_hba *phba, struct lpfc_nodelist *ndlp, uint16_t xritag, uint16_t rxid, uint16_t send_rrq)

    set RRQ active bit in xri_bitmap.

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_nodelist \*ndlp:
        nodelist pointer for this target.

    :param uint16_t xritag:
        xri used in this exchange.

    :param uint16_t rxid:
        Remote Exchange ID.

    :param uint16_t send_rrq:
        Flag used to determine if we should send rrq els cmd.

.. _`lpfc_set_rrq_active.description`:

Description
-----------

This function takes the hbalock.
The active bit is always set in the active rrq xri_bitmap even
if there is no slot avaiable for the other rrq information.

returns 0 rrq actived for this xri
< 0 No memory or invalid ndlp.

.. _`__lpfc_sli_get_els_sglq`:

\__lpfc_sli_get_els_sglq
========================

.. c:function:: struct lpfc_sglq *__lpfc_sli_get_els_sglq(struct lpfc_hba *phba, struct lpfc_iocbq *piocbq)

    Allocates an iocb object from sgl pool

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*piocbq:
        *undescribed*

.. _`__lpfc_sli_get_els_sglq.description`:

Description
-----------

This function is called with the ring lock held. This function
gets a new driver sglq object from the sglq list. If the
list is not empty then it is successful, it returns pointer to the newly
allocated sglq object else it returns NULL.

.. _`__lpfc_sli_get_nvmet_sglq`:

\__lpfc_sli_get_nvmet_sglq
==========================

.. c:function:: struct lpfc_sglq *__lpfc_sli_get_nvmet_sglq(struct lpfc_hba *phba, struct lpfc_iocbq *piocbq)

    Allocates an iocb object from sgl pool

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*piocbq:
        *undescribed*

.. _`__lpfc_sli_get_nvmet_sglq.description`:

Description
-----------

This function is called with the sgl_list lock held. This function
gets a new driver sglq object from the sglq list. If the
list is not empty then it is successful, it returns pointer to the newly
allocated sglq object else it returns NULL.

.. _`lpfc_sli_get_iocbq`:

lpfc_sli_get_iocbq
==================

.. c:function:: struct lpfc_iocbq *lpfc_sli_get_iocbq(struct lpfc_hba *phba)

    Allocates an iocb object from iocb pool

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_get_iocbq.description`:

Description
-----------

This function is called with no lock held. This function
allocates a new driver iocb object from the iocb pool. If the
allocation is successful, it returns pointer to the newly
allocated iocb object else it returns NULL.

.. _`__lpfc_sli_release_iocbq_s4`:

\__lpfc_sli_release_iocbq_s4
============================

.. c:function:: void __lpfc_sli_release_iocbq_s4(struct lpfc_hba *phba, struct lpfc_iocbq *iocbq)

    Release iocb to the iocb pool

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*iocbq:
        Pointer to driver iocb object.

.. _`__lpfc_sli_release_iocbq_s4.description`:

Description
-----------

This function is called with hbalock held to release driver
iocb object to the iocb pool. The iotag in the iocb object
does not change for each use of the iocb object. This function
clears all other fields of the iocb object when it is freed.
The sqlq structure that holds the xritag and phys and virtual
mappings for the scatter gather list is retrieved from the
active array of sglq. The get of the sglq pointer also clears
the entry in the array. If the status of the IO indiactes that
this IO was aborted then the sglq entry it put on the
lpfc_abts_els_sgl_list until the CQ_ABORTED_XRI is received. If the
IO has good status or fails for any other reason then the sglq
entry is added to the free list (lpfc_els_sgl_list).

.. _`__lpfc_sli_release_iocbq_s3`:

\__lpfc_sli_release_iocbq_s3
============================

.. c:function:: void __lpfc_sli_release_iocbq_s3(struct lpfc_hba *phba, struct lpfc_iocbq *iocbq)

    Release iocb to the iocb pool

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*iocbq:
        Pointer to driver iocb object.

.. _`__lpfc_sli_release_iocbq_s3.description`:

Description
-----------

This function is called with hbalock held to release driver
iocb object to the iocb pool. The iotag in the iocb object
does not change for each use of the iocb object. This function
clears all other fields of the iocb object when it is freed.

.. _`__lpfc_sli_release_iocbq`:

\__lpfc_sli_release_iocbq
=========================

.. c:function:: void __lpfc_sli_release_iocbq(struct lpfc_hba *phba, struct lpfc_iocbq *iocbq)

    Release iocb to the iocb pool

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*iocbq:
        Pointer to driver iocb object.

.. _`__lpfc_sli_release_iocbq.description`:

Description
-----------

This function is called with hbalock held to release driver
iocb object to the iocb pool. The iotag in the iocb object
does not change for each use of the iocb object. This function
clears all other fields of the iocb object when it is freed.

.. _`lpfc_sli_release_iocbq`:

lpfc_sli_release_iocbq
======================

.. c:function:: void lpfc_sli_release_iocbq(struct lpfc_hba *phba, struct lpfc_iocbq *iocbq)

    Release iocb to the iocb pool

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*iocbq:
        Pointer to driver iocb object.

.. _`lpfc_sli_release_iocbq.description`:

Description
-----------

This function is called with no lock held to release the iocb to
iocb pool.

.. _`lpfc_sli_cancel_iocbs`:

lpfc_sli_cancel_iocbs
=====================

.. c:function:: void lpfc_sli_cancel_iocbs(struct lpfc_hba *phba, struct list_head *iocblist, uint32_t ulpstatus, uint32_t ulpWord4)

    Cancel all iocbs from a list.

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct list_head \*iocblist:
        List of IOCBs.

    :param uint32_t ulpstatus:
        ULP status in IOCB command field.

    :param uint32_t ulpWord4:
        ULP word-4 in IOCB command field.

.. _`lpfc_sli_cancel_iocbs.description`:

Description
-----------

This function is called with a list of IOCBs to cancel. It cancels the IOCB
on the list by invoking the complete callback function associated with the
IOCB with the provided \ ``ulpstatus``\  and \ ``ulpword4``\  set to the IOCB commond
fields.

.. _`lpfc_sli_iocb_cmd_type`:

lpfc_sli_iocb_cmd_type
======================

.. c:function:: lpfc_iocb_type lpfc_sli_iocb_cmd_type(uint8_t iocb_cmnd)

    Get the iocb type

    :param uint8_t iocb_cmnd:
        iocb command code.

.. _`lpfc_sli_iocb_cmd_type.description`:

Description
-----------

This function is called by ring event handler function to get the iocb type.
This function translates the iocb command to an iocb command type used to
decide the final disposition of each completed IOCB.
The function returns
LPFC_UNKNOWN_IOCB if it is an unsupported iocb
LPFC_SOL_IOCB     if it is a solicited iocb completion
LPFC_ABORT_IOCB   if it is an abort iocb
LPFC_UNSOL_IOCB   if it is an unsolicited iocb

The caller is not required to hold any lock.

.. _`lpfc_sli_ring_map`:

lpfc_sli_ring_map
=================

.. c:function:: int lpfc_sli_ring_map(struct lpfc_hba *phba)

    Issue config_ring mbox for all rings

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_ring_map.description`:

Description
-----------

This function is called from SLI initialization code
to configure every ring of the HBA's SLI interface. The
caller is not required to hold any lock. This function issues
a config_ring mailbox command for each ring.
This function returns zero if successful else returns a negative
error code.

.. _`lpfc_sli_ringtxcmpl_put`:

lpfc_sli_ringtxcmpl_put
=======================

.. c:function:: int lpfc_sli_ringtxcmpl_put(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, struct lpfc_iocbq *piocb)

    Adds new iocb to the txcmplq

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param struct lpfc_iocbq \*piocb:
        Pointer to the driver iocb object.

.. _`lpfc_sli_ringtxcmpl_put.description`:

Description
-----------

This function is called with hbalock held. The function adds the
new iocb to txcmplq of the given ring. This function always returns
0. If this function is called for ELS ring, this function checks if
there is a vport associated with the ELS command. This function also
starts els_tmofunc timer if this is an ELS command.

.. _`lpfc_sli_ringtx_get`:

lpfc_sli_ringtx_get
===================

.. c:function:: struct lpfc_iocbq *lpfc_sli_ringtx_get(struct lpfc_hba *phba, struct lpfc_sli_ring *pring)

    Get first element of the txq

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

.. _`lpfc_sli_ringtx_get.description`:

Description
-----------

This function is called with hbalock held to get next
iocb in txq of the given ring. If there is any iocb in
the txq, the function returns first iocb in the list after
removing the iocb from the list, else it returns NULL.

.. _`lpfc_sli_next_iocb_slot`:

lpfc_sli_next_iocb_slot
=======================

.. c:function:: IOCB_t *lpfc_sli_next_iocb_slot(struct lpfc_hba *phba, struct lpfc_sli_ring *pring)

    Get next iocb slot in the ring

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

.. _`lpfc_sli_next_iocb_slot.description`:

Description
-----------

This function is called with hbalock held and the caller must post the
iocb without releasing the lock. If the caller releases the lock,
iocb slot returned by the function is not guaranteed to be available.
The function returns pointer to the next available iocb slot if there
is available slot in the ring, else it returns NULL.
If the get index of the ring is ahead of the put index, the function
will post an error attention event to the worker thread to take the
HBA to offline state.

.. _`lpfc_sli_next_iotag`:

lpfc_sli_next_iotag
===================

.. c:function:: uint16_t lpfc_sli_next_iotag(struct lpfc_hba *phba, struct lpfc_iocbq *iocbq)

    Get an iotag for the iocb

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*iocbq:
        Pointer to driver iocb object.

.. _`lpfc_sli_next_iotag.description`:

Description
-----------

This function gets an iotag for the iocb. If there is no unused iotag and
the iocbq_lookup_len < 0xffff, this function allocates a bigger iotag_lookup
array and assigns a new iotag.
The function returns the allocated iotag if successful, else returns zero.
Zero is not a valid iotag.
The caller is not required to hold any lock.

.. _`lpfc_sli_submit_iocb`:

lpfc_sli_submit_iocb
====================

.. c:function:: void lpfc_sli_submit_iocb(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, IOCB_t *iocb, struct lpfc_iocbq *nextiocb)

    Submit an iocb to the firmware

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param IOCB_t \*iocb:
        Pointer to iocb slot in the ring.

    :param struct lpfc_iocbq \*nextiocb:
        Pointer to driver iocb object which need to be
        posted to firmware.

.. _`lpfc_sli_submit_iocb.description`:

Description
-----------

This function is called with hbalock held to post a new iocb to
the firmware. This function copies the new iocb to ring iocb slot and
updates the ring pointers. It adds the new iocb to txcmplq if there is
a completion call back for this iocb else the function will free the
iocb object.

.. _`lpfc_sli_update_full_ring`:

lpfc_sli_update_full_ring
=========================

.. c:function:: void lpfc_sli_update_full_ring(struct lpfc_hba *phba, struct lpfc_sli_ring *pring)

    Update the chip attention register

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

.. _`lpfc_sli_update_full_ring.description`:

Description
-----------

The caller is not required to hold any lock for calling this function.
This function updates the chip attention bits for the ring to inform firmware
that there are pending work to be done for this ring and requests an
interrupt when there is space available in the ring. This function is
called when the driver is unable to post more iocbs to the ring due
to unavailability of space in the ring.

.. _`lpfc_sli_update_ring`:

lpfc_sli_update_ring
====================

.. c:function:: void lpfc_sli_update_ring(struct lpfc_hba *phba, struct lpfc_sli_ring *pring)

    Update chip attention register

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

.. _`lpfc_sli_update_ring.description`:

Description
-----------

This function updates the chip attention register bit for the
given ring to inform HBA that there is more work to be done
in this ring. The caller is not required to hold any lock.

.. _`lpfc_sli_resume_iocb`:

lpfc_sli_resume_iocb
====================

.. c:function:: void lpfc_sli_resume_iocb(struct lpfc_hba *phba, struct lpfc_sli_ring *pring)

    Process iocbs in the txq

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

.. _`lpfc_sli_resume_iocb.description`:

Description
-----------

This function is called with hbalock held to post pending iocbs
in the txq to the firmware. This function is called when driver
detects space available in the ring.

.. _`lpfc_sli_next_hbq_slot`:

lpfc_sli_next_hbq_slot
======================

.. c:function:: struct lpfc_hbq_entry *lpfc_sli_next_hbq_slot(struct lpfc_hba *phba, uint32_t hbqno)

    Get next hbq entry for the HBQ

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint32_t hbqno:
        HBQ number.

.. _`lpfc_sli_next_hbq_slot.description`:

Description
-----------

This function is called with hbalock held to get the next
available slot for the given HBQ. If there is free slot
available for the HBQ it will return pointer to the next available
HBQ entry else it will return NULL.

.. _`lpfc_sli_hbqbuf_free_all`:

lpfc_sli_hbqbuf_free_all
========================

.. c:function:: void lpfc_sli_hbqbuf_free_all(struct lpfc_hba *phba)

    Free all the hbq buffers

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_hbqbuf_free_all.description`:

Description
-----------

This function is called with no lock held to free all the
hbq buffers while uninitializing the SLI interface. It also
frees the HBQ buffers returned by the firmware but not yet
processed by the upper layers.

.. _`lpfc_sli_hbq_to_firmware`:

lpfc_sli_hbq_to_firmware
========================

.. c:function:: int lpfc_sli_hbq_to_firmware(struct lpfc_hba *phba, uint32_t hbqno, struct hbq_dmabuf *hbq_buf)

    Post the hbq buffer to firmware

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint32_t hbqno:
        HBQ number.

    :param struct hbq_dmabuf \*hbq_buf:
        Pointer to HBQ buffer.

.. _`lpfc_sli_hbq_to_firmware.description`:

Description
-----------

This function is called with the hbalock held to post a
hbq buffer to the firmware. If the function finds an empty
slot in the HBQ, it will post the buffer. The function will return
pointer to the hbq entry if it successfully post the buffer
else it will return NULL.

.. _`lpfc_sli_hbq_to_firmware_s3`:

lpfc_sli_hbq_to_firmware_s3
===========================

.. c:function:: int lpfc_sli_hbq_to_firmware_s3(struct lpfc_hba *phba, uint32_t hbqno, struct hbq_dmabuf *hbq_buf)

    Post the hbq buffer to SLI3 firmware

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint32_t hbqno:
        HBQ number.

    :param struct hbq_dmabuf \*hbq_buf:
        Pointer to HBQ buffer.

.. _`lpfc_sli_hbq_to_firmware_s3.description`:

Description
-----------

This function is called with the hbalock held to post a hbq buffer to the
firmware. If the function finds an empty slot in the HBQ, it will post the
buffer and place it on the hbq_buffer_list. The function will return zero if
it successfully post the buffer else it will return an error.

.. _`lpfc_sli_hbq_to_firmware_s4`:

lpfc_sli_hbq_to_firmware_s4
===========================

.. c:function:: int lpfc_sli_hbq_to_firmware_s4(struct lpfc_hba *phba, uint32_t hbqno, struct hbq_dmabuf *hbq_buf)

    Post the hbq buffer to SLI4 firmware

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint32_t hbqno:
        HBQ number.

    :param struct hbq_dmabuf \*hbq_buf:
        Pointer to HBQ buffer.

.. _`lpfc_sli_hbq_to_firmware_s4.description`:

Description
-----------

This function is called with the hbalock held to post an RQE to the SLI4
firmware. If able to post the RQE to the RQ it will queue the hbq entry to
the hbq_buffer_list and return zero, otherwise it will return an error.

.. _`lpfc_sli_hbqbuf_fill_hbqs`:

lpfc_sli_hbqbuf_fill_hbqs
=========================

.. c:function:: int lpfc_sli_hbqbuf_fill_hbqs(struct lpfc_hba *phba, uint32_t hbqno, uint32_t count)

    Post more hbq buffers to HBQ

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint32_t hbqno:
        HBQ number.

    :param uint32_t count:
        Number of HBQ buffers to be posted.

.. _`lpfc_sli_hbqbuf_fill_hbqs.description`:

Description
-----------

This function is called with no lock held to post more hbq buffers to the
given HBQ. The function returns the number of HBQ buffers successfully
posted.

.. _`lpfc_sli_hbqbuf_add_hbqs`:

lpfc_sli_hbqbuf_add_hbqs
========================

.. c:function:: int lpfc_sli_hbqbuf_add_hbqs(struct lpfc_hba *phba, uint32_t qno)

    Post more HBQ buffers to firmware

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint32_t qno:
        HBQ number.

.. _`lpfc_sli_hbqbuf_add_hbqs.description`:

Description
-----------

This function posts more buffers to the HBQ. This function
is called with no lock held. The function returns the number of HBQ entries
successfully allocated.

.. _`lpfc_sli_hbqbuf_init_hbqs`:

lpfc_sli_hbqbuf_init_hbqs
=========================

.. c:function:: int lpfc_sli_hbqbuf_init_hbqs(struct lpfc_hba *phba, uint32_t qno)

    Post initial buffers to the HBQ

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint32_t qno:
        HBQ queue number.

.. _`lpfc_sli_hbqbuf_init_hbqs.description`:

Description
-----------

This function is called from SLI initialization code path with
no lock held to post initial HBQ buffers to firmware. The
function returns the number of HBQ entries successfully allocated.

.. _`lpfc_sli_hbqbuf_get`:

lpfc_sli_hbqbuf_get
===================

.. c:function:: struct hbq_dmabuf *lpfc_sli_hbqbuf_get(struct list_head *rb_list)

    Remove the first hbq off of an hbq list

    :param struct list_head \*rb_list:
        *undescribed*

.. _`lpfc_sli_hbqbuf_get.description`:

Description
-----------

This function removes the first hbq buffer on an hbq list and returns a
pointer to that buffer. If it finds no buffers on the list it returns NULL.

.. _`lpfc_sli_rqbuf_get`:

lpfc_sli_rqbuf_get
==================

.. c:function:: struct rqb_dmabuf *lpfc_sli_rqbuf_get(struct lpfc_hba *phba, struct lpfc_queue *hrq)

    Remove the first dma buffer off of an RQ list

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_queue \*hrq:
        *undescribed*

.. _`lpfc_sli_rqbuf_get.description`:

Description
-----------

This function removes the first RQ buffer on an RQ buffer list and returns a
pointer to that buffer. If it finds no buffers on the list it returns NULL.

.. _`lpfc_sli_hbqbuf_find`:

lpfc_sli_hbqbuf_find
====================

.. c:function:: struct hbq_dmabuf *lpfc_sli_hbqbuf_find(struct lpfc_hba *phba, uint32_t tag)

    Find the hbq buffer associated with a tag

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint32_t tag:
        Tag of the hbq buffer.

.. _`lpfc_sli_hbqbuf_find.description`:

Description
-----------

This function searches for the hbq buffer associated with the given tag in
the hbq buffer list. If it finds the hbq buffer, it returns the hbq_buffer
otherwise it returns NULL.

.. _`lpfc_sli_free_hbq`:

lpfc_sli_free_hbq
=================

.. c:function:: void lpfc_sli_free_hbq(struct lpfc_hba *phba, struct hbq_dmabuf *hbq_buffer)

    Give back the hbq buffer to firmware

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct hbq_dmabuf \*hbq_buffer:
        Pointer to HBQ buffer.

.. _`lpfc_sli_free_hbq.description`:

Description
-----------

This function is called with hbalock. This function gives back
the hbq buffer to firmware. If the HBQ does not have space to
post the buffer, it will free the buffer.

.. _`lpfc_sli_chk_mbx_command`:

lpfc_sli_chk_mbx_command
========================

.. c:function:: int lpfc_sli_chk_mbx_command(uint8_t mbxCommand)

    Check if the mailbox is a legitimate mailbox

    :param uint8_t mbxCommand:
        mailbox command code.

.. _`lpfc_sli_chk_mbx_command.description`:

Description
-----------

This function is called by the mailbox event handler function to verify
that the completed mailbox command is a legitimate mailbox command. If the
completed mailbox is not known to the function, it will return MBX_SHUTDOWN
and the mailbox event handler will take the HBA offline.

.. _`lpfc_sli_wake_mbox_wait`:

lpfc_sli_wake_mbox_wait
=======================

.. c:function:: void lpfc_sli_wake_mbox_wait(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmboxq)

    lpfc_sli_issue_mbox_wait mbox completion handler

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param LPFC_MBOXQ_t \*pmboxq:
        Pointer to mailbox command.

.. _`lpfc_sli_wake_mbox_wait.description`:

Description
-----------

This is completion handler function for mailbox commands issued from
lpfc_sli_issue_mbox_wait function. This function is called by the
mailbox event handler function with no lock held. This function
will wake up thread waiting on the wait queue pointed by context1
of the mailbox.

.. _`lpfc_sli_def_mbox_cmpl`:

lpfc_sli_def_mbox_cmpl
======================

.. c:function:: void lpfc_sli_def_mbox_cmpl(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb)

    Default mailbox completion handler

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param LPFC_MBOXQ_t \*pmb:
        Pointer to mailbox object.

.. _`lpfc_sli_def_mbox_cmpl.description`:

Description
-----------

This function is the default mailbox completion handler. It
frees the memory resources associated with the completed mailbox
command. If the completed command is a REG_LOGIN mailbox command,
this function will issue a UREG_LOGIN to re-claim the RPI.

.. _`lpfc_sli_handle_mb_event`:

lpfc_sli_handle_mb_event
========================

.. c:function:: int lpfc_sli_handle_mb_event(struct lpfc_hba *phba)

    Handle mailbox completions from firmware

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_handle_mb_event.description`:

Description
-----------

This function is called with no lock held. This function processes all
the completed mailbox commands and gives it to upper layers. The interrupt
service routine processes mailbox completion interrupt and adds completed
mailbox commands to the mboxq_cmpl queue and signals the worker thread.
Worker thread call lpfc_sli_handle_mb_event, which will return the
completed mailbox commands in mboxq_cmpl queue to the upper layers. This
function returns the mailbox commands to the upper layer by calling the
completion handler function of each mailbox.

.. _`lpfc_sli_get_buff`:

lpfc_sli_get_buff
=================

.. c:function:: struct lpfc_dmabuf *lpfc_sli_get_buff(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, uint32_t tag)

    Get the buffer associated with the buffer tag

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param uint32_t tag:
        buffer tag.

.. _`lpfc_sli_get_buff.description`:

Description
-----------

This function is called with no lock held. When QUE_BUFTAG_BIT bit
is set in the tag the buffer is posted for a particular exchange,
the function will return the buffer without replacing the buffer.
If the buffer is for unsolicited ELS or CT traffic, this function
returns the buffer and also posts another buffer to the firmware.

.. _`lpfc_complete_unsol_iocb`:

lpfc_complete_unsol_iocb
========================

.. c:function:: int lpfc_complete_unsol_iocb(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, struct lpfc_iocbq *saveq, uint32_t fch_r_ctl, uint32_t fch_type)

    Complete an unsolicited sequence

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param struct lpfc_iocbq \*saveq:
        Pointer to the iocbq struct representing the sequence starting frame.

    :param uint32_t fch_r_ctl:
        the r_ctl for the first frame of the sequence.

    :param uint32_t fch_type:
        the type for the first frame of the sequence.

.. _`lpfc_complete_unsol_iocb.description`:

Description
-----------

This function is called with no lock held. This function uses the r_ctl and
type of the received sequence to find the correct callback function to call
to process the sequence.

.. _`lpfc_sli_process_unsol_iocb`:

lpfc_sli_process_unsol_iocb
===========================

.. c:function:: int lpfc_sli_process_unsol_iocb(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, struct lpfc_iocbq *saveq)

    Unsolicited iocb handler

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param struct lpfc_iocbq \*saveq:
        Pointer to the unsolicited iocb.

.. _`lpfc_sli_process_unsol_iocb.description`:

Description
-----------

This function is called with no lock held by the ring event handler
when there is an unsolicited iocb posted to the response ring by the
firmware. This function gets the buffer associated with the iocbs
and calls the event handler for the ring. This function handles both
qring buffers and hbq buffers.
When the function returns 1 the caller can free the iocb object otherwise
upper layer functions will free the iocb objects.

.. _`lpfc_sli_iocbq_lookup`:

lpfc_sli_iocbq_lookup
=====================

.. c:function:: struct lpfc_iocbq *lpfc_sli_iocbq_lookup(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, struct lpfc_iocbq *prspiocb)

    Find command iocb for the given response iocb

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param struct lpfc_iocbq \*prspiocb:
        Pointer to response iocb object.

.. _`lpfc_sli_iocbq_lookup.description`:

Description
-----------

This function looks up the iocb_lookup table to get the command iocb
corresponding to the given response iocb using the iotag of the
response iocb. This function is called with the hbalock held
for sli3 devices or the ring_lock for sli4 devices.
This function returns the command iocb object if it finds the command
iocb else returns NULL.

.. _`lpfc_sli_iocbq_lookup_by_tag`:

lpfc_sli_iocbq_lookup_by_tag
============================

.. c:function:: struct lpfc_iocbq *lpfc_sli_iocbq_lookup_by_tag(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, uint16_t iotag)

    Find command iocb for the iotag

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param uint16_t iotag:
        IOCB tag.

.. _`lpfc_sli_iocbq_lookup_by_tag.description`:

Description
-----------

This function looks up the iocb_lookup table to get the command iocb
corresponding to the given iotag. This function is called with the
hbalock held.
This function returns the command iocb object if it finds the command
iocb else returns NULL.

.. _`lpfc_sli_process_sol_iocb`:

lpfc_sli_process_sol_iocb
=========================

.. c:function:: int lpfc_sli_process_sol_iocb(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, struct lpfc_iocbq *saveq)

    process solicited iocb completion

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param struct lpfc_iocbq \*saveq:
        Pointer to the response iocb to be processed.

.. _`lpfc_sli_process_sol_iocb.description`:

Description
-----------

This function is called by the ring event handler for non-fcp
rings when there is a new response iocb in the response ring.
The caller is not required to hold any locks. This function
gets the command iocb associated with the response iocb and
calls the completion handler for the command iocb. If there
is no completion handler, the function will free the resources
associated with command iocb. If the response iocb is for
an already aborted command iocb, the status of the completion
is changed to IOSTAT_LOCAL_REJECT/IOERR_SLI_ABORTED.
This function always returns 1.

.. _`lpfc_sli_rsp_pointers_error`:

lpfc_sli_rsp_pointers_error
===========================

.. c:function:: void lpfc_sli_rsp_pointers_error(struct lpfc_hba *phba, struct lpfc_sli_ring *pring)

    Response ring pointer error handler

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

.. _`lpfc_sli_rsp_pointers_error.description`:

Description
-----------

This function is called from the iocb ring event handlers when
put pointer is ahead of the get pointer for a ring. This function signal
an error attention condition to the worker thread and the worker
thread will transition the HBA to offline state.

.. _`lpfc_poll_eratt`:

lpfc_poll_eratt
===============

.. c:function:: void lpfc_poll_eratt(struct timer_list *t)

    Error attention polling timer timeout handler

    :param struct timer_list \*t:
        *undescribed*

.. _`lpfc_poll_eratt.description`:

Description
-----------

This function is invoked by the Error Attention polling timer when the
timer times out. It will check the SLI Error Attention register for
possible attention events. If so, it will post an Error Attention event
and wake up worker thread to process it. Otherwise, it will set up the
Error Attention polling timer for the next poll.

.. _`lpfc_sli_handle_fast_ring_event`:

lpfc_sli_handle_fast_ring_event
===============================

.. c:function:: int lpfc_sli_handle_fast_ring_event(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, uint32_t mask)

    Handle ring events on FCP ring

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param uint32_t mask:
        Host attention register mask for this ring.

.. _`lpfc_sli_handle_fast_ring_event.description`:

Description
-----------

This function is called from the interrupt context when there is a ring
event for the fcp ring. The caller does not hold any lock.
The function processes each response iocb in the response ring until it
finds an iocb with LE bit set and chains all the iocbs up to the iocb with
LE bit set. The function will call the completion handler of the command iocb
if the response iocb indicates a completion for a command iocb or it is
an abort completion. The function will call lpfc_sli_process_unsol_iocb
function if this is an unsolicited iocb.
This routine presumes LPFC_FCP_RING handling and doesn't bother
to check it explicitly.

.. _`lpfc_sli_sp_handle_rspiocb`:

lpfc_sli_sp_handle_rspiocb
==========================

.. c:function:: struct lpfc_iocbq *lpfc_sli_sp_handle_rspiocb(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, struct lpfc_iocbq *rspiocbp)

    Handle slow-path response iocb

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param struct lpfc_iocbq \*rspiocbp:
        Pointer to driver response IOCB object.

.. _`lpfc_sli_sp_handle_rspiocb.description`:

Description
-----------

This function is called from the worker thread when there is a slow-path
response IOCB to process. This function chains all the response iocbs until
seeing the iocb with the LE bit set. The function will call
lpfc_sli_process_sol_iocb function if the response iocb indicates a
completion of a command iocb. The function will call the
lpfc_sli_process_unsol_iocb function if this is an unsolicited iocb.
The function frees the resources or calls the completion handler if this
iocb is an abort completion. The function returns NULL when the response
iocb has the LE bit set and all the chained iocbs are processed, otherwise
this function shall chain the iocb on to the iocb_continueq and return the
response iocb passed in.

.. _`lpfc_sli_handle_slow_ring_event`:

lpfc_sli_handle_slow_ring_event
===============================

.. c:function:: void lpfc_sli_handle_slow_ring_event(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, uint32_t mask)

    Wrapper func for handling slow-path iocbs

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param uint32_t mask:
        Host attention register mask for this ring.

.. _`lpfc_sli_handle_slow_ring_event.description`:

Description
-----------

This routine wraps the actual slow_ring event process routine from the
API jump table function pointer from the lpfc_hba struct.

.. _`lpfc_sli_handle_slow_ring_event_s3`:

lpfc_sli_handle_slow_ring_event_s3
==================================

.. c:function:: void lpfc_sli_handle_slow_ring_event_s3(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, uint32_t mask)

    Handle SLI3 ring event for non-FCP rings

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param uint32_t mask:
        Host attention register mask for this ring.

.. _`lpfc_sli_handle_slow_ring_event_s3.description`:

Description
-----------

This function is called from the worker thread when there is a ring event
for non-fcp rings. The caller does not hold any lock. The function will
remove each response iocb in the response ring and calls the handle
response iocb routine (lpfc_sli_sp_handle_rspiocb) to process it.

.. _`lpfc_sli_handle_slow_ring_event_s4`:

lpfc_sli_handle_slow_ring_event_s4
==================================

.. c:function:: void lpfc_sli_handle_slow_ring_event_s4(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, uint32_t mask)

    Handle SLI4 slow-path els events

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param uint32_t mask:
        Host attention register mask for this ring.

.. _`lpfc_sli_handle_slow_ring_event_s4.description`:

Description
-----------

This function is called from the worker thread when there is a pending
ELS response iocb on the driver internal slow-path response iocb worker
queue. The caller does not hold any lock. The function will remove each
response iocb from the response worker queue and calls the handle
response iocb routine (lpfc_sli_sp_handle_rspiocb) to process it.

.. _`lpfc_sli_abort_iocb_ring`:

lpfc_sli_abort_iocb_ring
========================

.. c:function:: void lpfc_sli_abort_iocb_ring(struct lpfc_hba *phba, struct lpfc_sli_ring *pring)

    Abort all iocbs in the ring

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

.. _`lpfc_sli_abort_iocb_ring.description`:

Description
-----------

This function aborts all iocbs in the given ring and frees all the iocb
objects in txq. This function issues an abort iocb for all the iocb commands
in txcmplq. The iocbs in the txcmplq is not guaranteed to complete before
the return of this function. The caller is not required to hold any locks.

.. _`lpfc_sli_abort_wqe_ring`:

lpfc_sli_abort_wqe_ring
=======================

.. c:function:: void lpfc_sli_abort_wqe_ring(struct lpfc_hba *phba, struct lpfc_sli_ring *pring)

    Abort all iocbs in the ring

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

.. _`lpfc_sli_abort_wqe_ring.description`:

Description
-----------

This function aborts all iocbs in the given ring and frees all the iocb
objects in txq. This function issues an abort iocb for all the iocb commands
in txcmplq. The iocbs in the txcmplq is not guaranteed to complete before
the return of this function. The caller is not required to hold any locks.

.. _`lpfc_sli_abort_fcp_rings`:

lpfc_sli_abort_fcp_rings
========================

.. c:function:: void lpfc_sli_abort_fcp_rings(struct lpfc_hba *phba)

    Abort all iocbs in all FCP rings

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_abort_fcp_rings.description`:

Description
-----------

This function aborts all iocbs in FCP rings and frees all the iocb
objects in txq. This function issues an abort iocb for all the iocb commands
in txcmplq. The iocbs in the txcmplq is not guaranteed to complete before
the return of this function. The caller is not required to hold any locks.

.. _`lpfc_sli_abort_nvme_rings`:

lpfc_sli_abort_nvme_rings
=========================

.. c:function:: void lpfc_sli_abort_nvme_rings(struct lpfc_hba *phba)

    Abort all wqes in all NVME rings

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_abort_nvme_rings.description`:

Description
-----------

This function aborts all wqes in NVME rings. This function issues an
abort wqe for all the outstanding IO commands in txcmplq. The iocbs in
the txcmplq is not guaranteed to complete before the return of this
function. The caller is not required to hold any locks.

.. _`lpfc_sli_flush_fcp_rings`:

lpfc_sli_flush_fcp_rings
========================

.. c:function:: void lpfc_sli_flush_fcp_rings(struct lpfc_hba *phba)

    flush all iocbs in the fcp ring

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_flush_fcp_rings.description`:

Description
-----------

This function flushes all iocbs in the fcp ring and frees all the iocb
objects in txq and txcmplq. This function will not issue abort iocbs
for all the iocb commands in txcmplq, they will just be returned with
IOERR_SLI_DOWN. This function is invoked with EEH when device's PCI
slot has been permanently disabled.

.. _`lpfc_sli_flush_nvme_rings`:

lpfc_sli_flush_nvme_rings
=========================

.. c:function:: void lpfc_sli_flush_nvme_rings(struct lpfc_hba *phba)

    flush all wqes in the nvme rings

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_flush_nvme_rings.description`:

Description
-----------

This function flushes all wqes in the nvme rings and frees all resources
in the txcmplq. This function does not issue abort wqes for the IO
commands in txcmplq, they will just be returned with
IOERR_SLI_DOWN. This function is invoked with EEH when device's PCI
slot has been permanently disabled.

.. _`lpfc_sli_brdready_s3`:

lpfc_sli_brdready_s3
====================

.. c:function:: int lpfc_sli_brdready_s3(struct lpfc_hba *phba, uint32_t mask)

    Check for sli3 host ready status

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint32_t mask:
        Bit mask to be checked.

.. _`lpfc_sli_brdready_s3.description`:

Description
-----------

This function reads the host status register and compares
with the provided bit mask to check if HBA completed
the restart. This function will wait in a loop for the
HBA to complete restart. If the HBA does not restart within
15 iterations, the function will reset the HBA again. The
function returns 1 when HBA fail to restart otherwise returns
zero.

.. _`lpfc_sli_brdready_s4`:

lpfc_sli_brdready_s4
====================

.. c:function:: int lpfc_sli_brdready_s4(struct lpfc_hba *phba, uint32_t mask)

    Check for sli4 host ready status

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint32_t mask:
        Bit mask to be checked.

.. _`lpfc_sli_brdready_s4.description`:

Description
-----------

This function checks the host status register to check if HBA is
ready. This function will wait in a loop for the HBA to be ready
If the HBA is not ready , the function will will reset the HBA PCI
function again. The function returns 1 when HBA fail to be ready
otherwise returns zero.

.. _`lpfc_sli_brdready`:

lpfc_sli_brdready
=================

.. c:function:: int lpfc_sli_brdready(struct lpfc_hba *phba, uint32_t mask)

    Wrapper func for checking the hba readyness

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint32_t mask:
        Bit mask to be checked.

.. _`lpfc_sli_brdready.description`:

Description
-----------

This routine wraps the actual SLI3 or SLI4 hba readyness check routine
from the API jump table function pointer from the lpfc_hba struct.

.. _`lpfc_reset_barrier`:

lpfc_reset_barrier
==================

.. c:function:: void lpfc_reset_barrier(struct lpfc_hba *phba)

    Make HBA ready for HBA reset

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_reset_barrier.description`:

Description
-----------

This function is called before resetting an HBA. This function is called
with hbalock held and requests HBA to quiesce DMAs before a reset.

.. _`lpfc_sli_brdkill`:

lpfc_sli_brdkill
================

.. c:function:: int lpfc_sli_brdkill(struct lpfc_hba *phba)

    Issue a kill_board mailbox command

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_brdkill.description`:

Description
-----------

This function issues a kill_board mailbox command and waits for
the error attention interrupt. This function is called for stopping
the firmware processing. The caller is not required to hold any
locks. This function calls lpfc_hba_down_post function to free
any pending commands after the kill. The function will return 1 when it
fails to kill the board else will return 0.

.. _`lpfc_sli_brdreset`:

lpfc_sli_brdreset
=================

.. c:function:: int lpfc_sli_brdreset(struct lpfc_hba *phba)

    Reset a sli-2 or sli-3 HBA

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_brdreset.description`:

Description
-----------

This function resets the HBA by writing HC_INITFF to the control
register. After the HBA resets, this function resets all the iocb ring
indices. This function disables PCI layer parity checking during
the reset.
This function returns 0 always.
The caller is not required to hold any locks.

.. _`lpfc_sli4_brdreset`:

lpfc_sli4_brdreset
==================

.. c:function:: int lpfc_sli4_brdreset(struct lpfc_hba *phba)

    Reset a sli-4 HBA

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli4_brdreset.description`:

Description
-----------

This function resets a SLI4 HBA. This function disables PCI layer parity
checking during resets the device. The caller is not required to hold
any locks.

This function returns 0 always.

.. _`lpfc_sli_brdrestart_s3`:

lpfc_sli_brdrestart_s3
======================

.. c:function:: int lpfc_sli_brdrestart_s3(struct lpfc_hba *phba)

    Restart a sli-3 hba

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_brdrestart_s3.description`:

Description
-----------

This function is called in the SLI initialization code path to
restart the HBA. The caller is not required to hold any lock.
This function writes MBX_RESTART mailbox command to the SLIM and
resets the HBA. At the end of the function, it calls lpfc_hba_down_post
function to free any pending commands. The function enables
POST only during the first initialization. The function returns zero.
The function does not guarantee completion of MBX_RESTART mailbox
command before the return of this function.

.. _`lpfc_sli_brdrestart_s4`:

lpfc_sli_brdrestart_s4
======================

.. c:function:: int lpfc_sli_brdrestart_s4(struct lpfc_hba *phba)

    Restart the sli-4 hba

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_brdrestart_s4.description`:

Description
-----------

This function is called in the SLI initialization code path to restart
a SLI4 HBA. The caller is not required to hold any lock.
At the end of the function, it calls lpfc_hba_down_post function to
free any pending commands.

.. _`lpfc_sli_brdrestart`:

lpfc_sli_brdrestart
===================

.. c:function:: int lpfc_sli_brdrestart(struct lpfc_hba *phba)

    Wrapper func for restarting hba

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_brdrestart.description`:

Description
-----------

This routine wraps the actual SLI3 or SLI4 hba restart routine from the
API jump table function pointer from the lpfc_hba struct.

.. _`lpfc_sli_chipset_init`:

lpfc_sli_chipset_init
=====================

.. c:function:: int lpfc_sli_chipset_init(struct lpfc_hba *phba)

    Wait for the restart of the HBA after a restart

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_chipset_init.description`:

Description
-----------

This function is called after a HBA restart to wait for successful
restart of the HBA. Successful restart of the HBA is indicated by
HS_FFRDY and HS_MBRDY bits. If the HBA fails to restart even after 15
iteration, the function will restart the HBA again. The function returns
zero if HBA successfully restarted else returns negative error code.

.. _`lpfc_sli_hbq_count`:

lpfc_sli_hbq_count
==================

.. c:function:: int lpfc_sli_hbq_count( void)

    Get the number of HBQs to be configured

    :param  void:
        no arguments

.. _`lpfc_sli_hbq_count.description`:

Description
-----------

This function calculates and returns the number of HBQs required to be
configured.

.. _`lpfc_sli_hbq_entry_count`:

lpfc_sli_hbq_entry_count
========================

.. c:function:: int lpfc_sli_hbq_entry_count( void)

    Calculate total number of hbq entries

    :param  void:
        no arguments

.. _`lpfc_sli_hbq_entry_count.description`:

Description
-----------

This function adds the number of hbq entries in every HBQ to get
the total number of hbq entries required for the HBA and returns
the total count.

.. _`lpfc_sli_hbq_size`:

lpfc_sli_hbq_size
=================

.. c:function:: int lpfc_sli_hbq_size( void)

    Calculate memory required for all hbq entries

    :param  void:
        no arguments

.. _`lpfc_sli_hbq_size.description`:

Description
-----------

This function calculates amount of memory required for all hbq entries
to be configured and returns the total memory required.

.. _`lpfc_sli_hbq_setup`:

lpfc_sli_hbq_setup
==================

.. c:function:: int lpfc_sli_hbq_setup(struct lpfc_hba *phba)

    configure and initialize HBQs

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_hbq_setup.description`:

Description
-----------

This function is called during the SLI initialization to configure
all the HBQs and post buffers to the HBQ. The caller is not
required to hold any locks. This function will return zero if successful
else it will return negative error code.

.. _`lpfc_sli4_rb_setup`:

lpfc_sli4_rb_setup
==================

.. c:function:: int lpfc_sli4_rb_setup(struct lpfc_hba *phba)

    Initialize and post RBs to HBA

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli4_rb_setup.description`:

Description
-----------

This function is called during the SLI initialization to configure
all the HBQs and post buffers to the HBQ. The caller is not
required to hold any locks. This function will return zero if successful
else it will return negative error code.

.. _`lpfc_sli_config_port`:

lpfc_sli_config_port
====================

.. c:function:: int lpfc_sli_config_port(struct lpfc_hba *phba, int sli_mode)

    Issue config port mailbox command

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param int sli_mode:
        sli mode - 2/3

.. _`lpfc_sli_config_port.description`:

Description
-----------

This function is called by the sli initialization code path
to issue config_port mailbox command. This function restarts the
HBA firmware and issues a config_port mailbox command to configure
the SLI interface in the sli mode specified by sli_mode
variable. The caller is not required to hold any locks.
The function returns 0 if successful, else returns negative error
code.

.. _`lpfc_sli_hba_setup`:

lpfc_sli_hba_setup
==================

.. c:function:: int lpfc_sli_hba_setup(struct lpfc_hba *phba)

    SLI initialization function

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_hba_setup.description`:

Description
-----------

This function is the main SLI initialization function. This function
is called by the HBA initialization code, HBA reset code and HBA
error attention handler code. Caller is not required to hold any
locks. This function issues config_port mailbox command to configure
the SLI, setup iocb rings and HBQ rings. In the end the function
calls the config_port_post function to issue init_link mailbox
command and to start the discovery. The function will return zero
if successful, else it will return negative error code.

.. _`lpfc_sli4_read_fcoe_params`:

lpfc_sli4_read_fcoe_params
==========================

.. c:function:: int lpfc_sli4_read_fcoe_params(struct lpfc_hba *phba)

    Read fcoe params from conf region

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli4_read_rev`:

lpfc_sli4_read_rev
==================

.. c:function:: int lpfc_sli4_read_rev(struct lpfc_hba *phba, LPFC_MBOXQ_t *mboxq, uint8_t *vpd, uint32_t *vpd_size)

    Issue READ_REV and collect vpd data

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*mboxq:
        pointer to the LPFC_MBOXQ_t structure.

    :param uint8_t \*vpd:
        pointer to the memory to hold resulting port vpd data.

    :param uint32_t \*vpd_size:
        On input, the number of bytes allocated to \ ``vpd``\ .
        On output, the number of data bytes in \ ``vpd``\ .

.. _`lpfc_sli4_read_rev.description`:

Description
-----------

This routine executes a READ_REV SLI4 mailbox command.  In
addition, this routine gets the port vpd data.

Return codes
0 - successful
-ENOMEM - could not allocated memory.

.. _`lpfc_sli4_retrieve_pport_name`:

lpfc_sli4_retrieve_pport_name
=============================

.. c:function:: int lpfc_sli4_retrieve_pport_name(struct lpfc_hba *phba)

    Retrieve SLI4 device physical port name

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_sli4_retrieve_pport_name.description`:

Description
-----------

This routine retrieves SLI4 device physical port name this PCI function
is attached to.

Return codes
0 - successful
otherwise - failed to retrieve physical port name

.. _`lpfc_sli4_arm_cqeq_intr`:

lpfc_sli4_arm_cqeq_intr
=======================

.. c:function:: void lpfc_sli4_arm_cqeq_intr(struct lpfc_hba *phba)

    Arm sli-4 device completion and event queues

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_sli4_arm_cqeq_intr.description`:

Description
-----------

This routine is called to explicitly arm the SLI4 device's completion and
event queues

.. _`lpfc_sli4_get_avail_extnt_rsrc`:

lpfc_sli4_get_avail_extnt_rsrc
==============================

.. c:function:: int lpfc_sli4_get_avail_extnt_rsrc(struct lpfc_hba *phba, uint16_t type, uint16_t *extnt_count, uint16_t *extnt_size)

    Get available resource extent count.

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint16_t type:
        The resource extent type.

    :param uint16_t \*extnt_count:
        buffer to hold port available extent count.

    :param uint16_t \*extnt_size:
        buffer to hold element count per extent.

.. _`lpfc_sli4_get_avail_extnt_rsrc.description`:

Description
-----------

This function calls the port and retrievs the number of available
extents and their size for a particular extent type.

.. _`lpfc_sli4_get_avail_extnt_rsrc.return`:

Return
------

0 if successful.  Nonzero otherwise.

.. _`lpfc_sli4_chk_avail_extnt_rsrc`:

lpfc_sli4_chk_avail_extnt_rsrc
==============================

.. c:function:: int lpfc_sli4_chk_avail_extnt_rsrc(struct lpfc_hba *phba, uint16_t type)

    Check for available SLI4 resource extents.

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint16_t type:
        The extent type to check.

.. _`lpfc_sli4_chk_avail_extnt_rsrc.description`:

Description
-----------

This function reads the current available extents from the port and checks
if the extent count or extent size has changed since the last access.
Callers use this routine post port reset to understand if there is a
extent reprovisioning requirement.

.. _`lpfc_sli4_chk_avail_extnt_rsrc.return`:

Return
------

-Error: error indicates problem.
1: Extent count or size has changed.
0: No changes.

.. _`lpfc_sli4_cfg_post_extnts`:

lpfc_sli4_cfg_post_extnts
=========================

.. c:function:: int lpfc_sli4_cfg_post_extnts(struct lpfc_hba *phba, uint16_t extnt_cnt, uint16_t type, bool *emb, LPFC_MBOXQ_t *mbox)

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.
        \ ``extnt_cnt``\  - number of available extents.
        \ ``type``\  - the extent type (rpi, xri, vfi, vpi).
        \ ``emb``\  - buffer to hold either MBX_EMBED or MBX_NEMBED operation.
        \ ``mbox``\  - pointer to the caller's allocated mailbox structure.

    :param uint16_t extnt_cnt:
        *undescribed*

    :param uint16_t type:
        *undescribed*

    :param bool \*emb:
        *undescribed*

    :param LPFC_MBOXQ_t \*mbox:
        *undescribed*

.. _`lpfc_sli4_cfg_post_extnts.description`:

Description
-----------

This function executes the extents allocation request.  It also
takes care of the amount of memory needed to allocate or get the
allocated extents. It is the caller's responsibility to evaluate
the response.

.. _`lpfc_sli4_cfg_post_extnts.return`:

Return
------

-Error:  Error value describes the condition found.
0: if successful

.. _`lpfc_sli4_alloc_extent`:

lpfc_sli4_alloc_extent
======================

.. c:function:: int lpfc_sli4_alloc_extent(struct lpfc_hba *phba, uint16_t type)

    Allocate an SLI4 resource extent.

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint16_t type:
        The resource extent type to allocate.

.. _`lpfc_sli4_alloc_extent.description`:

Description
-----------

This function allocates the number of elements for the specified
resource type.

.. _`lpfc_sli4_dealloc_extent`:

lpfc_sli4_dealloc_extent
========================

.. c:function:: int lpfc_sli4_dealloc_extent(struct lpfc_hba *phba, uint16_t type)

    Deallocate an SLI4 resource extent.

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint16_t type:
        the extent's type.

.. _`lpfc_sli4_dealloc_extent.description`:

Description
-----------

This function deallocates all extents of a particular resource type.
SLI4 does not allow for deallocating a particular extent range.  It
is the caller's responsibility to release all kernel memory resources.

.. _`lpfc_sli4_alloc_resource_identifiers`:

lpfc_sli4_alloc_resource_identifiers
====================================

.. c:function:: int lpfc_sli4_alloc_resource_identifiers(struct lpfc_hba *phba)

    Allocate all SLI4 resource extents.

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli4_alloc_resource_identifiers.description`:

Description
-----------

This function allocates all SLI4 resource identifiers.

.. _`lpfc_sli4_dealloc_resource_identifiers`:

lpfc_sli4_dealloc_resource_identifiers
======================================

.. c:function:: int lpfc_sli4_dealloc_resource_identifiers(struct lpfc_hba *phba)

    Deallocate all SLI4 resource extents.

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli4_dealloc_resource_identifiers.description`:

Description
-----------

This function allocates the number of elements for the specified
resource type.

.. _`lpfc_sli4_get_allocated_extnts`:

lpfc_sli4_get_allocated_extnts
==============================

.. c:function:: int lpfc_sli4_get_allocated_extnts(struct lpfc_hba *phba, uint16_t type, uint16_t *extnt_cnt, uint16_t *extnt_size)

    Get the port's allocated extents.

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint16_t type:
        The resource extent type.

    :param uint16_t \*extnt_cnt:
        *undescribed*

    :param uint16_t \*extnt_size:
        buffer to hold port extent size response.

.. _`lpfc_sli4_get_allocated_extnts.description`:

Description
-----------

This function calls the port to read the host allocated extents
for a particular type.

.. _`lpfc_sli4_repost_sgl_list`:

lpfc_sli4_repost_sgl_list
=========================

.. c:function:: int lpfc_sli4_repost_sgl_list(struct lpfc_hba *phba, struct list_head *sgl_list, int cnt)

    Repost the buffers sgl pages as block

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct list_head \*sgl_list:
        linked link of sgl buffers to post

    :param int cnt:
        number of linked list buffers

.. _`lpfc_sli4_repost_sgl_list.description`:

Description
-----------

This routine walks the list of buffers that have been allocated and
repost them to the port by using SGL block post. This is needed after a
pci_function_reset/warm_start or start. It attempts to construct blocks
of buffer sgls which contains contiguous xris and uses the non-embedded
SGL block post mailbox commands to post them to the port. For single
buffer sgl with non-contiguous xri, if any, it shall use embedded SGL post
mailbox command for posting.

.. _`lpfc_sli4_repost_sgl_list.return`:

Return
------

0 = success, non-zero failure.

.. _`lpfc_sli4_hba_setup`:

lpfc_sli4_hba_setup
===================

.. c:function:: int lpfc_sli4_hba_setup(struct lpfc_hba *phba)

    SLI4 device initialization PCI function

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli4_hba_setup.description`:

Description
-----------

This function is the main SLI4 device initialization PCI function. This
function is called by the HBA initialization code, HBA reset code and
HBA error attention handler code. Caller is not required to hold any
locks.

.. _`lpfc_mbox_timeout`:

lpfc_mbox_timeout
=================

.. c:function:: void lpfc_mbox_timeout(struct timer_list *t)

    Timeout call back function for mbox timer

    :param struct timer_list \*t:
        *undescribed*

.. _`lpfc_mbox_timeout.description`:

Description
-----------

This is the callback function for mailbox timer. The mailbox
timer is armed when a new mailbox command is issued and the timer
is deleted when the mailbox complete. The function is called by
the kernel timer code when a mailbox does not complete within
expected time. This function wakes up the worker thread to
process the mailbox timeout and returns. All the processing is
done by the worker thread function lpfc_mbox_timeout_handler.

.. _`lpfc_sli4_mbox_completions_pending`:

lpfc_sli4_mbox_completions_pending
==================================

.. c:function:: bool lpfc_sli4_mbox_completions_pending(struct lpfc_hba *phba)

    check to see if any mailbox completions are pending

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli4_mbox_completions_pending.description`:

Description
-----------

This function checks if any mailbox completions are present on the mailbox
completion queue.

.. _`lpfc_sli4_process_missed_mbox_completions`:

lpfc_sli4_process_missed_mbox_completions
=========================================

.. c:function:: bool lpfc_sli4_process_missed_mbox_completions(struct lpfc_hba *phba)

    process mbox completions that were missed.

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli4_process_missed_mbox_completions.description`:

Description
-----------

For sli4, it is possible to miss an interrupt. As such mbox completions
maybe missed causing erroneous mailbox timeouts to occur. This function
checks to see if mbox completions are on the mailbox completion queue
and will process all the completions associated with the eq for the
mailbox completion queue.

.. _`lpfc_mbox_timeout_handler`:

lpfc_mbox_timeout_handler
=========================

.. c:function:: void lpfc_mbox_timeout_handler(struct lpfc_hba *phba)

    Worker thread function to handle mailbox timeout

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_mbox_timeout_handler.description`:

Description
-----------

This function is called from worker thread when a mailbox command times out.
The caller is not required to hold any locks. This function will reset the
HBA and recover all the pending commands.

.. _`lpfc_sli_issue_mbox_s3`:

lpfc_sli_issue_mbox_s3
======================

.. c:function:: int lpfc_sli_issue_mbox_s3(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmbox, uint32_t flag)

    Issue an SLI3 mailbox command to firmware

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param LPFC_MBOXQ_t \*pmbox:
        Pointer to mailbox object.

    :param uint32_t flag:
        Flag indicating how the mailbox need to be processed.

.. _`lpfc_sli_issue_mbox_s3.description`:

Description
-----------

This function is called by discovery code and HBA management code
to submit a mailbox command to firmware with SLI-3 interface spec. This
function gets the hbalock to protect the data structures.
The mailbox command can be submitted in polling mode, in which case
this function will wait in a polling loop for the completion of the
mailbox.
If the mailbox is submitted in no_wait mode (not polling) the
function will submit the command and returns immediately without waiting
for the mailbox completion. The no_wait is supported only when HBA
is in SLI2/SLI3 mode - interrupts are enabled.
The SLI interface allows only one mailbox pending at a time. If the
mailbox is issued in polling mode and there is already a mailbox
pending, then the function will return an error. If the mailbox is issued
in NO_WAIT mode and there is a mailbox pending already, the function
will return MBX_BUSY after queuing the mailbox into mailbox queue.
The sli layer owns the mailbox object until the completion of mailbox
command if this function return MBX_BUSY or MBX_SUCCESS. For all other
return codes the caller owns the mailbox command after the return of
the function.

.. _`lpfc_sli4_async_mbox_block`:

lpfc_sli4_async_mbox_block
==========================

.. c:function:: int lpfc_sli4_async_mbox_block(struct lpfc_hba *phba)

    Block posting SLI4 asynchronous mailbox command

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli4_async_mbox_block.description`:

Description
-----------

The function blocks the posting of SLI4 asynchronous mailbox commands from
the driver internal pending mailbox queue. It will then try to wait out the
possible outstanding mailbox command before return.

.. _`lpfc_sli4_async_mbox_block.return`:

Return
------

0 - the outstanding mailbox command completed; otherwise, the wait for
the outstanding mailbox command timed out.

.. _`lpfc_sli4_async_mbox_unblock`:

lpfc_sli4_async_mbox_unblock
============================

.. c:function:: void lpfc_sli4_async_mbox_unblock(struct lpfc_hba *phba)

    Block posting SLI4 async mailbox command

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli4_async_mbox_unblock.description`:

Description
-----------

The function unblocks and resume posting of SLI4 asynchronous mailbox
commands from the driver internal pending mailbox queue. It makes sure
that there is no outstanding mailbox command before resuming posting
asynchronous mailbox commands. If, for any reason, there is outstanding
mailbox command, it will try to wait it out before resuming asynchronous
mailbox command posting.

.. _`lpfc_sli4_wait_bmbx_ready`:

lpfc_sli4_wait_bmbx_ready
=========================

.. c:function:: int lpfc_sli4_wait_bmbx_ready(struct lpfc_hba *phba, LPFC_MBOXQ_t *mboxq)

    Wait for bootstrap mailbox register ready

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param LPFC_MBOXQ_t \*mboxq:
        Pointer to mailbox object.

.. _`lpfc_sli4_wait_bmbx_ready.description`:

Description
-----------

The function waits for the bootstrap mailbox register ready bit from
port for twice the regular mailbox command timeout value.

0 - no timeout on waiting for bootstrap mailbox register ready.
MBXERR_ERROR - wait for bootstrap mailbox register timed out.

.. _`lpfc_sli4_post_sync_mbox`:

lpfc_sli4_post_sync_mbox
========================

.. c:function:: int lpfc_sli4_post_sync_mbox(struct lpfc_hba *phba, LPFC_MBOXQ_t *mboxq)

    Post an SLI4 mailbox to the bootstrap mailbox

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param LPFC_MBOXQ_t \*mboxq:
        Pointer to mailbox object.

.. _`lpfc_sli4_post_sync_mbox.description`:

Description
-----------

The function posts a mailbox to the port.  The mailbox is expected
to be comletely filled in and ready for the port to operate on it.
This routine executes a synchronous completion operation on the
mailbox by polling for its completion.

The caller must not be holding any locks when calling this routine.

.. _`lpfc_sli4_post_sync_mbox.return`:

Return
------

MBX_SUCCESS - mailbox posted successfully
Any of the MBX error values.

.. _`lpfc_sli_issue_mbox_s4`:

lpfc_sli_issue_mbox_s4
======================

.. c:function:: int lpfc_sli_issue_mbox_s4(struct lpfc_hba *phba, LPFC_MBOXQ_t *mboxq, uint32_t flag)

    Issue an SLI4 mailbox command to firmware

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param LPFC_MBOXQ_t \*mboxq:
        *undescribed*

    :param uint32_t flag:
        Flag indicating how the mailbox need to be processed.

.. _`lpfc_sli_issue_mbox_s4.description`:

Description
-----------

This function is called by discovery code and HBA management code to submit
a mailbox command to firmware with SLI-4 interface spec.

Return codes the caller owns the mailbox command after the return of the
function.

.. _`lpfc_sli4_post_async_mbox`:

lpfc_sli4_post_async_mbox
=========================

.. c:function:: int lpfc_sli4_post_async_mbox(struct lpfc_hba *phba)

    Post an SLI4 mailbox command to device

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli4_post_async_mbox.description`:

Description
-----------

This function is called by worker thread to send a mailbox command to
SLI4 HBA firmware.

.. _`lpfc_sli_issue_mbox`:

lpfc_sli_issue_mbox
===================

.. c:function:: int lpfc_sli_issue_mbox(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmbox, uint32_t flag)

    Wrapper func for issuing mailbox command

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param LPFC_MBOXQ_t \*pmbox:
        Pointer to mailbox object.

    :param uint32_t flag:
        Flag indicating how the mailbox need to be processed.

.. _`lpfc_sli_issue_mbox.description`:

Description
-----------

This routine wraps the actual SLI3 or SLI4 mailbox issuing routine from
the API jump table function pointer from the lpfc_hba struct.

Return codes the caller owns the mailbox command after the return of the
function.

.. _`lpfc_mbox_api_table_setup`:

lpfc_mbox_api_table_setup
=========================

.. c:function:: int lpfc_mbox_api_table_setup(struct lpfc_hba *phba, uint8_t dev_grp)

    Set up mbox api function jump table

    :param struct lpfc_hba \*phba:
        The hba struct for which this call is being executed.

    :param uint8_t dev_grp:
        The HBA PCI-Device group number.

.. _`lpfc_mbox_api_table_setup.description`:

Description
-----------

This routine sets up the mbox interface API function jump table in \ ``phba``\ 
struct.

.. _`lpfc_mbox_api_table_setup.return`:

Return
------

0 - success, -ENODEV - failure.

.. _`__lpfc_sli_ringtx_put`:

\__lpfc_sli_ringtx_put
======================

.. c:function:: void __lpfc_sli_ringtx_put(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, struct lpfc_iocbq *piocb)

    Add an iocb to the txq

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param struct lpfc_iocbq \*piocb:
        Pointer to address of newly added command iocb.

.. _`__lpfc_sli_ringtx_put.description`:

Description
-----------

This function is called with hbalock held to add a command
iocb to the txq when SLI layer cannot submit the command iocb
to the ring.

.. _`lpfc_sli_next_iocb`:

lpfc_sli_next_iocb
==================

.. c:function:: struct lpfc_iocbq *lpfc_sli_next_iocb(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, struct lpfc_iocbq **piocb)

    Get the next iocb in the txq

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param struct lpfc_iocbq \*\*piocb:
        Pointer to address of newly added command iocb.

.. _`lpfc_sli_next_iocb.description`:

Description
-----------

This function is called with hbalock held before a new
iocb is submitted to the firmware. This function checks
txq to flush the iocbs in txq to Firmware before
submitting new iocbs to the Firmware.
If there are iocbs in the txq which need to be submitted
to firmware, lpfc_sli_next_iocb returns the first element
of the txq after dequeuing it from txq.
If there is no iocb in the txq then the function will return
\*piocb and \*piocb is set to NULL. Caller needs to check
\*piocb to find if there are more commands in the txq.

.. _`__lpfc_sli_issue_iocb_s3`:

\__lpfc_sli_issue_iocb_s3
=========================

.. c:function:: int __lpfc_sli_issue_iocb_s3(struct lpfc_hba *phba, uint32_t ring_number, struct lpfc_iocbq *piocb, uint32_t flag)

    SLI3 device lockless ver of lpfc_sli_issue_iocb

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint32_t ring_number:
        SLI ring number to issue iocb on.

    :param struct lpfc_iocbq \*piocb:
        Pointer to command iocb.

    :param uint32_t flag:
        Flag indicating if this command can be put into txq.

.. _`__lpfc_sli_issue_iocb_s3.description`:

Description
-----------

\__lpfc_sli_issue_iocb_s3 is used by other functions in the driver to issue
an iocb command to an HBA with SLI-3 interface spec. If the PCI slot is
recovering from error state, if HBA is resetting or if LPFC_STOP_IOCB_EVENT
flag is turned on, the function returns IOCB_ERROR. When the link is down,
this function allows only iocbs for posting buffers. This function finds
next available slot in the command ring and posts the command to the
available slot and writes the port attention register to request HBA start
processing new iocb. If there is no slot available in the ring and
flag & SLI_IOCB_RET_IOCB is set, the new iocb is added to the txq, otherwise
the function returns IOCB_BUSY.

This function is called with hbalock held. The function will return success
after it successfully submit the iocb to firmware or after adding to the
txq.

.. _`lpfc_sli4_bpl2sgl`:

lpfc_sli4_bpl2sgl
=================

.. c:function:: uint16_t lpfc_sli4_bpl2sgl(struct lpfc_hba *phba, struct lpfc_iocbq *piocbq, struct lpfc_sglq *sglq)

    Convert the bpl/bde to a sgl.

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*piocbq:
        *undescribed*

    :param struct lpfc_sglq \*sglq:
        Pointer to the scatter gather queue object.

.. _`lpfc_sli4_bpl2sgl.description`:

Description
-----------

This routine converts the bpl or bde that is in the IOCB
to a sgl list for the sli4 hardware. The physical address
of the bpl/bde is converted back to a virtual address.
If the IOCB contains a BPL then the list of BDE's is
converted to sli4_sge's. If the IOCB contains a single
BDE then it is converted to a single sli_sge.
The IOCB is still in cpu endianess so the contents of
the bpl can be used without byte swapping.

Returns valid XRI = Success, NO_XRI = Failure.

.. _`lpfc_sli4_iocb2wqe`:

lpfc_sli4_iocb2wqe
==================

.. c:function:: int lpfc_sli4_iocb2wqe(struct lpfc_hba *phba, struct lpfc_iocbq *iocbq, union lpfc_wqe *wqe)

    Convert the IOCB to a work queue entry.

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*iocbq:
        *undescribed*

    :param union lpfc_wqe \*wqe:
        Pointer to the work queue entry.

.. _`lpfc_sli4_iocb2wqe.description`:

Description
-----------

This routine converts the iocb command to its Work Queue Entry
equivalent. The wqe pointer should not have any fields set when
this routine is called because it will memcpy over them.
This routine does not set the CQ_ID or the WQEC bits in the
wqe.

.. _`lpfc_sli4_iocb2wqe.return`:

Return
------

0 = Success, IOCB_ERROR = Failure.

.. _`__lpfc_sli_issue_iocb_s4`:

\__lpfc_sli_issue_iocb_s4
=========================

.. c:function:: int __lpfc_sli_issue_iocb_s4(struct lpfc_hba *phba, uint32_t ring_number, struct lpfc_iocbq *piocb, uint32_t flag)

    SLI4 device lockless ver of lpfc_sli_issue_iocb

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint32_t ring_number:
        SLI ring number to issue iocb on.

    :param struct lpfc_iocbq \*piocb:
        Pointer to command iocb.

    :param uint32_t flag:
        Flag indicating if this command can be put into txq.

.. _`__lpfc_sli_issue_iocb_s4.description`:

Description
-----------

\__lpfc_sli_issue_iocb_s4 is used by other functions in the driver to issue
an iocb command to an HBA with SLI-4 interface spec.

This function is called with hbalock held. The function will return success
after it successfully submit the iocb to firmware or after adding to the
txq.

.. _`__lpfc_sli_issue_iocb`:

\__lpfc_sli_issue_iocb
======================

.. c:function:: int __lpfc_sli_issue_iocb(struct lpfc_hba *phba, uint32_t ring_number, struct lpfc_iocbq *piocb, uint32_t flag)

    Wrapper func of lockless version for issuing iocb

    :param struct lpfc_hba \*phba:
        *undescribed*

    :param uint32_t ring_number:
        *undescribed*

    :param struct lpfc_iocbq \*piocb:
        *undescribed*

    :param uint32_t flag:
        *undescribed*

.. _`__lpfc_sli_issue_iocb.description`:

Description
-----------

This routine wraps the actual lockless version for issusing IOCB function
pointer from the lpfc_hba struct.

.. _`__lpfc_sli_issue_iocb.return-codes`:

Return codes
------------

IOCB_ERROR - Error
IOCB_SUCCESS - Success
IOCB_BUSY - Busy

.. _`lpfc_sli_api_table_setup`:

lpfc_sli_api_table_setup
========================

.. c:function:: int lpfc_sli_api_table_setup(struct lpfc_hba *phba, uint8_t dev_grp)

    Set up sli api function jump table

    :param struct lpfc_hba \*phba:
        The hba struct for which this call is being executed.

    :param uint8_t dev_grp:
        The HBA PCI-Device group number.

.. _`lpfc_sli_api_table_setup.description`:

Description
-----------

This routine sets up the SLI interface API function jump table in \ ``phba``\ 
struct.

.. _`lpfc_sli_api_table_setup.return`:

Return
------

0 - success, -ENODEV - failure.

.. _`lpfc_sli4_calc_ring`:

lpfc_sli4_calc_ring
===================

.. c:function:: struct lpfc_sli_ring *lpfc_sli4_calc_ring(struct lpfc_hba *phba, struct lpfc_iocbq *piocb)

    Calculates which ring to use

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*piocb:
        Pointer to command iocb.

.. _`lpfc_sli4_calc_ring.description`:

Description
-----------

For SLI4 only, FCP IO can deferred to one fo many WQs, based on
hba_wqidx, thus we need to calculate the corresponding ring.
Since ABORTS must go on the same WQ of the command they are
aborting, we use command's hba_wqidx.

.. _`lpfc_sli_issue_iocb`:

lpfc_sli_issue_iocb
===================

.. c:function:: int lpfc_sli_issue_iocb(struct lpfc_hba *phba, uint32_t ring_number, struct lpfc_iocbq *piocb, uint32_t flag)

    Wrapper function for \__lpfc_sli_issue_iocb

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint32_t ring_number:
        *undescribed*

    :param struct lpfc_iocbq \*piocb:
        Pointer to command iocb.

    :param uint32_t flag:
        Flag indicating if this command can be put into txq.

.. _`lpfc_sli_issue_iocb.description`:

Description
-----------

lpfc_sli_issue_iocb is a wrapper around \__lpfc_sli_issue_iocb
function. This function gets the hbalock and calls
\__lpfc_sli_issue_iocb function and will return the error returned
by \__lpfc_sli_issue_iocb function. This wrapper is used by
functions which do not hold hbalock.

.. _`lpfc_extra_ring_setup`:

lpfc_extra_ring_setup
=====================

.. c:function:: int lpfc_extra_ring_setup(struct lpfc_hba *phba)

    Extra ring setup function

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_extra_ring_setup.description`:

Description
-----------

This function is called while driver attaches with the
HBA to setup the extra ring. The extra ring is used
only when driver needs to support target mode functionality
or IP over FC functionalities.

This function is called with no lock held. SLI3 only.

.. _`lpfc_sli_async_event_handler`:

lpfc_sli_async_event_handler
============================

.. c:function:: void lpfc_sli_async_event_handler(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, struct lpfc_iocbq *iocbq)

    ASYNC iocb handler function

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param struct lpfc_iocbq \*iocbq:
        Pointer to iocb object.

.. _`lpfc_sli_async_event_handler.description`:

Description
-----------

This function is called by the slow ring event handler
function when there is an ASYNC event iocb in the ring.
This function is called with no lock held.
Currently this function handles only temperature related
ASYNC events. The function decodes the temperature sensor
event message and posts events for the management applications.

.. _`lpfc_sli4_setup`:

lpfc_sli4_setup
===============

.. c:function:: int lpfc_sli4_setup(struct lpfc_hba *phba)

    SLI ring setup function

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli4_setup.description`:

Description
-----------

lpfc_sli_setup sets up rings of the SLI interface with
number of iocbs per ring and iotags. This function is
called while driver attach to the HBA and before the
interrupts are enabled. So there is no need for locking.

This function always returns 0.

.. _`lpfc_sli_setup`:

lpfc_sli_setup
==============

.. c:function:: int lpfc_sli_setup(struct lpfc_hba *phba)

    SLI ring setup function

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_setup.description`:

Description
-----------

lpfc_sli_setup sets up rings of the SLI interface with
number of iocbs per ring and iotags. This function is
called while driver attach to the HBA and before the
interrupts are enabled. So there is no need for locking.

This function always returns 0. SLI3 only.

.. _`lpfc_sli4_queue_init`:

lpfc_sli4_queue_init
====================

.. c:function:: void lpfc_sli4_queue_init(struct lpfc_hba *phba)

    Queue initialization function

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli4_queue_init.description`:

Description
-----------

lpfc_sli4_queue_init sets up mailbox queues and iocb queues for each
ring. This function also initializes ring indices of each ring.
This function is called during the initialization of the SLI
interface of an HBA.
This function is called with no lock held and always returns
1.

.. _`lpfc_sli_queue_init`:

lpfc_sli_queue_init
===================

.. c:function:: void lpfc_sli_queue_init(struct lpfc_hba *phba)

    Queue initialization function

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_queue_init.description`:

Description
-----------

lpfc_sli_queue_init sets up mailbox queues and iocb queues for each
ring. This function also initializes ring indices of each ring.
This function is called during the initialization of the SLI
interface of an HBA.
This function is called with no lock held and always returns
1.

.. _`lpfc_sli_mbox_sys_flush`:

lpfc_sli_mbox_sys_flush
=======================

.. c:function:: void lpfc_sli_mbox_sys_flush(struct lpfc_hba *phba)

    Flush mailbox command sub-system

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_mbox_sys_flush.description`:

Description
-----------

This routine flushes the mailbox command subsystem. It will unconditionally
flush all the mailbox commands in the three possible stages in the mailbox
command sub-system: pending mailbox command queue; the outstanding mailbox
command; and completed mailbox command queue. It is caller's responsibility
to make sure that the driver is in the proper state to flush the mailbox
command sub-system. Namely, the posting of mailbox commands into the
pending mailbox command queue from the various clients must be stopped;
either the HBA is in a state that it will never works on the outstanding
mailbox command (such as in EEH or ERATT conditions) or the outstanding
mailbox command has been completed.

.. _`lpfc_sli_host_down`:

lpfc_sli_host_down
==================

.. c:function:: int lpfc_sli_host_down(struct lpfc_vport *vport)

    Vport cleanup function

    :param struct lpfc_vport \*vport:
        Pointer to virtual port object.

.. _`lpfc_sli_host_down.description`:

Description
-----------

lpfc_sli_host_down is called to clean up the resources
associated with a vport before destroying virtual
port data structures.

.. _`lpfc_sli_host_down.this-function-does-following-operations`:

This function does following operations
---------------------------------------

- Free discovery resources associated with this virtual
port.
- Free iocbs associated with this virtual port in
the txq.
- Send abort for all iocb commands associated with this
vport in txcmplq.

This function is called with no lock held and always returns 1.

.. _`lpfc_sli_hba_down`:

lpfc_sli_hba_down
=================

.. c:function:: int lpfc_sli_hba_down(struct lpfc_hba *phba)

    Resource cleanup function for the HBA

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_hba_down.description`:

Description
-----------

This function cleans up all iocb, buffers, mailbox commands
while shutting down the HBA. This function is called with no
lock held and always returns 1.

.. _`lpfc_sli_hba_down.this-function-does-the-following-to-cleanup-driver-resources`:

This function does the following to cleanup driver resources
------------------------------------------------------------

- Free discovery resources for each virtual port
- Cleanup any pending fabric iocbs
- Iterate through the iocb txq and free each entry
in the list.
- Free up any buffer posted to the HBA
- Free mailbox commands in the mailbox queue.

.. _`lpfc_sli_pcimem_bcopy`:

lpfc_sli_pcimem_bcopy
=====================

.. c:function:: void lpfc_sli_pcimem_bcopy(void *srcp, void *destp, uint32_t cnt)

    SLI memory copy function

    :param void \*srcp:
        Source memory pointer.

    :param void \*destp:
        Destination memory pointer.

    :param uint32_t cnt:
        Number of words required to be copied.

.. _`lpfc_sli_pcimem_bcopy.description`:

Description
-----------

This function is used for copying data between driver memory
and the SLI memory. This function also changes the endianness
of each word if native endianness is different from SLI
endianness. This function can be called with or without
lock.

.. _`lpfc_sli_bemem_bcopy`:

lpfc_sli_bemem_bcopy
====================

.. c:function:: void lpfc_sli_bemem_bcopy(void *srcp, void *destp, uint32_t cnt)

    SLI memory copy function

    :param void \*srcp:
        Source memory pointer.

    :param void \*destp:
        Destination memory pointer.

    :param uint32_t cnt:
        Number of words required to be copied.

.. _`lpfc_sli_bemem_bcopy.description`:

Description
-----------

This function is used for copying data between a data structure
with big endian representation to local endianness.
This function can be called with or without lock.

.. _`lpfc_sli_ringpostbuf_put`:

lpfc_sli_ringpostbuf_put
========================

.. c:function:: int lpfc_sli_ringpostbuf_put(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, struct lpfc_dmabuf *mp)

    Function to add a buffer to postbufq

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param struct lpfc_dmabuf \*mp:
        Pointer to driver buffer object.

.. _`lpfc_sli_ringpostbuf_put.description`:

Description
-----------

This function is called with no lock held.
It always return zero after adding the buffer to the postbufq
buffer list.

.. _`lpfc_sli_get_buffer_tag`:

lpfc_sli_get_buffer_tag
=======================

.. c:function:: uint32_t lpfc_sli_get_buffer_tag(struct lpfc_hba *phba)

    allocates a tag for a CMD_QUE_XRI64_CX buffer

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli_get_buffer_tag.description`:

Description
-----------

When HBQ is enabled, buffers are searched based on tags. This function
allocates a tag for buffer posted using CMD_QUE_XRI64_CX iocb. The
tag is bit wise or-ed with QUE_BUFTAG_BIT to make sure that the tag
does not conflict with tags of buffer posted for unsolicited events.
The function returns the allocated tag. The function is called with
no locks held.

.. _`lpfc_sli_ring_taggedbuf_get`:

lpfc_sli_ring_taggedbuf_get
===========================

.. c:function:: struct lpfc_dmabuf *lpfc_sli_ring_taggedbuf_get(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, uint32_t tag)

    find HBQ buffer associated with given tag

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param uint32_t tag:
        Buffer tag.

.. _`lpfc_sli_ring_taggedbuf_get.description`:

Description
-----------

Buffers posted using CMD_QUE_XRI64_CX iocb are in pring->postbufq
list. After HBA DMA data to these buffers, CMD_IOCB_RET_XRI64_CX
iocb is posted to the response ring with the tag of the buffer.
This function searches the pring->postbufq list using the tag
to find buffer associated with CMD_IOCB_RET_XRI64_CX
iocb. If the buffer is found then lpfc_dmabuf object of the
buffer is returned to the caller else NULL is returned.
This function is called with no lock held.

.. _`lpfc_sli_ringpostbuf_get`:

lpfc_sli_ringpostbuf_get
========================

.. c:function:: struct lpfc_dmabuf *lpfc_sli_ringpostbuf_get(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, dma_addr_t phys)

    search buffers for unsolicited CT and ELS events

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param dma_addr_t phys:
        DMA address of the buffer.

.. _`lpfc_sli_ringpostbuf_get.description`:

Description
-----------

This function searches the buffer list using the dma_address
of unsolicited event to find the driver's lpfc_dmabuf object
corresponding to the dma_address. The function returns the
lpfc_dmabuf object if a buffer is found else it returns NULL.
This function is called by the ct and els unsolicited event
handlers to get the buffer associated with the unsolicited
event.

This function is called with no lock held.

.. _`lpfc_sli_abort_els_cmpl`:

lpfc_sli_abort_els_cmpl
=======================

.. c:function:: void lpfc_sli_abort_els_cmpl(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocb, struct lpfc_iocbq *rspiocb)

    Completion handler for the els abort iocbs

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*cmdiocb:
        Pointer to driver command iocb object.

    :param struct lpfc_iocbq \*rspiocb:
        Pointer to driver response iocb object.

.. _`lpfc_sli_abort_els_cmpl.description`:

Description
-----------

This function is the completion handler for the abort iocbs for
ELS commands. This function is called from the ELS ring event
handler with no lock held. This function frees memory resources
associated with the abort iocb.

.. _`lpfc_ignore_els_cmpl`:

lpfc_ignore_els_cmpl
====================

.. c:function:: void lpfc_ignore_els_cmpl(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocb, struct lpfc_iocbq *rspiocb)

    Completion handler for aborted ELS command

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*cmdiocb:
        Pointer to driver command iocb object.

    :param struct lpfc_iocbq \*rspiocb:
        Pointer to driver response iocb object.

.. _`lpfc_ignore_els_cmpl.description`:

Description
-----------

The function is called from SLI ring event handler with no
lock held. This function is the completion handler for ELS commands
which are aborted. The function frees memory resources used for
the aborted ELS commands.

.. _`lpfc_sli_abort_iotag_issue`:

lpfc_sli_abort_iotag_issue
==========================

.. c:function:: int lpfc_sli_abort_iotag_issue(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, struct lpfc_iocbq *cmdiocb)

    Issue abort for a command iocb

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param struct lpfc_iocbq \*cmdiocb:
        Pointer to driver command iocb object.

.. _`lpfc_sli_abort_iotag_issue.description`:

Description
-----------

This function issues an abort iocb for the provided command iocb down to
the port. Other than the case the outstanding command iocb is an abort
request, this function issues abort out unconditionally. This function is
called with hbalock held. The function returns 0 when it fails due to
memory allocation failure or when the command iocb is an abort request.

.. _`lpfc_sli_issue_abort_iotag`:

lpfc_sli_issue_abort_iotag
==========================

.. c:function:: int lpfc_sli_issue_abort_iotag(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, struct lpfc_iocbq *cmdiocb)

    Abort function for a command iocb

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param struct lpfc_iocbq \*cmdiocb:
        Pointer to driver command iocb object.

.. _`lpfc_sli_issue_abort_iotag.description`:

Description
-----------

This function issues an abort iocb for the provided command iocb. In case
of unloading, the abort iocb will not be issued to commands on the ELS
ring. Instead, the callback function shall be changed to those commands
so that nothing happens when them finishes. This function is called with
hbalock held. The function returns 0 when the command iocb is an abort
request.

.. _`lpfc_sli4_abort_nvme_io`:

lpfc_sli4_abort_nvme_io
=======================

.. c:function:: int lpfc_sli4_abort_nvme_io(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, struct lpfc_iocbq *cmdiocb)

    Issue abort for a command iocb

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param struct lpfc_iocbq \*cmdiocb:
        Pointer to driver command iocb object.

.. _`lpfc_sli4_abort_nvme_io.description`:

Description
-----------

This function issues an abort iocb for the provided command iocb down to
the port. Other than the case the outstanding command iocb is an abort
request, this function issues abort out unconditionally. This function is
called with hbalock held. The function returns 0 when it fails due to
memory allocation failure or when the command iocb is an abort request.

.. _`lpfc_sli_hba_iocb_abort`:

lpfc_sli_hba_iocb_abort
=======================

.. c:function:: void lpfc_sli_hba_iocb_abort(struct lpfc_hba *phba)

    Abort all iocbs to an hba.

    :param struct lpfc_hba \*phba:
        pointer to lpfc HBA data structure.

.. _`lpfc_sli_hba_iocb_abort.description`:

Description
-----------

This routine will abort all pending and outstanding iocbs to an HBA.

.. _`lpfc_sli_validate_fcp_iocb`:

lpfc_sli_validate_fcp_iocb
==========================

.. c:function:: int lpfc_sli_validate_fcp_iocb(struct lpfc_iocbq *iocbq, struct lpfc_vport *vport, uint16_t tgt_id, uint64_t lun_id, lpfc_ctx_cmd ctx_cmd)

    find commands associated with a vport or LUN

    :param struct lpfc_iocbq \*iocbq:
        Pointer to driver iocb object.

    :param struct lpfc_vport \*vport:
        Pointer to driver virtual port object.

    :param uint16_t tgt_id:
        SCSI ID of the target.

    :param uint64_t lun_id:
        LUN ID of the scsi device.

    :param lpfc_ctx_cmd ctx_cmd:
        LPFC_CTX_LUN/LPFC_CTX_TGT/LPFC_CTX_HOST

.. _`lpfc_sli_validate_fcp_iocb.description`:

Description
-----------

This function acts as an iocb filter for functions which abort or count
all FCP iocbs pending on a lun/SCSI target/SCSI host. It will return
0 if the filtering criteria is met for the given iocb and will return
1 if the filtering criteria is not met.
If ctx_cmd == LPFC_CTX_LUN, the function returns 0 only if the
given iocb is for the SCSI device specified by vport, tgt_id and
lun_id parameter.
If ctx_cmd == LPFC_CTX_TGT,  the function returns 0 only if the
given iocb is for the SCSI target specified by vport and tgt_id
parameters.
If ctx_cmd == LPFC_CTX_HOST, the function returns 0 only if the
given iocb is for the SCSI host associated with the given vport.
This function is called with no locks held.

.. _`lpfc_sli_sum_iocb`:

lpfc_sli_sum_iocb
=================

.. c:function:: int lpfc_sli_sum_iocb(struct lpfc_vport *vport, uint16_t tgt_id, uint64_t lun_id, lpfc_ctx_cmd ctx_cmd)

    Function to count the number of FCP iocbs pending

    :param struct lpfc_vport \*vport:
        Pointer to virtual port.

    :param uint16_t tgt_id:
        SCSI ID of the target.

    :param uint64_t lun_id:
        LUN ID of the scsi device.

    :param lpfc_ctx_cmd ctx_cmd:
        LPFC_CTX_LUN/LPFC_CTX_TGT/LPFC_CTX_HOST.

.. _`lpfc_sli_sum_iocb.description`:

Description
-----------

This function returns number of FCP commands pending for the vport.
When ctx_cmd == LPFC_CTX_LUN, the function returns number of FCP
commands pending on the vport associated with SCSI device specified
by tgt_id and lun_id parameters.
When ctx_cmd == LPFC_CTX_TGT, the function returns number of FCP
commands pending on the vport associated with SCSI target specified
by tgt_id parameter.
When ctx_cmd == LPFC_CTX_HOST, the function returns number of FCP
commands pending on the vport.
This function returns the number of iocbs which satisfy the filter.
This function is called without any lock held.

.. _`lpfc_sli_abort_fcp_cmpl`:

lpfc_sli_abort_fcp_cmpl
=======================

.. c:function:: void lpfc_sli_abort_fcp_cmpl(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocb, struct lpfc_iocbq *rspiocb)

    Completion handler function for aborted FCP IOCBs

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object

    :param struct lpfc_iocbq \*cmdiocb:
        Pointer to command iocb object.

    :param struct lpfc_iocbq \*rspiocb:
        Pointer to response iocb object.

.. _`lpfc_sli_abort_fcp_cmpl.description`:

Description
-----------

This function is called when an aborted FCP iocb completes. This
function is called by the ring event handler with no lock held.
This function frees the iocb.

.. _`lpfc_sli_abort_iocb`:

lpfc_sli_abort_iocb
===================

.. c:function:: int lpfc_sli_abort_iocb(struct lpfc_vport *vport, struct lpfc_sli_ring *pring, uint16_t tgt_id, uint64_t lun_id, lpfc_ctx_cmd abort_cmd)

    issue abort for all commands on a host/target/LUN

    :param struct lpfc_vport \*vport:
        Pointer to virtual port.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param uint16_t tgt_id:
        SCSI ID of the target.

    :param uint64_t lun_id:
        LUN ID of the scsi device.

    :param lpfc_ctx_cmd abort_cmd:
        LPFC_CTX_LUN/LPFC_CTX_TGT/LPFC_CTX_HOST.

.. _`lpfc_sli_abort_iocb.description`:

Description
-----------

This function sends an abort command for every SCSI command
associated with the given virtual port pending on the ring
filtered by lpfc_sli_validate_fcp_iocb function.
When abort_cmd == LPFC_CTX_LUN, the function sends abort only to the
FCP iocbs associated with lun specified by tgt_id and lun_id
parameters
When abort_cmd == LPFC_CTX_TGT, the function sends abort only to the
FCP iocbs associated with SCSI target specified by tgt_id parameter.
When abort_cmd == LPFC_CTX_HOST, the function sends abort to all
FCP iocbs associated with virtual port.
This function returns number of iocbs it failed to abort.
This function is called with no locks held.

.. _`lpfc_sli_abort_taskmgmt`:

lpfc_sli_abort_taskmgmt
=======================

.. c:function:: int lpfc_sli_abort_taskmgmt(struct lpfc_vport *vport, struct lpfc_sli_ring *pring, uint16_t tgt_id, uint64_t lun_id, lpfc_ctx_cmd cmd)

    issue abort for all commands on a host/target/LUN

    :param struct lpfc_vport \*vport:
        Pointer to virtual port.

    :param struct lpfc_sli_ring \*pring:
        Pointer to driver SLI ring object.

    :param uint16_t tgt_id:
        SCSI ID of the target.

    :param uint64_t lun_id:
        LUN ID of the scsi device.

    :param lpfc_ctx_cmd cmd:
        *undescribed*

.. _`lpfc_sli_abort_taskmgmt.description`:

Description
-----------

This function sends an abort command for every SCSI command
associated with the given virtual port pending on the ring
filtered by lpfc_sli_validate_fcp_iocb function.
When taskmgmt_cmd == LPFC_CTX_LUN, the function sends abort only to the
FCP iocbs associated with lun specified by tgt_id and lun_id
parameters
When taskmgmt_cmd == LPFC_CTX_TGT, the function sends abort only to the
FCP iocbs associated with SCSI target specified by tgt_id parameter.
When taskmgmt_cmd == LPFC_CTX_HOST, the function sends abort to all
FCP iocbs associated with virtual port.
This function returns number of iocbs it aborted .
This function is called with no locks held right after a taskmgmt
command is sent.

.. _`lpfc_sli_wake_iocb_wait`:

lpfc_sli_wake_iocb_wait
=======================

.. c:function:: void lpfc_sli_wake_iocb_wait(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocbq, struct lpfc_iocbq *rspiocbq)

    lpfc_sli_issue_iocb_wait's completion handler

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*cmdiocbq:
        Pointer to command iocb.

    :param struct lpfc_iocbq \*rspiocbq:
        Pointer to response iocb.

.. _`lpfc_sli_wake_iocb_wait.description`:

Description
-----------

This function is the completion handler for iocbs issued using
lpfc_sli_issue_iocb_wait function. This function is called by the
ring event handler function without any lock held. This function
can be called from both worker thread context and interrupt
context. This function also can be called from other thread which
cleans up the SLI layer objects.
This function copy the contents of the response iocb to the
response iocb memory object provided by the caller of
lpfc_sli_issue_iocb_wait and then wakes up the thread which
sleeps for the iocb completion.

.. _`lpfc_chk_iocb_flg`:

lpfc_chk_iocb_flg
=================

.. c:function:: int lpfc_chk_iocb_flg(struct lpfc_hba *phba, struct lpfc_iocbq *piocbq, uint32_t flag)

    Test IOCB flag with lock held.

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object..

    :param struct lpfc_iocbq \*piocbq:
        Pointer to command iocb.

    :param uint32_t flag:
        Flag to test.

.. _`lpfc_chk_iocb_flg.description`:

Description
-----------

This routine grabs the hbalock and then test the iocb_flag to
see if the passed in flag is set.

.. _`lpfc_chk_iocb_flg.return`:

Return
------

1 if flag is set.
0 if flag is not set.

.. _`lpfc_sli_issue_iocb_wait`:

lpfc_sli_issue_iocb_wait
========================

.. c:function:: int lpfc_sli_issue_iocb_wait(struct lpfc_hba *phba, uint32_t ring_number, struct lpfc_iocbq *piocb, struct lpfc_iocbq *prspiocbq, uint32_t timeout)

    Synchronous function to issue iocb commands

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object..

    :param uint32_t ring_number:
        *undescribed*

    :param struct lpfc_iocbq \*piocb:
        Pointer to command iocb.

    :param struct lpfc_iocbq \*prspiocbq:
        Pointer to response iocb.

    :param uint32_t timeout:
        Timeout in number of seconds.

.. _`lpfc_sli_issue_iocb_wait.description`:

Description
-----------

This function issues the iocb to firmware and waits for the
iocb to complete. The iocb_cmpl field of the shall be used
to handle iocbs which time out. If the field is NULL, the
function shall free the iocbq structure.  If more clean up is
needed, the caller is expected to provide a completion function
that will provide the needed clean up.  If the iocb command is
not completed within timeout seconds, the function will either
free the iocbq structure (if iocb_cmpl == NULL) or execute the
completion function set in the iocb_cmpl field and then return
a status of IOCB_TIMEDOUT.  The caller should not free the iocb
resources if this function returns IOCB_TIMEDOUT.
The function waits for the iocb completion using an
non-interruptible wait.
This function will sleep while waiting for iocb completion.
So, this function should not be called from any context which
does not allow sleeping. Due to the same reason, this function
cannot be called with interrupt disabled.
This function assumes that the iocb completions occur while
this function sleep. So, this function cannot be called from
the thread which process iocb completion for this ring.
This function clears the iocb_flag of the iocb object before
issuing the iocb and the iocb completion handler sets this
flag and wakes this thread when the iocb completes.
The contents of the response iocb will be copied to prspiocbq
by the completion handler when the command completes.
This function returns IOCB_SUCCESS when success.
This function is called with no lock held.

.. _`lpfc_sli_issue_mbox_wait`:

lpfc_sli_issue_mbox_wait
========================

.. c:function:: int lpfc_sli_issue_mbox_wait(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmboxq, uint32_t timeout)

    Synchronous function to issue mailbox

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param LPFC_MBOXQ_t \*pmboxq:
        Pointer to driver mailbox object.

    :param uint32_t timeout:
        Timeout in number of seconds.

.. _`lpfc_sli_issue_mbox_wait.description`:

Description
-----------

This function issues the mailbox to firmware and waits for the
mailbox command to complete. If the mailbox command is not
completed within timeout seconds, it returns MBX_TIMEOUT.
The function waits for the mailbox completion using an
interruptible wait. If the thread is woken up due to a
signal, MBX_TIMEOUT error is returned to the caller. Caller
should not free the mailbox resources, if this function returns
MBX_TIMEOUT.
This function will sleep while waiting for mailbox completion.
So, this function should not be called from any context which
does not allow sleeping. Due to the same reason, this function
cannot be called with interrupt disabled.
This function assumes that the mailbox completion occurs while
this function sleep. So, this function cannot be called from
the worker thread which processes mailbox completion.
This function is called in the context of HBA management
applications.
This function returns MBX_SUCCESS when successful.
This function is called with no lock held.

.. _`lpfc_sli_mbox_sys_shutdown`:

lpfc_sli_mbox_sys_shutdown
==========================

.. c:function:: void lpfc_sli_mbox_sys_shutdown(struct lpfc_hba *phba, int mbx_action)

    shutdown mailbox command sub-system

    :param struct lpfc_hba \*phba:
        Pointer to HBA context.

    :param int mbx_action:
        *undescribed*

.. _`lpfc_sli_mbox_sys_shutdown.description`:

Description
-----------

This function is called to shutdown the driver's mailbox sub-system.
It first marks the mailbox sub-system is in a block state to prevent
the asynchronous mailbox command from issued off the pending mailbox
command queue. If the mailbox command sub-system shutdown is due to
HBA error conditions such as EEH or ERATT, this routine shall invoke
the mailbox sub-system flush routine to forcefully bring down the
mailbox sub-system. Otherwise, if it is due to normal condition (such
as with offline or HBA function reset), this routine will wait for the
outstanding mailbox command to complete before invoking the mailbox
sub-system flush routine to gracefully bring down mailbox sub-system.

.. _`lpfc_sli_eratt_read`:

lpfc_sli_eratt_read
===================

.. c:function:: int lpfc_sli_eratt_read(struct lpfc_hba *phba)

    read sli-3 error attention events

    :param struct lpfc_hba \*phba:
        Pointer to HBA context.

.. _`lpfc_sli_eratt_read.description`:

Description
-----------

This function is called to read the SLI3 device error attention registers
for possible error attention events. The caller must hold the hostlock
with \ :c:func:`spin_lock_irq`\ .

This function returns 1 when there is Error Attention in the Host Attention
Register and returns 0 otherwise.

.. _`lpfc_sli4_eratt_read`:

lpfc_sli4_eratt_read
====================

.. c:function:: int lpfc_sli4_eratt_read(struct lpfc_hba *phba)

    read sli-4 error attention events

    :param struct lpfc_hba \*phba:
        Pointer to HBA context.

.. _`lpfc_sli4_eratt_read.description`:

Description
-----------

This function is called to read the SLI4 device error attention registers
for possible error attention events. The caller must hold the hostlock
with \ :c:func:`spin_lock_irq`\ .

This function returns 1 when there is Error Attention in the Host Attention
Register and returns 0 otherwise.

.. _`lpfc_sli_check_eratt`:

lpfc_sli_check_eratt
====================

.. c:function:: int lpfc_sli_check_eratt(struct lpfc_hba *phba)

    check error attention events

    :param struct lpfc_hba \*phba:
        Pointer to HBA context.

.. _`lpfc_sli_check_eratt.description`:

Description
-----------

This function is called from timer soft interrupt context to check HBA's
error attention register bit for error attention events.

This function returns 1 when there is Error Attention in the Host Attention
Register and returns 0 otherwise.

.. _`lpfc_intr_state_check`:

lpfc_intr_state_check
=====================

.. c:function:: int lpfc_intr_state_check(struct lpfc_hba *phba)

    Check device state for interrupt handling

    :param struct lpfc_hba \*phba:
        Pointer to HBA context.

.. _`lpfc_intr_state_check.description`:

Description
-----------

This inline routine checks whether a device or its PCI slot is in a state
that the interrupt should be handled.

This function returns 0 if the device or the PCI slot is in a state that
interrupt should be handled, otherwise -EIO.

.. _`lpfc_sli_sp_intr_handler`:

lpfc_sli_sp_intr_handler
========================

.. c:function:: irqreturn_t lpfc_sli_sp_intr_handler(int irq, void *dev_id)

    Slow-path interrupt handler to SLI-3 device

    :param int irq:
        Interrupt number.

    :param void \*dev_id:
        The device context pointer.

.. _`lpfc_sli_sp_intr_handler.description`:

Description
-----------

This function is directly called from the PCI layer as an interrupt
service routine when device with SLI-3 interface spec is enabled with
MSI-X multi-message interrupt mode and there are slow-path events in
the HBA. However, when the device is enabled with either MSI or Pin-IRQ
interrupt mode, this function is called as part of the device-level
interrupt handler. When the PCI slot is in error recovery or the HBA
is undergoing initialization, the interrupt handler will not process
the interrupt. The link attention and ELS ring attention events are
handled by the worker thread. The interrupt handler signals the worker
thread and returns for these events. This function is called without
any lock held. It gets the hbalock to access and update SLI data
structures.

This function returns IRQ_HANDLED when interrupt is handled else it
returns IRQ_NONE.

.. _`lpfc_sli_fp_intr_handler`:

lpfc_sli_fp_intr_handler
========================

.. c:function:: irqreturn_t lpfc_sli_fp_intr_handler(int irq, void *dev_id)

    Fast-path interrupt handler to SLI-3 device.

    :param int irq:
        Interrupt number.

    :param void \*dev_id:
        The device context pointer.

.. _`lpfc_sli_fp_intr_handler.description`:

Description
-----------

This function is directly called from the PCI layer as an interrupt
service routine when device with SLI-3 interface spec is enabled with
MSI-X multi-message interrupt mode and there is a fast-path FCP IOCB
ring event in the HBA. However, when the device is enabled with either
MSI or Pin-IRQ interrupt mode, this function is called as part of the
device-level interrupt handler. When the PCI slot is in error recovery
or the HBA is undergoing initialization, the interrupt handler will not
process the interrupt. The SCSI FCP fast-path ring event are handled in
the intrrupt context. This function is called without any lock held.
It gets the hbalock to access and update SLI data structures.

This function returns IRQ_HANDLED when interrupt is handled else it
returns IRQ_NONE.

.. _`lpfc_sli_intr_handler`:

lpfc_sli_intr_handler
=====================

.. c:function:: irqreturn_t lpfc_sli_intr_handler(int irq, void *dev_id)

    Device-level interrupt handler to SLI-3 device

    :param int irq:
        Interrupt number.

    :param void \*dev_id:
        The device context pointer.

.. _`lpfc_sli_intr_handler.description`:

Description
-----------

This function is the HBA device-level interrupt handler to device with
SLI-3 interface spec, called from the PCI layer when either MSI or
Pin-IRQ interrupt mode is enabled and there is an event in the HBA which
requires driver attention. This function invokes the slow-path interrupt
attention handling function and fast-path interrupt attention handling
function in turn to process the relevant HBA attention events. This
function is called without any lock held. It gets the hbalock to access
and update SLI data structures.

This function returns IRQ_HANDLED when interrupt is handled, else it
returns IRQ_NONE.

.. _`lpfc_sli4_fcp_xri_abort_event_proc`:

lpfc_sli4_fcp_xri_abort_event_proc
==================================

.. c:function:: void lpfc_sli4_fcp_xri_abort_event_proc(struct lpfc_hba *phba)

    Process fcp xri abort event

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_sli4_fcp_xri_abort_event_proc.description`:

Description
-----------

This routine is invoked by the worker thread to process all the pending
SLI4 FCP abort XRI events.

.. _`lpfc_sli4_els_xri_abort_event_proc`:

lpfc_sli4_els_xri_abort_event_proc
==================================

.. c:function:: void lpfc_sli4_els_xri_abort_event_proc(struct lpfc_hba *phba)

    Process els xri abort event

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_sli4_els_xri_abort_event_proc.description`:

Description
-----------

This routine is invoked by the worker thread to process all the pending
SLI4 els abort xri events.

.. _`lpfc_sli4_iocb_param_transfer`:

lpfc_sli4_iocb_param_transfer
=============================

.. c:function:: void lpfc_sli4_iocb_param_transfer(struct lpfc_hba *phba, struct lpfc_iocbq *pIocbIn, struct lpfc_iocbq *pIocbOut, struct lpfc_wcqe_complete *wcqe)

    Transfer pIocbOut and cmpl status to pIocbIn

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure

    :param struct lpfc_iocbq \*pIocbIn:
        pointer to the rspiocbq

    :param struct lpfc_iocbq \*pIocbOut:
        pointer to the cmdiocbq

    :param struct lpfc_wcqe_complete \*wcqe:
        pointer to the complete wcqe

.. _`lpfc_sli4_iocb_param_transfer.description`:

Description
-----------

This routine transfers the fields of a command iocbq to a response iocbq
by copying all the IOCB fields from command iocbq and transferring the
completion status information from the complete wcqe.

.. _`lpfc_sli4_els_wcqe_to_rspiocbq`:

lpfc_sli4_els_wcqe_to_rspiocbq
==============================

.. c:function:: struct lpfc_iocbq *lpfc_sli4_els_wcqe_to_rspiocbq(struct lpfc_hba *phba, struct lpfc_iocbq *irspiocbq)

    Get response iocbq from els wcqe

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*irspiocbq:
        *undescribed*

.. _`lpfc_sli4_els_wcqe_to_rspiocbq.description`:

Description
-----------

This routine handles an ELS work-queue completion event and construct
a pseudo response ELS IODBQ from the SLI4 ELS WCQE for the common
discovery engine to handle.

.. _`lpfc_sli4_els_wcqe_to_rspiocbq.return`:

Return
------

Pointer to the receive IOCBQ, NULL otherwise.

.. _`lpfc_sli4_sp_handle_async_event`:

lpfc_sli4_sp_handle_async_event
===============================

.. c:function:: bool lpfc_sli4_sp_handle_async_event(struct lpfc_hba *phba, struct lpfc_mcqe *mcqe)

    Handle an asynchroous event

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_mcqe \*mcqe:
        *undescribed*

.. _`lpfc_sli4_sp_handle_async_event.description`:

Description
-----------

This routine process a mailbox completion queue entry with asynchrous
event.

.. _`lpfc_sli4_sp_handle_async_event.return`:

Return
------

true if work posted to worker thread, otherwise false.

.. _`lpfc_sli4_sp_handle_mbox_event`:

lpfc_sli4_sp_handle_mbox_event
==============================

.. c:function:: bool lpfc_sli4_sp_handle_mbox_event(struct lpfc_hba *phba, struct lpfc_mcqe *mcqe)

    Handle a mailbox completion event

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_mcqe \*mcqe:
        *undescribed*

.. _`lpfc_sli4_sp_handle_mbox_event.description`:

Description
-----------

This routine process a mailbox completion queue entry with mailbox
completion event.

.. _`lpfc_sli4_sp_handle_mbox_event.return`:

Return
------

true if work posted to worker thread, otherwise false.

.. _`lpfc_sli4_sp_handle_mcqe`:

lpfc_sli4_sp_handle_mcqe
========================

.. c:function:: bool lpfc_sli4_sp_handle_mcqe(struct lpfc_hba *phba, struct lpfc_cqe *cqe)

    Process a mailbox completion queue entry

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_cqe \*cqe:
        Pointer to mailbox completion queue entry.

.. _`lpfc_sli4_sp_handle_mcqe.description`:

Description
-----------

This routine process a mailbox completion queue entry, it invokes the
proper mailbox complete handling or asynchrous event handling routine
according to the MCQE's async bit.

.. _`lpfc_sli4_sp_handle_mcqe.return`:

Return
------

true if work posted to worker thread, otherwise false.

.. _`lpfc_sli4_sp_handle_els_wcqe`:

lpfc_sli4_sp_handle_els_wcqe
============================

.. c:function:: bool lpfc_sli4_sp_handle_els_wcqe(struct lpfc_hba *phba, struct lpfc_queue *cq, struct lpfc_wcqe_complete *wcqe)

    Handle els work-queue completion event

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_queue \*cq:
        Pointer to associated CQ

    :param struct lpfc_wcqe_complete \*wcqe:
        Pointer to work-queue completion queue entry.

.. _`lpfc_sli4_sp_handle_els_wcqe.description`:

Description
-----------

This routine handles an ELS work-queue completion event.

.. _`lpfc_sli4_sp_handle_els_wcqe.return`:

Return
------

true if work posted to worker thread, otherwise false.

.. _`lpfc_sli4_sp_handle_rel_wcqe`:

lpfc_sli4_sp_handle_rel_wcqe
============================

.. c:function:: void lpfc_sli4_sp_handle_rel_wcqe(struct lpfc_hba *phba, struct lpfc_wcqe_release *wcqe)

    Handle slow-path WQ entry consumed event

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_wcqe_release \*wcqe:
        Pointer to work-queue completion queue entry.

.. _`lpfc_sli4_sp_handle_rel_wcqe.description`:

Description
-----------

This routine handles slow-path WQ entry consumed event by invoking the
proper WQ release routine to the slow-path WQ.

.. _`lpfc_sli4_sp_handle_abort_xri_wcqe`:

lpfc_sli4_sp_handle_abort_xri_wcqe
==================================

.. c:function:: bool lpfc_sli4_sp_handle_abort_xri_wcqe(struct lpfc_hba *phba, struct lpfc_queue *cq, struct sli4_wcqe_xri_aborted *wcqe)

    Handle a xri abort event

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_queue \*cq:
        Pointer to a WQ completion queue.

    :param struct sli4_wcqe_xri_aborted \*wcqe:
        Pointer to work-queue completion queue entry.

.. _`lpfc_sli4_sp_handle_abort_xri_wcqe.description`:

Description
-----------

This routine handles an XRI abort event.

.. _`lpfc_sli4_sp_handle_abort_xri_wcqe.return`:

Return
------

true if work posted to worker thread, otherwise false.

.. _`lpfc_sli4_sp_handle_rcqe`:

lpfc_sli4_sp_handle_rcqe
========================

.. c:function:: bool lpfc_sli4_sp_handle_rcqe(struct lpfc_hba *phba, struct lpfc_rcqe *rcqe)

    Process a receive-queue completion queue entry

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_rcqe \*rcqe:
        Pointer to receive-queue completion queue entry.

.. _`lpfc_sli4_sp_handle_rcqe.description`:

Description
-----------

This routine process a receive-queue completion queue entry.

.. _`lpfc_sli4_sp_handle_rcqe.return`:

Return
------

true if work posted to worker thread, otherwise false.

.. _`lpfc_sli4_sp_handle_cqe`:

lpfc_sli4_sp_handle_cqe
=======================

.. c:function:: bool lpfc_sli4_sp_handle_cqe(struct lpfc_hba *phba, struct lpfc_queue *cq, struct lpfc_cqe *cqe)

    Process a slow path completion queue entry

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_queue \*cq:
        Pointer to the completion queue.

    :param struct lpfc_cqe \*cqe:
        *undescribed*

.. _`lpfc_sli4_sp_handle_cqe.description`:

Description
-----------

This routine process a slow-path work-queue or receive queue completion queue
entry.

.. _`lpfc_sli4_sp_handle_cqe.return`:

Return
------

true if work posted to worker thread, otherwise false.

.. _`lpfc_sli4_sp_handle_eqe`:

lpfc_sli4_sp_handle_eqe
=======================

.. c:function:: void lpfc_sli4_sp_handle_eqe(struct lpfc_hba *phba, struct lpfc_eqe *eqe, struct lpfc_queue *speq)

    Process a slow-path event queue entry

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_eqe \*eqe:
        Pointer to fast-path event queue entry.

    :param struct lpfc_queue \*speq:
        *undescribed*

.. _`lpfc_sli4_sp_handle_eqe.description`:

Description
-----------

This routine process a event queue entry from the slow-path event queue.
It will check the MajorCode and MinorCode to determine this is for a
completion event on a completion queue, if not, an error shall be logged
and just return. Otherwise, it will get to the corresponding completion
queue and process all the entries on that completion queue, rearm the
completion queue, and then return.

.. _`lpfc_sli4_sp_process_cq`:

lpfc_sli4_sp_process_cq
=======================

.. c:function:: void lpfc_sli4_sp_process_cq(struct work_struct *work)

    Process a slow-path event queue entry

    :param struct work_struct \*work:
        *undescribed*

.. _`lpfc_sli4_sp_process_cq.description`:

Description
-----------

This routine process a event queue entry from the slow-path event queue.
It will check the MajorCode and MinorCode to determine this is for a
completion event on a completion queue, if not, an error shall be logged
and just return. Otherwise, it will get to the corresponding completion
queue and process all the entries on that completion queue, rearm the
completion queue, and then return.

.. _`lpfc_sli4_fp_handle_fcp_wcqe`:

lpfc_sli4_fp_handle_fcp_wcqe
============================

.. c:function:: void lpfc_sli4_fp_handle_fcp_wcqe(struct lpfc_hba *phba, struct lpfc_queue *cq, struct lpfc_wcqe_complete *wcqe)

    Process fast-path work queue completion entry

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_queue \*cq:
        Pointer to associated CQ

    :param struct lpfc_wcqe_complete \*wcqe:
        Pointer to work-queue completion queue entry.

.. _`lpfc_sli4_fp_handle_fcp_wcqe.description`:

Description
-----------

This routine process a fast-path work queue completion entry from fast-path
event queue for FCP command response completion.

.. _`lpfc_sli4_fp_handle_rel_wcqe`:

lpfc_sli4_fp_handle_rel_wcqe
============================

.. c:function:: void lpfc_sli4_fp_handle_rel_wcqe(struct lpfc_hba *phba, struct lpfc_queue *cq, struct lpfc_wcqe_release *wcqe)

    Handle fast-path WQ entry consumed event

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_queue \*cq:
        Pointer to completion queue.

    :param struct lpfc_wcqe_release \*wcqe:
        Pointer to work-queue completion queue entry.

.. _`lpfc_sli4_fp_handle_rel_wcqe.description`:

Description
-----------

This routine handles an fast-path WQ entry consumed event by invoking the
proper WQ release routine to the slow-path WQ.

.. _`lpfc_sli4_nvmet_handle_rcqe`:

lpfc_sli4_nvmet_handle_rcqe
===========================

.. c:function:: bool lpfc_sli4_nvmet_handle_rcqe(struct lpfc_hba *phba, struct lpfc_queue *cq, struct lpfc_rcqe *rcqe)

    Process a receive-queue completion queue entry

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_queue \*cq:
        *undescribed*

    :param struct lpfc_rcqe \*rcqe:
        Pointer to receive-queue completion queue entry.

.. _`lpfc_sli4_nvmet_handle_rcqe.description`:

Description
-----------

This routine process a receive-queue completion queue entry.

.. _`lpfc_sli4_nvmet_handle_rcqe.return`:

Return
------

true if work posted to worker thread, otherwise false.

.. _`lpfc_sli4_fp_handle_cqe`:

lpfc_sli4_fp_handle_cqe
=======================

.. c:function:: int lpfc_sli4_fp_handle_cqe(struct lpfc_hba *phba, struct lpfc_queue *cq, struct lpfc_cqe *cqe)

    Process fast-path work queue completion entry

    :param struct lpfc_hba \*phba:
        *undescribed*

    :param struct lpfc_queue \*cq:
        Pointer to the completion queue.

    :param struct lpfc_cqe \*cqe:
        *undescribed*

.. _`lpfc_sli4_fp_handle_cqe.description`:

Description
-----------

This routine process a fast-path work queue completion entry from fast-path
event queue for FCP command response completion.

.. _`lpfc_sli4_hba_handle_eqe`:

lpfc_sli4_hba_handle_eqe
========================

.. c:function:: void lpfc_sli4_hba_handle_eqe(struct lpfc_hba *phba, struct lpfc_eqe *eqe, uint32_t qidx)

    Process a fast-path event queue entry

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_eqe \*eqe:
        Pointer to fast-path event queue entry.

    :param uint32_t qidx:
        *undescribed*

.. _`lpfc_sli4_hba_handle_eqe.description`:

Description
-----------

This routine process a event queue entry from the fast-path event queue.
It will check the MajorCode and MinorCode to determine this is for a
completion event on a completion queue, if not, an error shall be logged
and just return. Otherwise, it will get to the corresponding completion
queue and process all the entries on the completion queue, rearm the
completion queue, and then return.

.. _`lpfc_sli4_hba_process_cq`:

lpfc_sli4_hba_process_cq
========================

.. c:function:: void lpfc_sli4_hba_process_cq(struct work_struct *work)

    Process a fast-path event queue entry

    :param struct work_struct \*work:
        *undescribed*

.. _`lpfc_sli4_hba_process_cq.description`:

Description
-----------

This routine process a event queue entry from the fast-path event queue.
It will check the MajorCode and MinorCode to determine this is for a
completion event on a completion queue, if not, an error shall be logged
and just return. Otherwise, it will get to the corresponding completion
queue and process all the entries on the completion queue, rearm the
completion queue, and then return.

.. _`lpfc_sli4_fof_handle_eqe`:

lpfc_sli4_fof_handle_eqe
========================

.. c:function:: void lpfc_sli4_fof_handle_eqe(struct lpfc_hba *phba, struct lpfc_eqe *eqe)

    Process a Flash Optimized Fabric event queue entry

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_eqe \*eqe:
        Pointer to fast-path event queue entry.

.. _`lpfc_sli4_fof_handle_eqe.description`:

Description
-----------

This routine process a event queue entry from the Flash Optimized Fabric
event queue.  It will check the MajorCode and MinorCode to determine this
is for a completion event on a completion queue, if not, an error shall be
logged and just return. Otherwise, it will get to the corresponding
completion queue and process all the entries on the completion queue, rearm
the completion queue, and then return.

.. _`lpfc_sli4_fof_intr_handler`:

lpfc_sli4_fof_intr_handler
==========================

.. c:function:: irqreturn_t lpfc_sli4_fof_intr_handler(int irq, void *dev_id)

    HBA interrupt handler to SLI-4 device

    :param int irq:
        Interrupt number.

    :param void \*dev_id:
        The device context pointer.

.. _`lpfc_sli4_fof_intr_handler.description`:

Description
-----------

This function is directly called from the PCI layer as an interrupt
service routine when device with SLI-4 interface spec is enabled with
MSI-X multi-message interrupt mode and there is a Flash Optimized Fabric
IOCB ring event in the HBA. However, when the device is enabled with either
MSI or Pin-IRQ interrupt mode, this function is called as part of the
device-level interrupt handler. When the PCI slot is in error recovery
or the HBA is undergoing initialization, the interrupt handler will not
process the interrupt. The Flash Optimized Fabric ring event are handled in
the intrrupt context. This function is called without any lock held.
It gets the hbalock to access and update SLI data structures. Note that,
the EQ to CQ are one-to-one map such that the EQ index is
equal to that of CQ index.

This function returns IRQ_HANDLED when interrupt is handled else it
returns IRQ_NONE.

.. _`lpfc_sli4_hba_intr_handler`:

lpfc_sli4_hba_intr_handler
==========================

.. c:function:: irqreturn_t lpfc_sli4_hba_intr_handler(int irq, void *dev_id)

    HBA interrupt handler to SLI-4 device

    :param int irq:
        Interrupt number.

    :param void \*dev_id:
        The device context pointer.

.. _`lpfc_sli4_hba_intr_handler.description`:

Description
-----------

This function is directly called from the PCI layer as an interrupt
service routine when device with SLI-4 interface spec is enabled with
MSI-X multi-message interrupt mode and there is a fast-path FCP IOCB
ring event in the HBA. However, when the device is enabled with either
MSI or Pin-IRQ interrupt mode, this function is called as part of the
device-level interrupt handler. When the PCI slot is in error recovery
or the HBA is undergoing initialization, the interrupt handler will not
process the interrupt. The SCSI FCP fast-path ring event are handled in
the intrrupt context. This function is called without any lock held.
It gets the hbalock to access and update SLI data structures. Note that,
the FCP EQ to FCP CQ are one-to-one map such that the FCP EQ index is
equal to that of FCP CQ index.

The link attention and ELS ring attention events are handled
by the worker thread. The interrupt handler signals the worker thread
and returns for these events. This function is called without any lock
held. It gets the hbalock to access and update SLI data structures.

This function returns IRQ_HANDLED when interrupt is handled else it
returns IRQ_NONE.

.. _`lpfc_sli4_intr_handler`:

lpfc_sli4_intr_handler
======================

.. c:function:: irqreturn_t lpfc_sli4_intr_handler(int irq, void *dev_id)

    Device-level interrupt handler for SLI-4 device

    :param int irq:
        Interrupt number.

    :param void \*dev_id:
        The device context pointer.

.. _`lpfc_sli4_intr_handler.description`:

Description
-----------

This function is the device-level interrupt handler to device with SLI-4
interface spec, called from the PCI layer when either MSI or Pin-IRQ
interrupt mode is enabled and there is an event in the HBA which requires
driver attention. This function invokes the slow-path interrupt attention
handling function and fast-path interrupt attention handling function in
turn to process the relevant HBA attention events. This function is called
without any lock held. It gets the hbalock to access and update SLI data
structures.

This function returns IRQ_HANDLED when interrupt is handled, else it
returns IRQ_NONE.

.. _`lpfc_sli4_queue_free`:

lpfc_sli4_queue_free
====================

.. c:function:: void lpfc_sli4_queue_free(struct lpfc_queue *queue)

    free a queue structure and associated memory

    :param struct lpfc_queue \*queue:
        The queue structure to free.

.. _`lpfc_sli4_queue_free.description`:

Description
-----------

This function frees a queue structure and the DMAable memory used for
the host resident queue. This function must be called after destroying the
queue on the HBA.

.. _`lpfc_sli4_queue_alloc`:

lpfc_sli4_queue_alloc
=====================

.. c:function:: struct lpfc_queue *lpfc_sli4_queue_alloc(struct lpfc_hba *phba, uint32_t page_size, uint32_t entry_size, uint32_t entry_count)

    Allocate and initialize a queue structure

    :param struct lpfc_hba \*phba:
        The HBA that this queue is being created on.

    :param uint32_t page_size:
        The size of a queue page

    :param uint32_t entry_size:
        The size of each queue entry for this queue.

    :param uint32_t entry_count:
        *undescribed*

.. _`lpfc_sli4_queue_alloc.description`:

Description
-----------

This function allocates a queue structure and the DMAable memory used for
the host resident queue. This function must be called before creating the
queue on the HBA.

.. _`lpfc_dual_chute_pci_bar_map`:

lpfc_dual_chute_pci_bar_map
===========================

.. c:function:: void __iomem *lpfc_dual_chute_pci_bar_map(struct lpfc_hba *phba, uint16_t pci_barset)

    Map pci base address register to host memory

    :param struct lpfc_hba \*phba:
        HBA structure that indicates port to create a queue on.

    :param uint16_t pci_barset:
        PCI BAR set flag.

.. _`lpfc_dual_chute_pci_bar_map.description`:

Description
-----------

This function shall perform iomap of the specified PCI BAR address to host
memory address if not already done so and return it. The returned host
memory address can be NULL.

.. _`lpfc_modify_hba_eq_delay`:

lpfc_modify_hba_eq_delay
========================

.. c:function:: int lpfc_modify_hba_eq_delay(struct lpfc_hba *phba, uint32_t startq, uint32_t numq, uint32_t imax)

    Modify Delay Multiplier on FCP EQs

    :param struct lpfc_hba \*phba:
        HBA structure that indicates port to create a queue on.

    :param uint32_t startq:
        The starting FCP EQ to modify

    :param uint32_t numq:
        *undescribed*

    :param uint32_t imax:
        *undescribed*

.. _`lpfc_modify_hba_eq_delay.description`:

Description
-----------

This function sends an MODIFY_EQ_DELAY mailbox command to the HBA.
The command allows up to LPFC_MAX_EQ_DELAY_EQID_CNT EQ ID's to be
updated in one mailbox command.

The \ ``phba``\  struct is used to send mailbox command to HBA. The \ ``startq``\ 
is used to get the starting FCP EQ to change.
This function is asynchronous and will wait for the mailbox
command to finish before continuing.

On success this function will return a zero. If unable to allocate enough
memory this function will return -ENOMEM. If the queue create mailbox command
fails this function will return -ENXIO.

.. _`lpfc_eq_create`:

lpfc_eq_create
==============

.. c:function:: int lpfc_eq_create(struct lpfc_hba *phba, struct lpfc_queue *eq, uint32_t imax)

    Create an Event Queue on the HBA

    :param struct lpfc_hba \*phba:
        HBA structure that indicates port to create a queue on.

    :param struct lpfc_queue \*eq:
        The queue structure to use to create the event queue.

    :param uint32_t imax:
        The maximum interrupt per second limit.

.. _`lpfc_eq_create.description`:

Description
-----------

This function creates an event queue, as detailed in \ ``eq``\ , on a port,
described by \ ``phba``\  by sending an EQ_CREATE mailbox command to the HBA.

The \ ``phba``\  struct is used to send mailbox command to HBA. The \ ``eq``\  struct
is used to get the entry count and entry size that are necessary to
determine the number of pages to allocate and use for this queue. This
function will send the EQ_CREATE mailbox command to the HBA to setup the
event queue. This function is asynchronous and will wait for the mailbox
command to finish before continuing.

On success this function will return a zero. If unable to allocate enough
memory this function will return -ENOMEM. If the queue create mailbox command
fails this function will return -ENXIO.

.. _`lpfc_cq_create`:

lpfc_cq_create
==============

.. c:function:: int lpfc_cq_create(struct lpfc_hba *phba, struct lpfc_queue *cq, struct lpfc_queue *eq, uint32_t type, uint32_t subtype)

    Create a Completion Queue on the HBA

    :param struct lpfc_hba \*phba:
        HBA structure that indicates port to create a queue on.

    :param struct lpfc_queue \*cq:
        The queue structure to use to create the completion queue.

    :param struct lpfc_queue \*eq:
        The event queue to bind this completion queue to.

    :param uint32_t type:
        *undescribed*

    :param uint32_t subtype:
        *undescribed*

.. _`lpfc_cq_create.description`:

Description
-----------

This function creates a completion queue, as detailed in \ ``wq``\ , on a port,
described by \ ``phba``\  by sending a CQ_CREATE mailbox command to the HBA.

The \ ``phba``\  struct is used to send mailbox command to HBA. The \ ``cq``\  struct
is used to get the entry count and entry size that are necessary to
determine the number of pages to allocate and use for this queue. The \ ``eq``\ 
is used to indicate which event queue to bind this completion queue to. This
function will send the CQ_CREATE mailbox command to the HBA to setup the
completion queue. This function is asynchronous and will wait for the mailbox
command to finish before continuing.

On success this function will return a zero. If unable to allocate enough
memory this function will return -ENOMEM. If the queue create mailbox command
fails this function will return -ENXIO.

.. _`lpfc_cq_create_set`:

lpfc_cq_create_set
==================

.. c:function:: int lpfc_cq_create_set(struct lpfc_hba *phba, struct lpfc_queue **cqp, struct lpfc_queue **eqp, uint32_t type, uint32_t subtype)

    Create a set of Completion Queues on the HBA for MRQ

    :param struct lpfc_hba \*phba:
        HBA structure that indicates port to create a queue on.

    :param struct lpfc_queue \*\*cqp:
        The queue structure array to use to create the completion queues.

    :param struct lpfc_queue \*\*eqp:
        The event queue array to bind these completion queues to.

    :param uint32_t type:
        *undescribed*

    :param uint32_t subtype:
        *undescribed*

.. _`lpfc_cq_create_set.description`:

Description
-----------

This function creates a set of  completion queue, s to support MRQ
as detailed in \ ``cqp``\ , on a port,
described by \ ``phba``\  by sending a CREATE_CQ_SET mailbox command to the HBA.

The \ ``phba``\  struct is used to send mailbox command to HBA. The \ ``cq``\  struct
is used to get the entry count and entry size that are necessary to
determine the number of pages to allocate and use for this queue. The \ ``eq``\ 
is used to indicate which event queue to bind this completion queue to. This
function will send the CREATE_CQ_SET mailbox command to the HBA to setup the
completion queue. This function is asynchronous and will wait for the mailbox
command to finish before continuing.

On success this function will return a zero. If unable to allocate enough
memory this function will return -ENOMEM. If the queue create mailbox command
fails this function will return -ENXIO.

.. _`lpfc_mq_create_fb_init`:

lpfc_mq_create_fb_init
======================

.. c:function:: void lpfc_mq_create_fb_init(struct lpfc_hba *phba, struct lpfc_queue *mq, LPFC_MBOXQ_t *mbox, struct lpfc_queue *cq)

    Send MCC_CREATE without async events registration

    :param struct lpfc_hba \*phba:
        HBA structure that indicates port to create a queue on.

    :param struct lpfc_queue \*mq:
        The queue structure to use to create the mailbox queue.

    :param LPFC_MBOXQ_t \*mbox:
        An allocated pointer to type LPFC_MBOXQ_t

    :param struct lpfc_queue \*cq:
        The completion queue to associate with this cq.

.. _`lpfc_mq_create_fb_init.description`:

Description
-----------

This function provides failback (fb) functionality when the
mq_create_ext fails on older FW generations.  It's purpose is identical
to mq_create_ext otherwise.

This routine cannot fail as all attributes were previously accessed and
initialized in mq_create_ext.

.. _`lpfc_mq_create`:

lpfc_mq_create
==============

.. c:function:: int32_t lpfc_mq_create(struct lpfc_hba *phba, struct lpfc_queue *mq, struct lpfc_queue *cq, uint32_t subtype)

    Create a mailbox Queue on the HBA

    :param struct lpfc_hba \*phba:
        HBA structure that indicates port to create a queue on.

    :param struct lpfc_queue \*mq:
        The queue structure to use to create the mailbox queue.

    :param struct lpfc_queue \*cq:
        The completion queue to associate with this cq.

    :param uint32_t subtype:
        The queue's subtype.

.. _`lpfc_mq_create.description`:

Description
-----------

This function creates a mailbox queue, as detailed in \ ``mq``\ , on a port,
described by \ ``phba``\  by sending a MQ_CREATE mailbox command to the HBA.

The \ ``phba``\  struct is used to send mailbox command to HBA. The \ ``cq``\  struct
is used to get the entry count and entry size that are necessary to
determine the number of pages to allocate and use for this queue. This
function will send the MQ_CREATE mailbox command to the HBA to setup the
mailbox queue. This function is asynchronous and will wait for the mailbox
command to finish before continuing.

On success this function will return a zero. If unable to allocate enough
memory this function will return -ENOMEM. If the queue create mailbox command
fails this function will return -ENXIO.

.. _`lpfc_wq_create`:

lpfc_wq_create
==============

.. c:function:: int lpfc_wq_create(struct lpfc_hba *phba, struct lpfc_queue *wq, struct lpfc_queue *cq, uint32_t subtype)

    Create a Work Queue on the HBA

    :param struct lpfc_hba \*phba:
        HBA structure that indicates port to create a queue on.

    :param struct lpfc_queue \*wq:
        The queue structure to use to create the work queue.

    :param struct lpfc_queue \*cq:
        The completion queue to bind this work queue to.

    :param uint32_t subtype:
        The subtype of the work queue indicating its functionality.

.. _`lpfc_wq_create.description`:

Description
-----------

This function creates a work queue, as detailed in \ ``wq``\ , on a port, described
by \ ``phba``\  by sending a WQ_CREATE mailbox command to the HBA.

The \ ``phba``\  struct is used to send mailbox command to HBA. The \ ``wq``\  struct
is used to get the entry count and entry size that are necessary to
determine the number of pages to allocate and use for this queue. The \ ``cq``\ 
is used to indicate which completion queue to bind this work queue to. This
function will send the WQ_CREATE mailbox command to the HBA to setup the
work queue. This function is asynchronous and will wait for the mailbox
command to finish before continuing.

On success this function will return a zero. If unable to allocate enough
memory this function will return -ENOMEM. If the queue create mailbox command
fails this function will return -ENXIO.

.. _`lpfc_rq_create`:

lpfc_rq_create
==============

.. c:function:: int lpfc_rq_create(struct lpfc_hba *phba, struct lpfc_queue *hrq, struct lpfc_queue *drq, struct lpfc_queue *cq, uint32_t subtype)

    Create a Receive Queue on the HBA

    :param struct lpfc_hba \*phba:
        HBA structure that indicates port to create a queue on.

    :param struct lpfc_queue \*hrq:
        The queue structure to use to create the header receive queue.

    :param struct lpfc_queue \*drq:
        The queue structure to use to create the data receive queue.

    :param struct lpfc_queue \*cq:
        The completion queue to bind this work queue to.

    :param uint32_t subtype:
        *undescribed*

.. _`lpfc_rq_create.description`:

Description
-----------

This function creates a receive buffer queue pair , as detailed in \ ``hrq``\  and
\ ``drq``\ , on a port, described by \ ``phba``\  by sending a RQ_CREATE mailbox command
to the HBA.

The \ ``phba``\  struct is used to send mailbox command to HBA. The \ ``drq``\  and \ ``hrq``\ 
struct is used to get the entry count that is necessary to determine the
number of pages to use for this queue. The \ ``cq``\  is used to indicate which
completion queue to bind received buffers that are posted to these queues to.
This function will send the RQ_CREATE mailbox command to the HBA to setup the
receive queue pair. This function is asynchronous and will wait for the
mailbox command to finish before continuing.

On success this function will return a zero. If unable to allocate enough
memory this function will return -ENOMEM. If the queue create mailbox command
fails this function will return -ENXIO.

.. _`lpfc_mrq_create`:

lpfc_mrq_create
===============

.. c:function:: int lpfc_mrq_create(struct lpfc_hba *phba, struct lpfc_queue **hrqp, struct lpfc_queue **drqp, struct lpfc_queue **cqp, uint32_t subtype)

    Create MRQ Receive Queues on the HBA

    :param struct lpfc_hba \*phba:
        HBA structure that indicates port to create a queue on.

    :param struct lpfc_queue \*\*hrqp:
        The queue structure array to use to create the header receive queues.

    :param struct lpfc_queue \*\*drqp:
        The queue structure array to use to create the data receive queues.

    :param struct lpfc_queue \*\*cqp:
        The completion queue array to bind these receive queues to.

    :param uint32_t subtype:
        *undescribed*

.. _`lpfc_mrq_create.description`:

Description
-----------

This function creates a receive buffer queue pair , as detailed in \ ``hrq``\  and
\ ``drq``\ , on a port, described by \ ``phba``\  by sending a RQ_CREATE mailbox command
to the HBA.

The \ ``phba``\  struct is used to send mailbox command to HBA. The \ ``drq``\  and \ ``hrq``\ 
struct is used to get the entry count that is necessary to determine the
number of pages to use for this queue. The \ ``cq``\  is used to indicate which
completion queue to bind received buffers that are posted to these queues to.
This function will send the RQ_CREATE mailbox command to the HBA to setup the
receive queue pair. This function is asynchronous and will wait for the
mailbox command to finish before continuing.

On success this function will return a zero. If unable to allocate enough
memory this function will return -ENOMEM. If the queue create mailbox command
fails this function will return -ENXIO.

.. _`lpfc_eq_destroy`:

lpfc_eq_destroy
===============

.. c:function:: int lpfc_eq_destroy(struct lpfc_hba *phba, struct lpfc_queue *eq)

    Destroy an event Queue on the HBA

    :param struct lpfc_hba \*phba:
        *undescribed*

    :param struct lpfc_queue \*eq:
        The queue structure associated with the queue to destroy.

.. _`lpfc_eq_destroy.description`:

Description
-----------

This function destroys a queue, as detailed in \ ``eq``\  by sending an mailbox
command, specific to the type of queue, to the HBA.

The \ ``eq``\  struct is used to get the queue ID of the queue to destroy.

On success this function will return a zero. If the queue destroy mailbox
command fails this function will return -ENXIO.

.. _`lpfc_cq_destroy`:

lpfc_cq_destroy
===============

.. c:function:: int lpfc_cq_destroy(struct lpfc_hba *phba, struct lpfc_queue *cq)

    Destroy a Completion Queue on the HBA

    :param struct lpfc_hba \*phba:
        *undescribed*

    :param struct lpfc_queue \*cq:
        The queue structure associated with the queue to destroy.

.. _`lpfc_cq_destroy.description`:

Description
-----------

This function destroys a queue, as detailed in \ ``cq``\  by sending an mailbox
command, specific to the type of queue, to the HBA.

The \ ``cq``\  struct is used to get the queue ID of the queue to destroy.

On success this function will return a zero. If the queue destroy mailbox
command fails this function will return -ENXIO.

.. _`lpfc_mq_destroy`:

lpfc_mq_destroy
===============

.. c:function:: int lpfc_mq_destroy(struct lpfc_hba *phba, struct lpfc_queue *mq)

    Destroy a Mailbox Queue on the HBA

    :param struct lpfc_hba \*phba:
        *undescribed*

    :param struct lpfc_queue \*mq:
        *undescribed*

.. _`lpfc_mq_destroy.description`:

Description
-----------

This function destroys a queue, as detailed in \ ``mq``\  by sending an mailbox
command, specific to the type of queue, to the HBA.

The \ ``mq``\  struct is used to get the queue ID of the queue to destroy.

On success this function will return a zero. If the queue destroy mailbox
command fails this function will return -ENXIO.

.. _`lpfc_wq_destroy`:

lpfc_wq_destroy
===============

.. c:function:: int lpfc_wq_destroy(struct lpfc_hba *phba, struct lpfc_queue *wq)

    Destroy a Work Queue on the HBA

    :param struct lpfc_hba \*phba:
        *undescribed*

    :param struct lpfc_queue \*wq:
        The queue structure associated with the queue to destroy.

.. _`lpfc_wq_destroy.description`:

Description
-----------

This function destroys a queue, as detailed in \ ``wq``\  by sending an mailbox
command, specific to the type of queue, to the HBA.

The \ ``wq``\  struct is used to get the queue ID of the queue to destroy.

On success this function will return a zero. If the queue destroy mailbox
command fails this function will return -ENXIO.

.. _`lpfc_rq_destroy`:

lpfc_rq_destroy
===============

.. c:function:: int lpfc_rq_destroy(struct lpfc_hba *phba, struct lpfc_queue *hrq, struct lpfc_queue *drq)

    Destroy a Receive Queue on the HBA

    :param struct lpfc_hba \*phba:
        *undescribed*

    :param struct lpfc_queue \*hrq:
        *undescribed*

    :param struct lpfc_queue \*drq:
        *undescribed*

.. _`lpfc_rq_destroy.description`:

Description
-----------

This function destroys a queue, as detailed in \ ``rq``\  by sending an mailbox
command, specific to the type of queue, to the HBA.

The \ ``rq``\  struct is used to get the queue ID of the queue to destroy.

On success this function will return a zero. If the queue destroy mailbox
command fails this function will return -ENXIO.

.. _`lpfc_sli4_post_sgl`:

lpfc_sli4_post_sgl
==================

.. c:function:: int lpfc_sli4_post_sgl(struct lpfc_hba *phba, dma_addr_t pdma_phys_addr0, dma_addr_t pdma_phys_addr1, uint16_t xritag)

    Post scatter gather list for an XRI to HBA

    :param struct lpfc_hba \*phba:
        The virtual port for which this call being executed.

    :param dma_addr_t pdma_phys_addr0:
        Physical address of the 1st SGL page.

    :param dma_addr_t pdma_phys_addr1:
        Physical address of the 2nd SGL page.

    :param uint16_t xritag:
        the xritag that ties this io to the SGL pages.

.. _`lpfc_sli4_post_sgl.description`:

Description
-----------

This routine will post the sgl pages for the IO that has the xritag
that is in the iocbq structure. The xritag is assigned during iocbq
creation and persists for as long as the driver is loaded.
if the caller has fewer than 256 scatter gather segments to map then
pdma_phys_addr1 should be 0.
If the caller needs to map more than 256 scatter gather segment then
pdma_phys_addr1 should be a valid physical address.
physical address for SGLs must be 64 byte aligned.
If you are going to map 2 SGL's then the first one must have 256 entries
the second sgl can have between 1 and 256 entries.

.. _`lpfc_sli4_post_sgl.return-codes`:

Return codes
------------

0 - Success
-ENXIO, -ENOMEM - Failure

.. _`lpfc_sli4_alloc_xri`:

lpfc_sli4_alloc_xri
===================

.. c:function:: uint16_t lpfc_sli4_alloc_xri(struct lpfc_hba *phba)

    Get an available rpi in the device's range

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_sli4_alloc_xri.description`:

Description
-----------

This routine is invoked to post rpi header templates to the
HBA consistent with the SLI-4 interface spec.  This routine
posts a SLI4_PAGE_SIZE memory region to the port to hold up to
SLI4_PAGE_SIZE modulo 64 rpi context headers.

Returns
A nonzero rpi defined as rpi_base <= rpi < max_rpi if successful
LPFC_RPI_ALLOC_ERROR if no rpis are available.

.. _`__lpfc_sli4_free_xri`:

\__lpfc_sli4_free_xri
=====================

.. c:function:: void __lpfc_sli4_free_xri(struct lpfc_hba *phba, int xri)

    Release an xri for reuse.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param int xri:
        *undescribed*

.. _`__lpfc_sli4_free_xri.description`:

Description
-----------

This routine is invoked to release an xri to the pool of
available rpis maintained by the driver.

.. _`lpfc_sli4_free_xri`:

lpfc_sli4_free_xri
==================

.. c:function:: void lpfc_sli4_free_xri(struct lpfc_hba *phba, int xri)

    Release an xri for reuse.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param int xri:
        *undescribed*

.. _`lpfc_sli4_free_xri.description`:

Description
-----------

This routine is invoked to release an xri to the pool of
available rpis maintained by the driver.

.. _`lpfc_sli4_next_xritag`:

lpfc_sli4_next_xritag
=====================

.. c:function:: uint16_t lpfc_sli4_next_xritag(struct lpfc_hba *phba)

    Get an xritag for the io

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_sli4_next_xritag.description`:

Description
-----------

This function gets an xritag for the iocb. If there is no unused xritag
it will return 0xffff.
The function returns the allocated xritag if successful, else returns zero.
Zero is not a valid xritag.
The caller is not required to hold any lock.

.. _`lpfc_sli4_post_sgl_list`:

lpfc_sli4_post_sgl_list
=======================

.. c:function:: int lpfc_sli4_post_sgl_list(struct lpfc_hba *phba, struct list_head *post_sgl_list, int post_cnt)

    post a block of ELS sgls to the port.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct list_head \*post_sgl_list:
        pointer to els sgl entry list.

    :param int post_cnt:
        *undescribed*

.. _`lpfc_sli4_post_sgl_list.description`:

Description
-----------

This routine is invoked to post a block of driver's sgl pages to the
HBA using non-embedded mailbox command. No Lock is held. This routine
is only called when the driver is loading and after all IO has been
stopped.

.. _`lpfc_sli4_post_scsi_sgl_block`:

lpfc_sli4_post_scsi_sgl_block
=============================

.. c:function:: int lpfc_sli4_post_scsi_sgl_block(struct lpfc_hba *phba, struct list_head *sblist, int count)

    post a block of scsi sgl list to firmware

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct list_head \*sblist:
        pointer to scsi buffer list.

    :param int count:
        number of scsi buffers on the list.

.. _`lpfc_sli4_post_scsi_sgl_block.description`:

Description
-----------

This routine is invoked to post a block of \ ``count``\  scsi sgl pages from a
SCSI buffer list \ ``sblist``\  to the HBA using non-embedded mailbox command.
No Lock is held.

.. _`lpfc_fc_frame_check`:

lpfc_fc_frame_check
===================

.. c:function:: int lpfc_fc_frame_check(struct lpfc_hba *phba, struct fc_frame_header *fc_hdr)

    Check that this frame is a valid frame to handle

    :param struct lpfc_hba \*phba:
        pointer to lpfc_hba struct that the frame was received on

    :param struct fc_frame_header \*fc_hdr:
        A pointer to the FC Header data (In Big Endian Format)

.. _`lpfc_fc_frame_check.description`:

Description
-----------

This function checks the fields in the \ ``fc_hdr``\  to see if the FC frame is a
valid type of frame that the LPFC driver will handle. This function will
return a zero if the frame is a valid frame or a non zero value when the
frame does not pass the check.

.. _`lpfc_fc_hdr_get_vfi`:

lpfc_fc_hdr_get_vfi
===================

.. c:function:: uint32_t lpfc_fc_hdr_get_vfi(struct fc_frame_header *fc_hdr)

    Get the VFI from an FC frame

    :param struct fc_frame_header \*fc_hdr:
        A pointer to the FC Header data (In Big Endian Format)

.. _`lpfc_fc_hdr_get_vfi.description`:

Description
-----------

This function processes the FC header to retrieve the VFI from the VF
header, if one exists. This function will return the VFI if one exists
or 0 if no VSAN Header exists.

.. _`lpfc_fc_frame_to_vport`:

lpfc_fc_frame_to_vport
======================

.. c:function:: struct lpfc_vport *lpfc_fc_frame_to_vport(struct lpfc_hba *phba, struct fc_frame_header *fc_hdr, uint16_t fcfi, uint32_t did)

    Finds the vport that a frame is destined to

    :param struct lpfc_hba \*phba:
        Pointer to the HBA structure to search for the vport on

    :param struct fc_frame_header \*fc_hdr:
        A pointer to the FC Header data (In Big Endian Format)

    :param uint16_t fcfi:
        The FC Fabric ID that the frame came from

    :param uint32_t did:
        *undescribed*

.. _`lpfc_fc_frame_to_vport.description`:

Description
-----------

This function searches the \ ``phba``\  for a vport that matches the content of the
\ ``fc_hdr``\  passed in and the \ ``fcfi``\ . This function uses the \ ``fc_hdr``\  to fetch the
VFI, if the Virtual Fabric Tagging Header exists, and the DID. This function
returns the matching vport pointer or NULL if unable to match frame to a
vport.

.. _`lpfc_update_rcv_time_stamp`:

lpfc_update_rcv_time_stamp
==========================

.. c:function:: void lpfc_update_rcv_time_stamp(struct lpfc_vport *vport)

    Update vport's rcv seq time stamp

    :param struct lpfc_vport \*vport:
        The vport to work on.

.. _`lpfc_update_rcv_time_stamp.description`:

Description
-----------

This function updates the receive sequence time stamp for this vport. The
receive sequence time stamp indicates the time that the last frame of the
the sequence that has been idle for the longest amount of time was received.
the driver uses this time stamp to indicate if any received sequences have
timed out.

.. _`lpfc_cleanup_rcv_buffers`:

lpfc_cleanup_rcv_buffers
========================

.. c:function:: void lpfc_cleanup_rcv_buffers(struct lpfc_vport *vport)

    Cleans up all outstanding receive sequences.

    :param struct lpfc_vport \*vport:
        The vport that the received sequences were sent to.

.. _`lpfc_cleanup_rcv_buffers.description`:

Description
-----------

This function cleans up all outstanding received sequences. This is called
by the driver when a link event or user action invalidates all the received
sequences.

.. _`lpfc_rcv_seq_check_edtov`:

lpfc_rcv_seq_check_edtov
========================

.. c:function:: void lpfc_rcv_seq_check_edtov(struct lpfc_vport *vport)

    Cleans up timed out receive sequences.

    :param struct lpfc_vport \*vport:
        The vport that the received sequences were sent to.

.. _`lpfc_rcv_seq_check_edtov.description`:

Description
-----------

This function determines whether any received sequences have timed out by
first checking the vport's rcv_buffer_time_stamp. If this time_stamp
indicates that there is at least one timed out sequence this routine will
go through the received sequences one at a time from most inactive to most
active to determine which ones need to be cleaned up. Once it has determined
that a sequence needs to be cleaned up it will simply free up the resources
without sending an abort.

.. _`lpfc_fc_frame_add`:

lpfc_fc_frame_add
=================

.. c:function:: struct hbq_dmabuf *lpfc_fc_frame_add(struct lpfc_vport *vport, struct hbq_dmabuf *dmabuf)

    Adds a frame to the vport's list of received sequences

    :param struct lpfc_vport \*vport:
        *undescribed*

    :param struct hbq_dmabuf \*dmabuf:
        pointer to a dmabuf that describes the hdr and data of the FC frame

.. _`lpfc_fc_frame_add.description`:

Description
-----------

This function searches through the existing incomplete sequences that have
been sent to this \ ``vport``\ . If the frame matches one of the incomplete
sequences then the dbuf in the \ ``dmabuf``\  is added to the list of frames that
make up that sequence. If no sequence is found that matches this frame then
the function will add the hbuf in the \ ``dmabuf``\  to the \ ``vport``\ 's rcv_buffer_list
This function returns a pointer to the first dmabuf in the sequence list that
the frame was linked to.

.. _`lpfc_sli4_abort_partial_seq`:

lpfc_sli4_abort_partial_seq
===========================

.. c:function:: bool lpfc_sli4_abort_partial_seq(struct lpfc_vport *vport, struct hbq_dmabuf *dmabuf)

    Abort partially assembled unsol sequence

    :param struct lpfc_vport \*vport:
        pointer to a vitural port

    :param struct hbq_dmabuf \*dmabuf:
        pointer to a dmabuf that describes the FC sequence

.. _`lpfc_sli4_abort_partial_seq.description`:

Description
-----------

This function tries to abort from the partially assembed sequence, described
by the information from basic abbort \ ``dmabuf``\ . It checks to see whether such
partially assembled sequence held by the driver. If so, it shall free up all
the frames from the partially assembled sequence.

Return
true  -- if there is matching partially assembled sequence present and all
the frames freed with the sequence;
false -- if there is no matching partially assembled sequence present so
nothing got aborted in the lower layer driver

.. _`lpfc_sli4_abort_ulp_seq`:

lpfc_sli4_abort_ulp_seq
=======================

.. c:function:: bool lpfc_sli4_abort_ulp_seq(struct lpfc_vport *vport, struct hbq_dmabuf *dmabuf)

    Abort assembled unsol sequence from ulp

    :param struct lpfc_vport \*vport:
        pointer to a vitural port

    :param struct hbq_dmabuf \*dmabuf:
        pointer to a dmabuf that describes the FC sequence

.. _`lpfc_sli4_abort_ulp_seq.description`:

Description
-----------

This function tries to abort from the assembed sequence from upper level
protocol, described by the information from basic abbort \ ``dmabuf``\ . It
checks to see whether such pending context exists at upper level protocol.
If so, it shall clean up the pending context.

Return
true  -- if there is matching pending context of the sequence cleaned
at ulp;
false -- if there is no matching pending context of the sequence present
at ulp.

.. _`lpfc_sli4_seq_abort_rsp_cmpl`:

lpfc_sli4_seq_abort_rsp_cmpl
============================

.. c:function:: void lpfc_sli4_seq_abort_rsp_cmpl(struct lpfc_hba *phba, struct lpfc_iocbq *cmd_iocbq, struct lpfc_iocbq *rsp_iocbq)

    BLS ABORT RSP seq abort iocb complete handler

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*cmd_iocbq:
        pointer to the command iocbq structure.

    :param struct lpfc_iocbq \*rsp_iocbq:
        pointer to the response iocbq structure.

.. _`lpfc_sli4_seq_abort_rsp_cmpl.description`:

Description
-----------

This function handles the sequence abort response iocb command complete
event. It properly releases the memory allocated to the sequence abort
accept iocb.

.. _`lpfc_sli4_xri_inrange`:

lpfc_sli4_xri_inrange
=====================

.. c:function:: uint16_t lpfc_sli4_xri_inrange(struct lpfc_hba *phba, uint16_t xri)

    check xri is in range of xris owned by driver.

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint16_t xri:
        xri id in transaction.

.. _`lpfc_sli4_xri_inrange.description`:

Description
-----------

This function validates the xri maps to the known range of XRIs allocated an
used by the driver.

.. _`lpfc_sli4_seq_abort_rsp`:

lpfc_sli4_seq_abort_rsp
=======================

.. c:function:: void lpfc_sli4_seq_abort_rsp(struct lpfc_vport *vport, struct fc_frame_header *fc_hdr, bool aborted)

    bls rsp to sequence abort

    :param struct lpfc_vport \*vport:
        *undescribed*

    :param struct fc_frame_header \*fc_hdr:
        pointer to a FC frame header.

    :param bool aborted:
        *undescribed*

.. _`lpfc_sli4_seq_abort_rsp.description`:

Description
-----------

This function sends a basic response to a previous unsol sequence abort
event after aborting the sequence handling.

.. _`lpfc_sli4_handle_unsol_abort`:

lpfc_sli4_handle_unsol_abort
============================

.. c:function:: void lpfc_sli4_handle_unsol_abort(struct lpfc_vport *vport, struct hbq_dmabuf *dmabuf)

    Handle sli-4 unsolicited abort event

    :param struct lpfc_vport \*vport:
        Pointer to the vport on which this sequence was received

    :param struct hbq_dmabuf \*dmabuf:
        pointer to a dmabuf that describes the FC sequence

.. _`lpfc_sli4_handle_unsol_abort.description`:

Description
-----------

This function handles an SLI-4 unsolicited abort event. If the unsolicited
receive sequence is only partially assembed by the driver, it shall abort
the partially assembled frames for the sequence. Otherwise, if the
unsolicited receive sequence has been completely assembled and passed to
the Upper Layer Protocol (UPL), it then mark the per oxid status for the
unsolicited sequence has been aborted. After that, it will issue a basic
accept to accept the abort.

.. _`lpfc_seq_complete`:

lpfc_seq_complete
=================

.. c:function:: int lpfc_seq_complete(struct hbq_dmabuf *dmabuf)

    Indicates if a sequence is complete

    :param struct hbq_dmabuf \*dmabuf:
        pointer to a dmabuf that describes the FC sequence

.. _`lpfc_seq_complete.description`:

Description
-----------

This function checks the sequence, starting with the frame described by
\ ``dmabuf``\ , to see if all the frames associated with this sequence are present.
the frames associated with this sequence are linked to the \ ``dmabuf``\  using the
dbuf list. This function looks for two major things. 1) That the first frame
has a sequence count of zero. 2) There is a frame with last frame of sequence
set. 3) That there are no holes in the sequence count. The function will
return 1 when the sequence is complete, otherwise it will return 0.

.. _`lpfc_prep_seq`:

lpfc_prep_seq
=============

.. c:function:: struct lpfc_iocbq *lpfc_prep_seq(struct lpfc_vport *vport, struct hbq_dmabuf *seq_dmabuf)

    Prep sequence for ULP processing

    :param struct lpfc_vport \*vport:
        Pointer to the vport on which this sequence was received

    :param struct hbq_dmabuf \*seq_dmabuf:
        *undescribed*

.. _`lpfc_prep_seq.description`:

Description
-----------

This function takes a sequence, described by a list of frames, and creates
a list of iocbq structures to describe the sequence. This iocbq list will be
used to issue to the generic unsolicited sequence handler. This routine
returns a pointer to the first iocbq in the list. If the function is unable
to allocate an iocbq then it throw out the received frames that were not
able to be described and return a pointer to the first iocbq. If unable to
allocate any iocbqs (including the first) this function will return NULL.

.. _`lpfc_sli4_handle_received_buffer`:

lpfc_sli4_handle_received_buffer
================================

.. c:function:: void lpfc_sli4_handle_received_buffer(struct lpfc_hba *phba, struct hbq_dmabuf *dmabuf)

    Handle received buffers from firmware

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct hbq_dmabuf \*dmabuf:
        *undescribed*

.. _`lpfc_sli4_handle_received_buffer.description`:

Description
-----------

This function is called with no lock held. This function processes all
the received buffers and gives it to upper layers when a received buffer
indicates that it is the final frame in the sequence. The interrupt
service routine processes received buffers at interrupt contexts.
Worker thread calls lpfc_sli4_handle_received_buffer, which will call the
appropriate receive function when the final frame in a sequence is received.

.. _`lpfc_sli4_post_all_rpi_hdrs`:

lpfc_sli4_post_all_rpi_hdrs
===========================

.. c:function:: int lpfc_sli4_post_all_rpi_hdrs(struct lpfc_hba *phba)

    Post the rpi header memory region to the port

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_sli4_post_all_rpi_hdrs.description`:

Description
-----------

This routine is invoked to post rpi header templates to the
HBA consistent with the SLI-4 interface spec.  This routine
posts a SLI4_PAGE_SIZE memory region to the port to hold up to
SLI4_PAGE_SIZE modulo 64 rpi context headers.

This routine does not require any locks.  It's usage is expected
to be driver load or reset recovery when the driver is
sequential.

Return codes
0 - successful
-EIO - The mailbox failed to complete successfully.
When this error occurs, the driver is not guaranteed
to have any rpi regions posted to the device and
must either attempt to repost the regions or take a
fatal error.

.. _`lpfc_sli4_post_rpi_hdr`:

lpfc_sli4_post_rpi_hdr
======================

.. c:function:: int lpfc_sli4_post_rpi_hdr(struct lpfc_hba *phba, struct lpfc_rpi_hdr *rpi_page)

    Post an rpi header memory region to the port

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_rpi_hdr \*rpi_page:
        pointer to the rpi memory region.

.. _`lpfc_sli4_post_rpi_hdr.description`:

Description
-----------

This routine is invoked to post a single rpi header to the
HBA consistent with the SLI-4 interface spec.  This memory region
maps up to 64 rpi context regions.

Return codes
0 - successful
-ENOMEM - No available memory
-EIO - The mailbox failed to complete successfully.

.. _`lpfc_sli4_alloc_rpi`:

lpfc_sli4_alloc_rpi
===================

.. c:function:: int lpfc_sli4_alloc_rpi(struct lpfc_hba *phba)

    Get an available rpi in the device's range

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_sli4_alloc_rpi.description`:

Description
-----------

This routine is invoked to post rpi header templates to the
HBA consistent with the SLI-4 interface spec.  This routine
posts a SLI4_PAGE_SIZE memory region to the port to hold up to
SLI4_PAGE_SIZE modulo 64 rpi context headers.

Returns
A nonzero rpi defined as rpi_base <= rpi < max_rpi if successful
LPFC_RPI_ALLOC_ERROR if no rpis are available.

.. _`__lpfc_sli4_free_rpi`:

\__lpfc_sli4_free_rpi
=====================

.. c:function:: void __lpfc_sli4_free_rpi(struct lpfc_hba *phba, int rpi)

    Release an rpi for reuse.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param int rpi:
        *undescribed*

.. _`__lpfc_sli4_free_rpi.description`:

Description
-----------

This routine is invoked to release an rpi to the pool of
available rpis maintained by the driver.

.. _`lpfc_sli4_free_rpi`:

lpfc_sli4_free_rpi
==================

.. c:function:: void lpfc_sli4_free_rpi(struct lpfc_hba *phba, int rpi)

    Release an rpi for reuse.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param int rpi:
        *undescribed*

.. _`lpfc_sli4_free_rpi.description`:

Description
-----------

This routine is invoked to release an rpi to the pool of
available rpis maintained by the driver.

.. _`lpfc_sli4_remove_rpis`:

lpfc_sli4_remove_rpis
=====================

.. c:function:: void lpfc_sli4_remove_rpis(struct lpfc_hba *phba)

    Remove the rpi bitmask region

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_sli4_remove_rpis.description`:

Description
-----------

This routine is invoked to remove the memory region that
provided rpi via a bitmask.

.. _`lpfc_sli4_resume_rpi`:

lpfc_sli4_resume_rpi
====================

.. c:function:: int lpfc_sli4_resume_rpi(struct lpfc_nodelist *ndlp, void (*cmpl)(struct lpfc_hba *, LPFC_MBOXQ_t *), void *arg)

    Remove the rpi bitmask region

    :param struct lpfc_nodelist \*ndlp:
        *undescribed*

    :param void (\*cmpl)(struct lpfc_hba \*, LPFC_MBOXQ_t \*):
        *undescribed*

    :param void \*arg:
        *undescribed*

.. _`lpfc_sli4_resume_rpi.description`:

Description
-----------

This routine is invoked to remove the memory region that
provided rpi via a bitmask.

.. _`lpfc_sli4_init_vpi`:

lpfc_sli4_init_vpi
==================

.. c:function:: int lpfc_sli4_init_vpi(struct lpfc_vport *vport)

    Initialize a vpi with the port

    :param struct lpfc_vport \*vport:
        Pointer to the vport for which the vpi is being initialized

.. _`lpfc_sli4_init_vpi.description`:

Description
-----------

This routine is invoked to activate a vpi with the port.

.. _`lpfc_sli4_init_vpi.return`:

Return
------

0 success
-Evalue otherwise

.. _`lpfc_mbx_cmpl_add_fcf_record`:

lpfc_mbx_cmpl_add_fcf_record
============================

.. c:function:: void lpfc_mbx_cmpl_add_fcf_record(struct lpfc_hba *phba, LPFC_MBOXQ_t *mboxq)

    add fcf mbox completion handler.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*mboxq:
        Pointer to mailbox object.

.. _`lpfc_mbx_cmpl_add_fcf_record.description`:

Description
-----------

This routine is invoked to manually add a single FCF record. The caller
must pass a completely initialized FCF_Record.  This routine takes
care of the nonembedded mailbox operations.

.. _`lpfc_sli4_add_fcf_record`:

lpfc_sli4_add_fcf_record
========================

.. c:function:: int lpfc_sli4_add_fcf_record(struct lpfc_hba *phba, struct fcf_record *fcf_record)

    Manually add an FCF Record.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct fcf_record \*fcf_record:
        pointer to the initialized fcf record to add.

.. _`lpfc_sli4_add_fcf_record.description`:

Description
-----------

This routine is invoked to manually add a single FCF record. The caller
must pass a completely initialized FCF_Record.  This routine takes
care of the nonembedded mailbox operations.

.. _`lpfc_sli4_build_dflt_fcf_record`:

lpfc_sli4_build_dflt_fcf_record
===============================

.. c:function:: void lpfc_sli4_build_dflt_fcf_record(struct lpfc_hba *phba, struct fcf_record *fcf_record, uint16_t fcf_index)

    Build the driver's default FCF Record.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct fcf_record \*fcf_record:
        pointer to the fcf record to write the default data.

    :param uint16_t fcf_index:
        FCF table entry index.

.. _`lpfc_sli4_build_dflt_fcf_record.description`:

Description
-----------

This routine is invoked to build the driver's default FCF record.  The
values used are hardcoded.  This routine handles memory initialization.

.. _`lpfc_sli4_fcf_scan_read_fcf_rec`:

lpfc_sli4_fcf_scan_read_fcf_rec
===============================

.. c:function:: int lpfc_sli4_fcf_scan_read_fcf_rec(struct lpfc_hba *phba, uint16_t fcf_index)

    Read hba fcf record for fcf scan.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param uint16_t fcf_index:
        FCF table entry offset.

.. _`lpfc_sli4_fcf_scan_read_fcf_rec.description`:

Description
-----------

This routine is invoked to scan the entire FCF table by reading FCF
record and processing it one at a time starting from the \ ``fcf_index``\ 
for initial FCF discovery or fast FCF failover rediscovery.

Return 0 if the mailbox command is submitted successfully, none 0
otherwise.

.. _`lpfc_sli4_fcf_rr_read_fcf_rec`:

lpfc_sli4_fcf_rr_read_fcf_rec
=============================

.. c:function:: int lpfc_sli4_fcf_rr_read_fcf_rec(struct lpfc_hba *phba, uint16_t fcf_index)

    Read hba fcf record for roundrobin fcf.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param uint16_t fcf_index:
        FCF table entry offset.

.. _`lpfc_sli4_fcf_rr_read_fcf_rec.description`:

Description
-----------

This routine is invoked to read an FCF record indicated by \ ``fcf_index``\ 
and to use it for FLOGI roundrobin FCF failover.

Return 0 if the mailbox command is submitted successfully, none 0
otherwise.

.. _`lpfc_sli4_read_fcf_rec`:

lpfc_sli4_read_fcf_rec
======================

.. c:function:: int lpfc_sli4_read_fcf_rec(struct lpfc_hba *phba, uint16_t fcf_index)

    Read hba fcf record for update eligible fcf bmask.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param uint16_t fcf_index:
        FCF table entry offset.

.. _`lpfc_sli4_read_fcf_rec.description`:

Description
-----------

This routine is invoked to read an FCF record indicated by \ ``fcf_index``\  to
determine whether it's eligible for FLOGI roundrobin failover list.

Return 0 if the mailbox command is submitted successfully, none 0
otherwise.

.. _`lpfc_check_next_fcf_pri_level`:

lpfc_check_next_fcf_pri_level
=============================

.. c:function:: int lpfc_check_next_fcf_pri_level(struct lpfc_hba *phba)

    phba pointer to the lpfc_hba struct for this port. This routine is called from the lpfc_sli4_fcf_rr_next_index_get routine when the rr_bmask is empty. The FCF indecies are put into the rr_bmask based on their priority level. Starting from the highest priority to the lowest. The most likely FCF candidate will be in the highest priority group. When this routine is called it searches the fcf_pri list for next lowest priority group and repopulates the rr_bmask with only those fcf_indexes.

    :param struct lpfc_hba \*phba:
        *undescribed*

.. _`lpfc_check_next_fcf_pri_level.return`:

Return
------

1=success 0=failure

.. _`lpfc_sli4_fcf_rr_next_index_get`:

lpfc_sli4_fcf_rr_next_index_get
===============================

.. c:function:: uint16_t lpfc_sli4_fcf_rr_next_index_get(struct lpfc_hba *phba)

    Get next eligible fcf record index

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_sli4_fcf_rr_next_index_get.description`:

Description
-----------

This routine is to get the next eligible FCF record index in a round
robin fashion. If the next eligible FCF record index equals to the
initial roundrobin FCF record index, LPFC_FCOE_FCF_NEXT_NONE (0xFFFF)
shall be returned, otherwise, the next eligible FCF record's index
shall be returned.

.. _`lpfc_sli4_fcf_rr_index_set`:

lpfc_sli4_fcf_rr_index_set
==========================

.. c:function:: int lpfc_sli4_fcf_rr_index_set(struct lpfc_hba *phba, uint16_t fcf_index)

    Set bmask with eligible fcf record index

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param uint16_t fcf_index:
        *undescribed*

.. _`lpfc_sli4_fcf_rr_index_set.description`:

Description
-----------

This routine sets the FCF record index in to the eligible bmask for
roundrobin failover search. It checks to make sure that the index
does not go beyond the range of the driver allocated bmask dimension
before setting the bit.

Returns 0 if the index bit successfully set, otherwise, it returns
-EINVAL.

.. _`lpfc_sli4_fcf_rr_index_clear`:

lpfc_sli4_fcf_rr_index_clear
============================

.. c:function:: void lpfc_sli4_fcf_rr_index_clear(struct lpfc_hba *phba, uint16_t fcf_index)

    Clear bmask from eligible fcf record index

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param uint16_t fcf_index:
        *undescribed*

.. _`lpfc_sli4_fcf_rr_index_clear.description`:

Description
-----------

This routine clears the FCF record index from the eligible bmask for
roundrobin failover search. It checks to make sure that the index
does not go beyond the range of the driver allocated bmask dimension
before clearing the bit.

.. _`lpfc_mbx_cmpl_redisc_fcf_table`:

lpfc_mbx_cmpl_redisc_fcf_table
==============================

.. c:function:: void lpfc_mbx_cmpl_redisc_fcf_table(struct lpfc_hba *phba, LPFC_MBOXQ_t *mbox)

    completion routine for rediscover FCF table

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*mbox:
        *undescribed*

.. _`lpfc_mbx_cmpl_redisc_fcf_table.description`:

Description
-----------

This routine is the completion routine for the rediscover FCF table mailbox
command. If the mailbox command returned failure, it will try to stop the
FCF rediscover wait timer.

.. _`lpfc_sli4_redisc_fcf_table`:

lpfc_sli4_redisc_fcf_table
==========================

.. c:function:: int lpfc_sli4_redisc_fcf_table(struct lpfc_hba *phba)

    Request to rediscover entire FCF table by port.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_sli4_redisc_fcf_table.description`:

Description
-----------

This routine is invoked to request for rediscovery of the entire FCF table
by the port.

.. _`lpfc_sli4_fcf_dead_failthrough`:

lpfc_sli4_fcf_dead_failthrough
==============================

.. c:function:: void lpfc_sli4_fcf_dead_failthrough(struct lpfc_hba *phba)

    Failthrough routine to fcf dead event

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_sli4_fcf_dead_failthrough.description`:

Description
-----------

This function is the failover routine as a last resort to the FCF DEAD
event when driver failed to perform fast FCF failover.

.. _`lpfc_sli_get_config_region23`:

lpfc_sli_get_config_region23
============================

.. c:function:: uint32_t lpfc_sli_get_config_region23(struct lpfc_hba *phba, char *rgn23_data)

    Get sli3 port region 23 data.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param char \*rgn23_data:
        pointer to configure region 23 data.

.. _`lpfc_sli_get_config_region23.description`:

Description
-----------

This function gets SLI3 port configure region 23 data through memory dump
mailbox command. When it successfully retrieves data, the size of the data
will be returned, otherwise, 0 will be returned.

.. _`lpfc_sli4_get_config_region23`:

lpfc_sli4_get_config_region23
=============================

.. c:function:: uint32_t lpfc_sli4_get_config_region23(struct lpfc_hba *phba, char *rgn23_data)

    Get sli4 port region 23 data.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param char \*rgn23_data:
        pointer to configure region 23 data.

.. _`lpfc_sli4_get_config_region23.description`:

Description
-----------

This function gets SLI4 port configure region 23 data through memory dump
mailbox command. When it successfully retrieves data, the size of the data
will be returned, otherwise, 0 will be returned.

.. _`lpfc_sli_read_link_ste`:

lpfc_sli_read_link_ste
======================

.. c:function:: void lpfc_sli_read_link_ste(struct lpfc_hba *phba)

    Read region 23 to decide if link is disabled.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_sli_read_link_ste.description`:

Description
-----------

This function read region 23 and parse TLV for port status to
decide if the user disaled the port. If the TLV indicates the
port is disabled, the hba_flag is set accordingly.

.. _`lpfc_wr_object`:

lpfc_wr_object
==============

.. c:function:: int lpfc_wr_object(struct lpfc_hba *phba, struct list_head *dmabuf_list, uint32_t size, uint32_t *offset)

    write an object to the firmware

    :param struct lpfc_hba \*phba:
        HBA structure that indicates port to create a queue on.

    :param struct list_head \*dmabuf_list:
        list of dmabufs to write to the port.

    :param uint32_t size:
        the total byte value of the objects to write to the port.

    :param uint32_t \*offset:
        the current offset to be used to start the transfer.

.. _`lpfc_wr_object.description`:

Description
-----------

This routine will create a wr_object mailbox command to send to the port.
the mailbox command will be constructed using the dma buffers described in
\ ``dmabuf_list``\  to create a list of BDEs. This routine will fill in as many
BDEs that the imbedded mailbox can support. The \ ``offset``\  variable will be
used to indicate the starting offset of the transfer and will also return
the offset after the write object mailbox has completed. \ ``size``\  is used to
determine the end of the object and whether the eof bit should be set.

Return 0 is successful and offset will contain the the new offset to use
for the next write.
Return negative value for error cases.

.. _`lpfc_cleanup_pending_mbox`:

lpfc_cleanup_pending_mbox
=========================

.. c:function:: void lpfc_cleanup_pending_mbox(struct lpfc_vport *vport)

    Free up vport discovery mailbox commands.

    :param struct lpfc_vport \*vport:
        pointer to vport data structure.

.. _`lpfc_cleanup_pending_mbox.description`:

Description
-----------

This function iterate through the mailboxq and clean up all REG_LOGIN
and REG_VPI mailbox commands associated with the vport. This function
is called when driver want to restart discovery of the vport due to
a Clear Virtual Link event.

.. _`lpfc_drain_txq`:

lpfc_drain_txq
==============

.. c:function:: uint32_t lpfc_drain_txq(struct lpfc_hba *phba)

    Drain the txq

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_drain_txq.description`:

Description
-----------

This function attempt to submit IOCBs on the txq
to the adapter.  For SLI4 adapters, the txq contains
ELS IOCBs that have been deferred because the there
are no SGLs.  This congestion can occur with large
vport counts during node discovery.

.. _`lpfc_wqe_bpl2sgl`:

lpfc_wqe_bpl2sgl
================

.. c:function:: uint16_t lpfc_wqe_bpl2sgl(struct lpfc_hba *phba, struct lpfc_iocbq *pwqeq, struct lpfc_sglq *sglq)

    Convert the bpl/bde to a sgl.

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*pwqeq:
        *undescribed*

    :param struct lpfc_sglq \*sglq:
        Pointer to the scatter gather queue object.

.. _`lpfc_wqe_bpl2sgl.description`:

Description
-----------

This routine converts the bpl or bde that is in the WQE
to a sgl list for the sli4 hardware. The physical address
of the bpl/bde is converted back to a virtual address.
If the WQE contains a BPL then the list of BDE's is
converted to sli4_sge's. If the WQE contains a single
BDE then it is converted to a single sli_sge.
The WQE is still in cpu endianness so the contents of
the bpl can be used without byte swapping.

Returns valid XRI = Success, NO_XRI = Failure.

.. _`lpfc_sli4_issue_wqe`:

lpfc_sli4_issue_wqe
===================

.. c:function:: int lpfc_sli4_issue_wqe(struct lpfc_hba *phba, uint32_t ring_number, struct lpfc_iocbq *pwqe)

    Issue an SLI4 Work Queue Entry (WQE)

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param uint32_t ring_number:
        Base sli ring number

    :param struct lpfc_iocbq \*pwqe:
        Pointer to command WQE.

.. This file was automatic generated / don't edit.

