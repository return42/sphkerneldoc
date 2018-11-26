.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/isci.h

.. _`sci_status`:

enum sci_status
===============

.. c:type:: enum sci_status

    This is the general return status enumeration for non-IO, non-task management related SCI interface methods.

.. _`sci_status.definition`:

Definition
----------

.. code-block:: c

    enum sci_status {
        SCI_SUCCESS,
        SCI_SUCCESS_IO_COMPLETE_BEFORE_START,
        SCI_SUCCESS_IO_DONE_EARLY,
        SCI_WARNING_ALREADY_IN_STATE,
        SCI_WARNING_TIMER_CONFLICT,
        SCI_WARNING_SEQUENCE_INCOMPLETE,
        SCI_FAILURE,
        SCI_FATAL_ERROR,
        SCI_FAILURE_INVALID_STATE,
        SCI_FAILURE_INSUFFICIENT_RESOURCES,
        SCI_FAILURE_CONTROLLER_NOT_FOUND,
        SCI_FAILURE_UNSUPPORTED_CONTROLLER_TYPE,
        SCI_FAILURE_UNSUPPORTED_INIT_DATA_VERSION,
        SCI_FAILURE_UNSUPPORTED_PORT_CONFIGURATION,
        SCI_FAILURE_UNSUPPORTED_PROTOCOL,
        SCI_FAILURE_UNSUPPORTED_INFORMATION_TYPE,
        SCI_FAILURE_DEVICE_EXISTS,
        SCI_FAILURE_ADDING_PHY_UNSUPPORTED,
        SCI_FAILURE_UNSUPPORTED_INFORMATION_FIELD,
        SCI_FAILURE_UNSUPPORTED_TIME_LIMIT,
        SCI_FAILURE_INVALID_PHY,
        SCI_FAILURE_INVALID_PORT,
        SCI_FAILURE_RESET_PORT_PARTIAL_SUCCESS,
        SCI_FAILURE_RESET_PORT_FAILURE,
        SCI_FAILURE_INVALID_REMOTE_DEVICE,
        SCI_FAILURE_REMOTE_DEVICE_RESET_REQUIRED,
        SCI_FAILURE_INVALID_IO_TAG,
        SCI_FAILURE_IO_RESPONSE_VALID,
        SCI_FAILURE_CONTROLLER_SPECIFIC_IO_ERR,
        SCI_FAILURE_IO_TERMINATED,
        SCI_FAILURE_IO_REQUIRES_SCSI_ABORT,
        SCI_FAILURE_DEVICE_NOT_FOUND,
        SCI_FAILURE_INVALID_ASSOCIATION,
        SCI_FAILURE_TIMEOUT,
        SCI_FAILURE_INVALID_PARAMETER_VALUE,
        SCI_FAILURE_UNSUPPORTED_MESSAGE_COUNT,
        SCI_FAILURE_NO_NCQ_TAG_AVAILABLE,
        SCI_FAILURE_PROTOCOL_VIOLATION,
        SCI_FAILURE_RETRY_REQUIRED,
        SCI_FAILURE_RETRY_LIMIT_REACHED,
        SCI_FAILURE_RESET_DEVICE_PARTIAL_SUCCESS,
        SCI_FAILURE_ILLEGAL_ROUTING_ATTRIBUTE_CONFIGURATION,
        SCI_FAILURE_EXCEED_MAX_ROUTE_INDEX,
        SCI_FAILURE_UNSUPPORTED_PCI_DEVICE_ID
    };

.. _`sci_status.constants`:

Constants
---------

SCI_SUCCESS
    *undescribed*

SCI_SUCCESS_IO_COMPLETE_BEFORE_START
    *undescribed*

SCI_SUCCESS_IO_DONE_EARLY
    *undescribed*

SCI_WARNING_ALREADY_IN_STATE
    *undescribed*

SCI_WARNING_TIMER_CONFLICT
    *undescribed*

SCI_WARNING_SEQUENCE_INCOMPLETE
    *undescribed*

SCI_FAILURE
    *undescribed*

SCI_FATAL_ERROR
    *undescribed*

SCI_FAILURE_INVALID_STATE
    *undescribed*

SCI_FAILURE_INSUFFICIENT_RESOURCES
    *undescribed*

SCI_FAILURE_CONTROLLER_NOT_FOUND
    *undescribed*

SCI_FAILURE_UNSUPPORTED_CONTROLLER_TYPE
    *undescribed*

SCI_FAILURE_UNSUPPORTED_INIT_DATA_VERSION
    *undescribed*

SCI_FAILURE_UNSUPPORTED_PORT_CONFIGURATION
    *undescribed*

SCI_FAILURE_UNSUPPORTED_PROTOCOL
    *undescribed*

SCI_FAILURE_UNSUPPORTED_INFORMATION_TYPE
    *undescribed*

SCI_FAILURE_DEVICE_EXISTS
    *undescribed*

SCI_FAILURE_ADDING_PHY_UNSUPPORTED
    *undescribed*

SCI_FAILURE_UNSUPPORTED_INFORMATION_FIELD
    *undescribed*

SCI_FAILURE_UNSUPPORTED_TIME_LIMIT
    *undescribed*

SCI_FAILURE_INVALID_PHY
    *undescribed*

SCI_FAILURE_INVALID_PORT
    *undescribed*

SCI_FAILURE_RESET_PORT_PARTIAL_SUCCESS
    *undescribed*

SCI_FAILURE_RESET_PORT_FAILURE
    *undescribed*

SCI_FAILURE_INVALID_REMOTE_DEVICE
    *undescribed*

SCI_FAILURE_REMOTE_DEVICE_RESET_REQUIRED
    *undescribed*

SCI_FAILURE_INVALID_IO_TAG
    *undescribed*

SCI_FAILURE_IO_RESPONSE_VALID
    *undescribed*

SCI_FAILURE_CONTROLLER_SPECIFIC_IO_ERR
    *undescribed*

SCI_FAILURE_IO_TERMINATED
    *undescribed*

SCI_FAILURE_IO_REQUIRES_SCSI_ABORT
    *undescribed*

SCI_FAILURE_DEVICE_NOT_FOUND
    *undescribed*

SCI_FAILURE_INVALID_ASSOCIATION
    *undescribed*

SCI_FAILURE_TIMEOUT
    *undescribed*

SCI_FAILURE_INVALID_PARAMETER_VALUE
    *undescribed*

SCI_FAILURE_UNSUPPORTED_MESSAGE_COUNT
    *undescribed*

SCI_FAILURE_NO_NCQ_TAG_AVAILABLE
    *undescribed*

SCI_FAILURE_PROTOCOL_VIOLATION
    *undescribed*

SCI_FAILURE_RETRY_REQUIRED
    *undescribed*

SCI_FAILURE_RETRY_LIMIT_REACHED
    *undescribed*

SCI_FAILURE_RESET_DEVICE_PARTIAL_SUCCESS
    *undescribed*

SCI_FAILURE_ILLEGAL_ROUTING_ATTRIBUTE_CONFIGURATION
    *undescribed*

SCI_FAILURE_EXCEED_MAX_ROUTE_INDEX
    *undescribed*

SCI_FAILURE_UNSUPPORTED_PCI_DEVICE_ID
    *undescribed*

.. _`sci_status.description`:

Description
-----------

???

.. _`sci_io_status`:

enum sci_io_status
==================

.. c:type:: enum sci_io_status

    This enumeration depicts all of the possible IO completion status values.  Each value in this enumeration maps directly to a value in the enum sci_status enumeration.  Please refer to that enumeration for detailed comments concerning what the status represents.

.. _`sci_io_status.definition`:

Definition
----------

.. code-block:: c

    enum sci_io_status {
        SCI_IO_SUCCESS,
        SCI_IO_FAILURE,
        SCI_IO_SUCCESS_COMPLETE_BEFORE_START,
        SCI_IO_SUCCESS_IO_DONE_EARLY,
        SCI_IO_FAILURE_INVALID_STATE,
        SCI_IO_FAILURE_INSUFFICIENT_RESOURCES,
        SCI_IO_FAILURE_UNSUPPORTED_PROTOCOL,
        SCI_IO_FAILURE_RESPONSE_VALID,
        SCI_IO_FAILURE_CONTROLLER_SPECIFIC_ERR,
        SCI_IO_FAILURE_TERMINATED,
        SCI_IO_FAILURE_REQUIRES_SCSI_ABORT,
        SCI_IO_FAILURE_INVALID_PARAMETER_VALUE,
        SCI_IO_FAILURE_NO_NCQ_TAG_AVAILABLE,
        SCI_IO_FAILURE_PROTOCOL_VIOLATION,
        SCI_IO_FAILURE_REMOTE_DEVICE_RESET_REQUIRED,
        SCI_IO_FAILURE_RETRY_REQUIRED,
        SCI_IO_FAILURE_RETRY_LIMIT_REACHED,
        SCI_IO_FAILURE_INVALID_REMOTE_DEVICE
    };

.. _`sci_io_status.constants`:

Constants
---------

SCI_IO_SUCCESS
    *undescribed*

SCI_IO_FAILURE
    *undescribed*

SCI_IO_SUCCESS_COMPLETE_BEFORE_START
    *undescribed*

SCI_IO_SUCCESS_IO_DONE_EARLY
    *undescribed*

SCI_IO_FAILURE_INVALID_STATE
    *undescribed*

SCI_IO_FAILURE_INSUFFICIENT_RESOURCES
    *undescribed*

SCI_IO_FAILURE_UNSUPPORTED_PROTOCOL
    *undescribed*

SCI_IO_FAILURE_RESPONSE_VALID
    *undescribed*

SCI_IO_FAILURE_CONTROLLER_SPECIFIC_ERR
    *undescribed*

SCI_IO_FAILURE_TERMINATED
    *undescribed*

SCI_IO_FAILURE_REQUIRES_SCSI_ABORT
    *undescribed*

SCI_IO_FAILURE_INVALID_PARAMETER_VALUE
    *undescribed*

SCI_IO_FAILURE_NO_NCQ_TAG_AVAILABLE
    *undescribed*

SCI_IO_FAILURE_PROTOCOL_VIOLATION
    *undescribed*

SCI_IO_FAILURE_REMOTE_DEVICE_RESET_REQUIRED
    *undescribed*

SCI_IO_FAILURE_RETRY_REQUIRED
    *undescribed*

SCI_IO_FAILURE_RETRY_LIMIT_REACHED
    *undescribed*

SCI_IO_FAILURE_INVALID_REMOTE_DEVICE
    *undescribed*

.. _`sci_io_status.description`:

Description
-----------

Add the API to retrieve the SCU status from the core. Check to see that the

.. _`sci_io_status.following-status-are-properly-handled`:

following status are properly handled
-------------------------------------

- SCI_IO_FAILURE_UNSUPPORTED_PROTOCOL
- SCI_IO_FAILURE_INVALID_IO_TAG

.. _`sci_task_status`:

enum sci_task_status
====================

.. c:type:: enum sci_task_status

    This enumeration depicts all of the possible task completion status values.  Each value in this enumeration maps directly to a value in the enum sci_status enumeration.  Please refer to that enumeration for detailed comments concerning what the status represents.

.. _`sci_task_status.definition`:

Definition
----------

.. code-block:: c

    enum sci_task_status {
        SCI_TASK_SUCCESS,
        SCI_TASK_FAILURE,
        SCI_TASK_FAILURE_INVALID_STATE,
        SCI_TASK_FAILURE_INSUFFICIENT_RESOURCES,
        SCI_TASK_FAILURE_UNSUPPORTED_PROTOCOL,
        SCI_TASK_FAILURE_INVALID_TAG,
        SCI_TASK_FAILURE_RESPONSE_VALID,
        SCI_TASK_FAILURE_CONTROLLER_SPECIFIC_ERR,
        SCI_TASK_FAILURE_TERMINATED,
        SCI_TASK_FAILURE_INVALID_PARAMETER_VALUE,
        SCI_TASK_FAILURE_REMOTE_DEVICE_RESET_REQUIRED,
        SCI_TASK_FAILURE_RESET_DEVICE_PARTIAL_SUCCESS
    };

.. _`sci_task_status.constants`:

Constants
---------

SCI_TASK_SUCCESS
    *undescribed*

SCI_TASK_FAILURE
    *undescribed*

SCI_TASK_FAILURE_INVALID_STATE
    *undescribed*

SCI_TASK_FAILURE_INSUFFICIENT_RESOURCES
    *undescribed*

SCI_TASK_FAILURE_UNSUPPORTED_PROTOCOL
    *undescribed*

SCI_TASK_FAILURE_INVALID_TAG
    *undescribed*

SCI_TASK_FAILURE_RESPONSE_VALID
    *undescribed*

SCI_TASK_FAILURE_CONTROLLER_SPECIFIC_ERR
    *undescribed*

SCI_TASK_FAILURE_TERMINATED
    *undescribed*

SCI_TASK_FAILURE_INVALID_PARAMETER_VALUE
    *undescribed*

SCI_TASK_FAILURE_REMOTE_DEVICE_RESET_REQUIRED
    *undescribed*

SCI_TASK_FAILURE_RESET_DEVICE_PARTIAL_SUCCESS
    *undescribed*

.. _`sci_swab32_cpy`:

sci_swab32_cpy
==============

.. c:function:: void sci_swab32_cpy(void *_dest, void *_src, ssize_t word_cnt)

    convert between scsi and scu-hardware byte format

    :param _dest:
        *undescribed*
    :type _dest: void \*

    :param _src:
        *undescribed*
    :type _src: void \*

    :param word_cnt:
        *undescribed*
    :type word_cnt: ssize_t

.. _`sci_swab32_cpy.description`:

Description
-----------

scu hardware handles SSP/SMP control, response, and unidentified
frames in "big endian dword" order.  Regardless of host endian this
is always a \ :c:func:`swab32`\ -per-dword conversion of the standard definition,
i.e. single byte fields swapped and multi-byte fields in little-
endian

.. This file was automatic generated / don't edit.

