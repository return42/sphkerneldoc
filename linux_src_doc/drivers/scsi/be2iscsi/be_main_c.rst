.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/be2iscsi/be_main.c

.. _`beiscsi_get_params`:

beiscsi_get_params
==================

.. c:function:: void beiscsi_get_params(struct beiscsi_hba *phba)

    Set the config paramters

    :param struct beiscsi_hba \*phba:
        ptr  device priv structure

.. _`be_isr_mcc`:

be_isr_mcc
==========

.. c:function:: irqreturn_t be_isr_mcc(int irq, void *dev_id)

    The isr routine of the driver.

    :param int irq:
        Not used

    :param void \*dev_id:
        Pointer to host adapter structure

.. _`be_isr_msix`:

be_isr_msix
===========

.. c:function:: irqreturn_t be_isr_msix(int irq, void *dev_id)

    The isr routine of the driver.

    :param int irq:
        Not used

    :param void \*dev_id:
        Pointer to host adapter structure

.. _`be_isr`:

be_isr
======

.. c:function:: irqreturn_t be_isr(int irq, void *dev_id)

    The isr routine of the driver.

    :param int irq:
        Not used

    :param void \*dev_id:
        Pointer to host adapter structure

.. _`alloc_wrb_handle`:

alloc_wrb_handle
================

.. c:function:: struct wrb_handle *alloc_wrb_handle(struct beiscsi_hba *phba, unsigned int cid, struct hwi_wrb_context **pcontext)

    To allocate a wrb handle

    :param struct beiscsi_hba \*phba:
        The hba pointer

    :param unsigned int cid:
        The cid to use for allocation

    :param struct hwi_wrb_context \*\*pcontext:
        *undescribed*

.. _`alloc_wrb_handle.description`:

Description
-----------

This happens under session_lock until submission to chip

.. _`free_wrb_handle`:

free_wrb_handle
===============

.. c:function:: void free_wrb_handle(struct beiscsi_hba *phba, struct hwi_wrb_context *pwrb_context, struct wrb_handle *pwrb_handle)

    To free the wrb handle back to pool

    :param struct beiscsi_hba \*phba:
        The hba pointer

    :param struct hwi_wrb_context \*pwrb_context:
        The context to free from

    :param struct wrb_handle \*pwrb_handle:
        The wrb_handle to free

.. _`free_wrb_handle.description`:

Description
-----------

This happens under session_lock until submission to chip

.. _`beiscsi_complete_pdu`:

beiscsi_complete_pdu
====================

.. c:function:: unsigned int beiscsi_complete_pdu(struct beiscsi_conn *beiscsi_conn, struct pdu_base *phdr, void *pdata, unsigned int dlen)

    a. Unsolicited NOP-In (target initiated NOP-In) b. ASYNC Messages c. Reject PDU d. Login response These headers arrive unprocessed by the EP firmware. iSCSI layer processes them.

    :param struct beiscsi_conn \*beiscsi_conn:
        *undescribed*

    :param struct pdu_base \*phdr:
        *undescribed*

    :param void \*pdata:
        *undescribed*

    :param unsigned int dlen:
        *undescribed*

.. _`beiscsi_process_cq`:

beiscsi_process_cq
==================

.. c:function:: unsigned int beiscsi_process_cq(struct be_eq_obj *pbe_eq, int budget)

    Process the Completion Queue

    :param struct be_eq_obj \*pbe_eq:
        Event Q on which the Completion has come

    :param int budget:
        Max number of events to processed

.. _`beiscsi_process_cq.description`:

Description
-----------

return
Number of Completion Entries processed.

.. _`hwi_write_buffer`:

hwi_write_buffer
================

.. c:function:: int hwi_write_buffer(struct iscsi_wrb *pwrb, struct iscsi_task *task)

    Populate the WRB with task info

    :param struct iscsi_wrb \*pwrb:
        ptr to the WRB entry

    :param struct iscsi_task \*task:
        iscsi task which is to be executed

.. _`beiscsi_find_mem_req`:

beiscsi_find_mem_req
====================

.. c:function:: void beiscsi_find_mem_req(struct beiscsi_hba *phba)

    Find mem needed

    :param struct beiscsi_hba \*phba:
        ptr to HBA struct

.. _`beiscsi_free_mgmt_task_handles`:

beiscsi_free_mgmt_task_handles
==============================

.. c:function:: void beiscsi_free_mgmt_task_handles(struct beiscsi_conn *beiscsi_conn, struct iscsi_task *task)

    Free driver CXN resources

    :param struct beiscsi_conn \*beiscsi_conn:
        ptr to the conn to be cleaned up

    :param struct iscsi_task \*task:
        ptr to iscsi_task resource to be freed.

.. _`beiscsi_free_mgmt_task_handles.description`:

Description
-----------

Free driver mgmt resources binded to CXN.

.. _`beiscsi_cleanup_task`:

beiscsi_cleanup_task
====================

.. c:function:: void beiscsi_cleanup_task(struct iscsi_task *task)

    Free driver resources of the task

    :param struct iscsi_task \*task:
        ptr to the iscsi task

.. _`beiscsi_alloc_pdu`:

beiscsi_alloc_pdu
=================

.. c:function:: int beiscsi_alloc_pdu(struct iscsi_task *task, uint8_t opcode)

    allocates pdu and related resources

    :param struct iscsi_task \*task:
        libiscsi task

    :param uint8_t opcode:
        opcode of pdu for task

.. _`beiscsi_alloc_pdu.description`:

Description
-----------

This is called with the session lock held. It will allocate
the wrb and sgl if needed for the command. And it will prep
the pdu's itt. beiscsi_parse_pdu will later translate
the pdu itt to the libiscsi task itt.

.. _`beiscsi_bsg_request`:

beiscsi_bsg_request
===================

.. c:function:: int beiscsi_bsg_request(struct bsg_job *job)

    handle bsg request from ISCSI transport

    :param struct bsg_job \*job:
        job to handle

.. This file was automatic generated / don't edit.

