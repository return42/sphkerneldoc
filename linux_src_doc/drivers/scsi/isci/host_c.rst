.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/host.c

.. _`normalize_put_pointer`:

NORMALIZE_PUT_POINTER
=====================

.. c:function::  NORMALIZE_PUT_POINTER( x)

    :param x:
        *undescribed*
    :type x: 

.. _`normalize_put_pointer.description`:

Description
-----------

This macro will normalize the completion queue put pointer so its value can
be used as an array inde

.. _`normalize_event_pointer`:

NORMALIZE_EVENT_POINTER
=======================

.. c:function::  NORMALIZE_EVENT_POINTER( x)

    :param x:
        *undescribed*
    :type x: 

.. _`normalize_event_pointer.description`:

Description
-----------

This macro will normalize the completion queue event entry so its value can
be used as an index.

.. _`normalize_get_pointer`:

NORMALIZE_GET_POINTER
=====================

.. c:function::  NORMALIZE_GET_POINTER( x)

    :param x:
        *undescribed*
    :type x: 

.. _`normalize_get_pointer.description`:

Description
-----------

This macro will normalize the completion queue get pointer so its value can
be used as an index into an array

.. _`normalize_get_pointer_cycle_bit`:

NORMALIZE_GET_POINTER_CYCLE_BIT
===============================

.. c:function::  NORMALIZE_GET_POINTER_CYCLE_BIT( x)

    :param x:
        *undescribed*
    :type x: 

.. _`normalize_get_pointer_cycle_bit.description`:

Description
-----------

This macro will normalize the completion queue cycle pointer so it matches
the completion queue cycle bit

.. _`completion_queue_cycle_bit`:

COMPLETION_QUEUE_CYCLE_BIT
==========================

.. c:function::  COMPLETION_QUEUE_CYCLE_BIT( x)

    :param x:
        *undescribed*
    :type x: 

.. _`completion_queue_cycle_bit.description`:

Description
-----------

This macro will return the cycle bit of the completion queue entry

.. _`isci_host_start_complete`:

isci_host_start_complete
========================

.. c:function:: void isci_host_start_complete(struct isci_host *ihost, enum sci_status completion_status)

    This function is called by the core library, through the ISCI Module, to indicate controller start status.

    :param ihost:
        *undescribed*
    :type ihost: struct isci_host \*

    :param completion_status:
        This parameter specifies the completion status from the
        core library.
    :type completion_status: enum sci_status

.. _`sci_controller_get_suggested_start_timeout`:

sci_controller_get_suggested_start_timeout
==========================================

.. c:function:: u32 sci_controller_get_suggested_start_timeout(struct isci_host *ihost)

    This method returns the suggested \ :c:func:`sci_controller_start`\  timeout amount.  The user is free to use any timeout value, but this method provides the suggested minimum start timeout value.  The returned value is based upon empirical information determined as a result of interoperability testing.

    :param ihost:
        *undescribed*
    :type ihost: struct isci_host \*

.. _`sci_controller_get_suggested_start_timeout.description`:

Description
-----------

This method returns the number of milliseconds for the suggested start
operation timeout.

.. _`sci_controller_start_next_phy`:

sci_controller_start_next_phy
=============================

.. c:function:: enum sci_status sci_controller_start_next_phy(struct isci_host *ihost)

    start phy

    :param ihost:
        *undescribed*
    :type ihost: struct isci_host \*

.. _`sci_controller_start_next_phy.description`:

Description
-----------

If all the phys have been started, then attempt to transition the
controller to the READY state and inform the user
(sci_cb_controller_start_complete()).

.. _`isci_host_completion_routine`:

isci_host_completion_routine
============================

.. c:function:: void isci_host_completion_routine(unsigned long data)

    This function is the delayed service routine that calls the sci core library's completion handler. It's scheduled as a tasklet from the interrupt service routine when interrupts in use, or set as the timeout function in polled mode.

    :param data:
        This parameter specifies the ISCI host object
    :type data: unsigned long

.. _`sci_controller_stop`:

sci_controller_stop
===================

.. c:function:: enum sci_status sci_controller_stop(struct isci_host *ihost, u32 timeout)

    This method will stop an individual controller object.This method will invoke the associated user callback upon completion.  The completion callback is called when the following

    :param ihost:
        *undescribed*
    :type ihost: struct isci_host \*

    :param timeout:
        This parameter specifies the number of milliseconds in which the
        stop operation should complete.
    :type timeout: u32

.. _`sci_controller_stop.conditions-are-met`:

conditions are met
------------------

-# the method return status is SCI_SUCCESS. -# the
controller has been quiesced. This method will ensure that all IO
requests are quiesced, phys are stopped, and all additional operation by
the hardware is halted.

.. _`sci_controller_stop.description`:

Description
-----------

The controller must be in the STARTED or STOPPED state. Indicate if the
controller stop method succeeded or failed in some way. SCI_SUCCESS if the
stop operation successfully began. SCI_WARNING_ALREADY_IN_STATE if the
controller is already in the STOPPED state. SCI_FAILURE_INVALID_STATE if the
controller is not either in the STARTED or STOPPED states.

.. _`sci_controller_reset`:

sci_controller_reset
====================

.. c:function:: enum sci_status sci_controller_reset(struct isci_host *ihost)

    This method will reset the supplied core controller regardless of the state of said controller.  This operation is considered destructive.  In other words, all current operations are wiped out.  No IO completions for outstanding devices occur.  Outstanding IO requests are not aborted or completed at the actual remote device.

    :param ihost:
        *undescribed*
    :type ihost: struct isci_host \*

.. _`sci_controller_reset.description`:

Description
-----------

Indicate if the controller reset method succeeded or failed in some way.
SCI_SUCCESS if the reset operation successfully started. SCI_FATAL_ERROR if
the controller reset operation is unable to complete.

.. _`isci_host_deinit`:

isci_host_deinit
================

.. c:function:: void isci_host_deinit(struct isci_host *ihost)

    shutdown frame reception and dma

    :param ihost:
        host to take down
    :type ihost: struct isci_host \*

.. _`isci_host_deinit.description`:

Description
-----------

This is called in either the driver shutdown or the suspend path.  In
the shutdown case libsas went through port teardown and normal device
removal (i.e. physical links stayed up to service scsi_device removal
commands).  In the suspend case we disable the hardware without
notifying libsas of the link down events since we want libsas to
remember the domain across the suspend/resume cycle

.. _`sci_controller_set_interrupt_coalescence`:

sci_controller_set_interrupt_coalescence
========================================

.. c:function:: enum sci_status sci_controller_set_interrupt_coalescence(struct isci_host *ihost, u32 coalesce_number, u32 coalesce_timeout)

    This method allows the user to configure the interrupt coalescence.

    :param ihost:
        *undescribed*
    :type ihost: struct isci_host \*

    :param coalesce_number:
        Used to control the number of entries in the Completion
        Queue before an interrupt is generated. If the number of entries exceed
        this number, an interrupt will be generated. The valid range of the input
        is [0, 256]. A setting of 0 results in coalescing being disabled.
    :type coalesce_number: u32

    :param coalesce_timeout:
        Timeout value in microseconds. The valid range of the
        input is [0, 2700000] . A setting of 0 is allowed and results in no
        interrupt coalescing timeout.
    :type coalesce_timeout: u32

.. _`sci_controller_set_interrupt_coalescence.description`:

Description
-----------

Indicate if the user successfully set the interrupt coalesce parameters.
SCI_SUCCESS The user successfully updated the interrutp coalescence.
SCI_FAILURE_INVALID_PARAMETER_VALUE The user input value is out of range.

.. _`isci_host_init`:

isci_host_init
==============

.. c:function:: int isci_host_init(struct isci_host *ihost)

    (re-)initialize hardware and internal (private) state

    :param ihost:
        host to init
    :type ihost: struct isci_host \*

.. _`isci_host_init.description`:

Description
-----------

Any public facing objects (like asd_sas_port, and asd_sas_phys), or
one-time initialization objects like locks and waitqueues, are
not touched (they are initialized in isci_host_alloc)

.. _`sci_controller_allocate_remote_node_context`:

sci_controller_allocate_remote_node_context
===========================================

.. c:function:: enum sci_status sci_controller_allocate_remote_node_context(struct isci_host *ihost, struct isci_remote_device *idev, u16 *node_id)

    context space for use. This method can fail if there are no more remote node index available.

    :param ihost:
        *undescribed*
    :type ihost: struct isci_host \*

    :param idev:
        *undescribed*
    :type idev: struct isci_remote_device \*

    :param node_id:
        This is the remote node id that is assinged to the device if one
        is available
    :type node_id: u16 \*

.. _`sci_controller_allocate_remote_node_context.description`:

Description
-----------

enum sci_status SCI_FAILURE_OUT_OF_RESOURCES if there are no available remote
node index available.

.. _`sci_controller_complete_io`:

sci_controller_complete_io
==========================

.. c:function:: enum sci_status sci_controller_complete_io(struct isci_host *ihost, struct isci_remote_device *idev, struct isci_request *ireq)

    This method will perform core specific completion operations for an IO request.  After this method is invoked, the user should consider the IO request as invalid until it is properly reused (i.e. re-constructed).

    :param ihost:
        The handle to the controller object for which to complete the
        IO request.
    :type ihost: struct isci_host \*

    :param idev:
        The handle to the remote device object for which to complete
        the IO request.
    :type idev: struct isci_remote_device \*

    :param ireq:
        the handle to the io request object to complete.
    :type ireq: struct isci_request \*

.. _`sci_controller_start_task`:

sci_controller_start_task
=========================

.. c:function:: enum sci_status sci_controller_start_task(struct isci_host *ihost, struct isci_remote_device *idev, struct isci_request *ireq)

    This method is called by the SCIC user to send/start a framework task management request.

    :param ihost:
        *undescribed*
    :type ihost: struct isci_host \*

    :param idev:
        *undescribed*
    :type idev: struct isci_remote_device \*

    :param ireq:
        *undescribed*
    :type ireq: struct isci_request \*

.. This file was automatic generated / don't edit.

