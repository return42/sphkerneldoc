.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/pmcraid.c

.. _`pmcraid_slave_alloc`:

pmcraid_slave_alloc
===================

.. c:function:: int pmcraid_slave_alloc(struct scsi_device *scsi_dev)

    Prepare for commands to a device

    :param scsi_dev:
        scsi device struct
    :type scsi_dev: struct scsi_device \*

.. _`pmcraid_slave_alloc.description`:

Description
-----------

This function is called by mid-layer prior to sending any command to the new
device. Stores resource entry details of the device in scsi_device struct.
Queuecommand uses the resource handle and other details to fill up IOARCB
while sending commands to the device.

.. _`pmcraid_slave_alloc.return-value`:

Return value
------------

0 on success / -ENXIO if device does not exist

.. _`pmcraid_slave_configure`:

pmcraid_slave_configure
=======================

.. c:function:: int pmcraid_slave_configure(struct scsi_device *scsi_dev)

    Configures a SCSI device

    :param scsi_dev:
        scsi device struct
    :type scsi_dev: struct scsi_device \*

.. _`pmcraid_slave_configure.description`:

Description
-----------

This function is executed by SCSI mid layer just after a device is first
scanned (i.e. it has responded to an INQUIRY). For VSET resources, the
timeout value (default 30s) will be over-written to a higher value (60s)
and max_sectors value will be over-written to 512. It also sets queue depth
to host->cmd_per_lun value

.. _`pmcraid_slave_configure.return-value`:

Return value
------------

0 on success

.. _`pmcraid_slave_destroy`:

pmcraid_slave_destroy
=====================

.. c:function:: void pmcraid_slave_destroy(struct scsi_device *scsi_dev)

    Unconfigure a SCSI device before removing it

    :param scsi_dev:
        scsi device struct
    :type scsi_dev: struct scsi_device \*

.. _`pmcraid_slave_destroy.description`:

Description
-----------

This is called by mid-layer before removing a device. Pointer assignments
done in pmcraid_slave_alloc will be reset to NULL here.

Return value
none

.. _`pmcraid_change_queue_depth`:

pmcraid_change_queue_depth
==========================

.. c:function:: int pmcraid_change_queue_depth(struct scsi_device *scsi_dev, int depth)

    Change the device's queue depth

    :param scsi_dev:
        scsi device struct
    :type scsi_dev: struct scsi_device \*

    :param depth:
        depth to set
    :type depth: int

.. _`pmcraid_change_queue_depth.description`:

Description
-----------

Return value
actual depth set

.. _`pmcraid_init_cmdblk`:

pmcraid_init_cmdblk
===================

.. c:function:: void pmcraid_init_cmdblk(struct pmcraid_cmd *cmd, int index)

    initializes a command block

    :param cmd:
        pointer to struct pmcraid_cmd to be initialized
    :type cmd: struct pmcraid_cmd \*

    :param index:
        if >=0 first time initialization; otherwise reinitialization
    :type index: int

.. _`pmcraid_init_cmdblk.description`:

Description
-----------

Return Value
None

.. _`pmcraid_reinit_cmdblk`:

pmcraid_reinit_cmdblk
=====================

.. c:function:: void pmcraid_reinit_cmdblk(struct pmcraid_cmd *cmd)

    reinitialize a command block

    :param cmd:
        pointer to struct pmcraid_cmd to be reinitialized
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_reinit_cmdblk.description`:

Description
-----------

Return Value
None

.. _`pmcraid_get_free_cmd`:

pmcraid_get_free_cmd
====================

.. c:function:: struct pmcraid_cmd *pmcraid_get_free_cmd(struct pmcraid_instance *pinstance)

    get a free cmd block from command block pool

    :param pinstance:
        adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_get_free_cmd.return-value`:

Return Value
------------

returns pointer to cmd block or NULL if no blocks are available

.. _`pmcraid_return_cmd`:

pmcraid_return_cmd
==================

.. c:function:: void pmcraid_return_cmd(struct pmcraid_cmd *cmd)

    return a completed command block back into free pool

    :param cmd:
        pointer to the command block
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_return_cmd.return-value`:

Return Value
------------

nothing

.. _`pmcraid_read_interrupts`:

pmcraid_read_interrupts
=======================

.. c:function:: u32 pmcraid_read_interrupts(struct pmcraid_instance *pinstance)

    reads IOA interrupts

    :param pinstance:
        pointer to adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_read_interrupts.description`:

Description
-----------

Return value
interrupts read from IOA

.. _`pmcraid_disable_interrupts`:

pmcraid_disable_interrupts
==========================

.. c:function:: void pmcraid_disable_interrupts(struct pmcraid_instance *pinstance, u32 intrs)

    Masks and clears all specified interrupts

    :param pinstance:
        pointer to per adapter instance structure
    :type pinstance: struct pmcraid_instance \*

    :param intrs:
        interrupts to disable
    :type intrs: u32

.. _`pmcraid_disable_interrupts.description`:

Description
-----------

Return Value
None

.. _`pmcraid_enable_interrupts`:

pmcraid_enable_interrupts
=========================

.. c:function:: void pmcraid_enable_interrupts(struct pmcraid_instance *pinstance, u32 intrs)

    Enables specified interrupts

    :param pinstance:
        pointer to per adapter instance structure
    :type pinstance: struct pmcraid_instance \*

    :param intrs:
        *undescribed*
    :type intrs: u32

.. _`pmcraid_enable_interrupts.description`:

Description
-----------

Return Value
None

.. _`pmcraid_clr_trans_op`:

pmcraid_clr_trans_op
====================

.. c:function:: void pmcraid_clr_trans_op(struct pmcraid_instance *pinstance)

    clear trans to op interrupt

    :param pinstance:
        pointer to per adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_clr_trans_op.description`:

Description
-----------

Return Value
None

.. _`pmcraid_reset_type`:

pmcraid_reset_type
==================

.. c:function:: void pmcraid_reset_type(struct pmcraid_instance *pinstance)

    Determine the required reset type

    :param pinstance:
        pointer to adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_reset_type.description`:

Description
-----------

IOA requires hard reset if any of the following conditions is true.
1. If HRRQ valid interrupt is not masked
2. IOA reset alert doorbell is set
3. If there are any error interrupts

.. _`pmcraid_ioa_reset`:

pmcraid_ioa_reset
=================

.. c:function:: void pmcraid_ioa_reset(struct pmcraid_cmd *)

    completion function for PCI BIST

    :param :
        *undescribed*
    :type : struct pmcraid_cmd \*

.. _`pmcraid_start_bist`:

pmcraid_start_bist
==================

.. c:function:: void pmcraid_start_bist(struct pmcraid_cmd *cmd)

    starts BIST

    :param cmd:
        pointer to reset cmd
        Return Value
        none
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_reset_alert_done`:

pmcraid_reset_alert_done
========================

.. c:function:: void pmcraid_reset_alert_done(struct timer_list *t)

    completion routine for reset_alert

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`pmcraid_notify_ioastate`:

pmcraid_notify_ioastate
=======================

.. c:function:: void pmcraid_notify_ioastate(struct pmcraid_instance *,  u32)

    alerts IOA for a possible reset

    :param :
        *undescribed*
    :type : struct pmcraid_instance \*

    :param u32:
        *undescribed*
    :type u32: 

.. _`pmcraid_notify_ioastate.description`:

Description
-----------

Return Value
returns 0 if pci config-space is accessible and RESET_DOORBELL is
successfully written to IOA. Returns non-zero in case pci_config_space
is not accessible

.. _`pmcraid_timeout_handler`:

pmcraid_timeout_handler
=======================

.. c:function:: void pmcraid_timeout_handler(struct timer_list *t)

    Timeout handler for internally generated ops

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`pmcraid_timeout_handler.description`:

Description
-----------

This function blocks host requests and initiates an adapter reset.

.. _`pmcraid_timeout_handler.return-value`:

Return value
------------

None

.. _`pmcraid_internal_done`:

pmcraid_internal_done
=====================

.. c:function:: void pmcraid_internal_done(struct pmcraid_cmd *cmd)

    completion routine for internally generated cmds

    :param cmd:
        command that got response from IOA
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_internal_done.return-value`:

Return Value
------------

none

.. _`pmcraid_reinit_cfgtable_done`:

pmcraid_reinit_cfgtable_done
============================

.. c:function:: void pmcraid_reinit_cfgtable_done(struct pmcraid_cmd *cmd)

    done function for cfg table reinitialization

    :param cmd:
        command that got response from IOA
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_reinit_cfgtable_done.description`:

Description
-----------

This routine is called after driver re-reads configuration table due to a
lost CCN. It returns the command block back to free pool and schedules
worker thread to add/delete devices into the system.

.. _`pmcraid_reinit_cfgtable_done.return-value`:

Return Value
------------

none

.. _`pmcraid_erp_done`:

pmcraid_erp_done
================

.. c:function:: void pmcraid_erp_done(struct pmcraid_cmd *cmd)

    Process completion of SCSI error response from device

    :param cmd:
        pmcraid_command
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_erp_done.description`:

Description
-----------

This function copies the sense buffer into the scsi_cmd struct and completes
scsi_cmd by calling scsi_done function.

.. _`pmcraid_erp_done.return-value`:

Return value
------------

none

.. _`_pmcraid_fire_command`:

\_pmcraid_fire_command
======================

.. c:function:: void _pmcraid_fire_command(struct pmcraid_cmd *cmd)

    sends an IOA command to adapter

    :param cmd:
        command to be sent to the device
    :type cmd: struct pmcraid_cmd \*

.. _`_pmcraid_fire_command.description`:

Description
-----------

This function adds the given block into pending command list
and returns without waiting

Return Value
None

.. _`pmcraid_send_cmd`:

pmcraid_send_cmd
================

.. c:function:: void pmcraid_send_cmd(struct pmcraid_cmd *cmd, void (*cmd_done)(struct pmcraid_cmd *), unsigned long timeout, void (*timeout_func)(struct timer_list *))

    fires a command to IOA

    :param cmd:
        pointer to the command block to be fired to IOA
    :type cmd: struct pmcraid_cmd \*

    :param void (\*cmd_done)(struct pmcraid_cmd \*):
        command completion function, called once IOA responds

    :param timeout:
        timeout to wait for this command completion
    :type timeout: unsigned long

    :param void (\*timeout_func)(struct timer_list \*):
        timeout handler

.. _`pmcraid_send_cmd.description`:

Description
-----------

This function also sets up timeout function, and command completion
function

Return value
none

.. _`pmcraid_ioa_shutdown_done`:

pmcraid_ioa_shutdown_done
=========================

.. c:function:: void pmcraid_ioa_shutdown_done(struct pmcraid_cmd *cmd)

    completion function for IOA shutdown command

    :param cmd:
        pointer to the command block used for sending IOA shutdown command
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_ioa_shutdown_done.description`:

Description
-----------

Return value
None

.. _`pmcraid_ioa_shutdown`:

pmcraid_ioa_shutdown
====================

.. c:function:: void pmcraid_ioa_shutdown(struct pmcraid_cmd *cmd)

    sends SHUTDOWN command to ioa

    :param cmd:
        pointer to the command block used as part of reset sequence
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_ioa_shutdown.description`:

Description
-----------

Return Value
None

.. _`pmcraid_querycfg`:

pmcraid_querycfg
================

.. c:function:: void pmcraid_querycfg(struct pmcraid_cmd *)

    completion function for get_fwversion

    :param :
        *undescribed*
    :type : struct pmcraid_cmd \*

.. _`pmcraid_querycfg.description`:

Description
-----------

Return Value
none

.. _`pmcraid_get_fwversion`:

pmcraid_get_fwversion
=====================

.. c:function:: void pmcraid_get_fwversion(struct pmcraid_cmd *cmd)

    reads firmware version information

    :param cmd:
        pointer to command block used to send INQUIRY command
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_get_fwversion.description`:

Description
-----------

Return Value
none

.. _`pmcraid_identify_hrrq`:

pmcraid_identify_hrrq
=====================

.. c:function:: void pmcraid_identify_hrrq(struct pmcraid_cmd *cmd)

    registers host rrq buffers with IOA

    :param cmd:
        pointer to command block to be used for identify hrrq
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_identify_hrrq.description`:

Description
-----------

Return Value
none

.. _`pmcraid_send_hcam_cmd`:

pmcraid_send_hcam_cmd
=====================

.. c:function:: void pmcraid_send_hcam_cmd(struct pmcraid_cmd *cmd)

    send an initialized command block(HCAM) to IOA

    :param cmd:
        initialized command block pointer
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_send_hcam_cmd.description`:

Description
-----------

Return Value
none

.. _`pmcraid_init_hcam`:

pmcraid_init_hcam
=================

.. c:function:: struct pmcraid_cmd *pmcraid_init_hcam(struct pmcraid_instance *pinstance, u8 type)

    send an initialized command block(HCAM) to IOA

    :param pinstance:
        pointer to adapter instance structure
    :type pinstance: struct pmcraid_instance \*

    :param type:
        HCAM type
    :type type: u8

.. _`pmcraid_init_hcam.description`:

Description
-----------

Return Value
pointer to initialized pmcraid_cmd structure or NULL

.. _`pmcraid_send_hcam`:

pmcraid_send_hcam
=================

.. c:function:: void pmcraid_send_hcam(struct pmcraid_instance *pinstance, u8 type)

    Send an HCAM to IOA

    :param pinstance:
        ioa config struct
    :type pinstance: struct pmcraid_instance \*

    :param type:
        HCAM type
    :type type: u8

.. _`pmcraid_send_hcam.description`:

Description
-----------

This function will send a Host Controlled Async command to IOA.

.. _`pmcraid_send_hcam.return-value`:

Return value
------------

none

.. _`pmcraid_prepare_cancel_cmd`:

pmcraid_prepare_cancel_cmd
==========================

.. c:function:: void pmcraid_prepare_cancel_cmd(struct pmcraid_cmd *cmd, struct pmcraid_cmd *cmd_to_cancel)

    prepares a command block to abort another

    :param cmd:
        pointer to cmd that is used as cancelling command
    :type cmd: struct pmcraid_cmd \*

    :param cmd_to_cancel:
        pointer to the command that needs to be cancelled
    :type cmd_to_cancel: struct pmcraid_cmd \*

.. _`pmcraid_cancel_hcam`:

pmcraid_cancel_hcam
===================

.. c:function:: void pmcraid_cancel_hcam(struct pmcraid_cmd *cmd, u8 type, void (*cmd_done)(struct pmcraid_cmd *))

    sends ABORT task to abort a given HCAM

    :param cmd:
        command to be used as cancelling command
    :type cmd: struct pmcraid_cmd \*

    :param type:
        HCAM type
    :type type: u8

    :param void (\*cmd_done)(struct pmcraid_cmd \*):
        op done function for the cancelling command

.. _`pmcraid_cancel_ccn`:

pmcraid_cancel_ccn
==================

.. c:function:: void pmcraid_cancel_ccn(struct pmcraid_cmd *cmd)

    cancel CCN HCAM already registered with IOA

    :param cmd:
        command block to be used for cancelling the HCAM
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_cancel_ldn`:

pmcraid_cancel_ldn
==================

.. c:function:: void pmcraid_cancel_ldn(struct pmcraid_cmd *cmd)

    cancel LDN HCAM already registered with IOA

    :param cmd:
        command block to be used for cancelling the HCAM
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_expose_resource`:

pmcraid_expose_resource
=======================

.. c:function:: int pmcraid_expose_resource(u16 fw_version, struct pmcraid_config_table_entry *cfgte)

    check if the resource can be exposed to OS

    :param fw_version:
        firmware version code
    :type fw_version: u16

    :param cfgte:
        pointer to configuration table entry of the resource
    :type cfgte: struct pmcraid_config_table_entry \*

.. _`pmcraid_expose_resource.return-value`:

Return value
------------

true if resource can be added to midlayer, false(0) otherwise

.. _`pmcraid_netlink_init`:

pmcraid_netlink_init
====================

.. c:function:: int pmcraid_netlink_init( void)

    registers pmcraid_event_family

    :param void:
        no arguments
    :type void: 

.. _`pmcraid_netlink_init.return-value`:

Return value
------------

0 if the pmcraid_event_family is successfully registered
with netlink generic, non-zero otherwise

.. _`pmcraid_netlink_release`:

pmcraid_netlink_release
=======================

.. c:function:: void pmcraid_netlink_release( void)

    unregisters pmcraid_event_family

    :param void:
        no arguments
    :type void: 

.. _`pmcraid_netlink_release.return-value`:

Return value
------------

none

.. _`pmcraid_notify_aen`:

pmcraid_notify_aen
==================

.. c:function:: int pmcraid_notify_aen(struct pmcraid_instance *pinstance, struct pmcraid_aen_msg *aen_msg, u32 data_size)

    sends event msg to user space application

    :param pinstance:
        pointer to adapter instance structure
    :type pinstance: struct pmcraid_instance \*

    :param aen_msg:
        *undescribed*
    :type aen_msg: struct pmcraid_aen_msg \*

    :param data_size:
        *undescribed*
    :type data_size: u32

.. _`pmcraid_notify_aen.return-value`:

Return value
------------

0 if success, error value in case of any failure.

.. _`pmcraid_notify_ccn`:

pmcraid_notify_ccn
==================

.. c:function:: int pmcraid_notify_ccn(struct pmcraid_instance *pinstance)

    notifies about CCN event msg to user space

    :param pinstance:
        pointer adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_notify_ccn.return-value`:

Return value
------------

0 if success, error value in case of any failure

.. _`pmcraid_notify_ldn`:

pmcraid_notify_ldn
==================

.. c:function:: int pmcraid_notify_ldn(struct pmcraid_instance *pinstance)

    notifies about CCN event msg to user space

    :param pinstance:
        pointer adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_notify_ldn.return-value`:

Return value
------------

0 if success, error value in case of any failure

.. _`pmcraid_notify_ioastate`:

pmcraid_notify_ioastate
=======================

.. c:function:: void pmcraid_notify_ioastate(struct pmcraid_instance *pinstance, u32 evt)

    sends IOA state event msg to user space

    :param pinstance:
        pointer adapter instance structure
    :type pinstance: struct pmcraid_instance \*

    :param evt:
        controller state event to be sent
    :type evt: u32

.. _`pmcraid_notify_ioastate.return-value`:

Return value
------------

0 if success, error value in case of any failure

.. _`pmcraid_handle_config_change`:

pmcraid_handle_config_change
============================

.. c:function:: void pmcraid_handle_config_change(struct pmcraid_instance *pinstance)

    Handle a config change from the adapter

    :param pinstance:
        pointer to per adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_handle_config_change.return-value`:

Return value
------------

none

.. _`pmcraid_get_error_info`:

pmcraid_get_error_info
======================

.. c:function:: struct pmcraid_ioasc_error *pmcraid_get_error_info(u32 ioasc)

    return error string for an ioasc

    :param ioasc:
        ioasc code
        Return Value
        none
    :type ioasc: u32

.. _`pmcraid_ioasc_logger`:

pmcraid_ioasc_logger
====================

.. c:function:: void pmcraid_ioasc_logger(u32 ioasc, struct pmcraid_cmd *cmd)

    log IOASC information based user-settings

    :param ioasc:
        ioasc code
    :type ioasc: u32

    :param cmd:
        pointer to command that resulted in 'ioasc'
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_handle_error_log`:

pmcraid_handle_error_log
========================

.. c:function:: void pmcraid_handle_error_log(struct pmcraid_instance *pinstance)

    Handle a config change (error log) from the IOA

    :param pinstance:
        pointer to per adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_handle_error_log.return-value`:

Return value
------------

none

.. _`pmcraid_process_ccn`:

pmcraid_process_ccn
===================

.. c:function:: void pmcraid_process_ccn(struct pmcraid_cmd *cmd)

    Op done function for a CCN.

    :param cmd:
        pointer to command struct
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_process_ccn.description`:

Description
-----------

This function is the op done function for a configuration
change notification

.. _`pmcraid_process_ccn.return-value`:

Return value
------------

none

.. _`pmcraid_initiate_reset`:

pmcraid_initiate_reset
======================

.. c:function:: void pmcraid_initiate_reset(struct pmcraid_instance *)

    op done function for an LDN

    :param :
        *undescribed*
    :type : struct pmcraid_instance \*

.. _`pmcraid_initiate_reset.description`:

Description
-----------

Return value
none

.. _`pmcraid_register_hcams`:

pmcraid_register_hcams
======================

.. c:function:: void pmcraid_register_hcams(struct pmcraid_instance *pinstance)

    register HCAMs for CCN and LDN

    :param pinstance:
        pointer per adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_register_hcams.description`:

Description
-----------

Return Value
none

.. _`pmcraid_unregister_hcams`:

pmcraid_unregister_hcams
========================

.. c:function:: void pmcraid_unregister_hcams(struct pmcraid_cmd *cmd)

    cancel HCAMs registered already

    :param cmd:
        pointer to command used as part of reset sequence
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_reinit_buffers`:

pmcraid_reinit_buffers
======================

.. c:function:: void pmcraid_reinit_buffers(struct pmcraid_instance *)

    re-enable IOA after a hard reset

    :param :
        *undescribed*
    :type : struct pmcraid_instance \*

.. _`pmcraid_soft_reset`:

pmcraid_soft_reset
==================

.. c:function:: void pmcraid_soft_reset(struct pmcraid_cmd *cmd)

    performs a soft reset and makes IOA become ready

    :param cmd:
        pointer to reset command block
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_soft_reset.description`:

Description
-----------

Return Value
none

.. _`pmcraid_get_dump`:

pmcraid_get_dump
================

.. c:function:: void pmcraid_get_dump(struct pmcraid_instance *pinstance)

    retrieves IOA dump in case of Unit Check interrupt

    :param pinstance:
        pointer to adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_get_dump.description`:

Description
-----------

Return Value
none

.. _`pmcraid_fail_outstanding_cmds`:

pmcraid_fail_outstanding_cmds
=============================

.. c:function:: void pmcraid_fail_outstanding_cmds(struct pmcraid_instance *pinstance)

    Fails all outstanding ops.

    :param pinstance:
        pointer to adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_fail_outstanding_cmds.description`:

Description
-----------

This function fails all outstanding ops. If they are submitted to IOA
already, it sends cancel all messages if IOA is still accepting IOARCBs,
otherwise just completes the commands and returns the cmd blocks to free
pool.

.. _`pmcraid_fail_outstanding_cmds.return-value`:

Return value
------------

none

.. _`pmcraid_ioa_reset`:

pmcraid_ioa_reset
=================

.. c:function:: void pmcraid_ioa_reset(struct pmcraid_cmd *cmd)

    Implementation of IOA reset logic

    :param cmd:
        pointer to the cmd block to be used for entire reset process
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_ioa_reset.description`:

Description
-----------

This function executes most of the steps required for IOA reset. This gets
called by user threads (modprobe/insmod/rmmod) timer, tasklet and midlayer's
'eh_' thread. Access to variables used for controlling the reset sequence is
synchronized using host lock. Various functions called during reset process
would make use of a single command block, pointer to which is also stored in
adapter instance structure.

Return Value
None

.. _`pmcraid_initiate_reset`:

pmcraid_initiate_reset
======================

.. c:function:: void pmcraid_initiate_reset(struct pmcraid_instance *pinstance)

    initiates reset sequence. This is called from ISR/tasklet during error interrupts including IOA unit check. If reset is already in progress, it just returns, otherwise initiates IOA reset to bring IOA up to operational state.

    :param pinstance:
        pointer to adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_initiate_reset.description`:

Description
-----------

Return value
none

.. _`pmcraid_reset_reload`:

pmcraid_reset_reload
====================

.. c:function:: int pmcraid_reset_reload(struct pmcraid_instance *pinstance, u8 shutdown_type, u8 target_state)

    utility routine for doing IOA reset either to bringup or bringdown IOA

    :param pinstance:
        pointer adapter instance structure
    :type pinstance: struct pmcraid_instance \*

    :param shutdown_type:
        shutdown type to be used NONE, NORMAL or ABRREV
    :type shutdown_type: u8

    :param target_state:
        expected target state after reset
    :type target_state: u8

.. _`pmcraid_reset_reload.note`:

Note
----

This command initiates reset and waits for its completion. Hence this
should not be called from isr/timer/tasklet functions (timeout handlers,
error response handlers and interrupt handlers).

Return Value
1 in case ioa_state is not target_state, 0 otherwise.

.. _`pmcraid_reset_bringdown`:

pmcraid_reset_bringdown
=======================

.. c:function:: int pmcraid_reset_bringdown(struct pmcraid_instance *pinstance)

    wrapper over pmcraid_reset_reload to bringdown IOA

    :param pinstance:
        pointer to adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_reset_bringdown.description`:

Description
-----------

Return Value
whatever is returned from pmcraid_reset_reload

.. _`pmcraid_reset_bringup`:

pmcraid_reset_bringup
=====================

.. c:function:: int pmcraid_reset_bringup(struct pmcraid_instance *pinstance)

    wrapper over pmcraid_reset_reload to bring up IOA

    :param pinstance:
        pointer to adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_reset_bringup.description`:

Description
-----------

Return Value
whatever is returned from pmcraid_reset_reload

.. _`pmcraid_request_sense`:

pmcraid_request_sense
=====================

.. c:function:: void pmcraid_request_sense(struct pmcraid_cmd *cmd)

    Send request sense to a device

    :param cmd:
        pmcraid command struct
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_request_sense.description`:

Description
-----------

This function sends a request sense to a device as a result of a check
condition. This method re-uses the same command block that failed earlier.

.. _`pmcraid_cancel_all`:

pmcraid_cancel_all
==================

.. c:function:: void pmcraid_cancel_all(struct pmcraid_cmd *cmd, u32 sense)

    cancel all outstanding IOARCBs as part of error recovery

    :param cmd:
        command that failed
    :type cmd: struct pmcraid_cmd \*

    :param sense:
        true if request_sense is required after cancel all
    :type sense: u32

.. _`pmcraid_cancel_all.description`:

Description
-----------

This function sends a cancel all to a device to clear the queue.

.. _`pmcraid_frame_auto_sense`:

pmcraid_frame_auto_sense
========================

.. c:function:: void pmcraid_frame_auto_sense(struct pmcraid_cmd *cmd)

    frame fixed format sense information

    :param cmd:
        pointer to failing command block
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_frame_auto_sense.description`:

Description
-----------

Return value
none

.. _`pmcraid_error_handler`:

pmcraid_error_handler
=====================

.. c:function:: int pmcraid_error_handler(struct pmcraid_cmd *cmd)

    Error response handlers for a SCSI op

    :param cmd:
        pointer to pmcraid_cmd that has failed
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_error_handler.description`:

Description
-----------

This function determines whether or not to initiate ERP on the affected
device. This is called from a tasklet, which doesn't hold any locks.

.. _`pmcraid_error_handler.return-value`:

Return value
------------

0 it caller can complete the request, otherwise 1 where in error
handler itself completes the request and returns the command block
back to free-pool

.. _`pmcraid_reset_device`:

pmcraid_reset_device
====================

.. c:function:: int pmcraid_reset_device(struct scsi_cmnd *scsi_cmd, unsigned long timeout, u8 modifier)

    device reset handler functions

    :param scsi_cmd:
        scsi command struct
    :type scsi_cmd: struct scsi_cmnd \*

    :param timeout:
        *undescribed*
    :type timeout: unsigned long

    :param modifier:
        reset modifier indicating the reset sequence to be performed
    :type modifier: u8

.. _`pmcraid_reset_device.description`:

Description
-----------

This function issues a device reset to the affected device.
A LUN reset will be sent to the device first. If that does
not work, a target reset will be sent.

.. _`pmcraid_reset_device.return-value`:

Return value
------------

SUCCESS / FAILED

.. _`_pmcraid_io_done`:

\_pmcraid_io_done
=================

.. c:function:: int _pmcraid_io_done(struct pmcraid_cmd *cmd, int reslen, int ioasc)

    helper for pmcraid_io_done function

    :param cmd:
        pointer to pmcraid command struct
    :type cmd: struct pmcraid_cmd \*

    :param reslen:
        residual data length to be set in the ioasa
    :type reslen: int

    :param ioasc:
        ioasc either returned by IOA or set by driver itself.
    :type ioasc: int

.. _`_pmcraid_io_done.description`:

Description
-----------

This function is invoked by pmcraid_io_done to complete mid-layer
scsi ops.

.. _`_pmcraid_io_done.return-value`:

Return value
------------

0 if caller is required to return it to free_pool. Returns 1 if
caller need not worry about freeing command block as error handler
will take care of that.

.. _`pmcraid_io_done`:

pmcraid_io_done
===============

.. c:function:: void pmcraid_io_done(struct pmcraid_cmd *cmd)

    SCSI completion function

    :param cmd:
        pointer to pmcraid command struct
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_io_done.description`:

Description
-----------

This function is invoked by tasklet/mid-layer error handler to completing
the SCSI ops sent from mid-layer.

Return value
none

.. _`pmcraid_abort_cmd`:

pmcraid_abort_cmd
=================

.. c:function:: struct pmcraid_cmd *pmcraid_abort_cmd(struct pmcraid_cmd *cmd)

    Aborts a single IOARCB already submitted to IOA

    :param cmd:
        command block of the command to be aborted
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_abort_cmd.return-value`:

Return Value
------------

returns pointer to command structure used as cancelling cmd

.. _`pmcraid_abort_complete`:

pmcraid_abort_complete
======================

.. c:function:: int pmcraid_abort_complete(struct pmcraid_cmd *cancel_cmd)

    Waits for ABORT TASK completion

    :param cancel_cmd:
        command block use as cancelling command
    :type cancel_cmd: struct pmcraid_cmd \*

.. _`pmcraid_abort_complete.return-value`:

Return Value
------------

returns SUCCESS if ABORT TASK has good completion
otherwise FAILED

.. _`pmcraid_eh_abort_handler`:

pmcraid_eh_abort_handler
========================

.. c:function:: int pmcraid_eh_abort_handler(struct scsi_cmnd *scsi_cmd)

    entry point for aborting a single task on errors

    :param scsi_cmd:
        scsi command struct given by mid-layer. When this is called
        mid-layer ensures that no other commands are queued. This
        never gets called under interrupt, but a separate eh thread.
    :type scsi_cmd: struct scsi_cmnd \*

.. _`pmcraid_eh_abort_handler.return-value`:

Return value
------------

SUCCESS / FAILED

.. _`pmcraid_eh_device_reset_handler`:

pmcraid_eh_device_reset_handler
===============================

.. c:function:: int pmcraid_eh_device_reset_handler(struct scsi_cmnd *scmd)

    bus/target/device reset handler callbacks

    :param scmd:
        pointer to scsi_cmd that was sent to the resource to be reset.
    :type scmd: struct scsi_cmnd \*

.. _`pmcraid_eh_device_reset_handler.description`:

Description
-----------

All these routines invokve pmcraid_reset_device with appropriate parameters.
Since these are called from mid-layer EH thread, no other IO will be queued
to the resource being reset. However, control path (IOCTL) may be active so
it is necessary to synchronize IOARRIN writes which pmcraid_reset_device
takes care by locking/unlocking host_lock.

Return value
SUCCESS or FAILED

.. _`pmcraid_eh_host_reset_handler`:

pmcraid_eh_host_reset_handler
=============================

.. c:function:: int pmcraid_eh_host_reset_handler(struct scsi_cmnd *scmd)

    adapter reset handler callback

    :param scmd:
        pointer to scsi_cmd that was sent to a resource of adapter
    :type scmd: struct scsi_cmnd \*

.. _`pmcraid_eh_host_reset_handler.description`:

Description
-----------

Initiates adapter reset to bring it up to operational state

Return value
SUCCESS or FAILED

.. _`pmcraid_init_ioadls`:

pmcraid_init_ioadls
===================

.. c:function:: struct pmcraid_ioadl_desc *pmcraid_init_ioadls(struct pmcraid_cmd *cmd, int sgcount)

    initializes IOADL related fields in IOARCB

    :param cmd:
        pmcraid command struct
    :type cmd: struct pmcraid_cmd \*

    :param sgcount:
        count of scatter-gather elements
    :type sgcount: int

.. _`pmcraid_init_ioadls.description`:

Description
-----------

Return value
returns pointer pmcraid_ioadl_desc, initialized to point to internal
or external IOADLs

.. _`pmcraid_build_ioadl`:

pmcraid_build_ioadl
===================

.. c:function:: int pmcraid_build_ioadl(struct pmcraid_instance *pinstance, struct pmcraid_cmd *cmd)

    Build a scatter/gather list and map the buffer

    :param pinstance:
        pointer to adapter instance structure
    :type pinstance: struct pmcraid_instance \*

    :param cmd:
        pmcraid command struct
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_build_ioadl.description`:

Description
-----------

This function is invoked by queuecommand entry point while sending a command
to firmware. This builds ioadl descriptors and sets up ioarcb fields.

.. _`pmcraid_build_ioadl.return-value`:

Return value
------------

0 on success or -1 on failure

.. _`pmcraid_free_sglist`:

pmcraid_free_sglist
===================

.. c:function:: void pmcraid_free_sglist(struct pmcraid_sglist *sglist)

    Frees an allocated SG buffer list

    :param sglist:
        scatter/gather list pointer
    :type sglist: struct pmcraid_sglist \*

.. _`pmcraid_free_sglist.description`:

Description
-----------

Free a DMA'able memory previously allocated with pmcraid_alloc_sglist

.. _`pmcraid_free_sglist.return-value`:

Return value
------------

none

.. _`pmcraid_alloc_sglist`:

pmcraid_alloc_sglist
====================

.. c:function:: struct pmcraid_sglist *pmcraid_alloc_sglist(int buflen)

    Allocates memory for a SG list

    :param buflen:
        buffer length
    :type buflen: int

.. _`pmcraid_alloc_sglist.description`:

Description
-----------

Allocates a DMA'able buffer in chunks and assembles a scatter/gather
list.

Return value
pointer to sglist / NULL on failure

.. _`pmcraid_copy_sglist`:

pmcraid_copy_sglist
===================

.. c:function:: int pmcraid_copy_sglist(struct pmcraid_sglist *sglist, void __user *buffer, u32 len, int direction)

    Copy user buffer to kernel buffer's SG list

    :param sglist:
        scatter/gather list pointer
    :type sglist: struct pmcraid_sglist \*

    :param buffer:
        buffer pointer
    :type buffer: void __user \*

    :param len:
        buffer length
    :type len: u32

    :param direction:
        data transfer direction
    :type direction: int

.. _`pmcraid_copy_sglist.description`:

Description
-----------

Copy a user buffer into a buffer allocated by pmcraid_alloc_sglist

.. _`pmcraid_copy_sglist.return-value`:

Return value
------------

0 on success / other on failure

.. _`pmcraid_queuecommand_lck`:

pmcraid_queuecommand_lck
========================

.. c:function:: int pmcraid_queuecommand_lck(struct scsi_cmnd *scsi_cmd, void (*done)(struct scsi_cmnd *))

    Queue a mid-layer request

    :param scsi_cmd:
        scsi command struct
    :type scsi_cmd: struct scsi_cmnd \*

    :param void (\*done)(struct scsi_cmnd \*):
        done function

.. _`pmcraid_queuecommand_lck.description`:

Description
-----------

This function queues a request generated by the mid-layer. Midlayer calls
this routine within host->lock. Some of the functions called by queuecommand
would use cmd block queue locks (free_pool_lock and pending_pool_lock)

.. _`pmcraid_queuecommand_lck.return-value`:

Return value
------------

0 on success
SCSI_MLQUEUE_DEVICE_BUSY if device is busy
SCSI_MLQUEUE_HOST_BUSY if host is busy

.. _`pmcraid_chr_open`:

pmcraid_chr_open
================

.. c:function:: int pmcraid_chr_open(struct inode *inode, struct file *filep)

    char node "open" entry, allowed only users with admin access

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param filep:
        *undescribed*
    :type filep: struct file \*

.. _`pmcraid_chr_fasync`:

pmcraid_chr_fasync
==================

.. c:function:: int pmcraid_chr_fasync(int fd, struct file *filep, int mode)

    Async notifier registration from applications

    :param fd:
        *undescribed*
    :type fd: int

    :param filep:
        *undescribed*
    :type filep: struct file \*

    :param mode:
        *undescribed*
    :type mode: int

.. _`pmcraid_chr_fasync.description`:

Description
-----------

This function adds the calling process to a driver global queue. When an
event occurs, SIGIO will be sent to all processes in this queue.

.. _`pmcraid_build_passthrough_ioadls`:

pmcraid_build_passthrough_ioadls
================================

.. c:function:: int pmcraid_build_passthrough_ioadls(struct pmcraid_cmd *cmd, int buflen, int direction)

    builds SG elements for passthrough commands sent over IOCTL interface

    :param cmd:
        pointer to struct pmcraid_cmd
    :type cmd: struct pmcraid_cmd \*

    :param buflen:
        length of the request buffer
    :type buflen: int

    :param direction:
        data transfer direction
    :type direction: int

.. _`pmcraid_build_passthrough_ioadls.description`:

Description
-----------

Return value
0 on success, non-zero error code on failure

.. _`pmcraid_release_passthrough_ioadls`:

pmcraid_release_passthrough_ioadls
==================================

.. c:function:: void pmcraid_release_passthrough_ioadls(struct pmcraid_cmd *cmd, int buflen, int direction)

    release passthrough ioadls

    :param cmd:
        pointer to struct pmcraid_cmd for which ioadls were allocated
    :type cmd: struct pmcraid_cmd \*

    :param buflen:
        size of the request buffer
    :type buflen: int

    :param direction:
        data transfer direction
    :type direction: int

.. _`pmcraid_release_passthrough_ioadls.description`:

Description
-----------

Return value
0 on success, non-zero error code on failure

.. _`pmcraid_ioctl_passthrough`:

pmcraid_ioctl_passthrough
=========================

.. c:function:: long pmcraid_ioctl_passthrough(struct pmcraid_instance *pinstance, unsigned int ioctl_cmd, unsigned int buflen, void __user *arg)

    handling passthrough IOCTL commands

    :param pinstance:
        pointer to adapter instance structure
    :type pinstance: struct pmcraid_instance \*

    :param ioctl_cmd:
        *undescribed*
    :type ioctl_cmd: unsigned int

    :param buflen:
        *undescribed*
    :type buflen: unsigned int

    :param arg:
        pointer to pmcraid_passthrough_buffer user buffer
    :type arg: void __user \*

.. _`pmcraid_ioctl_passthrough.description`:

Description
-----------

Return value
0 on success, non-zero error code on failure

.. _`pmcraid_ioctl_driver`:

pmcraid_ioctl_driver
====================

.. c:function:: long pmcraid_ioctl_driver(struct pmcraid_instance *pinstance, unsigned int cmd, unsigned int buflen, void __user *user_buffer)

    ioctl handler for commands handled by driver itself

    :param pinstance:
        pointer to adapter instance structure
    :type pinstance: struct pmcraid_instance \*

    :param cmd:
        ioctl command passed in
    :type cmd: unsigned int

    :param buflen:
        length of user_buffer
    :type buflen: unsigned int

    :param user_buffer:
        user buffer pointer
    :type user_buffer: void __user \*

.. _`pmcraid_ioctl_driver.description`:

Description
-----------

Return Value
0 in case of success, otherwise appropriate error code

.. _`pmcraid_check_ioctl_buffer`:

pmcraid_check_ioctl_buffer
==========================

.. c:function:: int pmcraid_check_ioctl_buffer(int cmd, void __user *arg, struct pmcraid_ioctl_header *hdr)

    check for proper access to user buffer

    :param cmd:
        ioctl command
    :type cmd: int

    :param arg:
        user buffer
    :type arg: void __user \*

    :param hdr:
        pointer to kernel memory for pmcraid_ioctl_header
    :type hdr: struct pmcraid_ioctl_header \*

.. _`pmcraid_check_ioctl_buffer.description`:

Description
-----------

Return Value
negetive error code if there are access issues, otherwise zero.
Upon success, returns ioctl header copied out of user buffer.

.. _`pmcraid_chr_ioctl`:

pmcraid_chr_ioctl
=================

.. c:function:: long pmcraid_chr_ioctl(struct file *filep, unsigned int cmd, unsigned long arg)

    char node ioctl entry point

    :param filep:
        *undescribed*
    :type filep: struct file \*

    :param cmd:
        *undescribed*
    :type cmd: unsigned int

    :param arg:
        *undescribed*
    :type arg: unsigned long

.. _`pmcraid_show_log_level`:

pmcraid_show_log_level
======================

.. c:function:: ssize_t pmcraid_show_log_level(struct device *dev, struct device_attribute *attr, char *buf)

    Display adapter's error logging level

    :param dev:
        class device struct
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: char \*

.. _`pmcraid_show_log_level.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`pmcraid_store_log_level`:

pmcraid_store_log_level
=======================

.. c:function:: ssize_t pmcraid_store_log_level(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Change the adapter's error logging level

    :param dev:
        class device struct
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: const char \*

    :param count:
        not used
    :type count: size_t

.. _`pmcraid_store_log_level.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`pmcraid_show_drv_version`:

pmcraid_show_drv_version
========================

.. c:function:: ssize_t pmcraid_show_drv_version(struct device *dev, struct device_attribute *attr, char *buf)

    Display driver version

    :param dev:
        class device struct
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: char \*

.. _`pmcraid_show_drv_version.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`pmcraid_show_adapter_id`:

pmcraid_show_adapter_id
=======================

.. c:function:: ssize_t pmcraid_show_adapter_id(struct device *dev, struct device_attribute *attr, char *buf)

    Display driver assigned adapter id

    :param dev:
        class device struct
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: char \*

.. _`pmcraid_show_adapter_id.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`pmcraid_isr`:

pmcraid_isr
===========

.. c:function:: irqreturn_t pmcraid_isr(int irq, void *dev_id)

    implements legacy interrupt handling routine

    :param irq:
        interrupt vector number
    :type irq: int

    :param dev_id:
        pointer hrrq_vector
    :type dev_id: void \*

.. _`pmcraid_isr.description`:

Description
-----------

Return Value
IRQ_HANDLED if interrupt is handled or IRQ_NONE if ignored

.. _`pmcraid_worker_function`:

pmcraid_worker_function
=======================

.. c:function:: void pmcraid_worker_function(struct work_struct *workp)

    worker thread function

    :param workp:
        pointer to struct work queue
    :type workp: struct work_struct \*

.. _`pmcraid_worker_function.description`:

Description
-----------

Return Value
None

.. _`pmcraid_tasklet_function`:

pmcraid_tasklet_function
========================

.. c:function:: void pmcraid_tasklet_function(unsigned long instance)

    Tasklet function

    :param instance:
        pointer to msix param structure
    :type instance: unsigned long

.. _`pmcraid_tasklet_function.description`:

Description
-----------

Return Value
None

.. _`pmcraid_unregister_interrupt_handler`:

pmcraid_unregister_interrupt_handler
====================================

.. c:function:: void pmcraid_unregister_interrupt_handler(struct pmcraid_instance *pinstance)

    de-register interrupts handlers

    :param pinstance:
        pointer to adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_unregister_interrupt_handler.description`:

Description
-----------

This routine un-registers registered interrupt handler and
also frees irqs/vectors.

Retun Value
None

.. _`pmcraid_register_interrupt_handler`:

pmcraid_register_interrupt_handler
==================================

.. c:function:: int pmcraid_register_interrupt_handler(struct pmcraid_instance *pinstance)

    registers interrupt handler

    :param pinstance:
        pointer to per-adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_register_interrupt_handler.description`:

Description
-----------

Return Value
0 on success, non-zero error code otherwise.

.. _`pmcraid_release_cmd_blocks`:

pmcraid_release_cmd_blocks
==========================

.. c:function:: void pmcraid_release_cmd_blocks(struct pmcraid_instance *pinstance, int max_index)

    release buufers allocated for command blocks

    :param pinstance:
        per adapter instance structure pointer
    :type pinstance: struct pmcraid_instance \*

    :param max_index:
        number of buffer blocks to release
    :type max_index: int

.. _`pmcraid_release_cmd_blocks.description`:

Description
-----------

Return Value
None

.. _`pmcraid_release_control_blocks`:

pmcraid_release_control_blocks
==============================

.. c:function:: void pmcraid_release_control_blocks(struct pmcraid_instance *pinstance, int max_index)

    releases buffers alloced for control blocks

    :param pinstance:
        pointer to per adapter instance structure
    :type pinstance: struct pmcraid_instance \*

    :param max_index:
        number of buffers (from 0 onwards) to release
    :type max_index: int

.. _`pmcraid_release_control_blocks.description`:

Description
-----------

This function assumes that the command blocks for which control blocks are
linked are not released.

Return Value
None

.. _`pmcraid_allocate_cmd_blocks`:

pmcraid_allocate_cmd_blocks
===========================

.. c:function:: int pmcraid_allocate_cmd_blocks(struct pmcraid_instance *pinstance)

    allocate memory for cmd block structures \ ``pinstance``\  - pointer to per adapter instance structure

    :param pinstance:
        *undescribed*
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_allocate_cmd_blocks.description`:

Description
-----------

Allocates memory for command blocks using kernel slab allocator.

Return Value
0 in case of success; -ENOMEM in case of failure

.. _`pmcraid_allocate_control_blocks`:

pmcraid_allocate_control_blocks
===============================

.. c:function:: int pmcraid_allocate_control_blocks(struct pmcraid_instance *pinstance)

    allocates memory control blocks

    :param pinstance:
        pointer to per adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_allocate_control_blocks.description`:

Description
-----------

This function allocates PCI memory for DMAable buffers like IOARCB, IOADLs
and IOASAs. This is called after command blocks are already allocated.

Return Value
0 in case it can allocate all control blocks, otherwise -ENOMEM

.. _`pmcraid_release_host_rrqs`:

pmcraid_release_host_rrqs
=========================

.. c:function:: void pmcraid_release_host_rrqs(struct pmcraid_instance *pinstance, int maxindex)

    release memory allocated for hrrq buffer(s)

    :param pinstance:
        pointer to per adapter instance structure
    :type pinstance: struct pmcraid_instance \*

    :param maxindex:
        size of hrrq buffer pointer array
    :type maxindex: int

.. _`pmcraid_release_host_rrqs.description`:

Description
-----------

Return Value
None

.. _`pmcraid_allocate_host_rrqs`:

pmcraid_allocate_host_rrqs
==========================

.. c:function:: int pmcraid_allocate_host_rrqs(struct pmcraid_instance *pinstance)

    Allocate and initialize host RRQ buffers

    :param pinstance:
        pointer to per adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_allocate_host_rrqs.description`:

Description
-----------

Return value
0 hrrq buffers are allocated, -ENOMEM otherwise.

.. _`pmcraid_release_hcams`:

pmcraid_release_hcams
=====================

.. c:function:: void pmcraid_release_hcams(struct pmcraid_instance *pinstance)

    release HCAM buffers

    :param pinstance:
        pointer to per adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_release_hcams.description`:

Description
-----------

Return value
none

.. _`pmcraid_allocate_hcams`:

pmcraid_allocate_hcams
======================

.. c:function:: int pmcraid_allocate_hcams(struct pmcraid_instance *pinstance)

    allocates HCAM buffers

    :param pinstance:
        pointer to per adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_allocate_hcams.return-value`:

Return Value
------------

0 in case of successful allocation, non-zero otherwise

.. _`pmcraid_release_config_buffers`:

pmcraid_release_config_buffers
==============================

.. c:function:: void pmcraid_release_config_buffers(struct pmcraid_instance *pinstance)

    release config.table buffers

    :param pinstance:
        pointer to per adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_release_config_buffers.description`:

Description
-----------

Return Value
none

.. _`pmcraid_allocate_config_buffers`:

pmcraid_allocate_config_buffers
===============================

.. c:function:: int pmcraid_allocate_config_buffers(struct pmcraid_instance *pinstance)

    allocates DMAable memory for config table

    :param pinstance:
        pointer to per adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_allocate_config_buffers.description`:

Description
-----------

Return Value
0 for successful allocation, -ENOMEM for any failure

.. _`pmcraid_init_tasklets`:

pmcraid_init_tasklets
=====================

.. c:function:: void pmcraid_init_tasklets(struct pmcraid_instance *pinstance)

    registers tasklets for response handling

    :param pinstance:
        pointer adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_init_tasklets.description`:

Description
-----------

Return value
none

.. _`pmcraid_kill_tasklets`:

pmcraid_kill_tasklets
=====================

.. c:function:: void pmcraid_kill_tasklets(struct pmcraid_instance *pinstance)

    destroys tasklets registered for response handling

    :param pinstance:
        pointer to adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_kill_tasklets.description`:

Description
-----------

Return value
none

.. _`pmcraid_release_buffers`:

pmcraid_release_buffers
=======================

.. c:function:: void pmcraid_release_buffers(struct pmcraid_instance *pinstance)

    release per-adapter buffers allocated

    :param pinstance:
        pointer to adapter soft state
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_release_buffers.description`:

Description
-----------

Return Value
none

.. _`pmcraid_init_buffers`:

pmcraid_init_buffers
====================

.. c:function:: int pmcraid_init_buffers(struct pmcraid_instance *pinstance)

    allocates memory and initializes various structures

    :param pinstance:
        pointer to per adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_init_buffers.description`:

Description
-----------

This routine pre-allocates memory based on the type of block as below:
cmdblocks(PMCRAID_MAX_CMD): kernel memory using kernel's slab_allocator,
IOARCBs(PMCRAID_MAX_CMD)  : DMAable memory, using pci pool allocator
config-table entries      : DMAable memory using pci_alloc_consistent
HostRRQs                  : DMAable memory, using pci_alloc_consistent

Return Value
0 in case all of the blocks are allocated, -ENOMEM otherwise.

.. _`pmcraid_reinit_buffers`:

pmcraid_reinit_buffers
======================

.. c:function:: void pmcraid_reinit_buffers(struct pmcraid_instance *pinstance)

    resets various buffer pointers

    :param pinstance:
        pointer to adapter instance
        Return value
        none
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_init_instance`:

pmcraid_init_instance
=====================

.. c:function:: int pmcraid_init_instance(struct pci_dev *pdev, struct Scsi_Host *host, void __iomem *mapped_pci_addr)

    initialize per instance data structure

    :param pdev:
        pointer to pci device structure
    :type pdev: struct pci_dev \*

    :param host:
        pointer to Scsi_Host structure
    :type host: struct Scsi_Host \*

    :param mapped_pci_addr:
        memory mapped IOA configuration registers
    :type mapped_pci_addr: void __iomem \*

.. _`pmcraid_init_instance.description`:

Description
-----------

Return Value
0 on success, non-zero in case of any failure

.. _`pmcraid_shutdown`:

pmcraid_shutdown
================

.. c:function:: void pmcraid_shutdown(struct pci_dev *pdev)

    shutdown adapter controller.

    :param pdev:
        pci device struct
    :type pdev: struct pci_dev \*

.. _`pmcraid_shutdown.description`:

Description
-----------

Issues an adapter shutdown to the card waits for its completion

Return value
none

.. _`pmcraid_get_minor`:

pmcraid_get_minor
=================

.. c:function:: unsigned short pmcraid_get_minor( void)

    returns unused minor number from minor number bitmap

    :param void:
        no arguments
    :type void: 

.. _`pmcraid_release_minor`:

pmcraid_release_minor
=====================

.. c:function:: void pmcraid_release_minor(unsigned short minor)

    releases given minor back to minor number bitmap

    :param minor:
        *undescribed*
    :type minor: unsigned short

.. _`pmcraid_setup_chrdev`:

pmcraid_setup_chrdev
====================

.. c:function:: int pmcraid_setup_chrdev(struct pmcraid_instance *pinstance)

    allocates a minor number and registers a char device

    :param pinstance:
        pointer to adapter instance for which to register device
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_setup_chrdev.description`:

Description
-----------

Return value
0 in case of success, otherwise non-zero

.. _`pmcraid_release_chrdev`:

pmcraid_release_chrdev
======================

.. c:function:: void pmcraid_release_chrdev(struct pmcraid_instance *pinstance)

    unregisters per-adapter management interface

    :param pinstance:
        pointer to adapter instance structure
    :type pinstance: struct pmcraid_instance \*

.. _`pmcraid_release_chrdev.description`:

Description
-----------

Return value
none

.. _`pmcraid_remove`:

pmcraid_remove
==============

.. c:function:: void pmcraid_remove(struct pci_dev *pdev)

    IOA hot plug remove entry point

    :param pdev:
        pci device struct
    :type pdev: struct pci_dev \*

.. _`pmcraid_remove.description`:

Description
-----------

Return value
none

.. _`pmcraid_suspend`:

pmcraid_suspend
===============

.. c:function:: int pmcraid_suspend(struct pci_dev *pdev, pm_message_t state)

    driver suspend entry point for power management

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

    :param state:
        PCI power state to suspend routine
    :type state: pm_message_t

.. _`pmcraid_suspend.description`:

Description
-----------

Return Value - 0 always

.. _`pmcraid_resume`:

pmcraid_resume
==============

.. c:function:: int pmcraid_resume(struct pci_dev *pdev)

    driver resume entry point PCI power management

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

.. _`pmcraid_resume.description`:

Description
-----------

Return Value - 0 in case of success. Error code in case of any failure

.. _`pmcraid_complete_ioa_reset`:

pmcraid_complete_ioa_reset
==========================

.. c:function:: void pmcraid_complete_ioa_reset(struct pmcraid_cmd *cmd)

    Called by either timer or tasklet during completion of the ioa reset

    :param cmd:
        pointer to reset command block
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_set_supported_devs`:

pmcraid_set_supported_devs
==========================

.. c:function:: void pmcraid_set_supported_devs(struct pmcraid_cmd *cmd)

    sends SET SUPPORTED DEVICES to IOAFP

    :param cmd:
        pointer to pmcraid_cmd structure
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_set_supported_devs.description`:

Description
-----------

Return Value
0 for success or non-zero for failure cases

.. _`pmcraid_set_timestamp`:

pmcraid_set_timestamp
=====================

.. c:function:: void pmcraid_set_timestamp(struct pmcraid_cmd *cmd)

    set the timestamp to IOAFP

    :param cmd:
        pointer to pmcraid_cmd structure
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_set_timestamp.description`:

Description
-----------

Return Value
0 for success or non-zero for failure cases

.. _`pmcraid_init_res_table`:

pmcraid_init_res_table
======================

.. c:function:: void pmcraid_init_res_table(struct pmcraid_cmd *cmd)

    Initialize the resource table

    :param cmd:
        pointer to pmcraid command struct
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_init_res_table.description`:

Description
-----------

This function looks through the existing resource table, comparing
it with the config table. This function will take care of old/new
devices and schedule adding/removing them from the mid-layer
as appropriate.

Return value
None

.. _`pmcraid_querycfg`:

pmcraid_querycfg
================

.. c:function:: void pmcraid_querycfg(struct pmcraid_cmd *cmd)

    Send a Query IOA Config to the adapter.

    :param cmd:
        pointer pmcraid_cmd struct
    :type cmd: struct pmcraid_cmd \*

.. _`pmcraid_querycfg.description`:

Description
-----------

This function sends a Query IOA Configuration command to the adapter to
retrieve the IOA configuration table.

.. _`pmcraid_querycfg.return-value`:

Return value
------------

none

.. _`pmcraid_probe`:

pmcraid_probe
=============

.. c:function:: int pmcraid_probe(struct pci_dev *pdev, const struct pci_device_id *dev_id)

    PCI probe entry pointer for PMC MaxRAID controller driver

    :param pdev:
        pointer to pci device structure
    :type pdev: struct pci_dev \*

    :param dev_id:
        pointer to device ids structure
    :type dev_id: const struct pci_device_id \*

.. _`pmcraid_probe.description`:

Description
-----------

Return Value
returns 0 if the device is claimed and successfully configured.
returns non-zero error code in case of any failure

.. _`pmcraid_init`:

pmcraid_init
============

.. c:function:: int pmcraid_init( void)

    module load entry point

    :param void:
        no arguments
    :type void: 

.. _`pmcraid_exit`:

pmcraid_exit
============

.. c:function:: void __exit pmcraid_exit( void)

    module unload entry point

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

