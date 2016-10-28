.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aic94xx/aic94xx_tmf.c

.. _`asd_abort_task`:

asd_abort_task
==============

.. c:function:: int asd_abort_task(struct sas_task *task)

    - ABORT TASK TMF

    :param struct sas_task \*task:
        the task to be aborted

.. _`asd_abort_task.description`:

Description
-----------

Before calling ABORT TASK the task state flags should be ORed with
SAS_TASK_STATE_ABORTED (unless SAS_TASK_STATE_DONE is set) under
the task_state_lock IRQ spinlock, then ABORT TASK \*must\* be called.

Implements the ABORT TASK TMF, I_T_L_Q nexus.

.. _`asd_abort_task.return`:

Return
------

SAS TMF responses (see sas_task.h),
-ENOMEM,
-SAS_QUEUE_FULL.

When ABORT TASK returns, the caller of ABORT TASK checks first the
task->task_state_flags, and then the return value of ABORT TASK.

If the task has task state bit SAS_TASK_STATE_DONE set, then the
task was completed successfully prior to it being aborted.  The
caller of ABORT TASK has responsibility to call task->\ :c:func:`task_done`\ 
xor free the task, depending on their framework.  The return code
is TMF_RESP_FUNC_FAILED in this case.

Else the SAS_TASK_STATE_DONE bit is not set,
If the return code is TMF_RESP_FUNC_COMPLETE, then
the task was aborted successfully.  The caller of
ABORT TASK has responsibility to call task->\ :c:func:`task_done`\ 
to finish the task, xor free the task depending on their
framework.
else
the ABORT TASK returned some kind of error. The task
was \_not\_ cancelled.  Nothing can be assumed.
The caller of ABORT TASK may wish to retry.

.. _`asd_initiate_ssp_tmf`:

asd_initiate_ssp_tmf
====================

.. c:function:: int asd_initiate_ssp_tmf(struct domain_device *dev, u8 *lun, int tmf, int index)

    - send a TMF to an I_T_L or I_T_L_Q nexus

    :param struct domain_device \*dev:
        pointer to struct domain_device of interest

    :param u8 \*lun:
        pointer to u8[8] which is the LUN

    :param int tmf:
        the TMF to be performed (see sas_task.h or the SAS spec)

    :param int index:
        the transaction context of the task to be queried if QT TMF

.. _`asd_initiate_ssp_tmf.description`:

Description
-----------

This function is used to send ABORT TASK SET, CLEAR ACA,
CLEAR TASK SET, LU RESET and QUERY TASK TMFs.

No SCBs should be queued to the I_T_L nexus when this SCB is
pending.

.. _`asd_initiate_ssp_tmf.return`:

Return
------

TMF response code (see sas_task.h or the SAS spec)

.. _`asd_query_task`:

asd_query_task
==============

.. c:function:: int asd_query_task(struct sas_task *task)

    - send a QUERY TASK TMF to an I_T_L_Q nexus

    :param struct sas_task \*task:
        *undescribed*

.. _`asd_query_task.task`:

task
----

pointer to sas_task struct of interest

.. _`asd_query_task.return`:

Return
------

TMF_RESP_FUNC_COMPLETE if the task is not in the task set,
or TMF_RESP_FUNC_SUCC if the task is in the task set.

Normally the management layer sets the task to aborted state,
and then calls query task and then abort task.

.. This file was automatic generated / don't edit.

