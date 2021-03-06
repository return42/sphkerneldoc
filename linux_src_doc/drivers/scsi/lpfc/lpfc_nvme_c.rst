.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/lpfc/lpfc_nvme.c

.. _`lpfc_nvme_create_queue`:

lpfc_nvme_create_queue
======================

.. c:function:: int lpfc_nvme_create_queue(struct nvme_fc_local_port *pnvme_lport, unsigned int qidx, u16 qsize, void **handle)

    :param pnvme_lport:
        *undescribed*
    :type pnvme_lport: struct nvme_fc_local_port \*

    :param qidx:
        An cpu index used to affinitize IO queues and MSIX vectors.
    :type qidx: unsigned int

    :param qsize:
        *undescribed*
    :type qsize: u16

    :param handle:
        An opaque driver handle used in follow-up calls.
    :type handle: void \*\*

.. _`lpfc_nvme_create_queue.description`:

Description
-----------

Driver registers this routine to preallocate and initialize any
internal data structures to bind the \ ``qidx``\  to its internal IO queues.
A hardware queue maps (qidx) to a specific driver MSI-X vector/EQ/CQ/WQ.

Return value :
0 - Success
-EINVAL - Unsupported input value.
-ENOMEM - Could not alloc necessary memory

.. _`lpfc_nvme_delete_queue`:

lpfc_nvme_delete_queue
======================

.. c:function:: void lpfc_nvme_delete_queue(struct nvme_fc_local_port *pnvme_lport, unsigned int qidx, void *handle)

    :param pnvme_lport:
        *undescribed*
    :type pnvme_lport: struct nvme_fc_local_port \*

    :param qidx:
        An cpu index used to affinitize IO queues and MSIX vectors.
    :type qidx: unsigned int

    :param handle:
        An opaque driver handle from lpfc_nvme_create_queue
    :type handle: void \*

.. _`lpfc_nvme_delete_queue.description`:

Description
-----------

Driver registers this routine to free
any internal data structures to bind the \ ``qidx``\  to its internal
IO queues.

Return value :
0 - Success

.. _`lpfc_nvme_delete_queue.todo`:

TODO
----

What are the failure codes.

.. _`lpfc_nvme_ls_req`:

lpfc_nvme_ls_req
================

.. c:function:: int lpfc_nvme_ls_req(struct nvme_fc_local_port *pnvme_lport, struct nvme_fc_remote_port *pnvme_rport, struct nvmefc_ls_req *pnvme_lsreq)

    Issue an Link Service request

    :param pnvme_lport:
        *undescribed*
    :type pnvme_lport: struct nvme_fc_local_port \*

    :param pnvme_rport:
        *undescribed*
    :type pnvme_rport: struct nvme_fc_remote_port \*

    :param pnvme_lsreq:
        *undescribed*
    :type pnvme_lsreq: struct nvmefc_ls_req \*

.. _`lpfc_nvme_ls_req.description`:

Description
-----------

Driver registers this routine to handle any link service request
from the nvme_fc transport to a remote nvme-aware port.

Return value :
0 - Success

.. _`lpfc_nvme_ls_req.todo`:

TODO
----

What are the failure codes.

.. _`lpfc_nvme_ls_abort`:

lpfc_nvme_ls_abort
==================

.. c:function:: void lpfc_nvme_ls_abort(struct nvme_fc_local_port *pnvme_lport, struct nvme_fc_remote_port *pnvme_rport, struct nvmefc_ls_req *pnvme_lsreq)

    Issue an Link Service request

    :param pnvme_lport:
        *undescribed*
    :type pnvme_lport: struct nvme_fc_local_port \*

    :param pnvme_rport:
        *undescribed*
    :type pnvme_rport: struct nvme_fc_remote_port \*

    :param pnvme_lsreq:
        *undescribed*
    :type pnvme_lsreq: struct nvmefc_ls_req \*

.. _`lpfc_nvme_ls_abort.description`:

Description
-----------

Driver registers this routine to handle any link service request
from the nvme_fc transport to a remote nvme-aware port.

Return value :
0 - Success

.. _`lpfc_nvme_ls_abort.todo`:

TODO
----

What are the failure codes.

.. _`lpfc_nvme_io_cmd_wqe_cmpl`:

lpfc_nvme_io_cmd_wqe_cmpl
=========================

.. c:function:: void lpfc_nvme_io_cmd_wqe_cmpl(struct lpfc_hba *phba, struct lpfc_iocbq *pwqeIn, struct lpfc_wcqe_complete *wcqe)

    Complete an NVME-over-FCP IO

    :param phba:
        *undescribed*
    :type phba: struct lpfc_hba \*

    :param pwqeIn:
        *undescribed*
    :type pwqeIn: struct lpfc_iocbq \*

    :param wcqe:
        *undescribed*
    :type wcqe: struct lpfc_wcqe_complete \*

.. _`lpfc_nvme_io_cmd_wqe_cmpl.description`:

Description
-----------

Driver registers this routine as it io request handler.  This
routine issues an fcp WQE with data from the \ ``lpfc_nvme_fcpreq``\ 
data structure to the rport indicated in \ ``lpfc_nvme_rport``\ .

Return value :
0 - Success

.. _`lpfc_nvme_io_cmd_wqe_cmpl.todo`:

TODO
----

What are the failure codes.

.. _`lpfc_nvme_prep_io_cmd`:

lpfc_nvme_prep_io_cmd
=====================

.. c:function:: int lpfc_nvme_prep_io_cmd(struct lpfc_vport *vport, struct lpfc_nvme_buf *lpfc_ncmd, struct lpfc_nodelist *pnode, struct lpfc_nvme_ctrl_stat *cstat)

    Issue an NVME-over-FCP IO

    :param vport:
        *undescribed*
    :type vport: struct lpfc_vport \*

    :param lpfc_ncmd:
        *undescribed*
    :type lpfc_ncmd: struct lpfc_nvme_buf \*

    :param pnode:
        *undescribed*
    :type pnode: struct lpfc_nodelist \*

    :param cstat:
        *undescribed*
    :type cstat: struct lpfc_nvme_ctrl_stat \*

.. _`lpfc_nvme_prep_io_cmd.description`:

Description
-----------

Driver registers this routine as it io request handler.  This
routine issues an fcp WQE with data from the \ ``lpfc_nvme_fcpreq``\ 
data structure to the rport indicated in \ ``lpfc_nvme_rport``\ .

Return value :
0 - Success

.. _`lpfc_nvme_prep_io_cmd.todo`:

TODO
----

What are the failure codes.

.. _`lpfc_nvme_prep_io_dma`:

lpfc_nvme_prep_io_dma
=====================

.. c:function:: int lpfc_nvme_prep_io_dma(struct lpfc_vport *vport, struct lpfc_nvme_buf *lpfc_ncmd)

    Issue an NVME-over-FCP IO

    :param vport:
        *undescribed*
    :type vport: struct lpfc_vport \*

    :param lpfc_ncmd:
        *undescribed*
    :type lpfc_ncmd: struct lpfc_nvme_buf \*

.. _`lpfc_nvme_prep_io_dma.description`:

Description
-----------

Driver registers this routine as it io request handler.  This
routine issues an fcp WQE with data from the \ ``lpfc_nvme_fcpreq``\ 
data structure to the rport indicated in \ ``lpfc_nvme_rport``\ .

Return value :
0 - Success

.. _`lpfc_nvme_prep_io_dma.todo`:

TODO
----

What are the failure codes.

.. _`lpfc_nvme_fcp_io_submit`:

lpfc_nvme_fcp_io_submit
=======================

.. c:function:: int lpfc_nvme_fcp_io_submit(struct nvme_fc_local_port *pnvme_lport, struct nvme_fc_remote_port *pnvme_rport, void *hw_queue_handle, struct nvmefc_fcp_req *pnvme_fcreq)

    Issue an NVME-over-FCP IO

    :param pnvme_lport:
        *undescribed*
    :type pnvme_lport: struct nvme_fc_local_port \*

    :param pnvme_rport:
        *undescribed*
    :type pnvme_rport: struct nvme_fc_remote_port \*

    :param hw_queue_handle:
        Driver-returned handle in lpfc_nvme_create_queue
    :type hw_queue_handle: void \*

    :param pnvme_fcreq:
        *undescribed*
    :type pnvme_fcreq: struct nvmefc_fcp_req \*

.. _`lpfc_nvme_fcp_io_submit.description`:

Description
-----------

Driver registers this routine as it io request handler.  This
routine issues an fcp WQE with data from the \ ``lpfc_nvme_fcpreq``\ 
data structure to the rport

Return value :
0 - Success

.. _`lpfc_nvme_fcp_io_submit.todo`:

TODO
----

What are the failure codes.

.. _`lpfc_nvme_abort_fcreq_cmpl`:

lpfc_nvme_abort_fcreq_cmpl
==========================

.. c:function:: void lpfc_nvme_abort_fcreq_cmpl(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocb, struct lpfc_wcqe_complete *abts_cmpl)

    Complete an NVME FCP abort request.

    :param phba:
        Pointer to HBA context object
    :type phba: struct lpfc_hba \*

    :param cmdiocb:
        Pointer to command iocb object.
    :type cmdiocb: struct lpfc_iocbq \*

    :param abts_cmpl:
        *undescribed*
    :type abts_cmpl: struct lpfc_wcqe_complete \*

.. _`lpfc_nvme_abort_fcreq_cmpl.description`:

Description
-----------

This is the callback function for any NVME FCP IO that was aborted.

.. _`lpfc_nvme_abort_fcreq_cmpl.return-value`:

Return value
------------

None

.. _`lpfc_nvme_fcp_abort`:

lpfc_nvme_fcp_abort
===================

.. c:function:: void lpfc_nvme_fcp_abort(struct nvme_fc_local_port *pnvme_lport, struct nvme_fc_remote_port *pnvme_rport, void *hw_queue_handle, struct nvmefc_fcp_req *pnvme_fcreq)

    Issue an NVME-over-FCP ABTS

    :param pnvme_lport:
        *undescribed*
    :type pnvme_lport: struct nvme_fc_local_port \*

    :param pnvme_rport:
        *undescribed*
    :type pnvme_rport: struct nvme_fc_remote_port \*

    :param hw_queue_handle:
        Driver-returned handle in lpfc_nvme_create_queue
    :type hw_queue_handle: void \*

    :param pnvme_fcreq:
        *undescribed*
    :type pnvme_fcreq: struct nvmefc_fcp_req \*

.. _`lpfc_nvme_fcp_abort.description`:

Description
-----------

Driver registers this routine as its nvme request io abort handler.  This
routine issues an fcp Abort WQE with data from the \ ``lpfc_nvme_fcpreq``\ 
data structure to the rport indicated in \ ``lpfc_nvme_rport``\ .  This routine
is executed asynchronously - one the target is validated as "MAPPED" and
ready for IO, the driver issues the abort request and returns.

.. _`lpfc_nvme_fcp_abort.return-value`:

Return value
------------

None

.. _`lpfc_sli4_post_nvme_sgl_block`:

lpfc_sli4_post_nvme_sgl_block
=============================

.. c:function:: int lpfc_sli4_post_nvme_sgl_block(struct lpfc_hba *phba, struct list_head *nblist, int count)

    post a block of nvme sgl list to firmware

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param nblist:
        pointer to nvme buffer list.
    :type nblist: struct list_head \*

    :param count:
        number of scsi buffers on the list.
    :type count: int

.. _`lpfc_sli4_post_nvme_sgl_block.description`:

Description
-----------

This routine is invoked to post a block of \ ``count``\  scsi sgl pages from a
SCSI buffer list \ ``nblist``\  to the HBA using non-embedded mailbox command.
No Lock is held.

.. _`lpfc_post_nvme_sgl_list`:

lpfc_post_nvme_sgl_list
=======================

.. c:function:: int lpfc_post_nvme_sgl_list(struct lpfc_hba *phba, struct list_head *post_nblist, int sb_count)

    Post blocks of nvme buffer sgls from a list

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param post_nblist:
        pointer to the nvme buffer list.
    :type post_nblist: struct list_head \*

    :param sb_count:
        *undescribed*
    :type sb_count: int

.. _`lpfc_post_nvme_sgl_list.description`:

Description
-----------

This routine walks a list of nvme buffers that was passed in. It attempts
to construct blocks of nvme buffer sgls which contains contiguous xris and
uses the non-embedded SGL block post mailbox commands to post to the port.
For single NVME buffer sgl with non-contiguous xri, if any, it shall use
embedded SGL post mailbox command for posting. The \ ``post_nblist``\  passed in
must be local list, thus no lock is needed when manipulate the list.

.. _`lpfc_post_nvme_sgl_list.return`:

Return
------

0 = failure, non-zero number of successfully posted buffers.

.. _`lpfc_repost_nvme_sgl_list`:

lpfc_repost_nvme_sgl_list
=========================

.. c:function:: int lpfc_repost_nvme_sgl_list(struct lpfc_hba *phba)

    Repost all the allocated nvme buffer sgls

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_repost_nvme_sgl_list.description`:

Description
-----------

This routine walks the list of nvme buffers that have been allocated and
repost them to the port by using SGL block post. This is needed after a
pci_function_reset/warm_start or start. The lpfc_hba_down_post_s4 routine
is responsible for moving all nvme buffers on the lpfc_abts_nvme_sgl_list
to the lpfc_nvme_buf_list. If the repost fails, reject all nvme buffers.

.. _`lpfc_repost_nvme_sgl_list.return`:

Return
------

0 = success, non-zero failure.

.. _`lpfc_new_nvme_buf`:

lpfc_new_nvme_buf
=================

.. c:function:: int lpfc_new_nvme_buf(struct lpfc_vport *vport, int num_to_alloc)

    Scsi buffer allocator for HBA with SLI4 IF spec

    :param vport:
        The virtual port for which this call being executed.
    :type vport: struct lpfc_vport \*

    :param num_to_alloc:
        *undescribed*
    :type num_to_alloc: int

.. _`lpfc_new_nvme_buf.description`:

Description
-----------

This routine allocates nvme buffers for device with SLI-4 interface spec,
the nvme buffer contains all the necessary information needed to initiate
a NVME I/O. After allocating up to \ ``num_to_allocate``\  NVME buffers and put
them on a list, it post them to the port by using SGL block post.

.. _`lpfc_new_nvme_buf.return-codes`:

Return codes
------------

int - number of nvme buffers that were allocated and posted.
0 = failure, less than num_to_alloc is a partial failure.

.. _`lpfc_get_nvme_buf`:

lpfc_get_nvme_buf
=================

.. c:function:: struct lpfc_nvme_buf *lpfc_get_nvme_buf(struct lpfc_hba *phba, struct lpfc_nodelist *ndlp, int expedite)

    Get a nvme buffer from lpfc_nvme_buf_list of the HBA

    :param phba:
        The HBA for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param ndlp:
        *undescribed*
    :type ndlp: struct lpfc_nodelist \*

    :param expedite:
        *undescribed*
    :type expedite: int

.. _`lpfc_get_nvme_buf.description`:

Description
-----------

This routine removes a nvme buffer from head of \ ``phba``\  lpfc_nvme_buf_list list
and returns to caller.

.. _`lpfc_get_nvme_buf.return-codes`:

Return codes
------------

NULL - Error
Pointer to lpfc_nvme_buf - Success

.. _`lpfc_release_nvme_buf`:

lpfc_release_nvme_buf
=====================

.. c:function:: void lpfc_release_nvme_buf(struct lpfc_hba *phba, struct lpfc_nvme_buf *lpfc_ncmd)

    Return a nvme buffer back to hba nvme buf list.

    :param phba:
        The Hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param lpfc_ncmd:
        The nvme buffer which is being released.
    :type lpfc_ncmd: struct lpfc_nvme_buf \*

.. _`lpfc_release_nvme_buf.description`:

Description
-----------

This routine releases \ ``lpfc_ncmd``\  nvme buffer by adding it to tail of \ ``phba``\ 
lpfc_nvme_buf_list list. For SLI4 XRI's are tied to the nvme buffer
and cannot be reused for at least RA_TOV amount of time if it was
aborted.

.. _`lpfc_nvme_create_localport`:

lpfc_nvme_create_localport
==========================

.. c:function:: int lpfc_nvme_create_localport(struct lpfc_vport *vport)

    Create/Bind an nvme localport instance. \ ``pvport``\  - the lpfc_vport instance requesting a localport.

    :param vport:
        *undescribed*
    :type vport: struct lpfc_vport \*

.. _`lpfc_nvme_create_localport.description`:

Description
-----------

This routine is invoked to create an nvme localport instance to bind
to the nvme_fc_transport.  It is called once during driver load
like lpfc_create_shost after all other services are initialized.
It requires a vport, vpi, and wwns at call time.  Other localport
parameters are modified as the driver's FCID and the Fabric WWN
are established.

Return codes
0 - successful
-ENOMEM - no heap memory available
other values - from nvme registration upcall

.. _`lpfc_nvme_destroy_localport`:

lpfc_nvme_destroy_localport
===========================

.. c:function:: void lpfc_nvme_destroy_localport(struct lpfc_vport *vport)

    Destroy lpfc_nvme bound to nvme transport.

    :param vport:
        *undescribed*
    :type vport: struct lpfc_vport \*

.. _`lpfc_nvme_destroy_localport.description`:

Description
-----------

This routine is invoked to destroy all lports bound to the phba.
The lport memory was allocated by the nvme fc transport and is
released there.  This routine ensures all rports bound to the
lport have been disconnected.

.. _`lpfc_sli4_nvme_xri_aborted`:

lpfc_sli4_nvme_xri_aborted
==========================

.. c:function:: void lpfc_sli4_nvme_xri_aborted(struct lpfc_hba *phba, struct sli4_wcqe_xri_aborted *axri)

    Fast-path process of NVME xri abort

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param axri:
        pointer to the fcp xri abort wcqe structure.
    :type axri: struct sli4_wcqe_xri_aborted \*

.. _`lpfc_sli4_nvme_xri_aborted.description`:

Description
-----------

This routine is invoked by the worker thread to process a SLI4 fast-path
NVME aborted xri.  Aborted NVME IO commands are completed to the transport
here.

.. _`lpfc_nvme_wait_for_io_drain`:

lpfc_nvme_wait_for_io_drain
===========================

.. c:function:: void lpfc_nvme_wait_for_io_drain(struct lpfc_hba *phba)

    Wait for all NVME wqes to complete

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

.. _`lpfc_nvme_wait_for_io_drain.description`:

Description
-----------

This function flushes all wqes in the nvme rings and frees all resources
in the txcmplq. This function does not issue abort wqes for the IO
commands in txcmplq, they will just be returned with
IOERR_SLI_DOWN. This function is invoked with EEH when device's PCI
slot has been permanently disabled.

.. This file was automatic generated / don't edit.

