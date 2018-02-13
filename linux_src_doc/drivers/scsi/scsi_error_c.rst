.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/scsi_error.c

.. _`scsi_schedule_eh`:

scsi_schedule_eh
================

.. c:function:: void scsi_schedule_eh(struct Scsi_Host *shost)

    schedule EH for SCSI host

    :param struct Scsi_Host \*shost:
        SCSI host to invoke error handling on.

.. _`scsi_schedule_eh.description`:

Description
-----------

Schedule SCSI EH without scmd.

.. _`scmd_eh_abort_handler`:

scmd_eh_abort_handler
=====================

.. c:function:: void scmd_eh_abort_handler(struct work_struct *work)

    Handle command aborts

    :param struct work_struct \*work:
        command to be aborted.

.. _`scsi_abort_command`:

scsi_abort_command
==================

.. c:function:: int scsi_abort_command(struct scsi_cmnd *scmd)

    schedule a command abort

    :param struct scsi_cmnd \*scmd:
        scmd to abort.

.. _`scsi_abort_command.description`:

Description
-----------

We only need to abort commands after a command timeout

.. _`scsi_eh_reset`:

scsi_eh_reset
=============

.. c:function:: void scsi_eh_reset(struct scsi_cmnd *scmd)

    call into ->eh_action to reset internal counters

    :param struct scsi_cmnd \*scmd:
        scmd to run eh on.

.. _`scsi_eh_reset.description`:

Description
-----------

The scsi driver might be carrying internal state about the
devices, so we need to call into the driver to reset the
internal state once the error handler is started.

.. _`scsi_eh_scmd_add`:

scsi_eh_scmd_add
================

.. c:function:: void scsi_eh_scmd_add(struct scsi_cmnd *scmd)

    add scsi cmd to error handling.

    :param struct scsi_cmnd \*scmd:
        scmd to run eh on.

.. _`scsi_times_out`:

scsi_times_out
==============

.. c:function:: enum blk_eh_timer_return scsi_times_out(struct request *req)

    Timeout function for normal scsi commands.

    :param struct request \*req:
        request that is timing out.

.. _`scsi_times_out.notes`:

Notes
-----

    We do not need to lock this.  There is the potential for a race
    only in that the normal completion handling might run, but if the
    normal completion function determines that the timer has already
    fired, then it mustn't do anything.

.. _`scsi_block_when_processing_errors`:

scsi_block_when_processing_errors
=================================

.. c:function:: int scsi_block_when_processing_errors(struct scsi_device *sdev)

    Prevent cmds from being queued.

    :param struct scsi_device \*sdev:
        Device on which we are performing recovery.

.. _`scsi_block_when_processing_errors.description`:

Description
-----------

    We block until the host is out of error recovery, and then check to
    see whether the host or the device is offline.

.. _`scsi_block_when_processing_errors.return-value`:

Return value
------------

    0 when dev was taken offline by error recovery. 1 OK to proceed.

.. _`scsi_eh_prt_fail_stats`:

scsi_eh_prt_fail_stats
======================

.. c:function:: void scsi_eh_prt_fail_stats(struct Scsi_Host *shost, struct list_head *work_q)

    Log info on failures.

    :param struct Scsi_Host \*shost:
        scsi host being recovered.

    :param struct list_head \*work_q:
        Queue of scsi cmds to process.

.. _`scsi_report_sense`:

scsi_report_sense
=================

.. c:function:: void scsi_report_sense(struct scsi_device *sdev, struct scsi_sense_hdr *sshdr)

    Examine scsi sense information and log messages for certain conditions, also issue uevents for some of them.

    :param struct scsi_device \*sdev:
        Device reporting the sense code

    :param struct scsi_sense_hdr \*sshdr:
        sshdr to be examined

.. _`scsi_check_sense`:

scsi_check_sense
================

.. c:function:: int scsi_check_sense(struct scsi_cmnd *scmd)

    Examine scsi cmd sense

    :param struct scsi_cmnd \*scmd:
        Cmd to have sense checked.

.. _`scsi_check_sense.return-value`:

Return value
------------

     SUCCESS or FAILED or NEEDS_RETRY or ADD_TO_MLQUEUE

.. _`scsi_check_sense.notes`:

Notes
-----

     When a deferred error is detected the current command has
     not been executed and needs retrying.

.. _`scsi_eh_completed_normally`:

scsi_eh_completed_normally
==========================

.. c:function:: int scsi_eh_completed_normally(struct scsi_cmnd *scmd)

    Disposition a eh cmd on return from LLD.

    :param struct scsi_cmnd \*scmd:
        SCSI cmd to examine.

.. _`scsi_eh_completed_normally.notes`:

Notes
-----

   This is *only* called when we are examining the status of commands
   queued during error recovery.  the main difference here is that we
   don't allow for the possibility of retries here, and we are a lot
   more restrictive about what we consider acceptable.

.. _`scsi_eh_done`:

scsi_eh_done
============

.. c:function:: void scsi_eh_done(struct scsi_cmnd *scmd)

    Completion function for error handling.

    :param struct scsi_cmnd \*scmd:
        Cmd that is done.

.. _`scsi_try_host_reset`:

scsi_try_host_reset
===================

.. c:function:: int scsi_try_host_reset(struct scsi_cmnd *scmd)

    ask host adapter to reset itself

    :param struct scsi_cmnd \*scmd:
        SCSI cmd to send host reset.

.. _`scsi_try_bus_reset`:

scsi_try_bus_reset
==================

.. c:function:: int scsi_try_bus_reset(struct scsi_cmnd *scmd)

    ask host to perform a bus reset

    :param struct scsi_cmnd \*scmd:
        SCSI cmd to send bus reset.

.. _`scsi_try_target_reset`:

scsi_try_target_reset
=====================

.. c:function:: int scsi_try_target_reset(struct scsi_cmnd *scmd)

    Ask host to perform a target reset

    :param struct scsi_cmnd \*scmd:
        SCSI cmd used to send a target reset

.. _`scsi_try_target_reset.notes`:

Notes
-----

   There is no timeout for this operation.  if this operation is
   unreliable for a given host, then the host itself needs to put a
   timer on it, and set the host back to a consistent state prior to
   returning.

.. _`scsi_try_bus_device_reset`:

scsi_try_bus_device_reset
=========================

.. c:function:: int scsi_try_bus_device_reset(struct scsi_cmnd *scmd)

    Ask host to perform a BDR on a dev

    :param struct scsi_cmnd \*scmd:
        SCSI cmd used to send BDR

.. _`scsi_try_bus_device_reset.notes`:

Notes
-----

   There is no timeout for this operation.  if this operation is
   unreliable for a given host, then the host itself needs to put a
   timer on it, and set the host back to a consistent state prior to
   returning.

.. _`scsi_try_to_abort_cmd`:

scsi_try_to_abort_cmd
=====================

.. c:function:: int scsi_try_to_abort_cmd(struct scsi_host_template *hostt, struct scsi_cmnd *scmd)

    Ask host to abort a SCSI command

    :param struct scsi_host_template \*hostt:
        SCSI driver host template

    :param struct scsi_cmnd \*scmd:
        SCSI cmd used to send a target reset

.. _`scsi_try_to_abort_cmd.return-value`:

Return value
------------

     SUCCESS, FAILED, or FAST_IO_FAIL

.. _`scsi_try_to_abort_cmd.notes`:

Notes
-----

   SUCCESS does not necessarily indicate that the command
   has been aborted; it only indicates that the LLDDs
   has cleared all references to that command.
   LLDDs should return FAILED only if an abort was required
   but could not be executed. LLDDs should return FAST_IO_FAIL
   if the device is temporarily unavailable (eg due to a
   link down on FibreChannel)

.. _`scsi_eh_prep_cmnd`:

scsi_eh_prep_cmnd
=================

.. c:function:: void scsi_eh_prep_cmnd(struct scsi_cmnd *scmd, struct scsi_eh_save *ses, unsigned char *cmnd, int cmnd_size, unsigned sense_bytes)

    Save a scsi command info as part of error recovery

    :param struct scsi_cmnd \*scmd:
        SCSI command structure to hijack

    :param struct scsi_eh_save \*ses:
        structure to save restore information

    :param unsigned char \*cmnd:
        CDB to send. Can be NULL if no new cmnd is needed

    :param int cmnd_size:
        size in bytes of \ ``cmnd``\  (must be <= BLK_MAX_CDB)

    :param unsigned sense_bytes:
        size of sense data to copy. or 0 (if != 0 \ ``cmnd``\  is ignored)

.. _`scsi_eh_prep_cmnd.description`:

Description
-----------

This function is used to save a scsi command information before re-execution
as part of the error recovery process.  If \ ``sense_bytes``\  is 0 the command
sent must be one that does not transfer any data.  If \ ``sense_bytes``\  != 0
\ ``cmnd``\  is ignored and this functions sets up a REQUEST_SENSE command
and cmnd buffers to read \ ``sense_bytes``\  into \ ``scmd``\ ->sense_buffer.

.. _`scsi_eh_restore_cmnd`:

scsi_eh_restore_cmnd
====================

.. c:function:: void scsi_eh_restore_cmnd(struct scsi_cmnd*scmd, struct scsi_eh_save *ses)

    Restore a scsi command info as part of error recovery

    :param struct scsi_cmnd\*scmd:
        SCSI command structure to restore

    :param struct scsi_eh_save \*ses:
        saved information from a coresponding call to scsi_eh_prep_cmnd

.. _`scsi_eh_restore_cmnd.description`:

Description
-----------

Undo any damage done by above \ :c:func:`scsi_eh_prep_cmnd`\ .

.. _`scsi_send_eh_cmnd`:

scsi_send_eh_cmnd
=================

.. c:function:: int scsi_send_eh_cmnd(struct scsi_cmnd *scmd, unsigned char *cmnd, int cmnd_size, int timeout, unsigned sense_bytes)

    submit a scsi command as part of error recovery

    :param struct scsi_cmnd \*scmd:
        SCSI command structure to hijack

    :param unsigned char \*cmnd:
        CDB to send

    :param int cmnd_size:
        size in bytes of \ ``cmnd``\ 

    :param int timeout:
        timeout for this request

    :param unsigned sense_bytes:
        size of sense data to copy or 0

.. _`scsi_send_eh_cmnd.description`:

Description
-----------

This function is used to send a scsi command down to a target device
as part of the error recovery process. See also \ :c:func:`scsi_eh_prep_cmnd`\  above.

.. _`scsi_send_eh_cmnd.return-value`:

Return value
------------

   SUCCESS or FAILED or NEEDS_RETRY

.. _`scsi_request_sense`:

scsi_request_sense
==================

.. c:function:: int scsi_request_sense(struct scsi_cmnd *scmd)

    Request sense data from a particular target.

    :param struct scsi_cmnd \*scmd:
        SCSI cmd for request sense.

.. _`scsi_request_sense.notes`:

Notes
-----

   Some hosts automatically obtain this information, others require
   that we obtain it on our own. This function will *not* return until
   the command either times out, or it completes.

.. _`scsi_eh_finish_cmd`:

scsi_eh_finish_cmd
==================

.. c:function:: void scsi_eh_finish_cmd(struct scsi_cmnd *scmd, struct list_head *done_q)

    Handle a cmd that eh is finished with.

    :param struct scsi_cmnd \*scmd:
        Original SCSI cmd that eh has finished.

    :param struct list_head \*done_q:
        Queue for processed commands.

.. _`scsi_eh_finish_cmd.notes`:

Notes
-----

   We don't want to use the normal command completion while we are are
   still handling errors - it may cause other commands to be queued,
   and that would disturb what we are doing.  Thus we really want to
   keep a list of pending commands for final completion, and once we
   are ready to leave error handling we handle completion for real.

.. _`scsi_eh_get_sense`:

scsi_eh_get_sense
=================

.. c:function:: int scsi_eh_get_sense(struct list_head *work_q, struct list_head *done_q)

    Get device sense data.

    :param struct list_head \*work_q:
        Queue of commands to process.

    :param struct list_head \*done_q:
        Queue of processed commands.

.. _`scsi_eh_get_sense.description`:

Description
-----------

   See if we need to request sense information.  if so, then get it
   now, so we have a better idea of what to do.

.. _`scsi_eh_get_sense.notes`:

Notes
-----

   This has the unfortunate side effect that if a shost adapter does
   not automatically request sense information, we end up shutting
   it down before we request it.

   All drivers should request sense information internally these days,
   so for now all I have to say is tough noogies if you end up in here.

   XXX: Long term this code should go away, but that needs an audit of
        all LLDDs first.

.. _`scsi_eh_tur`:

scsi_eh_tur
===========

.. c:function:: int scsi_eh_tur(struct scsi_cmnd *scmd)

    Send TUR to device.

    :param struct scsi_cmnd \*scmd:
        \ :c:type:`struct scsi_cmnd <scsi_cmnd>`\  to send TUR

.. _`scsi_eh_tur.return-value`:

Return value
------------

   0 - Device is ready. 1 - Device NOT ready.

.. _`scsi_eh_test_devices`:

scsi_eh_test_devices
====================

.. c:function:: int scsi_eh_test_devices(struct list_head *cmd_list, struct list_head *work_q, struct list_head *done_q, int try_stu)

    check if devices are responding from error recovery.

    :param struct list_head \*cmd_list:
        scsi commands in error recovery.

    :param struct list_head \*work_q:
        queue for commands which still need more error recovery

    :param struct list_head \*done_q:
        queue for commands which are finished

    :param int try_stu:
        boolean on if a STU command should be tried in addition to TUR.

.. _`scsi_eh_test_devices.decription`:

Decription
----------

   Tests if devices are in a working state.  Commands to devices now in
   a working state are sent to the done_q while commands to devices which
   are still failing to respond are returned to the work_q for more
   processing.

.. _`scsi_eh_try_stu`:

scsi_eh_try_stu
===============

.. c:function:: int scsi_eh_try_stu(struct scsi_cmnd *scmd)

    Send START_UNIT to device.

    :param struct scsi_cmnd \*scmd:
        \ :c:type:`struct scsi_cmnd <scsi_cmnd>`\  to send START_UNIT

.. _`scsi_eh_try_stu.return-value`:

Return value
------------

   0 - Device is ready. 1 - Device NOT ready.

.. _`scsi_eh_bus_device_reset`:

scsi_eh_bus_device_reset
========================

.. c:function:: int scsi_eh_bus_device_reset(struct Scsi_Host *shost, struct list_head *work_q, struct list_head *done_q)

    send bdr if needed

    :param struct Scsi_Host \*shost:
        scsi host being recovered.

    :param struct list_head \*work_q:
        \ :c:type:`struct list_head <list_head>`\  for pending commands.

    :param struct list_head \*done_q:
        \ :c:type:`struct list_head <list_head>`\  for processed commands.

.. _`scsi_eh_bus_device_reset.notes`:

Notes
-----

   Try a bus device reset.  Still, look to see whether we have multiple
   devices that are jammed or not - if we have multiple devices, it
   makes no sense to try bus_device_reset - we really would need to try
   a bus_reset instead.

.. _`scsi_eh_target_reset`:

scsi_eh_target_reset
====================

.. c:function:: int scsi_eh_target_reset(struct Scsi_Host *shost, struct list_head *work_q, struct list_head *done_q)

    send target reset if needed

    :param struct Scsi_Host \*shost:
        scsi host being recovered.

    :param struct list_head \*work_q:
        \ :c:type:`struct list_head <list_head>`\  for pending commands.

    :param struct list_head \*done_q:
        \ :c:type:`struct list_head <list_head>`\  for processed commands.

.. _`scsi_eh_target_reset.notes`:

Notes
-----

   Try a target reset.

.. _`scsi_eh_bus_reset`:

scsi_eh_bus_reset
=================

.. c:function:: int scsi_eh_bus_reset(struct Scsi_Host *shost, struct list_head *work_q, struct list_head *done_q)

    send a bus reset

    :param struct Scsi_Host \*shost:
        \ :c:type:`struct scsi <scsi>`\  host being recovered.

    :param struct list_head \*work_q:
        \ :c:type:`struct list_head <list_head>`\  for pending commands.

    :param struct list_head \*done_q:
        \ :c:type:`struct list_head <list_head>`\  for processed commands.

.. _`scsi_eh_host_reset`:

scsi_eh_host_reset
==================

.. c:function:: int scsi_eh_host_reset(struct Scsi_Host *shost, struct list_head *work_q, struct list_head *done_q)

    send a host reset

    :param struct Scsi_Host \*shost:
        host to be reset.

    :param struct list_head \*work_q:
        \ :c:type:`struct list_head <list_head>`\  for pending commands.

    :param struct list_head \*done_q:
        \ :c:type:`struct list_head <list_head>`\  for processed commands.

.. _`scsi_eh_offline_sdevs`:

scsi_eh_offline_sdevs
=====================

.. c:function:: void scsi_eh_offline_sdevs(struct list_head *work_q, struct list_head *done_q)

    offline scsi devices that fail to recover

    :param struct list_head \*work_q:
        \ :c:type:`struct list_head <list_head>`\  for pending commands.

    :param struct list_head \*done_q:
        \ :c:type:`struct list_head <list_head>`\  for processed commands.

.. _`scsi_noretry_cmd`:

scsi_noretry_cmd
================

.. c:function:: int scsi_noretry_cmd(struct scsi_cmnd *scmd)

    determine if command should be failed fast

    :param struct scsi_cmnd \*scmd:
        SCSI cmd to examine.

.. _`scsi_decide_disposition`:

scsi_decide_disposition
=======================

.. c:function:: int scsi_decide_disposition(struct scsi_cmnd *scmd)

    Disposition a cmd on return from LLD.

    :param struct scsi_cmnd \*scmd:
        SCSI cmd to examine.

.. _`scsi_decide_disposition.notes`:

Notes
-----

   This is *only* called when we are examining the status after sending
   out the actual data command.  any commands that are queued for error
   recovery (e.g. test_unit_ready) do *not* come through here.

   When this routine returns failed, it means the error handler thread
   is woken.  In cases where the error code indicates an error that
   doesn't require the error handler read (i.e. we don't need to
   abort/reset), this function should return SUCCESS.

.. _`scsi_eh_lock_door`:

scsi_eh_lock_door
=================

.. c:function:: void scsi_eh_lock_door(struct scsi_device *sdev)

    Prevent medium removal for the specified device

    :param struct scsi_device \*sdev:
        SCSI device to prevent medium removal

.. _`scsi_eh_lock_door.locking`:

Locking
-------

     We must be called from process context.

.. _`scsi_eh_lock_door.notes`:

Notes
-----

     We queue up an asynchronous "ALLOW MEDIUM REMOVAL" request on the
     head of the devices request queue, and continue.

.. _`scsi_restart_operations`:

scsi_restart_operations
=======================

.. c:function:: void scsi_restart_operations(struct Scsi_Host *shost)

    restart io operations to the specified host.

    :param struct Scsi_Host \*shost:
        Host we are restarting.

.. _`scsi_restart_operations.notes`:

Notes
-----

   When we entered the error handler, we blocked all further i/o to
   this device.  we need to 'reverse' this process.

.. _`scsi_eh_ready_devs`:

scsi_eh_ready_devs
==================

.. c:function:: void scsi_eh_ready_devs(struct Scsi_Host *shost, struct list_head *work_q, struct list_head *done_q)

    check device ready state and recover if not.

    :param struct Scsi_Host \*shost:
        host to be recovered.

    :param struct list_head \*work_q:
        \ :c:type:`struct list_head <list_head>`\  for pending commands.

    :param struct list_head \*done_q:
        \ :c:type:`struct list_head <list_head>`\  for processed commands.

.. _`scsi_eh_flush_done_q`:

scsi_eh_flush_done_q
====================

.. c:function:: void scsi_eh_flush_done_q(struct list_head *done_q)

    finish processed commands or retry them.

    :param struct list_head \*done_q:
        list_head of processed commands.

.. _`scsi_unjam_host`:

scsi_unjam_host
===============

.. c:function:: void scsi_unjam_host(struct Scsi_Host *shost)

    Attempt to fix a host which has a cmd that failed.

    :param struct Scsi_Host \*shost:
        Host to unjam.

.. _`scsi_unjam_host.notes`:

Notes
-----

   When we come in here, we *know* that all commands on the bus have
   either completed, failed or timed out.  we also know that no further
   commands are being sent to the host, so things are relatively quiet
   and we have freedom to fiddle with things as we wish.

   This is only the *default* implementation.  it is possible for
   individual drivers to supply their own version of this function, and
   if the maintainer wishes to do this, it is strongly suggested that
   this function be taken as a template and modified.  this function
   was designed to correctly handle problems for about 95% of the
   different cases out there, and it should always provide at least a
   reasonable amount of error recovery.

   Any command marked 'failed' or 'timeout' must eventually have
   \ :c:func:`scsi_finish_cmd`\  called for it.  we do all of the retry stuff
   here, so when we restart the host after we return it should have an
   empty queue.

.. _`scsi_error_handler`:

scsi_error_handler
==================

.. c:function:: int scsi_error_handler(void *data)

    SCSI error handler thread

    :param void \*data:
        Host for which we are running.

.. _`scsi_error_handler.notes`:

Notes
-----

   This is the main error handling loop.  This is run as a kernel thread
   for every SCSI host and handles all error handling activity.

.. _`scsi_ioctl_reset`:

scsi_ioctl_reset
================

.. c:function:: int scsi_ioctl_reset(struct scsi_device *dev, int __user *arg)

    explicitly reset a host/bus/target/device

    :param struct scsi_device \*dev:
        scsi_device to operate on

    :param int __user \*arg:
        reset type (see sg.h)

.. _`scsi_get_sense_info_fld`:

scsi_get_sense_info_fld
=======================

.. c:function:: bool scsi_get_sense_info_fld(const u8 *sense_buffer, int sb_len, u64 *info_out)

    get information field from sense data (either fixed or descriptor format)

    :param const u8 \*sense_buffer:
        byte array of sense data

    :param int sb_len:
        number of valid bytes in sense_buffer

    :param u64 \*info_out:
        pointer to 64 integer where 8 or 4 byte information
        field will be placed if found.

.. _`scsi_get_sense_info_fld.return-value`:

Return value
------------

     true if information field found, false if not found.

.. This file was automatic generated / don't edit.

