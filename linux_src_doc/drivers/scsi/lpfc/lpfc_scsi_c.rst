.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/lpfc/lpfc_scsi.c

.. _`lpfc_sli4_set_rsp_sgl_last`:

lpfc_sli4_set_rsp_sgl_last
==========================

.. c:function:: void lpfc_sli4_set_rsp_sgl_last(struct lpfc_hba *phba, struct lpfc_scsi_buf *lpfc_cmd)

    Set the last bit in the response sge.

    :param phba:
        Pointer to HBA object.
    :type phba: struct lpfc_hba \*

    :param lpfc_cmd:
        lpfc scsi command object pointer.
    :type lpfc_cmd: struct lpfc_scsi_buf \*

.. _`lpfc_sli4_set_rsp_sgl_last.description`:

Description
-----------

This function is called from the lpfc_prep_task_mgmt_cmd function to
set the last bit in the response sge entry.

.. _`lpfc_update_stats`:

lpfc_update_stats
=================

.. c:function:: void lpfc_update_stats(struct lpfc_hba *phba, struct lpfc_scsi_buf *lpfc_cmd)

    Update statistical data for the command completion

    :param phba:
        Pointer to HBA object.
    :type phba: struct lpfc_hba \*

    :param lpfc_cmd:
        lpfc scsi command object pointer.
    :type lpfc_cmd: struct lpfc_scsi_buf \*

.. _`lpfc_update_stats.description`:

Description
-----------

This function is called when there is a command completion and this
function updates the statistical data for the command completion.

.. _`lpfc_rampdown_queue_depth`:

lpfc_rampdown_queue_depth
=========================

.. c:function:: void lpfc_rampdown_queue_depth(struct lpfc_hba *phba)

    Post RAMP_DOWN_QUEUE event to worker thread

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

.. _`lpfc_rampdown_queue_depth.description`:

Description
-----------

This routine is called when there is resource error in driver or firmware.
This routine posts WORKER_RAMP_DOWN_QUEUE event for \ ``phba``\ . This routine
posts at most 1 event each second. This routine wakes up worker thread of
\ ``phba``\  to process WORKER_RAM_DOWN_EVENT event.

This routine should be called with no lock held.

.. _`lpfc_ramp_down_queue_handler`:

lpfc_ramp_down_queue_handler
============================

.. c:function:: void lpfc_ramp_down_queue_handler(struct lpfc_hba *phba)

    WORKER_RAMP_DOWN_QUEUE event handler

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

.. _`lpfc_ramp_down_queue_handler.description`:

Description
-----------

This routine is called to  process WORKER_RAMP_DOWN_QUEUE event for worker
thread.This routine reduces queue depth for all scsi device on each vport
associated with \ ``phba``\ .

.. _`lpfc_scsi_dev_block`:

lpfc_scsi_dev_block
===================

.. c:function:: void lpfc_scsi_dev_block(struct lpfc_hba *phba)

    set all scsi hosts to block state

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

.. _`lpfc_scsi_dev_block.description`:

Description
-----------

This function walks vport list and set each SCSI host to block state
by invoking \ :c:func:`fc_remote_port_delete`\  routine. This function is invoked
with EEH when device's PCI slot has been permanently disabled.

.. _`lpfc_new_scsi_buf_s3`:

lpfc_new_scsi_buf_s3
====================

.. c:function:: int lpfc_new_scsi_buf_s3(struct lpfc_vport *vport, int num_to_alloc)

    Scsi buffer allocator for HBA with SLI3 IF spec

    :param vport:
        The virtual port for which this call being executed.
    :type vport: struct lpfc_vport \*

    :param num_to_alloc:
        *undescribed*
    :type num_to_alloc: int

.. _`lpfc_new_scsi_buf_s3.description`:

Description
-----------

This routine allocates a scsi buffer for device with SLI-3 interface spec,
the scsi buffer contains all the necessary information needed to initiate
a SCSI I/O. The non-DMAable buffer region contains information to build
the IOCB. The DMAable region contains memory for the FCP CMND, FCP RSP,
and the initial BPL. In addition to allocating memory, the FCP CMND and
FCP RSP BDEs are setup in the BPL and the BPL BDE is setup in the IOCB.

.. _`lpfc_new_scsi_buf_s3.return-codes`:

Return codes
------------

int - number of scsi buffers that were allocated.
0 = failure, less than num_to_alloc is a partial failure.

.. _`lpfc_sli4_vport_delete_fcp_xri_aborted`:

lpfc_sli4_vport_delete_fcp_xri_aborted
======================================

.. c:function:: void lpfc_sli4_vport_delete_fcp_xri_aborted(struct lpfc_vport *vport)

    Remove all ndlp references for vport

    :param vport:
        pointer to lpfc vport data structure.
    :type vport: struct lpfc_vport \*

.. _`lpfc_sli4_vport_delete_fcp_xri_aborted.description`:

Description
-----------

This routine is invoked by the vport cleanup for deletions and the cleanup
for an ndlp on removal.

.. _`lpfc_sli4_fcp_xri_aborted`:

lpfc_sli4_fcp_xri_aborted
=========================

.. c:function:: void lpfc_sli4_fcp_xri_aborted(struct lpfc_hba *phba, struct sli4_wcqe_xri_aborted *axri)

    Fast-path process of fcp xri abort

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param axri:
        pointer to the fcp xri abort wcqe structure.
    :type axri: struct sli4_wcqe_xri_aborted \*

.. _`lpfc_sli4_fcp_xri_aborted.description`:

Description
-----------

This routine is invoked by the worker thread to process a SLI4 fast-path
FCP aborted xri.

.. _`lpfc_sli4_post_scsi_sgl_list`:

lpfc_sli4_post_scsi_sgl_list
============================

.. c:function:: int lpfc_sli4_post_scsi_sgl_list(struct lpfc_hba *phba, struct list_head *post_sblist, int sb_count)

    Post blocks of scsi buffer sgls from a list

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param post_sblist:
        pointer to the scsi buffer list.
    :type post_sblist: struct list_head \*

    :param sb_count:
        *undescribed*
    :type sb_count: int

.. _`lpfc_sli4_post_scsi_sgl_list.description`:

Description
-----------

This routine walks a list of scsi buffers that was passed in. It attempts
to construct blocks of scsi buffer sgls which contains contiguous xris and
uses the non-embedded SGL block post mailbox commands to post to the port.
For single SCSI buffer sgl with non-contiguous xri, if any, it shall use
embedded SGL post mailbox command for posting. The \ ``post_sblist``\  passed in
must be local list, thus no lock is needed when manipulate the list.

.. _`lpfc_sli4_post_scsi_sgl_list.return`:

Return
------

0 = failure, non-zero number of successfully posted buffers.

.. _`lpfc_sli4_repost_scsi_sgl_list`:

lpfc_sli4_repost_scsi_sgl_list
==============================

.. c:function:: int lpfc_sli4_repost_scsi_sgl_list(struct lpfc_hba *phba)

    Repost all the allocated scsi buffer sgls

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_repost_scsi_sgl_list.description`:

Description
-----------

This routine walks the list of scsi buffers that have been allocated and
repost them to the port by using SGL block post. This is needed after a
pci_function_reset/warm_start or start. The lpfc_hba_down_post_s4 routine
is responsible for moving all scsi buffers on the lpfc_abts_scsi_sgl_list
to the lpfc_scsi_buf_list. If the repost fails, reject all scsi buffers.

.. _`lpfc_sli4_repost_scsi_sgl_list.return`:

Return
------

0 = success, non-zero failure.

.. _`lpfc_new_scsi_buf_s4`:

lpfc_new_scsi_buf_s4
====================

.. c:function:: int lpfc_new_scsi_buf_s4(struct lpfc_vport *vport, int num_to_alloc)

    Scsi buffer allocator for HBA with SLI4 IF spec

    :param vport:
        The virtual port for which this call being executed.
    :type vport: struct lpfc_vport \*

    :param num_to_alloc:
        *undescribed*
    :type num_to_alloc: int

.. _`lpfc_new_scsi_buf_s4.description`:

Description
-----------

This routine allocates scsi buffers for device with SLI-4 interface spec,
the scsi buffer contains all the necessary information needed to initiate
a SCSI I/O. After allocating up to \ ``num_to_allocate``\  SCSI buffers and put
them on a list, it post them to the port by using SGL block post.

.. _`lpfc_new_scsi_buf_s4.return-codes`:

Return codes
------------

int - number of scsi buffers that were allocated and posted.
0 = failure, less than num_to_alloc is a partial failure.

.. _`lpfc_new_scsi_buf`:

lpfc_new_scsi_buf
=================

.. c:function:: int lpfc_new_scsi_buf(struct lpfc_vport *vport, int num_to_alloc)

    Wrapper funciton for scsi buffer allocator

    :param vport:
        The virtual port for which this call being executed.
    :type vport: struct lpfc_vport \*

    :param num_to_alloc:
        *undescribed*
    :type num_to_alloc: int

.. _`lpfc_new_scsi_buf.description`:

Description
-----------

This routine wraps the actual SCSI buffer allocator function pointer from
the lpfc_hba struct.

.. _`lpfc_new_scsi_buf.return-codes`:

Return codes
------------

int - number of scsi buffers that were allocated.
0 = failure, less than num_to_alloc is a partial failure.

.. _`lpfc_get_scsi_buf_s3`:

lpfc_get_scsi_buf_s3
====================

.. c:function:: struct lpfc_scsi_buf* lpfc_get_scsi_buf_s3(struct lpfc_hba *phba, struct lpfc_nodelist *ndlp)

    Get a scsi buffer from lpfc_scsi_buf_list of the HBA

    :param phba:
        The HBA for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param ndlp:
        *undescribed*
    :type ndlp: struct lpfc_nodelist \*

.. _`lpfc_get_scsi_buf_s3.description`:

Description
-----------

This routine removes a scsi buffer from head of \ ``phba``\  lpfc_scsi_buf_list list
and returns to caller.

.. _`lpfc_get_scsi_buf_s3.return-codes`:

Return codes
------------

NULL - Error
Pointer to lpfc_scsi_buf - Success

.. _`lpfc_get_scsi_buf_s4`:

lpfc_get_scsi_buf_s4
====================

.. c:function:: struct lpfc_scsi_buf* lpfc_get_scsi_buf_s4(struct lpfc_hba *phba, struct lpfc_nodelist *ndlp)

    Get a scsi buffer from lpfc_scsi_buf_list of the HBA

    :param phba:
        The HBA for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param ndlp:
        *undescribed*
    :type ndlp: struct lpfc_nodelist \*

.. _`lpfc_get_scsi_buf_s4.description`:

Description
-----------

This routine removes a scsi buffer from head of \ ``phba``\  lpfc_scsi_buf_list list
and returns to caller.

.. _`lpfc_get_scsi_buf_s4.return-codes`:

Return codes
------------

NULL - Error
Pointer to lpfc_scsi_buf - Success

.. _`lpfc_get_scsi_buf`:

lpfc_get_scsi_buf
=================

.. c:function:: struct lpfc_scsi_buf* lpfc_get_scsi_buf(struct lpfc_hba *phba, struct lpfc_nodelist *ndlp)

    Get a scsi buffer from lpfc_scsi_buf_list of the HBA

    :param phba:
        The HBA for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param ndlp:
        *undescribed*
    :type ndlp: struct lpfc_nodelist \*

.. _`lpfc_get_scsi_buf.description`:

Description
-----------

This routine removes a scsi buffer from head of \ ``phba``\  lpfc_scsi_buf_list list
and returns to caller.

.. _`lpfc_get_scsi_buf.return-codes`:

Return codes
------------

NULL - Error
Pointer to lpfc_scsi_buf - Success

.. _`lpfc_release_scsi_buf_s3`:

lpfc_release_scsi_buf_s3
========================

.. c:function:: void lpfc_release_scsi_buf_s3(struct lpfc_hba *phba, struct lpfc_scsi_buf *psb)

    Return a scsi buffer back to hba scsi buf list

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param psb:
        The scsi buffer which is being released.
    :type psb: struct lpfc_scsi_buf \*

.. _`lpfc_release_scsi_buf_s3.description`:

Description
-----------

This routine releases \ ``psb``\  scsi buffer by adding it to tail of \ ``phba``\ 
lpfc_scsi_buf_list list.

.. _`lpfc_release_scsi_buf_s4`:

lpfc_release_scsi_buf_s4
========================

.. c:function:: void lpfc_release_scsi_buf_s4(struct lpfc_hba *phba, struct lpfc_scsi_buf *psb)

    Return a scsi buffer back to hba scsi buf list.

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param psb:
        The scsi buffer which is being released.
    :type psb: struct lpfc_scsi_buf \*

.. _`lpfc_release_scsi_buf_s4.description`:

Description
-----------

This routine releases \ ``psb``\  scsi buffer by adding it to tail of \ ``phba``\ 
lpfc_scsi_buf_list list. For SLI4 XRI's are tied to the scsi buffer
and cannot be reused for at least RA_TOV amount of time if it was
aborted.

.. _`lpfc_release_scsi_buf`:

lpfc_release_scsi_buf
=====================

.. c:function:: void lpfc_release_scsi_buf(struct lpfc_hba *phba, struct lpfc_scsi_buf *psb)

    Return a scsi buffer back to hba scsi buf list.

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param psb:
        The scsi buffer which is being released.
    :type psb: struct lpfc_scsi_buf \*

.. _`lpfc_release_scsi_buf.description`:

Description
-----------

This routine releases \ ``psb``\  scsi buffer by adding it to tail of \ ``phba``\ 
lpfc_scsi_buf_list list.

.. _`lpfc_scsi_prep_dma_buf_s3`:

lpfc_scsi_prep_dma_buf_s3
=========================

.. c:function:: int lpfc_scsi_prep_dma_buf_s3(struct lpfc_hba *phba, struct lpfc_scsi_buf *lpfc_cmd)

    DMA mapping for scsi buffer to SLI3 IF spec

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param lpfc_cmd:
        The scsi buffer which is going to be mapped.
    :type lpfc_cmd: struct lpfc_scsi_buf \*

.. _`lpfc_scsi_prep_dma_buf_s3.description`:

Description
-----------

This routine does the pci dma mapping for scatter-gather list of scsi cmnd
field of \ ``lpfc_cmd``\  for device with SLI-3 interface spec. This routine scans
through sg elements and format the bde. This routine also initializes all
IOCB fields which are dependent on scsi command request buffer.

.. _`lpfc_scsi_prep_dma_buf_s3.return-codes`:

Return codes
------------

1 - Error
0 - Success

.. _`bg_err_check`:

BG_ERR_CHECK
============

.. c:function::  BG_ERR_CHECK()

    error injection

.. _`lpfc_bg_err_inject`:

lpfc_bg_err_inject
==================

.. c:function:: int lpfc_bg_err_inject(struct lpfc_hba *phba, struct scsi_cmnd *sc, uint32_t *reftag, uint16_t *apptag, uint32_t new_guard)

    Determine if we should inject an error

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param sc:
        The SCSI command to examine
    :type sc: struct scsi_cmnd \*

    :param reftag:
        (out) BlockGuard reference tag for transmitted data
    :type reftag: uint32_t \*

    :param apptag:
        (out) BlockGuard application tag for transmitted data
        \ ``new_guard``\  (in) Value to replace CRC with if needed
    :type apptag: uint16_t \*

    :param new_guard:
        *undescribed*
    :type new_guard: uint32_t

.. _`lpfc_bg_err_inject.description`:

Description
-----------

Returns BG_ERR\_\* bit mask or 0 if request ignored

.. _`lpfc_sc_to_bg_opcodes`:

lpfc_sc_to_bg_opcodes
=====================

.. c:function:: int lpfc_sc_to_bg_opcodes(struct lpfc_hba *phba, struct scsi_cmnd *sc, uint8_t *txop, uint8_t *rxop)

    Determine the BlockGuard opcodes to be used with the specified SCSI command.

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param sc:
        The SCSI command to examine
    :type sc: struct scsi_cmnd \*

    :param txop:
        *undescribed*
    :type txop: uint8_t \*

    :param rxop:
        *undescribed*
    :type rxop: uint8_t \*

.. _`lpfc_sc_to_bg_opcodes.return`:

Return
------

zero on success; non-zero if tx and/or rx op cannot be determined

.. _`lpfc_bg_err_opcodes`:

lpfc_bg_err_opcodes
===================

.. c:function:: int lpfc_bg_err_opcodes(struct lpfc_hba *phba, struct scsi_cmnd *sc, uint8_t *txop, uint8_t *rxop)

    reDetermine the BlockGuard opcodes to be used with the specified SCSI command in order to force a guard tag error.

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param sc:
        The SCSI command to examine
    :type sc: struct scsi_cmnd \*

    :param txop:
        *undescribed*
    :type txop: uint8_t \*

    :param rxop:
        *undescribed*
    :type rxop: uint8_t \*

.. _`lpfc_bg_err_opcodes.return`:

Return
------

zero on success; non-zero if tx and/or rx op cannot be determined

.. _`lpfc_bg_setup_bpl`:

lpfc_bg_setup_bpl
=================

.. c:function:: int lpfc_bg_setup_bpl(struct lpfc_hba *phba, struct scsi_cmnd *sc, struct ulp_bde64 *bpl, int datasegcnt)

    Setup BlockGuard BPL with no protection data

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param sc:
        pointer to scsi command we're working on
    :type sc: struct scsi_cmnd \*

    :param bpl:
        pointer to buffer list for protection groups
    :type bpl: struct ulp_bde64 \*

    :param datasegcnt:
        *undescribed*
    :type datasegcnt: int

.. _`lpfc_bg_setup_bpl.description`:

Description
-----------

This function sets up BPL buffer list for protection groups of
type LPFC_PG_TYPE_NO_DIF

This is usually used when the HBA is instructed to generate
DIFs and insert them into data stream (or strip DIF from
incoming data stream)

The buffer list consists of just one protection group described

.. _`lpfc_bg_setup_bpl.below`:

below
-----

+-------------------------+
start of prot group  -->     \|          PDE_5          \|
+-------------------------+
\|          PDE_6          \|
+-------------------------+
\|         Data BDE        \|
+-------------------------+
\|more Data BDE's ... (opt)\|
+-------------------------+

.. _`lpfc_bg_setup_bpl.note`:

Note
----

Data s/g buffers have been dma mapped

Returns the number of BDEs added to the BPL.

.. _`lpfc_bg_setup_bpl_prot`:

lpfc_bg_setup_bpl_prot
======================

.. c:function:: int lpfc_bg_setup_bpl_prot(struct lpfc_hba *phba, struct scsi_cmnd *sc, struct ulp_bde64 *bpl, int datacnt, int protcnt)

    Setup BlockGuard BPL with protection data

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param sc:
        pointer to scsi command we're working on
    :type sc: struct scsi_cmnd \*

    :param bpl:
        pointer to buffer list for protection groups
    :type bpl: struct ulp_bde64 \*

    :param datacnt:
        number of segments of data that have been dma mapped
    :type datacnt: int

    :param protcnt:
        number of segment of protection data that have been dma mapped
    :type protcnt: int

.. _`lpfc_bg_setup_bpl_prot.description`:

Description
-----------

This function sets up BPL buffer list for protection groups of
type LPFC_PG_TYPE_DIF

This is usually used when DIFs are in their own buffers,
separate from the data. The HBA can then by instructed
to place the DIFs in the outgoing stream.  For read operations,
The HBA could extract the DIFs and place it in DIF buffers.

The buffer list for this type consists of one or more of the

.. _`lpfc_bg_setup_bpl_prot.protection-groups-described-below`:

protection groups described below
---------------------------------

+-------------------------+
start of first prot group  -->   \|          PDE_5          \|
+-------------------------+
\|          PDE_6          \|
+-------------------------+
\|      PDE_7 (Prot BDE)   \|
+-------------------------+
\|        Data BDE         \|
+-------------------------+
\|more Data BDE's ... (opt)\|
+-------------------------+
start of new  prot group  -->    \|          PDE_5          \|
+-------------------------+
\|          ...            \|
+-------------------------+

.. _`lpfc_bg_setup_bpl_prot.note`:

Note
----

It is assumed that both data and protection s/g buffers have been
mapped for DMA

Returns the number of BDEs added to the BPL.

.. _`lpfc_bg_setup_sgl`:

lpfc_bg_setup_sgl
=================

.. c:function:: int lpfc_bg_setup_sgl(struct lpfc_hba *phba, struct scsi_cmnd *sc, struct sli4_sge *sgl, int datasegcnt)

    Setup BlockGuard SGL with no protection data

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param sc:
        pointer to scsi command we're working on
    :type sc: struct scsi_cmnd \*

    :param sgl:
        pointer to buffer list for protection groups
    :type sgl: struct sli4_sge \*

    :param datasegcnt:
        *undescribed*
    :type datasegcnt: int

.. _`lpfc_bg_setup_sgl.description`:

Description
-----------

This function sets up SGL buffer list for protection groups of
type LPFC_PG_TYPE_NO_DIF

This is usually used when the HBA is instructed to generate
DIFs and insert them into data stream (or strip DIF from
incoming data stream)

The buffer list consists of just one protection group described

.. _`lpfc_bg_setup_sgl.below`:

below
-----

+-------------------------+
start of prot group  -->     \|         DI_SEED         \|
+-------------------------+
\|         Data SGE        \|
+-------------------------+
\|more Data SGE's ... (opt)\|
+-------------------------+

.. _`lpfc_bg_setup_sgl.note`:

Note
----

Data s/g buffers have been dma mapped

Returns the number of SGEs added to the SGL.

.. _`lpfc_bg_setup_sgl_prot`:

lpfc_bg_setup_sgl_prot
======================

.. c:function:: int lpfc_bg_setup_sgl_prot(struct lpfc_hba *phba, struct scsi_cmnd *sc, struct sli4_sge *sgl, int datacnt, int protcnt)

    Setup BlockGuard SGL with protection data

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param sc:
        pointer to scsi command we're working on
    :type sc: struct scsi_cmnd \*

    :param sgl:
        pointer to buffer list for protection groups
    :type sgl: struct sli4_sge \*

    :param datacnt:
        number of segments of data that have been dma mapped
    :type datacnt: int

    :param protcnt:
        number of segment of protection data that have been dma mapped
    :type protcnt: int

.. _`lpfc_bg_setup_sgl_prot.description`:

Description
-----------

This function sets up SGL buffer list for protection groups of
type LPFC_PG_TYPE_DIF

This is usually used when DIFs are in their own buffers,
separate from the data. The HBA can then by instructed
to place the DIFs in the outgoing stream.  For read operations,
The HBA could extract the DIFs and place it in DIF buffers.

The buffer list for this type consists of one or more of the

.. _`lpfc_bg_setup_sgl_prot.protection-groups-described-below`:

protection groups described below
---------------------------------

+-------------------------+
start of first prot group  -->   \|         DISEED          \|
+-------------------------+
\|      DIF (Prot SGE)     \|
+-------------------------+
\|        Data SGE         \|
+-------------------------+
\|more Data SGE's ... (opt)\|
+-------------------------+
start of new  prot group  -->    \|         DISEED          \|
+-------------------------+
\|          ...            \|
+-------------------------+

.. _`lpfc_bg_setup_sgl_prot.note`:

Note
----

It is assumed that both data and protection s/g buffers have been
mapped for DMA

Returns the number of SGEs added to the SGL.

.. _`lpfc_prot_group_type`:

lpfc_prot_group_type
====================

.. c:function:: int lpfc_prot_group_type(struct lpfc_hba *phba, struct scsi_cmnd *sc)

    Get prtotection group type of SCSI command

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param sc:
        pointer to scsi command we're working on
    :type sc: struct scsi_cmnd \*

.. _`lpfc_prot_group_type.description`:

Description
-----------

Given a SCSI command that supports DIF, determine composition of protection
groups involved in setting up buffer lists

.. _`lpfc_prot_group_type.return`:

Return
------

Protection group type (with or without DIF)

.. _`lpfc_bg_scsi_adjust_dl`:

lpfc_bg_scsi_adjust_dl
======================

.. c:function:: int lpfc_bg_scsi_adjust_dl(struct lpfc_hba *phba, struct lpfc_scsi_buf *lpfc_cmd)

    Adjust SCSI data length for BlockGuard

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param lpfc_cmd:
        The scsi buffer which is going to be adjusted.
    :type lpfc_cmd: struct lpfc_scsi_buf \*

.. _`lpfc_bg_scsi_adjust_dl.description`:

Description
-----------

Adjust the data length to account for how much data
is actually on the wire.

returns the adjusted data length

.. _`lpfc_bg_scsi_prep_dma_buf_s3`:

lpfc_bg_scsi_prep_dma_buf_s3
============================

.. c:function:: int lpfc_bg_scsi_prep_dma_buf_s3(struct lpfc_hba *phba, struct lpfc_scsi_buf *lpfc_cmd)

    DMA mapping for scsi buffer to SLI3 IF spec

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param lpfc_cmd:
        The scsi buffer which is going to be prep'ed.
    :type lpfc_cmd: struct lpfc_scsi_buf \*

.. _`lpfc_bg_scsi_prep_dma_buf_s3.description`:

Description
-----------

This is the protection/DIF aware version of
\ :c:func:`lpfc_scsi_prep_dma_buf`\ . It may be a good idea to combine the
two functions eventually, but for now, it's here

.. _`lpfc_scsi_prep_dma_buf_s4`:

lpfc_scsi_prep_dma_buf_s4
=========================

.. c:function:: int lpfc_scsi_prep_dma_buf_s4(struct lpfc_hba *phba, struct lpfc_scsi_buf *lpfc_cmd)

    DMA mapping for scsi buffer to SLI4 IF spec

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param lpfc_cmd:
        The scsi buffer which is going to be mapped.
    :type lpfc_cmd: struct lpfc_scsi_buf \*

.. _`lpfc_scsi_prep_dma_buf_s4.description`:

Description
-----------

This routine does the pci dma mapping for scatter-gather list of scsi cmnd
field of \ ``lpfc_cmd``\  for device with SLI-4 interface spec.

.. _`lpfc_scsi_prep_dma_buf_s4.return-codes`:

Return codes
------------

1 - Error
0 - Success

.. _`lpfc_bg_scsi_prep_dma_buf_s4`:

lpfc_bg_scsi_prep_dma_buf_s4
============================

.. c:function:: int lpfc_bg_scsi_prep_dma_buf_s4(struct lpfc_hba *phba, struct lpfc_scsi_buf *lpfc_cmd)

    DMA mapping for scsi buffer to SLI4 IF spec

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param lpfc_cmd:
        The scsi buffer which is going to be mapped.
    :type lpfc_cmd: struct lpfc_scsi_buf \*

.. _`lpfc_bg_scsi_prep_dma_buf_s4.description`:

Description
-----------

This is the protection/DIF aware version of
\ :c:func:`lpfc_scsi_prep_dma_buf`\ . It may be a good idea to combine the
two functions eventually, but for now, it's here

.. _`lpfc_scsi_prep_dma_buf`:

lpfc_scsi_prep_dma_buf
======================

.. c:function:: int lpfc_scsi_prep_dma_buf(struct lpfc_hba *phba, struct lpfc_scsi_buf *lpfc_cmd)

    Wrapper function for DMA mapping of scsi buffer

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param lpfc_cmd:
        The scsi buffer which is going to be mapped.
    :type lpfc_cmd: struct lpfc_scsi_buf \*

.. _`lpfc_scsi_prep_dma_buf.description`:

Description
-----------

This routine wraps the actual DMA mapping function pointer from the
lpfc_hba struct.

.. _`lpfc_scsi_prep_dma_buf.return-codes`:

Return codes
------------

1 - Error
0 - Success

.. _`lpfc_bg_scsi_prep_dma_buf`:

lpfc_bg_scsi_prep_dma_buf
=========================

.. c:function:: int lpfc_bg_scsi_prep_dma_buf(struct lpfc_hba *phba, struct lpfc_scsi_buf *lpfc_cmd)

    Wrapper function for DMA mapping of scsi buffer using BlockGuard.

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param lpfc_cmd:
        The scsi buffer which is going to be mapped.
    :type lpfc_cmd: struct lpfc_scsi_buf \*

.. _`lpfc_bg_scsi_prep_dma_buf.description`:

Description
-----------

This routine wraps the actual DMA mapping function pointer from the
lpfc_hba struct.

.. _`lpfc_bg_scsi_prep_dma_buf.return-codes`:

Return codes
------------

1 - Error
0 - Success

.. _`lpfc_send_scsi_error_event`:

lpfc_send_scsi_error_event
==========================

.. c:function:: void lpfc_send_scsi_error_event(struct lpfc_hba *phba, struct lpfc_vport *vport, struct lpfc_scsi_buf *lpfc_cmd, struct lpfc_iocbq *rsp_iocb)

    Posts an event when there is SCSI error

    :param phba:
        Pointer to hba context object.
    :type phba: struct lpfc_hba \*

    :param vport:
        Pointer to vport object.
    :type vport: struct lpfc_vport \*

    :param lpfc_cmd:
        Pointer to lpfc scsi command which reported the error.
    :type lpfc_cmd: struct lpfc_scsi_buf \*

    :param rsp_iocb:
        Pointer to response iocb object which reported error.
    :type rsp_iocb: struct lpfc_iocbq \*

.. _`lpfc_send_scsi_error_event.description`:

Description
-----------

This function posts an event when there is a SCSI command reporting
error from the scsi device.

.. _`lpfc_scsi_unprep_dma_buf`:

lpfc_scsi_unprep_dma_buf
========================

.. c:function:: void lpfc_scsi_unprep_dma_buf(struct lpfc_hba *phba, struct lpfc_scsi_buf *psb)

    Un-map DMA mapping of SG-list for dev

    :param phba:
        The HBA for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param psb:
        The scsi buffer which is going to be un-mapped.
    :type psb: struct lpfc_scsi_buf \*

.. _`lpfc_scsi_unprep_dma_buf.description`:

Description
-----------

This routine does DMA un-mapping of scatter gather list of scsi command
field of \ ``lpfc_cmd``\  for device with SLI-3 interface spec.

.. _`lpfc_handle_fcp_err`:

lpfc_handle_fcp_err
===================

.. c:function:: void lpfc_handle_fcp_err(struct lpfc_vport *vport, struct lpfc_scsi_buf *lpfc_cmd, struct lpfc_iocbq *rsp_iocb)

    FCP response handler

    :param vport:
        The virtual port for which this call is being executed.
    :type vport: struct lpfc_vport \*

    :param lpfc_cmd:
        Pointer to lpfc_scsi_buf data structure.
    :type lpfc_cmd: struct lpfc_scsi_buf \*

    :param rsp_iocb:
        The response IOCB which contains FCP error.
    :type rsp_iocb: struct lpfc_iocbq \*

.. _`lpfc_handle_fcp_err.description`:

Description
-----------

This routine is called to process response IOCB with status field
IOSTAT_FCP_RSP_ERROR. This routine sets result field of scsi command
based upon SCSI and FCP error.

.. _`lpfc_sli4_scmd_to_wqidx_distr`:

lpfc_sli4_scmd_to_wqidx_distr
=============================

.. c:function:: int lpfc_sli4_scmd_to_wqidx_distr(struct lpfc_hba *phba, struct lpfc_scsi_buf *lpfc_cmd)

    scsi command to SLI4 WQ index distribution

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

    :param lpfc_cmd:
        *undescribed*
    :type lpfc_cmd: struct lpfc_scsi_buf \*

.. _`lpfc_sli4_scmd_to_wqidx_distr.description`:

Description
-----------

This routine performs a roundrobin SCSI command to SLI4 FCP WQ index
distribution.  This is called by \__lpfc_sli_issue_iocb_s4() with the hbalock
held.
If scsi-mq is enabled, get the default block layer mapping of software queues
to hardware queues. This information is saved in request tag.

.. _`lpfc_sli4_scmd_to_wqidx_distr.return`:

Return
------

index into SLI4 fast-path FCP queue index.

.. _`lpfc_scsi_cmd_iocb_cmpl`:

lpfc_scsi_cmd_iocb_cmpl
=======================

.. c:function:: void lpfc_scsi_cmd_iocb_cmpl(struct lpfc_hba *phba, struct lpfc_iocbq *pIocbIn, struct lpfc_iocbq *pIocbOut)

    Scsi cmnd IOCB completion routine

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param pIocbIn:
        The command IOCBQ for the scsi cmnd.
    :type pIocbIn: struct lpfc_iocbq \*

    :param pIocbOut:
        The response IOCBQ for the scsi cmnd.
    :type pIocbOut: struct lpfc_iocbq \*

.. _`lpfc_scsi_cmd_iocb_cmpl.description`:

Description
-----------

This routine assigns scsi command result by looking into response IOCB
status field appropriately. This routine handles QUEUE FULL condition as
well by ramping down device queue depth.

.. _`lpfc_fcpcmd_to_iocb`:

lpfc_fcpcmd_to_iocb
===================

.. c:function:: void lpfc_fcpcmd_to_iocb(uint8_t *data, struct fcp_cmnd *fcp_cmnd)

    copy the fcp_cmd data into the IOCB

    :param data:
        A pointer to the immediate command data portion of the IOCB.
    :type data: uint8_t \*

    :param fcp_cmnd:
        The FCP Command that is provided by the SCSI layer.
    :type fcp_cmnd: struct fcp_cmnd \*

.. _`lpfc_fcpcmd_to_iocb.description`:

Description
-----------

The routine copies the entire FCP command from \ ``fcp_cmnd``\  to \ ``data``\  while
byte swapping the data to big endian format for transmission on the wire.

.. _`lpfc_scsi_prep_cmnd`:

lpfc_scsi_prep_cmnd
===================

.. c:function:: void lpfc_scsi_prep_cmnd(struct lpfc_vport *vport, struct lpfc_scsi_buf *lpfc_cmd, struct lpfc_nodelist *pnode)

    Wrapper func for convert scsi cmnd to FCP info unit

    :param vport:
        The virtual port for which this call is being executed.
    :type vport: struct lpfc_vport \*

    :param lpfc_cmd:
        The scsi command which needs to send.
    :type lpfc_cmd: struct lpfc_scsi_buf \*

    :param pnode:
        Pointer to lpfc_nodelist.
    :type pnode: struct lpfc_nodelist \*

.. _`lpfc_scsi_prep_cmnd.description`:

Description
-----------

This routine initializes fcp_cmnd and iocb data structure from scsi command
to transfer for device with SLI3 interface spec.

.. _`lpfc_scsi_prep_task_mgmt_cmd`:

lpfc_scsi_prep_task_mgmt_cmd
============================

.. c:function:: int lpfc_scsi_prep_task_mgmt_cmd(struct lpfc_vport *vport, struct lpfc_scsi_buf *lpfc_cmd, uint64_t lun, uint8_t task_mgmt_cmd)

    Convert SLI3 scsi TM cmd to FCP info unit

    :param vport:
        The virtual port for which this call is being executed.
    :type vport: struct lpfc_vport \*

    :param lpfc_cmd:
        Pointer to lpfc_scsi_buf data structure.
    :type lpfc_cmd: struct lpfc_scsi_buf \*

    :param lun:
        Logical unit number.
    :type lun: uint64_t

    :param task_mgmt_cmd:
        SCSI task management command.
    :type task_mgmt_cmd: uint8_t

.. _`lpfc_scsi_prep_task_mgmt_cmd.description`:

Description
-----------

This routine creates FCP information unit corresponding to \ ``task_mgmt_cmd``\ 
for device with SLI-3 interface spec.

.. _`lpfc_scsi_prep_task_mgmt_cmd.return-codes`:

Return codes
------------

0 - Error
1 - Success

.. _`lpfc_scsi_api_table_setup`:

lpfc_scsi_api_table_setup
=========================

.. c:function:: int lpfc_scsi_api_table_setup(struct lpfc_hba *phba, uint8_t dev_grp)

    Set up scsi api function jump table

    :param phba:
        The hba struct for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param dev_grp:
        The HBA PCI-Device group number.
    :type dev_grp: uint8_t

.. _`lpfc_scsi_api_table_setup.description`:

Description
-----------

This routine sets up the SCSI interface API function jump table in \ ``phba``\ 
struct.

.. _`lpfc_scsi_api_table_setup.return`:

Return
------

0 - success, -ENODEV - failure.

.. _`lpfc_tskmgmt_def_cmpl`:

lpfc_tskmgmt_def_cmpl
=====================

.. c:function:: void lpfc_tskmgmt_def_cmpl(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocbq, struct lpfc_iocbq *rspiocbq)

    IOCB completion routine for task management command

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param cmdiocbq:
        Pointer to lpfc_iocbq data structure.
    :type cmdiocbq: struct lpfc_iocbq \*

    :param rspiocbq:
        Pointer to lpfc_iocbq data structure.
    :type rspiocbq: struct lpfc_iocbq \*

.. _`lpfc_tskmgmt_def_cmpl.description`:

Description
-----------

This routine is IOCB completion routine for device reset and target reset
routine. This routine release scsi buffer associated with lpfc_cmd.

.. _`lpfc_info`:

lpfc_info
=========

.. c:function:: const char *lpfc_info(struct Scsi_Host *host)

    Info entry point of scsi_host_template data structure

    :param host:
        The scsi host for which this call is being executed.
    :type host: struct Scsi_Host \*

.. _`lpfc_info.description`:

Description
-----------

This routine provides module information about hba.

.. _`lpfc_info.reutrn-code`:

Reutrn code
-----------

Pointer to char - Success.

.. _`lpfc_poll_rearm_timer`:

lpfc_poll_rearm_timer
=====================

.. c:function:: void lpfc_poll_rearm_timer(struct lpfc_hba *phba)

    Routine to modify fcp_poll timer of hba

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

.. _`lpfc_poll_rearm_timer.description`:

Description
-----------

This routine modifies fcp_poll_timer  field of \ ``phba``\  by cfg_poll_tmo.
The default value of cfg_poll_tmo is 10 milliseconds.

.. _`lpfc_poll_start_timer`:

lpfc_poll_start_timer
=====================

.. c:function:: void lpfc_poll_start_timer(struct lpfc_hba *phba)

    Routine to start fcp_poll_timer of HBA

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

.. _`lpfc_poll_start_timer.description`:

Description
-----------

This routine starts the fcp_poll_timer of \ ``phba``\ .

.. _`lpfc_poll_timeout`:

lpfc_poll_timeout
=================

.. c:function:: void lpfc_poll_timeout(struct timer_list *t)

    Restart polling timer

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`lpfc_poll_timeout.description`:

Description
-----------

This routine restarts fcp_poll timer, when FCP ring  polling is enable
and FCP Ring interrupt is disable.

.. _`lpfc_queuecommand`:

lpfc_queuecommand
=================

.. c:function:: int lpfc_queuecommand(struct Scsi_Host *shost, struct scsi_cmnd *cmnd)

    scsi_host_template queuecommand entry point

    :param shost:
        *undescribed*
    :type shost: struct Scsi_Host \*

    :param cmnd:
        Pointer to scsi_cmnd data structure.
    :type cmnd: struct scsi_cmnd \*

.. _`lpfc_queuecommand.description`:

Description
-----------

Driver registers this routine to scsi midlayer to submit a \ ``cmd``\  to process.
This routine prepares an IOCB from scsi command and provides to firmware.
The \ ``done``\  callback is invoked after driver finished processing the command.

Return value :
0 - Success
SCSI_MLQUEUE_HOST_BUSY - Block all devices served by this host temporarily.

.. _`lpfc_abort_handler`:

lpfc_abort_handler
==================

.. c:function:: int lpfc_abort_handler(struct scsi_cmnd *cmnd)

    scsi_host_template eh_abort_handler entry point

    :param cmnd:
        Pointer to scsi_cmnd data structure.
    :type cmnd: struct scsi_cmnd \*

.. _`lpfc_abort_handler.description`:

Description
-----------

This routine aborts \ ``cmnd``\  pending in base driver.

Return code :
0x2003 - Error
0x2002 - Success

.. _`lpfc_check_fcp_rsp`:

lpfc_check_fcp_rsp
==================

.. c:function:: int lpfc_check_fcp_rsp(struct lpfc_vport *vport, struct lpfc_scsi_buf *lpfc_cmd)

    check the returned fcp_rsp to see if task failed

    :param vport:
        The virtual port for which this call is being executed.
    :type vport: struct lpfc_vport \*

    :param lpfc_cmd:
        Pointer to lpfc_scsi_buf data structure.
    :type lpfc_cmd: struct lpfc_scsi_buf \*

.. _`lpfc_check_fcp_rsp.description`:

Description
-----------

This routine checks the FCP RSP INFO to see if the tsk mgmt command succeded

Return code :
0x2003 - Error
0x2002 - Success

.. _`lpfc_send_taskmgmt`:

lpfc_send_taskmgmt
==================

.. c:function:: int lpfc_send_taskmgmt(struct lpfc_vport *vport, struct scsi_cmnd *cmnd, unsigned int tgt_id, uint64_t lun_id, uint8_t task_mgmt_cmd)

    Generic SCSI Task Mgmt Handler

    :param vport:
        The virtual port for which this call is being executed.
    :type vport: struct lpfc_vport \*

    :param cmnd:
        *undescribed*
    :type cmnd: struct scsi_cmnd \*

    :param tgt_id:
        Target ID of remote device.
    :type tgt_id: unsigned int

    :param lun_id:
        Lun number for the TMF
    :type lun_id: uint64_t

    :param task_mgmt_cmd:
        type of TMF to send
    :type task_mgmt_cmd: uint8_t

.. _`lpfc_send_taskmgmt.description`:

Description
-----------

This routine builds and sends a TMF (SCSI Task Mgmt Function) to
a remote port.

.. _`lpfc_send_taskmgmt.return-code`:

Return Code
-----------

0x2003 - Error
0x2002 - Success.

.. _`lpfc_chk_tgt_mapped`:

lpfc_chk_tgt_mapped
===================

.. c:function:: int lpfc_chk_tgt_mapped(struct lpfc_vport *vport, struct scsi_cmnd *cmnd)

    :param vport:
        The virtual port to check on
    :type vport: struct lpfc_vport \*

    :param cmnd:
        Pointer to scsi_cmnd data structure.
    :type cmnd: struct scsi_cmnd \*

.. _`lpfc_chk_tgt_mapped.description`:

Description
-----------

This routine delays until the scsi target (aka rport) for the
command exists (is present and logged in) or we declare it non-existent.

Return code :
0x2003 - Error
0x2002 - Success

.. _`lpfc_reset_flush_io_context`:

lpfc_reset_flush_io_context
===========================

.. c:function:: int lpfc_reset_flush_io_context(struct lpfc_vport *vport, uint16_t tgt_id, uint64_t lun_id, lpfc_ctx_cmd context)

    :param vport:
        The virtual port (scsi_host) for the flush context
    :type vport: struct lpfc_vport \*

    :param tgt_id:
        If aborting by Target contect - specifies the target id
    :type tgt_id: uint16_t

    :param lun_id:
        If aborting by Lun context - specifies the lun id
    :type lun_id: uint64_t

    :param context:
        specifies the context level to flush at.
    :type context: lpfc_ctx_cmd

.. _`lpfc_reset_flush_io_context.description`:

Description
-----------

After a reset condition via TMF, we need to flush orphaned i/o
contexts from the adapter. This routine aborts any contexts
outstanding, then waits for their completions. The wait is
bounded by devloss_tmo though.

Return code :
0x2003 - Error
0x2002 - Success

.. _`lpfc_device_reset_handler`:

lpfc_device_reset_handler
=========================

.. c:function:: int lpfc_device_reset_handler(struct scsi_cmnd *cmnd)

    scsi_host_template eh_device_reset entry point

    :param cmnd:
        Pointer to scsi_cmnd data structure.
    :type cmnd: struct scsi_cmnd \*

.. _`lpfc_device_reset_handler.description`:

Description
-----------

This routine does a device reset by sending a LUN_RESET task management
command.

Return code :
0x2003 - Error
0x2002 - Success

.. _`lpfc_target_reset_handler`:

lpfc_target_reset_handler
=========================

.. c:function:: int lpfc_target_reset_handler(struct scsi_cmnd *cmnd)

    scsi_host_template eh_target_reset entry point

    :param cmnd:
        Pointer to scsi_cmnd data structure.
    :type cmnd: struct scsi_cmnd \*

.. _`lpfc_target_reset_handler.description`:

Description
-----------

This routine does a target reset by sending a TARGET_RESET task management
command.

Return code :
0x2003 - Error
0x2002 - Success

.. _`lpfc_bus_reset_handler`:

lpfc_bus_reset_handler
======================

.. c:function:: int lpfc_bus_reset_handler(struct scsi_cmnd *cmnd)

    scsi_host_template eh_bus_reset_handler entry point

    :param cmnd:
        Pointer to scsi_cmnd data structure.
    :type cmnd: struct scsi_cmnd \*

.. _`lpfc_bus_reset_handler.description`:

Description
-----------

This routine does target reset to all targets on \ ``cmnd->device->host``\ .
This emulates Parallel SCSI Bus Reset Semantics.

Return code :
0x2003 - Error
0x2002 - Success

.. _`lpfc_host_reset_handler`:

lpfc_host_reset_handler
=======================

.. c:function:: int lpfc_host_reset_handler(struct scsi_cmnd *cmnd)

    scsi_host_template eh_host_reset_handler entry pt

    :param cmnd:
        Pointer to scsi_cmnd data structure.
    :type cmnd: struct scsi_cmnd \*

.. _`lpfc_host_reset_handler.description`:

Description
-----------

This routine does host reset to the adaptor port. It brings the HBA
offline, performs a board restart, and then brings the board back online.
The lpfc_offline calls lpfc_sli_hba_down which will abort and local
reject all outstanding SCSI commands to the host and error returned
back to SCSI mid-level. As this will be SCSI mid-level's last resort
of error handling, it will only return error if resetting of the adapter
is not successful; in all other cases, will return success.

Return code :
0x2003 - Error
0x2002 - Success

.. _`lpfc_slave_alloc`:

lpfc_slave_alloc
================

.. c:function:: int lpfc_slave_alloc(struct scsi_device *sdev)

    scsi_host_template slave_alloc entry point

    :param sdev:
        Pointer to scsi_device.
    :type sdev: struct scsi_device \*

.. _`lpfc_slave_alloc.description`:

Description
-----------

This routine populates the cmds_per_lun count + 2 scsi_bufs into  this host's
globally available list of scsi buffers. This routine also makes sure scsi
buffer is not allocated more than HBA limit conveyed to midlayer. This list
of scsi buffer exists for the lifetime of the driver.

.. _`lpfc_slave_alloc.return-codes`:

Return codes
------------

non-0 - Error
0 - Success

.. _`lpfc_slave_configure`:

lpfc_slave_configure
====================

.. c:function:: int lpfc_slave_configure(struct scsi_device *sdev)

    scsi_host_template slave_configure entry point

    :param sdev:
        Pointer to scsi_device.
    :type sdev: struct scsi_device \*

.. _`lpfc_slave_configure.description`:

Description
-----------

This routine configures following items
- Tag command queuing support for \ ``sdev``\  if supported.
- Enable SLI polling for fcp ring if ENABLE_FCP_RING_POLLING flag is set.

.. _`lpfc_slave_configure.return-codes`:

Return codes
------------

0 - Success

.. _`lpfc_slave_destroy`:

lpfc_slave_destroy
==================

.. c:function:: void lpfc_slave_destroy(struct scsi_device *sdev)

    slave_destroy entry point of SHT data structure

    :param sdev:
        Pointer to scsi_device.
    :type sdev: struct scsi_device \*

.. _`lpfc_slave_destroy.description`:

Description
-----------

This routine sets \ ``sdev``\  hostatdata filed to null.

.. _`lpfc_create_device_data`:

lpfc_create_device_data
=======================

.. c:function:: struct lpfc_device_data* lpfc_create_device_data(struct lpfc_hba *phba, struct lpfc_name *vport_wwpn, struct lpfc_name *target_wwpn, uint64_t lun, uint32_t pri, bool atomic_create)

    creates and initializes device data structure for OAS

    :param phba:
        *undescribed*
    :type phba: struct lpfc_hba \*

    :param vport_wwpn:
        Pointer to vport's wwpn information
    :type vport_wwpn: struct lpfc_name \*

    :param target_wwpn:
        Pointer to target's wwpn information
    :type target_wwpn: struct lpfc_name \*

    :param lun:
        Lun on target
    :type lun: uint64_t

    :param pri:
        *undescribed*
    :type pri: uint32_t

    :param atomic_create:
        Flag to indicate if memory should be allocated using the
        GFP_ATOMIC flag or not.
    :type atomic_create: bool

.. _`lpfc_create_device_data.description`:

Description
-----------

This routine creates a device data structure which will contain identifying
information for the device (host wwpn, target wwpn, lun), state of OAS,
whether or not the corresponding lun is available by the system,
and pointer to the rport data.

.. _`lpfc_create_device_data.return-codes`:

Return codes
------------

NULL - Error
Pointer to lpfc_device_data - Success

.. _`lpfc_delete_device_data`:

lpfc_delete_device_data
=======================

.. c:function:: void lpfc_delete_device_data(struct lpfc_hba *phba, struct lpfc_device_data *lun_info)

    frees a device data structure for OAS

    :param phba:
        *undescribed*
    :type phba: struct lpfc_hba \*

    :param lun_info:
        Pointer to device data structure to free.
    :type lun_info: struct lpfc_device_data \*

.. _`lpfc_delete_device_data.description`:

Description
-----------

This routine frees the previously allocated device data structure passed.

.. _`__lpfc_get_device_data`:

\__lpfc_get_device_data
=======================

.. c:function:: struct lpfc_device_data* __lpfc_get_device_data(struct lpfc_hba *phba, struct list_head *list, struct lpfc_name *vport_wwpn, struct lpfc_name *target_wwpn, uint64_t lun)

    returns the device data for the specified lun

    :param phba:
        *undescribed*
    :type phba: struct lpfc_hba \*

    :param list:
        Point to list to search.
    :type list: struct list_head \*

    :param vport_wwpn:
        Pointer to vport's wwpn information
    :type vport_wwpn: struct lpfc_name \*

    :param target_wwpn:
        Pointer to target's wwpn information
    :type target_wwpn: struct lpfc_name \*

    :param lun:
        Lun on target
    :type lun: uint64_t

.. _`__lpfc_get_device_data.description`:

Description
-----------

This routine searches the list passed for the specified lun's device data.
This function does not hold locks, it is the responsibility of the caller
to ensure the proper lock is held before calling the function.

.. _`__lpfc_get_device_data.return-codes`:

Return codes
------------

NULL - Error
Pointer to lpfc_device_data - Success

.. _`lpfc_find_next_oas_lun`:

lpfc_find_next_oas_lun
======================

.. c:function:: bool lpfc_find_next_oas_lun(struct lpfc_hba *phba, struct lpfc_name *vport_wwpn, struct lpfc_name *target_wwpn, uint64_t *starting_lun, struct lpfc_name *found_vport_wwpn, struct lpfc_name *found_target_wwpn, uint64_t *found_lun, uint32_t *found_lun_status, uint32_t *found_lun_pri)

    searches for the next oas lun

    :param phba:
        *undescribed*
    :type phba: struct lpfc_hba \*

    :param vport_wwpn:
        Pointer to vport's wwpn information
    :type vport_wwpn: struct lpfc_name \*

    :param target_wwpn:
        Pointer to target's wwpn information
    :type target_wwpn: struct lpfc_name \*

    :param starting_lun:
        Pointer to the lun to start searching for
    :type starting_lun: uint64_t \*

    :param found_vport_wwpn:
        Pointer to the found lun's vport wwpn information
    :type found_vport_wwpn: struct lpfc_name \*

    :param found_target_wwpn:
        Pointer to the found lun's target wwpn information
    :type found_target_wwpn: struct lpfc_name \*

    :param found_lun:
        Pointer to the found lun.
    :type found_lun: uint64_t \*

    :param found_lun_status:
        Pointer to status of the found lun.
    :type found_lun_status: uint32_t \*

    :param found_lun_pri:
        *undescribed*
    :type found_lun_pri: uint32_t \*

.. _`lpfc_find_next_oas_lun.description`:

Description
-----------

This routine searches the luns list for the specified lun
or the first lun for the vport/target.  If the vport wwpn contains
a zero value then a specific vport is not specified. In this case
any vport which contains the lun will be considered a match.  If the
target wwpn contains a zero value then a specific target is not specified.
In this case any target which contains the lun will be considered a
match.  If the lun is found, the lun, vport wwpn, target wwpn and lun status
are returned.  The function will also return the next lun if available.
If the next lun is not found, starting_lun parameter will be set to
NO_MORE_OAS_LUN.

.. _`lpfc_find_next_oas_lun.return-codes`:

Return codes
------------

non-0 - Error
0 - Success

.. _`lpfc_enable_oas_lun`:

lpfc_enable_oas_lun
===================

.. c:function:: bool lpfc_enable_oas_lun(struct lpfc_hba *phba, struct lpfc_name *vport_wwpn, struct lpfc_name *target_wwpn, uint64_t lun, uint8_t pri)

    enables a lun for OAS operations

    :param phba:
        *undescribed*
    :type phba: struct lpfc_hba \*

    :param vport_wwpn:
        Pointer to vport's wwpn information
    :type vport_wwpn: struct lpfc_name \*

    :param target_wwpn:
        Pointer to target's wwpn information
    :type target_wwpn: struct lpfc_name \*

    :param lun:
        Lun
    :type lun: uint64_t

    :param pri:
        *undescribed*
    :type pri: uint8_t

.. _`lpfc_enable_oas_lun.description`:

Description
-----------

This routine enables a lun for oas operations.  The routines does so by
doing the following :

1) Checks to see if the device data for the lun has been created.
2) If found, sets the OAS enabled flag if not set and returns.
3) Otherwise, creates a device data structure.
4) If successfully created, indicates the device data is for an OAS lun,
indicates the lun is not available and add to the list of luns.

.. _`lpfc_enable_oas_lun.return-codes`:

Return codes
------------

false - Error
true - Success

.. _`lpfc_disable_oas_lun`:

lpfc_disable_oas_lun
====================

.. c:function:: bool lpfc_disable_oas_lun(struct lpfc_hba *phba, struct lpfc_name *vport_wwpn, struct lpfc_name *target_wwpn, uint64_t lun, uint8_t pri)

    disables a lun for OAS operations

    :param phba:
        *undescribed*
    :type phba: struct lpfc_hba \*

    :param vport_wwpn:
        Pointer to vport's wwpn information
    :type vport_wwpn: struct lpfc_name \*

    :param target_wwpn:
        Pointer to target's wwpn information
    :type target_wwpn: struct lpfc_name \*

    :param lun:
        Lun
    :type lun: uint64_t

    :param pri:
        *undescribed*
    :type pri: uint8_t

.. _`lpfc_disable_oas_lun.description`:

Description
-----------

This routine disables a lun for oas operations.  The routines does so by
doing the following :

1) Checks to see if the device data for the lun is created.
2) If present, clears the flag indicating this lun is for OAS.
3) If the lun is not available by the system, the device data is
freed.

.. _`lpfc_disable_oas_lun.return-codes`:

Return codes
------------

false - Error
true - Success

.. This file was automatic generated / don't edit.

