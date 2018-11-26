.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/request.c

.. _`scu_ssp_request_construct_task_context`:

scu_ssp_request_construct_task_context
======================================

.. c:function:: void scu_ssp_request_construct_task_context(struct isci_request *ireq, struct scu_task_context *task_context)

    :param ireq:
        *undescribed*
    :type ireq: struct isci_request \*

    :param task_context:
        *undescribed*
    :type task_context: struct scu_task_context \*

.. _`scu_ssp_io_request_construct_task_context`:

scu_ssp_io_request_construct_task_context
=========================================

.. c:function:: void scu_ssp_io_request_construct_task_context(struct isci_request *ireq, enum dma_data_direction dir, u32 len)

    :param ireq:
        *undescribed*
    :type ireq: struct isci_request \*

    :param dir:
        *undescribed*
    :type dir: enum dma_data_direction

    :param len:
        *undescribed*
    :type len: u32

.. _`scu_ssp_task_request_construct_task_context`:

scu_ssp_task_request_construct_task_context
===========================================

.. c:function:: void scu_ssp_task_request_construct_task_context(struct isci_request *ireq)

    :param ireq:
        *undescribed*
    :type ireq: struct isci_request \*

.. _`scu_ssp_task_request_construct_task_context.following-important-settings-are-utilized`:

following important settings are utilized
-----------------------------------------

-# priority ==
SCU_TASK_PRIORITY_HIGH.  This ensures that the task request is issued
ahead of other task destined for the same Remote Node. -# task_type ==
SCU_TASK_TYPE_IOREAD.  This simply indicates that a normal request type
(i.e. non-raw frame) is being utilized to perform task management. -#
control_frame == 1.  This ensures that the proper endianess is set so
that the bytes are transmitted in the right order for a task frame.

.. _`scu_sata_request_construct_task_context`:

scu_sata_request_construct_task_context
=======================================

.. c:function:: void scu_sata_request_construct_task_context(struct isci_request *ireq, struct scu_task_context *task_context)

    request.  This is called from the various SATA constructors.

    :param ireq:
        *undescribed*
    :type ireq: struct isci_request \*

    :param task_context:
        The buffer pointer for the SCU task context which is being
        constructed.
    :type task_context: struct scu_task_context \*

.. _`scu_sata_request_construct_task_context.description`:

Description
-----------

The general io request construction is complete. The buffer assignment for
the command buffer is complete. none Revisit task context construction to
determine what is common for SSP/SMP/STP task context structures.

.. _`scu_task_context_sram`:

SCU_TASK_CONTEXT_SRAM
=====================

.. c:function::  SCU_TASK_CONTEXT_SRAM()

    bytes transferred when reply underruns request

.. _`isci_request_process_response_iu`:

isci_request_process_response_iu
================================

.. c:function:: void isci_request_process_response_iu(struct sas_task *task, struct ssp_response_iu *resp_iu, struct device *dev)

    This function sets the status and response iu, in the task struct, from the request object for the upper layer driver.

    :param task:
        *undescribed*
    :type task: struct sas_task \*

    :param resp_iu:
        This parameter points to the response iu of the completed request.
    :type resp_iu: struct ssp_response_iu \*

    :param dev:
        This parameter specifies the linux device struct.
    :type dev: struct device \*

.. _`isci_request_process_response_iu.description`:

Description
-----------

none.

.. _`isci_request_set_open_reject_status`:

isci_request_set_open_reject_status
===================================

.. c:function:: void isci_request_set_open_reject_status(struct isci_request *request, struct sas_task *task, enum service_response *response_ptr, enum exec_status *status_ptr, enum sas_open_rej_reason open_rej_reason)

    This function prepares the I/O completion for OPEN_REJECT conditions.

    :param request:
        This parameter is the completed isci_request object.
    :type request: struct isci_request \*

    :param task:
        *undescribed*
    :type task: struct sas_task \*

    :param response_ptr:
        This parameter specifies the service response for the I/O.
    :type response_ptr: enum service_response \*

    :param status_ptr:
        This parameter specifies the exec status for the I/O.
    :type status_ptr: enum exec_status \*

    :param open_rej_reason:
        This parameter specifies the encoded reason for the
        abandon-class reject.
    :type open_rej_reason: enum sas_open_rej_reason

.. _`isci_request_set_open_reject_status.description`:

Description
-----------

none.

.. _`isci_request_handle_controller_specific_errors`:

isci_request_handle_controller_specific_errors
==============================================

.. c:function:: void isci_request_handle_controller_specific_errors(struct isci_remote_device *idev, struct isci_request *request, struct sas_task *task, enum service_response *response_ptr, enum exec_status *status_ptr)

    This function decodes controller-specific I/O completion error conditions.

    :param idev:
        *undescribed*
    :type idev: struct isci_remote_device \*

    :param request:
        This parameter is the completed isci_request object.
    :type request: struct isci_request \*

    :param task:
        *undescribed*
    :type task: struct sas_task \*

    :param response_ptr:
        This parameter specifies the service response for the I/O.
    :type response_ptr: enum service_response \*

    :param status_ptr:
        This parameter specifies the exec status for the I/O.
    :type status_ptr: enum exec_status \*

.. _`isci_request_handle_controller_specific_errors.description`:

Description
-----------

none.

.. _`isci_io_request_build`:

isci_io_request_build
=====================

.. c:function:: enum sci_status isci_io_request_build(struct isci_host *ihost, struct isci_request *request, struct isci_remote_device *idev)

    This function builds the io request object.

    :param ihost:
        This parameter specifies the ISCI host object
    :type ihost: struct isci_host \*

    :param request:
        This parameter points to the isci_request object allocated in the
        request construct function.
    :type request: struct isci_request \*

    :param idev:
        *undescribed*
    :type idev: struct isci_remote_device \*

.. _`isci_io_request_build.description`:

Description
-----------

SCI_SUCCESS on successfull completion, or specific failure code.

.. This file was automatic generated / don't edit.

