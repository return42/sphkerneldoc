.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/be2iscsi/be_main.c

.. _`beiscsi_get_params`:

beiscsi_get_params
==================

.. c:function:: void beiscsi_get_params(struct beiscsi_hba *phba)

    Set the config paramters

    :param phba:
        ptr  device priv structure
    :type phba: struct beiscsi_hba \*

.. _`be_isr_mcc`:

be_isr_mcc
==========

.. c:function:: irqreturn_t be_isr_mcc(int irq, void *dev_id)

    The isr routine of the driver.

    :param irq:
        Not used
    :type irq: int

    :param dev_id:
        Pointer to host adapter structure
    :type dev_id: void \*

.. _`be_isr_msix`:

be_isr_msix
===========

.. c:function:: irqreturn_t be_isr_msix(int irq, void *dev_id)

    The isr routine of the driver.

    :param irq:
        Not used
    :type irq: int

    :param dev_id:
        Pointer to host adapter structure
    :type dev_id: void \*

.. _`be_isr`:

be_isr
======

.. c:function:: irqreturn_t be_isr(int irq, void *dev_id)

    The isr routine of the driver.

    :param irq:
        Not used
    :type irq: int

    :param dev_id:
        Pointer to host adapter structure
    :type dev_id: void \*

.. _`alloc_wrb_handle`:

alloc_wrb_handle
================

.. c:function:: struct wrb_handle *alloc_wrb_handle(struct beiscsi_hba *phba, unsigned int cid, struct hwi_wrb_context **pcontext)

    To allocate a wrb handle

    :param phba:
        The hba pointer
    :type phba: struct beiscsi_hba \*

    :param cid:
        The cid to use for allocation
    :type cid: unsigned int

    :param pcontext:
        *undescribed*
    :type pcontext: struct hwi_wrb_context \*\*

.. _`alloc_wrb_handle.description`:

Description
-----------

This happens under session_lock until submission to chip

.. _`free_wrb_handle`:

free_wrb_handle
===============

.. c:function:: void free_wrb_handle(struct beiscsi_hba *phba, struct hwi_wrb_context *pwrb_context, struct wrb_handle *pwrb_handle)

    To free the wrb handle back to pool

    :param phba:
        The hba pointer
    :type phba: struct beiscsi_hba \*

    :param pwrb_context:
        The context to free from
    :type pwrb_context: struct hwi_wrb_context \*

    :param pwrb_handle:
        The wrb_handle to free
    :type pwrb_handle: struct wrb_handle \*

.. _`free_wrb_handle.description`:

Description
-----------

This happens under session_lock until submission to chip

.. _`beiscsi_complete_pdu`:

beiscsi_complete_pdu
====================

.. c:function:: unsigned int beiscsi_complete_pdu(struct beiscsi_conn *beiscsi_conn, struct pdu_base *phdr, void *pdata, unsigned int dlen)

    a. Unsolicited NOP-In (target initiated NOP-In) b. ASYNC Messages c. Reject PDU d. Login response These headers arrive unprocessed by the EP firmware. iSCSI layer processes them.

    :param beiscsi_conn:
        *undescribed*
    :type beiscsi_conn: struct beiscsi_conn \*

    :param phdr:
        *undescribed*
    :type phdr: struct pdu_base \*

    :param pdata:
        *undescribed*
    :type pdata: void \*

    :param dlen:
        *undescribed*
    :type dlen: unsigned int

.. _`beiscsi_process_cq`:

beiscsi_process_cq
==================

.. c:function:: unsigned int beiscsi_process_cq(struct be_eq_obj *pbe_eq, int budget)

    Process the Completion Queue

    :param pbe_eq:
        Event Q on which the Completion has come
    :type pbe_eq: struct be_eq_obj \*

    :param budget:
        Max number of events to processed
    :type budget: int

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

    :param pwrb:
        ptr to the WRB entry
    :type pwrb: struct iscsi_wrb \*

    :param task:
        iscsi task which is to be executed
    :type task: struct iscsi_task \*

.. _`beiscsi_find_mem_req`:

beiscsi_find_mem_req
====================

.. c:function:: void beiscsi_find_mem_req(struct beiscsi_hba *phba)

    Find mem needed

    :param phba:
        ptr to HBA struct
    :type phba: struct beiscsi_hba \*

.. _`beiscsi_free_mgmt_task_handles`:

beiscsi_free_mgmt_task_handles
==============================

.. c:function:: void beiscsi_free_mgmt_task_handles(struct beiscsi_conn *beiscsi_conn, struct iscsi_task *task)

    Free driver CXN resources

    :param beiscsi_conn:
        ptr to the conn to be cleaned up
    :type beiscsi_conn: struct beiscsi_conn \*

    :param task:
        ptr to iscsi_task resource to be freed.
    :type task: struct iscsi_task \*

.. _`beiscsi_free_mgmt_task_handles.description`:

Description
-----------

Free driver mgmt resources binded to CXN.

.. _`beiscsi_cleanup_task`:

beiscsi_cleanup_task
====================

.. c:function:: void beiscsi_cleanup_task(struct iscsi_task *task)

    Free driver resources of the task

    :param task:
        ptr to the iscsi task
    :type task: struct iscsi_task \*

.. _`beiscsi_alloc_pdu`:

beiscsi_alloc_pdu
=================

.. c:function:: int beiscsi_alloc_pdu(struct iscsi_task *task, uint8_t opcode)

    allocates pdu and related resources

    :param task:
        libiscsi task
    :type task: struct iscsi_task \*

    :param opcode:
        opcode of pdu for task
    :type opcode: uint8_t

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

    :param job:
        job to handle
    :type job: struct bsg_job \*

.. _`beiscsi_sysfs_iscsi_boot_flags`:

BEISCSI_SYSFS_ISCSI_BOOT_FLAGS
==============================

.. c:function::  BEISCSI_SYSFS_ISCSI_BOOT_FLAGS()

    utilities Bit 0 Block valid flag Bit 1 Firmware booting selected

.. This file was automatic generated / don't edit.

