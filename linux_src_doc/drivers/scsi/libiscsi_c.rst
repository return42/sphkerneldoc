.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/libiscsi.c

.. _`iscsi_prep_data_out_pdu`:

iscsi_prep_data_out_pdu
=======================

.. c:function:: void iscsi_prep_data_out_pdu(struct iscsi_task *task, struct iscsi_r2t_info *r2t, struct iscsi_data *hdr)

    initialize Data-Out

    :param task:
        scsi command task
    :type task: struct iscsi_task \*

    :param r2t:
        R2T info
    :type r2t: struct iscsi_r2t_info \*

    :param hdr:
        iscsi data in pdu
    :type hdr: struct iscsi_data \*

.. _`iscsi_prep_data_out_pdu.notes`:

Notes
-----

     Initialize Data-Out within this R2T sequence and finds
     proper data_offset within this SCSI command.

     This function is called with connection lock taken.

.. _`iscsi_check_tmf_restrictions`:

iscsi_check_tmf_restrictions
============================

.. c:function:: int iscsi_check_tmf_restrictions(struct iscsi_task *task, int opcode)

    check if a task is affected by TMF

    :param task:
        iscsi task
    :type task: struct iscsi_task \*

    :param opcode:
        opcode to check for
    :type opcode: int

.. _`iscsi_check_tmf_restrictions.description`:

Description
-----------

During TMF a task has to be checked if it's affected.
All unrelated I/O can be passed through, but I/O to the
affected LUN should be restricted.
If 'fast_abort' is set we won't be sending any I/O to the
affected LUN.
Otherwise the target is waiting for all TTTs to be completed,
so we have to send all outstanding Data-Out PDUs to the target.

.. _`iscsi_prep_scsi_cmd_pdu`:

iscsi_prep_scsi_cmd_pdu
=======================

.. c:function:: int iscsi_prep_scsi_cmd_pdu(struct iscsi_task *task)

    prep iscsi scsi cmd pdu

    :param task:
        iscsi task
    :type task: struct iscsi_task \*

.. _`iscsi_prep_scsi_cmd_pdu.description`:

Description
-----------

Prep basic iSCSI PDU fields for a scsi cmd pdu. The LLD should set
fields like dlength or final based on how much data it sends

.. _`iscsi_free_task`:

iscsi_free_task
===============

.. c:function:: void iscsi_free_task(struct iscsi_task *task)

    free a task

    :param task:
        iscsi cmd task
    :type task: struct iscsi_task \*

.. _`iscsi_free_task.description`:

Description
-----------

Must be called with session back_lock.
This function returns the scsi command to scsi-ml or cleans
up mgmt tasks then returns the task to the pool.

.. _`iscsi_complete_task`:

iscsi_complete_task
===================

.. c:function:: void iscsi_complete_task(struct iscsi_task *task, int state)

    finish a task

    :param task:
        iscsi cmd task
    :type task: struct iscsi_task \*

    :param state:
        state to complete task with
    :type state: int

.. _`iscsi_complete_task.description`:

Description
-----------

Must be called with session back_lock.

.. _`iscsi_complete_scsi_task`:

iscsi_complete_scsi_task
========================

.. c:function:: void iscsi_complete_scsi_task(struct iscsi_task *task, uint32_t exp_cmdsn, uint32_t max_cmdsn)

    finish scsi task normally

    :param task:
        iscsi task for scsi cmd
    :type task: struct iscsi_task \*

    :param exp_cmdsn:
        expected cmd sn in cpu format
    :type exp_cmdsn: uint32_t

    :param max_cmdsn:
        max cmd sn in cpu format
    :type max_cmdsn: uint32_t

.. _`iscsi_complete_scsi_task.description`:

Description
-----------

This is used when drivers do not need or cannot perform
lower level pdu processing.

Called with session back_lock

.. _`iscsi_scsi_cmd_rsp`:

iscsi_scsi_cmd_rsp
==================

.. c:function:: void iscsi_scsi_cmd_rsp(struct iscsi_conn *conn, struct iscsi_hdr *hdr, struct iscsi_task *task, char *data, int datalen)

    SCSI Command Response processing

    :param conn:
        iscsi connection
    :type conn: struct iscsi_conn \*

    :param hdr:
        iscsi header
    :type hdr: struct iscsi_hdr \*

    :param task:
        scsi command task
    :type task: struct iscsi_task \*

    :param data:
        cmd data buffer
    :type data: char \*

    :param datalen:
        len of buffer
    :type datalen: int

.. _`iscsi_scsi_cmd_rsp.description`:

Description
-----------

iscsi_cmd_rsp sets up the scsi_cmnd fields based on the PDU and
then completes the command and task.

.. _`iscsi_data_in_rsp`:

iscsi_data_in_rsp
=================

.. c:function:: void iscsi_data_in_rsp(struct iscsi_conn *conn, struct iscsi_hdr *hdr, struct iscsi_task *task)

    SCSI Data-In Response processing

    :param conn:
        iscsi connection
    :type conn: struct iscsi_conn \*

    :param hdr:
        iscsi pdu
    :type hdr: struct iscsi_hdr \*

    :param task:
        scsi command task
    :type task: struct iscsi_task \*

.. _`iscsi_itt_to_task`:

iscsi_itt_to_task
=================

.. c:function:: struct iscsi_task *iscsi_itt_to_task(struct iscsi_conn *conn, itt_t itt)

    look up task by itt

    :param conn:
        iscsi connection
    :type conn: struct iscsi_conn \*

    :param itt:
        itt
    :type itt: itt_t

.. _`iscsi_itt_to_task.description`:

Description
-----------

This should be used for mgmt tasks like login and nops, or if
the LDD's itt space does not include the session age.

The session back_lock must be held.

.. _`__iscsi_complete_pdu`:

__iscsi_complete_pdu
====================

.. c:function:: int __iscsi_complete_pdu(struct iscsi_conn *conn, struct iscsi_hdr *hdr, char *data, int datalen)

    complete pdu

    :param conn:
        iscsi conn
    :type conn: struct iscsi_conn \*

    :param hdr:
        iscsi header
    :type hdr: struct iscsi_hdr \*

    :param data:
        data buffer
    :type data: char \*

    :param datalen:
        len of data buffer
    :type datalen: int

.. _`__iscsi_complete_pdu.description`:

Description
-----------

Completes pdu processing by freeing any resources allocated at
queuecommand or send generic. session back_lock must be held and verify
itt must have been called.

.. _`iscsi_itt_to_ctask`:

iscsi_itt_to_ctask
==================

.. c:function:: struct iscsi_task *iscsi_itt_to_ctask(struct iscsi_conn *conn, itt_t itt)

    look up ctask by itt

    :param conn:
        iscsi connection
    :type conn: struct iscsi_conn \*

    :param itt:
        itt
    :type itt: itt_t

.. _`iscsi_itt_to_ctask.description`:

Description
-----------

This should be used for cmd tasks.

The session back_lock must be held.

.. _`iscsi_requeue_task`:

iscsi_requeue_task
==================

.. c:function:: void iscsi_requeue_task(struct iscsi_task *task)

    requeue task to run from session workqueue

    :param task:
        task to requeue
    :type task: struct iscsi_task \*

.. _`iscsi_requeue_task.description`:

Description
-----------

LLDs that need to run a task from the session workqueue should call
this. The session frwd_lock must be held. This should only be called
by software drivers.

.. _`iscsi_data_xmit`:

iscsi_data_xmit
===============

.. c:function:: int iscsi_data_xmit(struct iscsi_conn *conn)

    xmit any command into the scheduled connection

    :param conn:
        iscsi connection
    :type conn: struct iscsi_conn \*

.. _`iscsi_data_xmit.notes`:

Notes
-----

     The function can return -EAGAIN in which case the caller must
     re-schedule it again later or recover. '0' return code means
     successful xmit.

.. _`iscsi_suspend_queue`:

iscsi_suspend_queue
===================

.. c:function:: void iscsi_suspend_queue(struct iscsi_conn *conn)

    suspend iscsi_queuecommand

    :param conn:
        iscsi conn to stop queueing IO on
    :type conn: struct iscsi_conn \*

.. _`iscsi_suspend_queue.description`:

Description
-----------

This grabs the session frwd_lock to make sure no one is in
xmit_task/queuecommand, and then sets suspend to prevent
new commands from being queued. This only needs to be called
by offload drivers that need to sync a path like ep disconnect
with the iscsi_queuecommand/xmit_task. To start IO again libiscsi
will call iscsi_start_tx and iscsi_unblock_session when in FFP.

.. _`iscsi_suspend_tx`:

iscsi_suspend_tx
================

.. c:function:: void iscsi_suspend_tx(struct iscsi_conn *conn)

    suspend iscsi_data_xmit

    :param conn:
        iscsi conn tp stop processing IO on.
    :type conn: struct iscsi_conn \*

.. _`iscsi_suspend_tx.description`:

Description
-----------

This function sets the suspend bit to prevent iscsi_data_xmit
from sending new IO, and if work is queued on the xmit thread
it will wait for it to be completed.

.. _`iscsi_eh_session_reset`:

iscsi_eh_session_reset
======================

.. c:function:: int iscsi_eh_session_reset(struct scsi_cmnd *sc)

    drop session and attempt relogin

    :param sc:
        scsi command
    :type sc: struct scsi_cmnd \*

.. _`iscsi_eh_session_reset.description`:

Description
-----------

This function will wait for a relogin, session termination from
userspace, or a recovery/replacement timeout.

.. _`iscsi_eh_target_reset`:

iscsi_eh_target_reset
=====================

.. c:function:: int iscsi_eh_target_reset(struct scsi_cmnd *sc)

    reset target

    :param sc:
        scsi command
    :type sc: struct scsi_cmnd \*

.. _`iscsi_eh_target_reset.description`:

Description
-----------

This will attempt to send a warm target reset.

.. _`iscsi_eh_recover_target`:

iscsi_eh_recover_target
=======================

.. c:function:: int iscsi_eh_recover_target(struct scsi_cmnd *sc)

    reset target and possibly the session

    :param sc:
        scsi command
    :type sc: struct scsi_cmnd \*

.. _`iscsi_eh_recover_target.description`:

Description
-----------

This will attempt to send a warm target reset. If that fails,
we will escalate to ERL0 session recovery.

.. _`iscsi_host_add`:

iscsi_host_add
==============

.. c:function:: int iscsi_host_add(struct Scsi_Host *shost, struct device *pdev)

    add host to system

    :param shost:
        scsi host
    :type shost: struct Scsi_Host \*

    :param pdev:
        parent device
    :type pdev: struct device \*

.. _`iscsi_host_add.description`:

Description
-----------

This should be called by partial offload and software iscsi drivers
to add a host to the system.

.. _`iscsi_host_alloc`:

iscsi_host_alloc
================

.. c:function:: struct Scsi_Host *iscsi_host_alloc(struct scsi_host_template *sht, int dd_data_size, bool xmit_can_sleep)

    allocate a host and driver data

    :param sht:
        scsi host template
    :type sht: struct scsi_host_template \*

    :param dd_data_size:
        driver host data size
    :type dd_data_size: int

    :param xmit_can_sleep:
        bool indicating if LLD will queue IO from a work queue
    :type xmit_can_sleep: bool

.. _`iscsi_host_alloc.description`:

Description
-----------

This should be called by partial offload and software iscsi drivers.
To access the driver specific memory use the \ :c:func:`iscsi_host_priv`\  macro.

.. _`iscsi_host_remove`:

iscsi_host_remove
=================

.. c:function:: void iscsi_host_remove(struct Scsi_Host *shost)

    remove host and sessions

    :param shost:
        scsi host
    :type shost: struct Scsi_Host \*

.. _`iscsi_host_remove.description`:

Description
-----------

If there are any sessions left, this will initiate the removal and wait
for the completion.

.. _`iscsi_session_setup`:

iscsi_session_setup
===================

.. c:function:: struct iscsi_cls_session *iscsi_session_setup(struct iscsi_transport *iscsit, struct Scsi_Host *shost, uint16_t cmds_max, int dd_size, int cmd_task_size, uint32_t initial_cmdsn, unsigned int id)

    create iscsi cls session and host and session

    :param iscsit:
        iscsi transport template
    :type iscsit: struct iscsi_transport \*

    :param shost:
        scsi host
    :type shost: struct Scsi_Host \*

    :param cmds_max:
        session can queue
    :type cmds_max: uint16_t

    :param dd_size:
        private driver data size, added to session allocation size
    :type dd_size: int

    :param cmd_task_size:
        LLD task private data size
    :type cmd_task_size: int

    :param initial_cmdsn:
        initial CmdSN
    :type initial_cmdsn: uint32_t

    :param id:
        target ID to add to this session
    :type id: unsigned int

.. _`iscsi_session_setup.description`:

Description
-----------

This can be used by software iscsi_transports that allocate
a session per scsi host.

Callers should set cmds_max to the largest total numer (mgmt + scsi) of
tasks they support. The iscsi layer reserves ISCSI_MGMT_CMDS_MAX tasks
for nop handling and login/logout requests.

.. _`iscsi_session_teardown`:

iscsi_session_teardown
======================

.. c:function:: void iscsi_session_teardown(struct iscsi_cls_session *cls_session)

    destroy session, host, and cls_session

    :param cls_session:
        iscsi session
    :type cls_session: struct iscsi_cls_session \*

.. _`iscsi_conn_setup`:

iscsi_conn_setup
================

.. c:function:: struct iscsi_cls_conn *iscsi_conn_setup(struct iscsi_cls_session *cls_session, int dd_size, uint32_t conn_idx)

    create iscsi_cls_conn and iscsi_conn

    :param cls_session:
        iscsi_cls_session
    :type cls_session: struct iscsi_cls_session \*

    :param dd_size:
        private driver data size
    :type dd_size: int

    :param conn_idx:
        cid
    :type conn_idx: uint32_t

.. _`iscsi_conn_teardown`:

iscsi_conn_teardown
===================

.. c:function:: void iscsi_conn_teardown(struct iscsi_cls_conn *cls_conn)

    teardown iscsi connection

    :param cls_conn:
        iscsi class connection
    :type cls_conn: struct iscsi_cls_conn \*

.. _`iscsi_conn_teardown.description`:

Description
-----------

TODO: we may need to make this into a two step process
like scsi-mls remove + put host

.. This file was automatic generated / don't edit.

