.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/lpfc/lpfc_ct.c

.. _`lpfc_ct_handle_unsol_abort`:

lpfc_ct_handle_unsol_abort
==========================

.. c:function:: int lpfc_ct_handle_unsol_abort(struct lpfc_hba *phba, struct hbq_dmabuf *dmabuf)

    ct upper level protocol abort handler

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct hbq_dmabuf \*dmabuf:
        pointer to a dmabuf that describes the FC sequence

.. _`lpfc_ct_handle_unsol_abort.description`:

Description
-----------

This function serves as the upper level protocol abort handler for CT
protocol.

Return 1 if abort has been handled, 0 otherwise.

.. _`lpfc_gen_req`:

lpfc_gen_req
============

.. c:function:: int lpfc_gen_req(struct lpfc_vport *vport, struct lpfc_dmabuf *bmp, struct lpfc_dmabuf *inp, struct lpfc_dmabuf *outp, void (*cmpl)(struct lpfc_hba *, struct lpfc_iocbq *, struct lpfc_iocbq *), struct lpfc_nodelist *ndlp, uint32_t usr_flg, uint32_t num_entry, uint32_t tmo, uint8_t retry)

    Build and issue a GEN_REQUEST command  to the SLI Layer

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_dmabuf \*bmp:
        Pointer to BPL for SLI command

    :param struct lpfc_dmabuf \*inp:
        Pointer to data buffer for response data.

    :param struct lpfc_dmabuf \*outp:
        Pointer to data buffer that hold the CT command.

    :param void (\*cmpl)(struct lpfc_hba \*, struct lpfc_iocbq \*, struct lpfc_iocbq \*):
        completion routine to call when command completes

    :param struct lpfc_nodelist \*ndlp:
        Destination NPort nodelist entry

    :param uint32_t usr_flg:
        *undescribed*

    :param uint32_t num_entry:
        *undescribed*

    :param uint32_t tmo:
        *undescribed*

    :param uint8_t retry:
        *undescribed*

.. _`lpfc_gen_req.description`:

Description
-----------

This function as the final part for issuing a CT command.

.. _`lpfc_ct_cmd`:

lpfc_ct_cmd
===========

.. c:function:: int lpfc_ct_cmd(struct lpfc_vport *vport, struct lpfc_dmabuf *inmp, struct lpfc_dmabuf *bmp, struct lpfc_nodelist *ndlp, void (*cmpl)(struct lpfc_hba *, struct lpfc_iocbq *, struct lpfc_iocbq *), uint32_t rsp_size, uint8_t retry)

    Build and issue a CT command

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_dmabuf \*inmp:
        Pointer to data buffer for response data.

    :param struct lpfc_dmabuf \*bmp:
        Pointer to BPL for SLI command

    :param struct lpfc_nodelist \*ndlp:
        Destination NPort nodelist entry

    :param void (\*cmpl)(struct lpfc_hba \*, struct lpfc_iocbq \*, struct lpfc_iocbq \*):
        completion routine to call when command completes

    :param uint32_t rsp_size:
        *undescribed*

    :param uint8_t retry:
        *undescribed*

.. _`lpfc_ct_cmd.description`:

Description
-----------

This function is called for issuing a CT command.

.. _`lpfc_cmpl_ct_disc_fdmi`:

lpfc_cmpl_ct_disc_fdmi
======================

.. c:function:: void lpfc_cmpl_ct_disc_fdmi(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocb, struct lpfc_iocbq *rspiocb)

    Handle a discovery FDMI completion

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param struct lpfc_iocbq \*cmdiocb:
        Pointer to the command IOCBQ.

    :param struct lpfc_iocbq \*rspiocb:
        Pointer to the response IOCBQ.

.. _`lpfc_cmpl_ct_disc_fdmi.description`:

Description
-----------

This function to handle the completion of a driver initiated FDMI
CT command issued during discovery.

.. _`lpfc_fdmi_num_disc_check`:

lpfc_fdmi_num_disc_check
========================

.. c:function:: void lpfc_fdmi_num_disc_check(struct lpfc_vport *vport)

    Check how many mapped NPorts we are connected to

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

.. _`lpfc_fdmi_num_disc_check.description`:

Description
-----------

Called from hbeat timeout routine to check if the number of discovered
ports has changed. If so, re-register thar port Attribute.

.. _`lpfc_fdmi_cmd`:

lpfc_fdmi_cmd
=============

.. c:function:: int lpfc_fdmi_cmd(struct lpfc_vport *vport, struct lpfc_nodelist *ndlp, int cmdcode, uint32_t new_mask)

    Build and send a FDMI cmd to the specified NPort

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_nodelist \*ndlp:
        ndlp to send FDMI cmd to (if NULL use FDMI_DID)

    :param int cmdcode:
        *undescribed*

    :param uint32_t new_mask:
        *undescribed*

.. _`lpfc_fdmi_cmd.cmdcode`:

cmdcode
-------

FDMI command to send

.. _`lpfc_fdmi_cmd.mask`:

mask
----

Mask of HBA or PORT Attributes to send

Builds and sends a FDMI command using the CT subsystem.

.. _`lpfc_delayed_disc_tmo`:

lpfc_delayed_disc_tmo
=====================

.. c:function:: void lpfc_delayed_disc_tmo(struct timer_list *t)

    Timeout handler for delayed discovery timer. \ ``ptr``\  - Context object of the timer.

    :param struct timer_list \*t:
        *undescribed*

.. _`lpfc_delayed_disc_tmo.description`:

Description
-----------

This function set the WORKER_DELAYED_DISC_TMO flag and wake up
the worker thread.

.. _`lpfc_delayed_disc_timeout_handler`:

lpfc_delayed_disc_timeout_handler
=================================

.. c:function:: void lpfc_delayed_disc_timeout_handler(struct lpfc_vport *vport)

    Function called by worker thread to handle delayed discovery.

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

.. _`lpfc_delayed_disc_timeout_handler.description`:

Description
-----------

This function start nport discovery of the vport.

.. This file was automatic generated / don't edit.

