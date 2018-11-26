.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/arm/fas216.c

.. _`fas216_get_last_msg`:

fas216_get_last_msg
===================

.. c:function:: unsigned short fas216_get_last_msg(FAS216_Info *info, int pos)

    retrive last message from the list

    :param info:
        interface to search
    :type info: FAS216_Info \*

    :param pos:
        current fifo position
    :type pos: int

.. _`fas216_get_last_msg.description`:

Description
-----------

Retrieve a last message from the list, using position in fifo.

.. _`fas216_syncperiod`:

fas216_syncperiod
=================

.. c:function:: int fas216_syncperiod(FAS216_Info *info, int ns)

    calculate STP register value

    :param info:
        state structure for interface connected to device
    :type info: FAS216_Info \*

    :param ns:
        period in ns (between subsequent bytes)
    :type ns: int

.. _`fas216_syncperiod.description`:

Description
-----------

Calculate value to be loaded into the STP register for a given period
in ns. Returns a value suitable for REG_STP.

.. _`fas216_set_sync`:

fas216_set_sync
===============

.. c:function:: void fas216_set_sync(FAS216_Info *info, int target)

    setup FAS216 chip for specified transfer period.

    :param info:
        state structure for interface connected to device
    :type info: FAS216_Info \*

    :param target:
        target
    :type target: int

.. _`fas216_set_sync.description`:

Description
-----------

Correctly setup FAS216 chip for specified transfer period.
Notes   : we need to switch the chip out of FASTSCSI mode if we have
a transfer period >= 200ns - otherwise the chip will violate
the SCSI timings.

.. _`fas216_handlesync`:

fas216_handlesync
=================

.. c:function:: void fas216_handlesync(FAS216_Info *info, char *msg)

    Handle a synchronous transfer message

    :param info:
        state structure for interface
    :type info: FAS216_Info \*

    :param msg:
        message from target
    :type msg: char \*

.. _`fas216_handlesync.description`:

Description
-----------

Handle a synchronous transfer message from the target

.. _`fas216_updateptrs`:

fas216_updateptrs
=================

.. c:function:: void fas216_updateptrs(FAS216_Info *info, int bytes_transferred)

    update data pointers after transfer suspended/paused

    :param info:
        interface's local pointer to update
    :type info: FAS216_Info \*

    :param bytes_transferred:
        number of bytes transferred
    :type bytes_transferred: int

.. _`fas216_updateptrs.description`:

Description
-----------

Update data pointers after transfer suspended/paused

.. _`fas216_pio`:

fas216_pio
==========

.. c:function:: void fas216_pio(FAS216_Info *info, fasdmadir_t direction)

    transfer data off of/on to card using programmed IO

    :param info:
        interface to transfer data to/from
    :type info: FAS216_Info \*

    :param direction:
        direction to transfer data (DMA_OUT/DMA_IN)
    :type direction: fasdmadir_t

.. _`fas216_pio.description`:

Description
-----------

Transfer data off of/on to card using programmed IO.

.. _`fas216_pio.notes`:

Notes
-----

this is incredibly slow.

.. _`fas216_cleanuptransfer`:

fas216_cleanuptransfer
======================

.. c:function:: void fas216_cleanuptransfer(FAS216_Info *info)

    clean up after a transfer has completed.

    :param info:
        interface to clean up
    :type info: FAS216_Info \*

.. _`fas216_cleanuptransfer.description`:

Description
-----------

Update the data pointers according to the number of bytes transferred
on the SCSI bus.

.. _`fas216_transfer`:

fas216_transfer
===============

.. c:function:: void fas216_transfer(FAS216_Info *info)

    Perform a DMA/PIO transfer off of/on to card

    :param info:
        interface from which device disconnected from
    :type info: FAS216_Info \*

.. _`fas216_transfer.description`:

Description
-----------

Start a DMA/PIO transfer off of/on to card

.. _`fas216_stoptransfer`:

fas216_stoptransfer
===================

.. c:function:: void fas216_stoptransfer(FAS216_Info *info)

    Stop a DMA transfer onto / off of the card

    :param info:
        interface from which device disconnected from
    :type info: FAS216_Info \*

.. _`fas216_stoptransfer.description`:

Description
-----------

Called when we switch away from DATA IN or DATA OUT phases.

.. _`fas216_disconnect_intr`:

fas216_disconnect_intr
======================

.. c:function:: void fas216_disconnect_intr(FAS216_Info *info)

    handle device disconnection

    :param info:
        interface from which device disconnected from
    :type info: FAS216_Info \*

.. _`fas216_disconnect_intr.description`:

Description
-----------

Handle device disconnection

.. _`fas216_reselected_intr`:

fas216_reselected_intr
======================

.. c:function:: void fas216_reselected_intr(FAS216_Info *info)

    start reconnection of a device

    :param info:
        interface which was reselected
    :type info: FAS216_Info \*

.. _`fas216_reselected_intr.description`:

Description
-----------

Start reconnection of a device

.. _`fas216_message`:

fas216_message
==============

.. c:function:: void fas216_message(FAS216_Info *info)

    handle a function done interrupt from FAS216 chip

    :param info:
        interface which caused function done interrupt
    :type info: FAS216_Info \*

.. _`fas216_message.description`:

Description
-----------

Handle a function done interrupt from FAS216 chip

.. _`fas216_send_command`:

fas216_send_command
===================

.. c:function:: void fas216_send_command(FAS216_Info *info)

    send command after all message bytes have been sent

    :param info:
        interface which caused bus service
    :type info: FAS216_Info \*

.. _`fas216_send_command.description`:

Description
-----------

Send a command to a target after all message bytes have been sent

.. _`fas216_send_messageout`:

fas216_send_messageout
======================

.. c:function:: void fas216_send_messageout(FAS216_Info *info, int start)

    handle bus service to send a message

    :param info:
        interface which caused bus service
    :type info: FAS216_Info \*

    :param start:
        *undescribed*
    :type start: int

.. _`fas216_send_messageout.description`:

Description
-----------

Handle bus service to send a message.

.. _`fas216_send_messageout.note`:

Note
----

We do not allow the device to change the data direction!

.. _`fas216_busservice_intr`:

fas216_busservice_intr
======================

.. c:function:: void fas216_busservice_intr(FAS216_Info *info, unsigned int stat, unsigned int is)

    handle bus service interrupt from FAS216 chip

    :param info:
        interface which caused bus service interrupt
    :type info: FAS216_Info \*

    :param stat:
        Status register contents
    :type stat: unsigned int

    :param is:
        SCSI Status register contents
    :type is: unsigned int

.. _`fas216_busservice_intr.description`:

Description
-----------

Handle a bus service interrupt from FAS216 chip

.. _`fas216_funcdone_intr`:

fas216_funcdone_intr
====================

.. c:function:: void fas216_funcdone_intr(FAS216_Info *info, unsigned int stat, unsigned int is)

    handle a function done interrupt from FAS216 chip

    :param info:
        interface which caused function done interrupt
    :type info: FAS216_Info \*

    :param stat:
        Status register contents
    :type stat: unsigned int

    :param is:
        SCSI Status register contents
    :type is: unsigned int

.. _`fas216_funcdone_intr.description`:

Description
-----------

Handle a function done interrupt from FAS216 chip

.. _`fas216_intr`:

fas216_intr
===========

.. c:function:: irqreturn_t fas216_intr(FAS216_Info *info)

    handle interrupts to progress a command

    :param info:
        interface to service
    :type info: FAS216_Info \*

.. _`fas216_intr.description`:

Description
-----------

Handle interrupts from the interface to progress a command

.. _`fas216_kick`:

fas216_kick
===========

.. c:function:: void fas216_kick(FAS216_Info *info)

    kick a command to the interface

    :param info:
        our host interface to kick
    :type info: FAS216_Info \*

.. _`fas216_kick.description`:

Description
-----------

Kick a command to the interface, interface should be idle.

.. _`fas216_kick.notes`:

Notes
-----

Interrupts are always disabled!

.. _`fas216_rq_sns_done`:

fas216_rq_sns_done
==================

.. c:function:: void fas216_rq_sns_done(FAS216_Info *info, struct scsi_cmnd *SCpnt, unsigned int result)

    Finish processing automatic request sense command

    :param info:
        interface that completed
    :type info: FAS216_Info \*

    :param SCpnt:
        command that completed
    :type SCpnt: struct scsi_cmnd \*

    :param result:
        driver byte of result
    :type result: unsigned int

.. _`fas216_rq_sns_done.description`:

Description
-----------

Finish processing automatic request sense command

.. _`fas216_std_done`:

fas216_std_done
===============

.. c:function:: void fas216_std_done(FAS216_Info *info, struct scsi_cmnd *SCpnt, unsigned int result)

    finish processing of standard command

    :param info:
        interface that completed
    :type info: FAS216_Info \*

    :param SCpnt:
        command that completed
    :type SCpnt: struct scsi_cmnd \*

    :param result:
        driver byte of result
    :type result: unsigned int

.. _`fas216_std_done.description`:

Description
-----------

Finish processing of standard command

.. _`fas216_done`:

fas216_done
===========

.. c:function:: void fas216_done(FAS216_Info *info, unsigned int result)

    complete processing for current command

    :param info:
        interface that completed
    :type info: FAS216_Info \*

    :param result:
        driver byte of result
    :type result: unsigned int

.. _`fas216_done.description`:

Description
-----------

Complete processing for current command

.. _`fas216_queue_command_lck`:

fas216_queue_command_lck
========================

.. c:function:: int fas216_queue_command_lck(struct scsi_cmnd *SCpnt, void (*done)(struct scsi_cmnd *))

    queue a command for adapter to process.

    :param SCpnt:
        Command to queue
    :type SCpnt: struct scsi_cmnd \*

    :param void (\*done)(struct scsi_cmnd \*):
        done function to call once command is complete

.. _`fas216_queue_command_lck.description`:

Description
-----------

Queue a command for adapter to process.

.. _`fas216_queue_command_lck.return`:

Return
------

0 on success, else error.

.. _`fas216_queue_command_lck.notes`:

Notes
-----

io_request_lock is held, interrupts are disabled.

.. _`fas216_internal_done`:

fas216_internal_done
====================

.. c:function:: void fas216_internal_done(struct scsi_cmnd *SCpnt)

    trigger restart of a waiting thread in fas216_noqueue_command

    :param SCpnt:
        Command to wake
    :type SCpnt: struct scsi_cmnd \*

.. _`fas216_internal_done.description`:

Description
-----------

Trigger restart of a waiting thread in fas216_command

.. _`fas216_noqueue_command_lck`:

fas216_noqueue_command_lck
==========================

.. c:function:: int fas216_noqueue_command_lck(struct scsi_cmnd *SCpnt, void (*done)(struct scsi_cmnd *))

    process a command for the adapter.

    :param SCpnt:
        Command to queue
    :type SCpnt: struct scsi_cmnd \*

    :param void (\*done)(struct scsi_cmnd \*):
        *undescribed*

.. _`fas216_noqueue_command_lck.description`:

Description
-----------

Queue a command for adapter to process.

.. _`fas216_noqueue_command_lck.return`:

Return
------

scsi result code.

.. _`fas216_noqueue_command_lck.notes`:

Notes
-----

io_request_lock is held, interrupts are disabled.

.. _`fas216_find_command`:

fas216_find_command
===================

.. c:function:: enum res_find fas216_find_command(FAS216_Info *info, struct scsi_cmnd *SCpnt)

    decide how to abort a command

    :param info:
        *undescribed*
    :type info: FAS216_Info \*

    :param SCpnt:
        command to abort
    :type SCpnt: struct scsi_cmnd \*

.. _`fas216_find_command.description`:

Description
-----------

Decide how to abort a command.

.. _`fas216_find_command.return`:

Return
------

abort status

.. _`fas216_eh_abort`:

fas216_eh_abort
===============

.. c:function:: int fas216_eh_abort(struct scsi_cmnd *SCpnt)

    abort this command

    :param SCpnt:
        command to abort
    :type SCpnt: struct scsi_cmnd \*

.. _`fas216_eh_abort.description`:

Description
-----------

Abort this command.

.. _`fas216_eh_abort.return`:

Return
------

FAILED if unable to abort

.. _`fas216_eh_abort.notes`:

Notes
-----

io_request_lock is taken, and irqs are disabled

.. _`fas216_eh_device_reset`:

fas216_eh_device_reset
======================

.. c:function:: int fas216_eh_device_reset(struct scsi_cmnd *SCpnt)

    Reset the device associated with this command

    :param SCpnt:
        command specifing device to reset
    :type SCpnt: struct scsi_cmnd \*

.. _`fas216_eh_device_reset.description`:

Description
-----------

Reset the device associated with this command.

.. _`fas216_eh_device_reset.return`:

Return
------

FAILED if unable to reset.

.. _`fas216_eh_device_reset.notes`:

Notes
-----

We won't be re-entered, so we'll only have one device
reset on the go at one time.

.. _`fas216_eh_bus_reset`:

fas216_eh_bus_reset
===================

.. c:function:: int fas216_eh_bus_reset(struct scsi_cmnd *SCpnt)

    Reset the bus associated with the command

    :param SCpnt:
        command specifing bus to reset
    :type SCpnt: struct scsi_cmnd \*

.. _`fas216_eh_bus_reset.description`:

Description
-----------

Reset the bus associated with the command.

.. _`fas216_eh_bus_reset.return`:

Return
------

FAILED if unable to reset.

.. _`fas216_eh_bus_reset.notes`:

Notes
-----

Further commands are blocked.

.. _`fas216_init_chip`:

fas216_init_chip
================

.. c:function:: void fas216_init_chip(FAS216_Info *info)

    Initialise FAS216 state after reset

    :param info:
        state structure for interface
    :type info: FAS216_Info \*

.. _`fas216_init_chip.description`:

Description
-----------

Initialise FAS216 state after reset

.. _`fas216_eh_host_reset`:

fas216_eh_host_reset
====================

.. c:function:: int fas216_eh_host_reset(struct scsi_cmnd *SCpnt)

    Reset the host associated with this command

    :param SCpnt:
        command specifing host to reset
    :type SCpnt: struct scsi_cmnd \*

.. _`fas216_eh_host_reset.description`:

Description
-----------

Reset the host associated with this command.

.. _`fas216_eh_host_reset.return`:

Return
------

FAILED if unable to reset.

.. _`fas216_eh_host_reset.notes`:

Notes
-----

io_request_lock is taken, and irqs are disabled

.. _`fas216_reset_state`:

fas216_reset_state
==================

.. c:function:: void fas216_reset_state(FAS216_Info *info)

    Initialise driver internal state

    :param info:
        state to initialise
    :type info: FAS216_Info \*

.. _`fas216_reset_state.description`:

Description
-----------

Initialise driver internal state

.. _`fas216_init`:

fas216_init
===========

.. c:function:: int fas216_init(struct Scsi_Host *host)

    initialise FAS/NCR/AMD SCSI structures.

    :param host:
        a driver-specific filled-out structure
    :type host: struct Scsi_Host \*

.. _`fas216_init.description`:

Description
-----------

Initialise FAS/NCR/AMD SCSI structures.

.. _`fas216_init.return`:

Return
------

0 on success

.. _`fas216_add`:

fas216_add
==========

.. c:function:: int fas216_add(struct Scsi_Host *host, struct device *dev)

    initialise FAS/NCR/AMD SCSI ic.

    :param host:
        a driver-specific filled-out structure
    :type host: struct Scsi_Host \*

    :param dev:
        parent device
    :type dev: struct device \*

.. _`fas216_add.description`:

Description
-----------

Initialise FAS/NCR/AMD SCSI ic.

.. _`fas216_add.return`:

Return
------

0 on success

.. _`fas216_release`:

fas216_release
==============

.. c:function:: void fas216_release(struct Scsi_Host *host)

    release all resources for FAS/NCR/AMD SCSI ic.

    :param host:
        a driver-specific filled-out structure
    :type host: struct Scsi_Host \*

.. _`fas216_release.description`:

Description
-----------

release all resources and put everything to bed for FAS/NCR/AMD SCSI ic.

.. This file was automatic generated / don't edit.

