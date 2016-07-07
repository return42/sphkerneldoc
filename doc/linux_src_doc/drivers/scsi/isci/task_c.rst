.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/task.c

.. _`isci_task_refuse`:

isci_task_refuse
================

.. c:function:: void isci_task_refuse(struct isci_host *ihost, struct sas_task *task, enum service_response response, enum exec_status status)

    complete the request to the upper layer driver in the case where an I/O needs to be completed back in the submit path.

    :param struct isci_host \*ihost:
        host on which the the request was queued

    :param struct sas_task \*task:
        request to complete

    :param enum service_response response:
        response code for the completed task.

    :param enum exec_status status:
        status code for the completed task.

.. _`isci_task_execute_task`:

isci_task_execute_task
======================

.. c:function:: int isci_task_execute_task(struct sas_task *task, gfp_t gfp_flags)

    This function is one of the SAS Domain Template functions. This function is called by libsas to send a task down to hardware.

    :param struct sas_task \*task:
        This parameter specifies the SAS task to send.

    :param gfp_t gfp_flags:
        This parameter specifies the context of this call.

.. _`isci_task_execute_task.description`:

Description
-----------

status, zero indicates success.

.. _`isci_task_send_lu_reset_sas`:

isci_task_send_lu_reset_sas
===========================

.. c:function:: int isci_task_send_lu_reset_sas(struct isci_host *isci_host, struct isci_remote_device *isci_device, u8 *lun)

    This function is called by of the SAS Domain Template functions.

    :param struct isci_host \*isci_host:
        *undescribed*

    :param struct isci_remote_device \*isci_device:
        *undescribed*

    :param u8 \*lun:
        This parameter specifies the lun to be reset.

.. _`isci_task_send_lu_reset_sas.description`:

Description
-----------

status, zero indicates success.

.. _`isci_task_abort_task`:

isci_task_abort_task
====================

.. c:function:: int isci_task_abort_task(struct sas_task *task)

    This function is one of the SAS Domain Template functions. This function is called by libsas to abort a specified task.

    :param struct sas_task \*task:
        This parameter specifies the SAS task to abort.

.. _`isci_task_abort_task.description`:

Description
-----------

status, zero indicates success.

.. _`isci_task_abort_task_set`:

isci_task_abort_task_set
========================

.. c:function:: int isci_task_abort_task_set(struct domain_device *d_device, u8 *lun)

    This function is one of the SAS Domain Template functions. This is one of the Task Management functoins called by libsas, to abort all task for the given lun.

    :param struct domain_device \*d_device:
        This parameter specifies the domain device associated with this
        request.

    :param u8 \*lun:
        This parameter specifies the lun associated with this request.

.. _`isci_task_abort_task_set.description`:

Description
-----------

status, zero indicates success.

.. _`isci_task_clear_aca`:

isci_task_clear_aca
===================

.. c:function:: int isci_task_clear_aca(struct domain_device *d_device, u8 *lun)

    This function is one of the SAS Domain Template functions. This is one of the Task Management functoins called by libsas.

    :param struct domain_device \*d_device:
        This parameter specifies the domain device associated with this
        request.

    :param u8 \*lun:
        This parameter specifies the lun        associated with this request.

.. _`isci_task_clear_aca.description`:

Description
-----------

status, zero indicates success.

.. _`isci_task_clear_task_set`:

isci_task_clear_task_set
========================

.. c:function:: int isci_task_clear_task_set(struct domain_device *d_device, u8 *lun)

    This function is one of the SAS Domain Template functions. This is one of the Task Management functoins called by libsas.

    :param struct domain_device \*d_device:
        This parameter specifies the domain device associated with this
        request.

    :param u8 \*lun:
        This parameter specifies the lun        associated with this request.

.. _`isci_task_clear_task_set.description`:

Description
-----------

status, zero indicates success.

.. _`isci_task_query_task`:

isci_task_query_task
====================

.. c:function:: int isci_task_query_task(struct sas_task *task)

    This function is implemented to cause libsas to correctly escalate the failed abort to a LUN or target reset (this is because sas_scsi_find_task libsas function does not correctly interpret all return codes from the abort task call).  When TMF_RESP_FUNC_SUCC is returned, libsas turns this into a LUN reset; when FUNC_FAILED is returned, libsas will turn this into a target reset

    :param struct sas_task \*task:
        This parameter specifies the sas task being queried.

.. _`isci_task_query_task.description`:

Description
-----------

status, zero indicates success.

.. This file was automatic generated / don't edit.

