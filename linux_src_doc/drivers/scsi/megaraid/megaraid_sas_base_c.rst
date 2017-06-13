.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/megaraid/megaraid_sas_base.c

.. _`megasas_get_cmd`:

megasas_get_cmd
===============

.. c:function:: struct megasas_cmd *megasas_get_cmd(struct megasas_instance *instance)

    Get a command from the free pool

    :param struct megasas_instance \*instance:
        Adapter soft state

.. _`megasas_get_cmd.description`:

Description
-----------

Returns a free command from the pool

.. _`megasas_return_cmd`:

megasas_return_cmd
==================

.. c:function:: void megasas_return_cmd(struct megasas_instance *instance, struct megasas_cmd *cmd)

    Return a cmd to free command pool

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param struct megasas_cmd \*cmd:
        Command packet to be returned to free command pool

.. _`megasas_decode_evt`:

megasas_decode_evt
==================

.. c:function:: void megasas_decode_evt(struct megasas_instance *instance)

    Decode FW AEN event and print critical event for information.

    :param struct megasas_instance \*instance:
        Adapter soft state

.. _`megasas_enable_intr_xscale`:

megasas_enable_intr_xscale
==========================

.. c:function:: void megasas_enable_intr_xscale(struct megasas_instance *instance)

    (deviceid : 1064R, PERC5) controllers

    :param struct megasas_instance \*instance:
        *undescribed*

.. _`megasas_disable_intr_xscale`:

megasas_disable_intr_xscale
===========================

.. c:function:: void megasas_disable_intr_xscale(struct megasas_instance *instance)

    Disables interrupt

    :param struct megasas_instance \*instance:
        *undescribed*

.. _`megasas_read_fw_status_reg_xscale`:

megasas_read_fw_status_reg_xscale
=================================

.. c:function:: u32 megasas_read_fw_status_reg_xscale(struct megasas_register_set __iomem *regs)

    returns the current FW status value

    :param struct megasas_register_set __iomem \*regs:
        MFI register set

.. _`megasas_clear_intr_xscale`:

megasas_clear_intr_xscale
=========================

.. c:function:: int megasas_clear_intr_xscale(struct megasas_register_set __iomem *regs)

    Check & clear interrupt

    :param struct megasas_register_set __iomem \*regs:
        MFI register set

.. _`megasas_fire_cmd_xscale`:

megasas_fire_cmd_xscale
=======================

.. c:function:: void megasas_fire_cmd_xscale(struct megasas_instance *instance, dma_addr_t frame_phys_addr, u32 frame_count, struct megasas_register_set __iomem *regs)

    Sends command to the FW

    :param struct megasas_instance \*instance:
        *undescribed*

    :param dma_addr_t frame_phys_addr:
        Physical address of cmd

    :param u32 frame_count:
        Number of frames for the command

    :param struct megasas_register_set __iomem \*regs:
        MFI register set

.. _`megasas_adp_reset_xscale`:

megasas_adp_reset_xscale
========================

.. c:function:: int megasas_adp_reset_xscale(struct megasas_instance *instance, struct megasas_register_set __iomem *regs)

    For controller reset

    :param struct megasas_instance \*instance:
        *undescribed*

    :param struct megasas_register_set __iomem \*regs:
        MFI register set

.. _`megasas_check_reset_xscale`:

megasas_check_reset_xscale
==========================

.. c:function:: int megasas_check_reset_xscale(struct megasas_instance *instance, struct megasas_register_set __iomem *regs)

    For controller reset check

    :param struct megasas_instance \*instance:
        *undescribed*

    :param struct megasas_register_set __iomem \*regs:
        MFI register set

.. _`megasas_enable_intr_ppc`:

megasas_enable_intr_ppc
=======================

.. c:function:: void megasas_enable_intr_ppc(struct megasas_instance *instance)

    to xscale (deviceid : 1064R, PERC5) controllers

    :param struct megasas_instance \*instance:
        *undescribed*

.. _`megasas_disable_intr_ppc`:

megasas_disable_intr_ppc
========================

.. c:function:: void megasas_disable_intr_ppc(struct megasas_instance *instance)

    Disable interrupt

    :param struct megasas_instance \*instance:
        *undescribed*

.. _`megasas_read_fw_status_reg_ppc`:

megasas_read_fw_status_reg_ppc
==============================

.. c:function:: u32 megasas_read_fw_status_reg_ppc(struct megasas_register_set __iomem *regs)

    returns the current FW status value

    :param struct megasas_register_set __iomem \*regs:
        MFI register set

.. _`megasas_clear_intr_ppc`:

megasas_clear_intr_ppc
======================

.. c:function:: int megasas_clear_intr_ppc(struct megasas_register_set __iomem *regs)

    Check & clear interrupt

    :param struct megasas_register_set __iomem \*regs:
        MFI register set

.. _`megasas_fire_cmd_ppc`:

megasas_fire_cmd_ppc
====================

.. c:function:: void megasas_fire_cmd_ppc(struct megasas_instance *instance, dma_addr_t frame_phys_addr, u32 frame_count, struct megasas_register_set __iomem *regs)

    Sends command to the FW

    :param struct megasas_instance \*instance:
        *undescribed*

    :param dma_addr_t frame_phys_addr:
        Physical address of cmd

    :param u32 frame_count:
        Number of frames for the command

    :param struct megasas_register_set __iomem \*regs:
        MFI register set

.. _`megasas_check_reset_ppc`:

megasas_check_reset_ppc
=======================

.. c:function:: int megasas_check_reset_ppc(struct megasas_instance *instance, struct megasas_register_set __iomem *regs)

    For controller reset check

    :param struct megasas_instance \*instance:
        *undescribed*

    :param struct megasas_register_set __iomem \*regs:
        MFI register set

.. _`megasas_enable_intr_skinny`:

megasas_enable_intr_skinny
==========================

.. c:function:: void megasas_enable_intr_skinny(struct megasas_instance *instance)

    Enables interrupts

    :param struct megasas_instance \*instance:
        *undescribed*

.. _`megasas_disable_intr_skinny`:

megasas_disable_intr_skinny
===========================

.. c:function:: void megasas_disable_intr_skinny(struct megasas_instance *instance)

    Disables interrupt

    :param struct megasas_instance \*instance:
        *undescribed*

.. _`megasas_read_fw_status_reg_skinny`:

megasas_read_fw_status_reg_skinny
=================================

.. c:function:: u32 megasas_read_fw_status_reg_skinny(struct megasas_register_set __iomem *regs)

    returns the current FW status value

    :param struct megasas_register_set __iomem \*regs:
        MFI register set

.. _`megasas_clear_intr_skinny`:

megasas_clear_intr_skinny
=========================

.. c:function:: int megasas_clear_intr_skinny(struct megasas_register_set __iomem *regs)

    Check & clear interrupt

    :param struct megasas_register_set __iomem \*regs:
        MFI register set

.. _`megasas_fire_cmd_skinny`:

megasas_fire_cmd_skinny
=======================

.. c:function:: void megasas_fire_cmd_skinny(struct megasas_instance *instance, dma_addr_t frame_phys_addr, u32 frame_count, struct megasas_register_set __iomem *regs)

    Sends command to the FW

    :param struct megasas_instance \*instance:
        *undescribed*

    :param dma_addr_t frame_phys_addr:
        Physical address of cmd

    :param u32 frame_count:
        Number of frames for the command

    :param struct megasas_register_set __iomem \*regs:
        MFI register set

.. _`megasas_check_reset_skinny`:

megasas_check_reset_skinny
==========================

.. c:function:: int megasas_check_reset_skinny(struct megasas_instance *instance, struct megasas_register_set __iomem *regs)

    For controller reset check

    :param struct megasas_instance \*instance:
        *undescribed*

    :param struct megasas_register_set __iomem \*regs:
        MFI register set

.. _`megasas_enable_intr_gen2`:

megasas_enable_intr_gen2
========================

.. c:function:: void megasas_enable_intr_gen2(struct megasas_instance *instance)

    0x78 0x79) controllers

    :param struct megasas_instance \*instance:
        *undescribed*

.. _`megasas_disable_intr_gen2`:

megasas_disable_intr_gen2
=========================

.. c:function:: void megasas_disable_intr_gen2(struct megasas_instance *instance)

    Disables interrupt

    :param struct megasas_instance \*instance:
        *undescribed*

.. _`megasas_read_fw_status_reg_gen2`:

megasas_read_fw_status_reg_gen2
===============================

.. c:function:: u32 megasas_read_fw_status_reg_gen2(struct megasas_register_set __iomem *regs)

    returns the current FW status value

    :param struct megasas_register_set __iomem \*regs:
        MFI register set

.. _`megasas_clear_intr_gen2`:

megasas_clear_intr_gen2
=======================

.. c:function:: int megasas_clear_intr_gen2(struct megasas_register_set __iomem *regs)

    Check & clear interrupt

    :param struct megasas_register_set __iomem \*regs:
        MFI register set

.. _`megasas_fire_cmd_gen2`:

megasas_fire_cmd_gen2
=====================

.. c:function:: void megasas_fire_cmd_gen2(struct megasas_instance *instance, dma_addr_t frame_phys_addr, u32 frame_count, struct megasas_register_set __iomem *regs)

    Sends command to the FW

    :param struct megasas_instance \*instance:
        *undescribed*

    :param dma_addr_t frame_phys_addr:
        Physical address of cmd

    :param u32 frame_count:
        Number of frames for the command

    :param struct megasas_register_set __iomem \*regs:
        MFI register set

.. _`megasas_adp_reset_gen2`:

megasas_adp_reset_gen2
======================

.. c:function:: int megasas_adp_reset_gen2(struct megasas_instance *instance, struct megasas_register_set __iomem *reg_set)

    For controller reset

    :param struct megasas_instance \*instance:
        *undescribed*

    :param struct megasas_register_set __iomem \*reg_set:
        *undescribed*

.. _`megasas_check_reset_gen2`:

megasas_check_reset_gen2
========================

.. c:function:: int megasas_check_reset_gen2(struct megasas_instance *instance, struct megasas_register_set __iomem *regs)

    For controller reset check

    :param struct megasas_instance \*instance:
        *undescribed*

    :param struct megasas_register_set __iomem \*regs:
        MFI register set

.. _`megasas_issue_polled`:

megasas_issue_polled
====================

.. c:function:: int megasas_issue_polled(struct megasas_instance *instance, struct megasas_cmd *cmd)

    Issues a polling command

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param struct megasas_cmd \*cmd:
        Command packet to be issued

.. _`megasas_issue_polled.description`:

Description
-----------

For polling, MFI requires the cmd_status to be set to MFI_STAT_INVALID_STATUS before posting.

.. _`megasas_issue_blocked_cmd`:

megasas_issue_blocked_cmd
=========================

.. c:function:: int megasas_issue_blocked_cmd(struct megasas_instance *instance, struct megasas_cmd *cmd, int timeout)

    Synchronous wrapper around regular FW cmds

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param struct megasas_cmd \*cmd:
        Command to be issued

    :param int timeout:
        Timeout in seconds

.. _`megasas_issue_blocked_cmd.description`:

Description
-----------

This function waits on an event for the command to be returned from ISR.
Max wait time is MEGASAS_INTERNAL_CMD_WAIT_TIME secs
Used to issue ioctl commands.

.. _`megasas_issue_blocked_abort_cmd`:

megasas_issue_blocked_abort_cmd
===============================

.. c:function:: int megasas_issue_blocked_abort_cmd(struct megasas_instance *instance, struct megasas_cmd *cmd_to_abort, int timeout)

    Aborts previously issued cmd

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param struct megasas_cmd \*cmd_to_abort:
        Previously issued cmd to be aborted

    :param int timeout:
        Timeout in seconds

.. _`megasas_issue_blocked_abort_cmd.description`:

Description
-----------

MFI firmware can abort previously issued AEN comamnd (automatic event
notification). The \ :c:func:`megasas_issue_blocked_abort_cmd`\  issues such abort
cmd and waits for return status.
Max wait time is MEGASAS_INTERNAL_CMD_WAIT_TIME secs

.. _`megasas_make_sgl32`:

megasas_make_sgl32
==================

.. c:function:: int megasas_make_sgl32(struct megasas_instance *instance, struct scsi_cmnd *scp, union megasas_sgl *mfi_sgl)

    Prepares 32-bit SGL

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param struct scsi_cmnd \*scp:
        SCSI command from the mid-layer

    :param union megasas_sgl \*mfi_sgl:
        SGL to be filled in

.. _`megasas_make_sgl32.description`:

Description
-----------

If successful, this function returns the number of SG elements. Otherwise,
it returnes -1.

.. _`megasas_make_sgl64`:

megasas_make_sgl64
==================

.. c:function:: int megasas_make_sgl64(struct megasas_instance *instance, struct scsi_cmnd *scp, union megasas_sgl *mfi_sgl)

    Prepares 64-bit SGL

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param struct scsi_cmnd \*scp:
        SCSI command from the mid-layer

    :param union megasas_sgl \*mfi_sgl:
        SGL to be filled in

.. _`megasas_make_sgl64.description`:

Description
-----------

If successful, this function returns the number of SG elements. Otherwise,
it returnes -1.

.. _`megasas_make_sgl_skinny`:

megasas_make_sgl_skinny
=======================

.. c:function:: int megasas_make_sgl_skinny(struct megasas_instance *instance, struct scsi_cmnd *scp, union megasas_sgl *mfi_sgl)

    Prepares IEEE SGL

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param struct scsi_cmnd \*scp:
        SCSI command from the mid-layer

    :param union megasas_sgl \*mfi_sgl:
        SGL to be filled in

.. _`megasas_make_sgl_skinny.description`:

Description
-----------

If successful, this function returns the number of SG elements. Otherwise,
it returnes -1.

.. _`megasas_build_dcdb`:

megasas_build_dcdb
==================

.. c:function:: int megasas_build_dcdb(struct megasas_instance *instance, struct scsi_cmnd *scp, struct megasas_cmd *cmd)

    Prepares a direct cdb (DCDB) command

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param struct scsi_cmnd \*scp:
        SCSI command

    :param struct megasas_cmd \*cmd:
        Command to be prepared in

.. _`megasas_build_dcdb.description`:

Description
-----------

This function prepares CDB commands. These are typcially pass-through
commands to the devices.

.. _`megasas_build_ldio`:

megasas_build_ldio
==================

.. c:function:: int megasas_build_ldio(struct megasas_instance *instance, struct scsi_cmnd *scp, struct megasas_cmd *cmd)

    Prepares IOs to logical devices

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param struct scsi_cmnd \*scp:
        SCSI command

    :param struct megasas_cmd \*cmd:
        Command to be prepared

.. _`megasas_build_ldio.description`:

Description
-----------

Frames (and accompanying SGLs) for regular SCSI IOs use this function.

.. _`megasas_cmd_type`:

megasas_cmd_type
================

.. c:function:: int megasas_cmd_type(struct scsi_cmnd *cmd)

    Checks if the cmd is for logical drive/sysPD and whether it's RW or non RW

    :param struct scsi_cmnd \*cmd:
        *undescribed*

.. _`megasas_queue_command`:

megasas_queue_command
=====================

.. c:function:: int megasas_queue_command(struct Scsi_Host *shost, struct scsi_cmnd *scmd)

    Queue entry point

    :param struct Scsi_Host \*shost:
        *undescribed*

    :param struct scsi_cmnd \*scmd:
        SCSI command to be queued

.. _`megasas_complete_cmd_dpc`:

megasas_complete_cmd_dpc
========================

.. c:function:: void megasas_complete_cmd_dpc(unsigned long instance_addr)

    Returns FW's controller structure

    :param unsigned long instance_addr:
        Address of adapter soft state

.. _`megasas_complete_cmd_dpc.description`:

Description
-----------

Tasklet to complete cmds

.. _`megasas_start_timer`:

megasas_start_timer
===================

.. c:function:: void megasas_start_timer(struct megasas_instance *instance, struct timer_list *timer, void *fn, unsigned long interval)

    Initializes a timer object

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param struct timer_list \*timer:
        timer object to be initialized

    :param void \*fn:
        timer function

    :param unsigned long interval:
        time interval between timer function call

.. _`megasas_wait_for_outstanding`:

megasas_wait_for_outstanding
============================

.. c:function:: int megasas_wait_for_outstanding(struct megasas_instance *instance)

    Wait for all outstanding cmds

    :param struct megasas_instance \*instance:
        Adapter soft state

.. _`megasas_wait_for_outstanding.description`:

Description
-----------

This function waits for up to MEGASAS_RESET_WAIT_TIME seconds for FW to
complete all its outstanding commands. Returns error if one or more IOs
are pending after this time period. It also marks the controller dead.

.. _`megasas_generic_reset`:

megasas_generic_reset
=====================

.. c:function:: int megasas_generic_reset(struct scsi_cmnd *scmd)

    Generic reset routine

    :param struct scsi_cmnd \*scmd:
        Mid-layer SCSI command

.. _`megasas_generic_reset.description`:

Description
-----------

This routine implements a generic reset handler for device, bus and host
reset requests. Device, bus and host specific reset handlers can use this
function after they do their specific tasks.

.. _`megasas_reset_timer`:

megasas_reset_timer
===================

.. c:function:: enum blk_eh_timer_return megasas_reset_timer(struct scsi_cmnd *scmd)

    quiesce the adapter if required

    :param struct scsi_cmnd \*scmd:
        scsi cmnd

.. _`megasas_reset_timer.description`:

Description
-----------

Sets the FW busy flag and reduces the host->can_queue if the
cmd has not been completed within the timeout period.

.. _`megasas_dump_frame`:

megasas_dump_frame
==================

.. c:function:: void megasas_dump_frame(void *mpi_request, int sz)

    This function will dump MPT/MFI frame

    :param void \*mpi_request:
        *undescribed*

    :param int sz:
        *undescribed*

.. _`megasas_reset_bus_host`:

megasas_reset_bus_host
======================

.. c:function:: int megasas_reset_bus_host(struct scsi_cmnd *scmd)

    Bus & host reset handler entry point

    :param struct scsi_cmnd \*scmd:
        *undescribed*

.. _`megasas_task_abort`:

megasas_task_abort
==================

.. c:function:: int megasas_task_abort(struct scsi_cmnd *scmd)

    Issues task abort request to firmware (supported only for fusion adapters)

    :param struct scsi_cmnd \*scmd:
        SCSI command pointer

.. _`megasas_reset_target`:

megasas_reset_target
====================

.. c:function:: int megasas_reset_target(struct scsi_cmnd *scmd)

    Issues target reset request to firmware (supported only for fusion adapters)

    :param struct scsi_cmnd \*scmd:
        SCSI command pointer

.. _`megasas_bios_param`:

megasas_bios_param
==================

.. c:function:: int megasas_bios_param(struct scsi_device *sdev, struct block_device *bdev, sector_t capacity, int geom[])

    Returns disk geometry for a disk

    :param struct scsi_device \*sdev:
        device handle

    :param struct block_device \*bdev:
        block device

    :param sector_t capacity:
        drive capacity

    :param int geom:
        geometry parameters

.. _`megasas_service_aen`:

megasas_service_aen
===================

.. c:function:: void megasas_service_aen(struct megasas_instance *instance, struct megasas_cmd *cmd)

    Processes an event notification

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param struct megasas_cmd \*cmd:
        AEN command completed by the ISR

.. _`megasas_service_aen.description`:

Description
-----------

For AEN, driver sends a command down to FW that is held by the FW till an
event occurs. When an event of interest occurs, FW completes the command
that it was previously holding.

This routines sends SIGIO signal to processes that have registered with the
driver for AEN.

.. _`megasas_complete_int_cmd`:

megasas_complete_int_cmd
========================

.. c:function:: void megasas_complete_int_cmd(struct megasas_instance *instance, struct megasas_cmd *cmd)

    Completes an internal command

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param struct megasas_cmd \*cmd:
        Command to be completed

.. _`megasas_complete_int_cmd.description`:

Description
-----------

The \ :c:func:`megasas_issue_blocked_cmd`\  function waits for a command to complete
after it issues a command. This function wakes up that waiting routine by
calling \ :c:func:`wake_up`\  on the wait queue.

.. _`megasas_complete_abort`:

megasas_complete_abort
======================

.. c:function:: void megasas_complete_abort(struct megasas_instance *instance, struct megasas_cmd *cmd)

    Completes aborting a command

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param struct megasas_cmd \*cmd:
        Cmd that was issued to abort another cmd

.. _`megasas_complete_abort.description`:

Description
-----------

The \ :c:func:`megasas_issue_blocked_abort_cmd`\  function waits on abort_cmd_wait_q
after it issues an abort on a previously issued command. This function
wakes up all functions waiting on the same wait queue.

.. _`megasas_complete_cmd`:

megasas_complete_cmd
====================

.. c:function:: void megasas_complete_cmd(struct megasas_instance *instance, struct megasas_cmd *cmd, u8 alt_status)

    Completes a command

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param struct megasas_cmd \*cmd:
        Command to be completed

    :param u8 alt_status:
        If non-zero, use this value as status to
        SCSI mid-layer instead of the value returned
        by the FW. This should be used if caller wants
        an alternate status (as in the case of aborted
        commands)

.. _`megasas_issue_pending_cmds_again`:

megasas_issue_pending_cmds_again
================================

.. c:function:: void megasas_issue_pending_cmds_again(struct megasas_instance *instance)

    issue all pending cmds in FW again because of the fw reset

    :param struct megasas_instance \*instance:
        Adapter soft state

.. _`megasas_internal_reset_defer_cmds`:

megasas_internal_reset_defer_cmds
=================================

.. c:function:: void megasas_internal_reset_defer_cmds(struct megasas_instance *instance)

    :param struct megasas_instance \*instance:
        *undescribed*

.. _`megasas_internal_reset_defer_cmds.description`:

Description
-----------

We move the commands pending at internal reset time to a
pending queue. This queue would be flushed after successful
completion of the internal reset sequence. if the internal reset
did not complete in time, the kernel reset handler would flush
these commands.

.. _`megasas_deplete_reply_queue`:

megasas_deplete_reply_queue
===========================

.. c:function:: int megasas_deplete_reply_queue(struct megasas_instance *instance, u8 alt_status)

    Processes all completed commands

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param u8 alt_status:
        Alternate status to be returned to
        SCSI mid-layer instead of the status
        returned by the FW

.. _`megasas_deplete_reply_queue.note`:

Note
----

this must be called with hba lock held

.. _`megasas_isr`:

megasas_isr
===========

.. c:function:: irqreturn_t megasas_isr(int irq, void *devp)

    isr entry point

    :param int irq:
        *undescribed*

    :param void \*devp:
        *undescribed*

.. _`megasas_transition_to_ready`:

megasas_transition_to_ready
===========================

.. c:function:: int megasas_transition_to_ready(struct megasas_instance *instance, int ocr)

    Move the FW to READY state

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param int ocr:
        *undescribed*

.. _`megasas_transition_to_ready.description`:

Description
-----------

During the initialization, FW passes can potentially be in any one of
several possible states. If the FW in operational, waiting-for-handshake
states, driver must take steps to bring it to ready state. Otherwise, it
has to wait for the ready state.

.. _`megasas_teardown_frame_pool`:

megasas_teardown_frame_pool
===========================

.. c:function:: void megasas_teardown_frame_pool(struct megasas_instance *instance)

    Destroy the cmd frame DMA pool

    :param struct megasas_instance \*instance:
        Adapter soft state

.. _`megasas_create_frame_pool`:

megasas_create_frame_pool
=========================

.. c:function:: int megasas_create_frame_pool(struct megasas_instance *instance)

    Creates DMA pool for cmd frames

    :param struct megasas_instance \*instance:
        Adapter soft state

.. _`megasas_create_frame_pool.description`:

Description
-----------

Each command packet has an embedded DMA memory buffer that is used for
filling MFI frame and the SG list that immediately follows the frame. This
function creates those DMA memory buffers for each command packet by using
PCI pool facility.

.. _`megasas_free_cmds`:

megasas_free_cmds
=================

.. c:function:: void megasas_free_cmds(struct megasas_instance *instance)

    Free all the cmds in the free cmd pool

    :param struct megasas_instance \*instance:
        Adapter soft state

.. _`megasas_alloc_cmds`:

megasas_alloc_cmds
==================

.. c:function:: int megasas_alloc_cmds(struct megasas_instance *instance)

    Allocates the command packets

    :param struct megasas_instance \*instance:
        Adapter soft state

.. _`megasas_alloc_cmds.description`:

Description
-----------

Each command that is issued to the FW, whether IO commands from the OS or
internal commands like IOCTLs, are wrapped in local data structure called
megasas_cmd. The frame embedded in this megasas_cmd is actually issued to
the FW.

Each frame has a 32-bit field called context (tag). This context is used
to get back the megasas_cmd from the frame when a frame gets completed in
the ISR. Typically the address of the megasas_cmd itself would be used as
the context. But we wanted to keep the differences between 32 and 64 bit
systems to the mininum. We always use 32 bit integers for the context. In
this driver, the 32 bit values are the indices into an array cmd_list.
This array is used only to look up the megasas_cmd given the context. The
free commands themselves are maintained in a linked list called cmd_pool.

.. _`megasas_ld_list_query`:

megasas_ld_list_query
=====================

.. c:function:: int megasas_ld_list_query(struct megasas_instance *instance, u8 query_type)

    Returns FW's ld_list structure

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param u8 query_type:
        *undescribed*

.. _`megasas_ld_list_query.description`:

Description
-----------

Issues an internal command (DCMD) to get the FW's controller PD
list structure.  This information is mainly used to find out SYSTEM
supported by the FW.

.. _`megasas_get_ctrl_info`:

megasas_get_ctrl_info
=====================

.. c:function:: int megasas_get_ctrl_info(struct megasas_instance *instance)

    Returns FW's controller structure

    :param struct megasas_instance \*instance:
        Adapter soft state

.. _`megasas_get_ctrl_info.description`:

Description
-----------

Issues an internal command (DCMD) to get the FW's controller structure.
This information is mainly used to find out the maximum IO transfer per
command supported by the FW.

.. _`megasas_issue_init_mfi`:

megasas_issue_init_mfi
======================

.. c:function:: int megasas_issue_init_mfi(struct megasas_instance *instance)

    Initializes the FW

    :param struct megasas_instance \*instance:
        Adapter soft state

.. _`megasas_issue_init_mfi.description`:

Description
-----------

Issues the INIT MFI cmd

.. _`megasas_setup_irqs_msix`:

megasas_setup_irqs_msix
=======================

.. c:function:: int megasas_setup_irqs_msix(struct megasas_instance *instance, u8 is_probe)

    register MSI-x interrupts.

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param u8 is_probe:
        Driver probe check

.. _`megasas_setup_irqs_msix.description`:

Description
-----------

Do not enable interrupt, only setup ISRs.

Return 0 on success.

.. _`megasas_setup_jbod_map`:

megasas_setup_jbod_map
======================

.. c:function:: void megasas_setup_jbod_map(struct megasas_instance *instance)

    setup jbod map for FP seq_number.

    :param struct megasas_instance \*instance:
        Adapter soft state

.. _`megasas_setup_jbod_map.description`:

Description
-----------

Return 0 on success.

.. _`megasas_init_fw`:

megasas_init_fw
===============

.. c:function:: int megasas_init_fw(struct megasas_instance *instance)

    Initializes the FW

    :param struct megasas_instance \*instance:
        Adapter soft state

.. _`megasas_init_fw.description`:

Description
-----------

This is the main function for initializing firmware

.. _`megasas_release_mfi`:

megasas_release_mfi
===================

.. c:function:: void megasas_release_mfi(struct megasas_instance *instance)

    Reverses the FW initialization

    :param struct megasas_instance \*instance:
        Adapter soft state

.. _`megasas_get_seq_num`:

megasas_get_seq_num
===================

.. c:function:: int megasas_get_seq_num(struct megasas_instance *instance, struct megasas_evt_log_info *eli)

    Gets latest event sequence numbers

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param struct megasas_evt_log_info \*eli:
        FW event log sequence numbers information

.. _`megasas_get_seq_num.description`:

Description
-----------

FW maintains a log of all events in a non-volatile area. Upper layers would
usually find out the latest sequence number of the events, the seq number at
the boot etc. They would "read" all the events below the latest seq number
by issuing a direct fw cmd (DCMD). For the future events (beyond latest seq
number), they would subsribe to AEN (asynchronous event notification) and
wait for the events to happen.

.. _`megasas_register_aen`:

megasas_register_aen
====================

.. c:function:: int megasas_register_aen(struct megasas_instance *instance, u32 seq_num, u32 class_locale_word)

    Registers for asynchronous event notification

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param u32 seq_num:
        The starting sequence number

    :param u32 class_locale_word:
        *undescribed*

.. _`megasas_register_aen.description`:

Description
-----------

This function subscribes for AEN for events beyond the \ ``seq_num``\ . It requests
to be notified if and only if the event is of type \ ``class_locale``\ 

.. _`megasas_start_aen`:

megasas_start_aen
=================

.. c:function:: int megasas_start_aen(struct megasas_instance *instance)

    Subscribes to AEN during driver load time

    :param struct megasas_instance \*instance:
        Adapter soft state

.. _`megasas_io_attach`:

megasas_io_attach
=================

.. c:function:: int megasas_io_attach(struct megasas_instance *instance)

    Attaches this driver to SCSI mid-layer

    :param struct megasas_instance \*instance:
        Adapter soft state

.. _`megasas_probe_one`:

megasas_probe_one
=================

.. c:function:: int megasas_probe_one(struct pci_dev *pdev, const struct pci_device_id *id)

    PCI hotplug entry point

    :param struct pci_dev \*pdev:
        PCI device structure

    :param const struct pci_device_id \*id:
        PCI ids of supported hotplugged adapter

.. _`megasas_flush_cache`:

megasas_flush_cache
===================

.. c:function:: void megasas_flush_cache(struct megasas_instance *instance)

    Requests FW to flush all its caches

    :param struct megasas_instance \*instance:
        Adapter soft state

.. _`megasas_shutdown_controller`:

megasas_shutdown_controller
===========================

.. c:function:: void megasas_shutdown_controller(struct megasas_instance *instance, u32 opcode)

    Instructs FW to shutdown the controller

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param u32 opcode:
        Shutdown/Hibernate

.. _`megasas_suspend`:

megasas_suspend
===============

.. c:function:: int megasas_suspend(struct pci_dev *pdev, pm_message_t state)

    driver suspend entry point

    :param struct pci_dev \*pdev:
        PCI device structure

    :param pm_message_t state:
        PCI power state to suspend routine

.. _`megasas_resume`:

megasas_resume
==============

.. c:function:: int megasas_resume(struct pci_dev *pdev)

    driver resume entry point

    :param struct pci_dev \*pdev:
        PCI device structure

.. _`megasas_detach_one`:

megasas_detach_one
==================

.. c:function:: void megasas_detach_one(struct pci_dev *pdev)

    PCI hot"un"plug entry point

    :param struct pci_dev \*pdev:
        PCI device structure

.. _`megasas_shutdown`:

megasas_shutdown
================

.. c:function:: void megasas_shutdown(struct pci_dev *pdev)

    Shutdown entry point

    :param struct pci_dev \*pdev:
        *undescribed*

.. _`megasas_mgmt_open`:

megasas_mgmt_open
=================

.. c:function:: int megasas_mgmt_open(struct inode *inode, struct file *filep)

    char node "open" entry point

    :param struct inode \*inode:
        *undescribed*

    :param struct file \*filep:
        *undescribed*

.. _`megasas_mgmt_fasync`:

megasas_mgmt_fasync
===================

.. c:function:: int megasas_mgmt_fasync(int fd, struct file *filep, int mode)

    Async notifier registration from applications

    :param int fd:
        *undescribed*

    :param struct file \*filep:
        *undescribed*

    :param int mode:
        *undescribed*

.. _`megasas_mgmt_fasync.description`:

Description
-----------

This function adds the calling process to a driver global queue. When an
event occurs, SIGIO will be sent to all processes in this queue.

.. _`megasas_mgmt_poll`:

megasas_mgmt_poll
=================

.. c:function:: unsigned int megasas_mgmt_poll(struct file *file, poll_table *wait)

    char node "poll" entry point

    :param struct file \*file:
        *undescribed*

    :param poll_table \*wait:
        *undescribed*

.. _`megasas_mgmt_fw_ioctl`:

megasas_mgmt_fw_ioctl
=====================

.. c:function:: int megasas_mgmt_fw_ioctl(struct megasas_instance *instance, struct megasas_iocpacket __user *user_ioc, struct megasas_iocpacket *ioc)

    Issues management ioctls to FW

    :param struct megasas_instance \*instance:
        Adapter soft state

    :param struct megasas_iocpacket __user \*user_ioc:
        *undescribed*

    :param struct megasas_iocpacket \*ioc:
        *undescribed*

.. _`megasas_mgmt_ioctl`:

megasas_mgmt_ioctl
==================

.. c:function:: long megasas_mgmt_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    char node ioctl entry point

    :param struct file \*file:
        *undescribed*

    :param unsigned int cmd:
        *undescribed*

    :param unsigned long arg:
        *undescribed*

.. _`megasas_init`:

megasas_init
============

.. c:function:: int megasas_init( void)

    Driver load entry point

    :param  void:
        no arguments

.. _`megasas_exit`:

megasas_exit
============

.. c:function:: void __exit megasas_exit( void)

    Driver unload entry point

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

