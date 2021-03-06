.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/scsi_error.c

.. _`scsi_schedule_eh`:

scsi_schedule_eh
================

.. c:function:: void scsi_schedule_eh(struct Scsi_Host *shost)

    schedule EH for SCSI host

    :param shost:
        SCSI host to invoke error handling on.
    :type shost: struct Scsi_Host \*

.. _`scsi_schedule_eh.description`:

Description
-----------

Schedule SCSI EH without scmd.

.. _`scmd_eh_abort_handler`:

scmd_eh_abort_handler
=====================

.. c:function:: void scmd_eh_abort_handler(struct work_struct *work)

    Handle command aborts

    :param work:
        command to be aborted.
    :type work: struct work_struct \*

.. _`scmd_eh_abort_handler.note`:

Note
----

this function must be called only for a command that has timed out.
Because the block layer marks a request as complete before it calls
\ :c:func:`scsi_times_out`\ , a .scsi_done() call from the LLD for a command that has
timed out do not have any effect. Hence it is safe to call
\ :c:func:`scsi_finish_command`\  from this function.

.. _`scsi_abort_command`:

scsi_abort_command
==================

.. c:function:: int scsi_abort_command(struct scsi_cmnd *scmd)

    schedule a command abort

    :param scmd:
        scmd to abort.
    :type scmd: struct scsi_cmnd \*

.. _`scsi_abort_command.description`:

Description
-----------

We only need to abort commands after a command timeout

.. _`scsi_eh_reset`:

scsi_eh_reset
=============

.. c:function:: void scsi_eh_reset(struct scsi_cmnd *scmd)

    call into ->eh_action to reset internal counters

    :param scmd:
        scmd to run eh on.
    :type scmd: struct scsi_cmnd \*

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

    :param scmd:
        scmd to run eh on.
    :type scmd: struct scsi_cmnd \*

.. _`scsi_times_out`:

scsi_times_out
==============

.. c:function:: enum blk_eh_timer_return scsi_times_out(struct request *req)

    Timeout function for normal scsi commands.

    :param req:
        request that is timing out.
    :type req: struct request \*

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

    :param sdev:
        Device on which we are performing recovery.
    :type sdev: struct scsi_device \*

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

    :param shost:
        scsi host being recovered.
    :type shost: struct Scsi_Host \*

    :param work_q:
        Queue of scsi cmds to process.
    :type work_q: struct list_head \*

.. _`scsi_report_sense`:

scsi_report_sense
=================

.. c:function:: void scsi_report_sense(struct scsi_device *sdev, struct scsi_sense_hdr *sshdr)

    Examine scsi sense information and log messages for certain conditions, also issue uevents for some of them.

    :param sdev:
        Device reporting the sense code
    :type sdev: struct scsi_device \*

    :param sshdr:
        sshdr to be examined
    :type sshdr: struct scsi_sense_hdr \*

.. _`scsi_check_sense`:

scsi_check_sense
================

.. c:function:: int scsi_check_sense(struct scsi_cmnd *scmd)

    Examine scsi cmd sense

    :param scmd:
        Cmd to have sense checked.
    :type scmd: struct scsi_cmnd \*

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

    :param scmd:
        SCSI cmd to examine.
    :type scmd: struct scsi_cmnd \*

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

    :param scmd:
        Cmd that is done.
    :type scmd: struct scsi_cmnd \*

.. _`scsi_try_host_reset`:

scsi_try_host_reset
===================

.. c:function:: int scsi_try_host_reset(struct scsi_cmnd *scmd)

    ask host adapter to reset itself

    :param scmd:
        SCSI cmd to send host reset.
    :type scmd: struct scsi_cmnd \*

.. _`scsi_try_bus_reset`:

scsi_try_bus_reset
==================

.. c:function:: int scsi_try_bus_reset(struct scsi_cmnd *scmd)

    ask host to perform a bus reset

    :param scmd:
        SCSI cmd to send bus reset.
    :type scmd: struct scsi_cmnd \*

.. _`scsi_try_target_reset`:

scsi_try_target_reset
=====================

.. c:function:: int scsi_try_target_reset(struct scsi_cmnd *scmd)

    Ask host to perform a target reset

    :param scmd:
        SCSI cmd used to send a target reset
    :type scmd: struct scsi_cmnd \*

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

    :param scmd:
        SCSI cmd used to send BDR
    :type scmd: struct scsi_cmnd \*

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

    :param hostt:
        SCSI driver host template
    :type hostt: struct scsi_host_template \*

    :param scmd:
        SCSI cmd used to send a target reset
    :type scmd: struct scsi_cmnd \*

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

    :param scmd:
        SCSI command structure to hijack
    :type scmd: struct scsi_cmnd \*

    :param ses:
        structure to save restore information
    :type ses: struct scsi_eh_save \*

    :param cmnd:
        CDB to send. Can be NULL if no new cmnd is needed
    :type cmnd: unsigned char \*

    :param cmnd_size:
        size in bytes of \ ``cmnd``\  (must be <= BLK_MAX_CDB)
    :type cmnd_size: int

    :param sense_bytes:
        size of sense data to copy. or 0 (if != 0 \ ``cmnd``\  is ignored)
    :type sense_bytes: unsigned

.. _`scsi_eh_prep_cmnd.description`:

Description
-----------

This function is used to save a scsi command information before re-execution
as part of the error recovery process.  If \ ``sense_bytes``\  is 0 the command
sent must be one that does not transfer any data.  If \ ``sense_bytes``\  != 0
\ ``cmnd``\  is ignored and this functions sets up a REQUEST_SENSE command
and cmnd buffers to read \ ``sense_bytes``\  into \ ``scmd->sense_buffer``\ .

.. _`scsi_eh_restore_cmnd`:

scsi_eh_restore_cmnd
====================

.. c:function:: void scsi_eh_restore_cmnd(struct scsi_cmnd* scmd, struct scsi_eh_save *ses)

    Restore a scsi command info as part of error recovery

    :param scmd:
        SCSI command structure to restore
    :type scmd: struct scsi_cmnd\*

    :param ses:
        saved information from a coresponding call to scsi_eh_prep_cmnd
    :type ses: struct scsi_eh_save \*

.. _`scsi_eh_restore_cmnd.description`:

Description
-----------

Undo any damage done by above \ :c:func:`scsi_eh_prep_cmnd`\ .

.. _`scsi_send_eh_cmnd`:

scsi_send_eh_cmnd
=================

.. c:function:: int scsi_send_eh_cmnd(struct scsi_cmnd *scmd, unsigned char *cmnd, int cmnd_size, int timeout, unsigned sense_bytes)

    submit a scsi command as part of error recovery

    :param scmd:
        SCSI command structure to hijack
    :type scmd: struct scsi_cmnd \*

    :param cmnd:
        CDB to send
    :type cmnd: unsigned char \*

    :param cmnd_size:
        size in bytes of \ ``cmnd``\ 
    :type cmnd_size: int

    :param timeout:
        timeout for this request
    :type timeout: int

    :param sense_bytes:
        size of sense data to copy or 0
    :type sense_bytes: unsigned

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

    :param scmd:
        SCSI cmd for request sense.
    :type scmd: struct scsi_cmnd \*

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

    :param scmd:
        Original SCSI cmd that eh has finished.
    :type scmd: struct scsi_cmnd \*

    :param done_q:
        Queue for processed commands.
    :type done_q: struct list_head \*

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

    :param work_q:
        Queue of commands to process.
    :type work_q: struct list_head \*

    :param done_q:
        Queue of processed commands.
    :type done_q: struct list_head \*

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

    :param scmd:
        \ :c:type:`struct scsi_cmnd <scsi_cmnd>`\  to send TUR
    :type scmd: struct scsi_cmnd \*

.. _`scsi_eh_tur.return-value`:

Return value
------------

   0 - Device is ready. 1 - Device NOT ready.

.. _`scsi_eh_test_devices`:

scsi_eh_test_devices
====================

.. c:function:: int scsi_eh_test_devices(struct list_head *cmd_list, struct list_head *work_q, struct list_head *done_q, int try_stu)

    check if devices are responding from error recovery.

    :param cmd_list:
        scsi commands in error recovery.
    :type cmd_list: struct list_head \*

    :param work_q:
        queue for commands which still need more error recovery
    :type work_q: struct list_head \*

    :param done_q:
        queue for commands which are finished
    :type done_q: struct list_head \*

    :param try_stu:
        boolean on if a STU command should be tried in addition to TUR.
    :type try_stu: int

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

    :param scmd:
        \ :c:type:`struct scsi_cmnd <scsi_cmnd>`\  to send START_UNIT
    :type scmd: struct scsi_cmnd \*

.. _`scsi_eh_try_stu.return-value`:

Return value
------------

   0 - Device is ready. 1 - Device NOT ready.

.. _`scsi_eh_bus_device_reset`:

scsi_eh_bus_device_reset
========================

.. c:function:: int scsi_eh_bus_device_reset(struct Scsi_Host *shost, struct list_head *work_q, struct list_head *done_q)

    send bdr if needed

    :param shost:
        scsi host being recovered.
    :type shost: struct Scsi_Host \*

    :param work_q:
        \ :c:type:`struct list_head <list_head>`\  for pending commands.
    :type work_q: struct list_head \*

    :param done_q:
        \ :c:type:`struct list_head <list_head>`\  for processed commands.
    :type done_q: struct list_head \*

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

    :param shost:
        scsi host being recovered.
    :type shost: struct Scsi_Host \*

    :param work_q:
        \ :c:type:`struct list_head <list_head>`\  for pending commands.
    :type work_q: struct list_head \*

    :param done_q:
        \ :c:type:`struct list_head <list_head>`\  for processed commands.
    :type done_q: struct list_head \*

.. _`scsi_eh_target_reset.notes`:

Notes
-----

   Try a target reset.

.. _`scsi_eh_bus_reset`:

scsi_eh_bus_reset
=================

.. c:function:: int scsi_eh_bus_reset(struct Scsi_Host *shost, struct list_head *work_q, struct list_head *done_q)

    send a bus reset

    :param shost:
        \ :c:type:`struct scsi <scsi>`\  host being recovered.
    :type shost: struct Scsi_Host \*

    :param work_q:
        \ :c:type:`struct list_head <list_head>`\  for pending commands.
    :type work_q: struct list_head \*

    :param done_q:
        \ :c:type:`struct list_head <list_head>`\  for processed commands.
    :type done_q: struct list_head \*

.. _`scsi_eh_host_reset`:

scsi_eh_host_reset
==================

.. c:function:: int scsi_eh_host_reset(struct Scsi_Host *shost, struct list_head *work_q, struct list_head *done_q)

    send a host reset

    :param shost:
        host to be reset.
    :type shost: struct Scsi_Host \*

    :param work_q:
        \ :c:type:`struct list_head <list_head>`\  for pending commands.
    :type work_q: struct list_head \*

    :param done_q:
        \ :c:type:`struct list_head <list_head>`\  for processed commands.
    :type done_q: struct list_head \*

.. _`scsi_eh_offline_sdevs`:

scsi_eh_offline_sdevs
=====================

.. c:function:: void scsi_eh_offline_sdevs(struct list_head *work_q, struct list_head *done_q)

    offline scsi devices that fail to recover

    :param work_q:
        \ :c:type:`struct list_head <list_head>`\  for pending commands.
    :type work_q: struct list_head \*

    :param done_q:
        \ :c:type:`struct list_head <list_head>`\  for processed commands.
    :type done_q: struct list_head \*

.. _`scsi_noretry_cmd`:

scsi_noretry_cmd
================

.. c:function:: int scsi_noretry_cmd(struct scsi_cmnd *scmd)

    determine if command should be failed fast

    :param scmd:
        SCSI cmd to examine.
    :type scmd: struct scsi_cmnd \*

.. _`scsi_decide_disposition`:

scsi_decide_disposition
=======================

.. c:function:: int scsi_decide_disposition(struct scsi_cmnd *scmd)

    Disposition a cmd on return from LLD.

    :param scmd:
        SCSI cmd to examine.
    :type scmd: struct scsi_cmnd \*

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

    :param sdev:
        SCSI device to prevent medium removal
    :type sdev: struct scsi_device \*

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

    :param shost:
        Host we are restarting.
    :type shost: struct Scsi_Host \*

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

    :param shost:
        host to be recovered.
    :type shost: struct Scsi_Host \*

    :param work_q:
        \ :c:type:`struct list_head <list_head>`\  for pending commands.
    :type work_q: struct list_head \*

    :param done_q:
        \ :c:type:`struct list_head <list_head>`\  for processed commands.
    :type done_q: struct list_head \*

.. _`scsi_eh_flush_done_q`:

scsi_eh_flush_done_q
====================

.. c:function:: void scsi_eh_flush_done_q(struct list_head *done_q)

    finish processed commands or retry them.

    :param done_q:
        list_head of processed commands.
    :type done_q: struct list_head \*

.. _`scsi_unjam_host`:

scsi_unjam_host
===============

.. c:function:: void scsi_unjam_host(struct Scsi_Host *shost)

    Attempt to fix a host which has a cmd that failed.

    :param shost:
        Host to unjam.
    :type shost: struct Scsi_Host \*

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

    :param data:
        Host for which we are running.
    :type data: void \*

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

    :param dev:
        scsi_device to operate on
    :type dev: struct scsi_device \*

    :param arg:
        reset type (see sg.h)
    :type arg: int __user \*

.. _`scsi_get_sense_info_fld`:

scsi_get_sense_info_fld
=======================

.. c:function:: bool scsi_get_sense_info_fld(const u8 *sense_buffer, int sb_len, u64 *info_out)

    get information field from sense data (either fixed or descriptor format)

    :param sense_buffer:
        byte array of sense data
    :type sense_buffer: const u8 \*

    :param sb_len:
        number of valid bytes in sense_buffer
    :type sb_len: int

    :param info_out:
        pointer to 64 integer where 8 or 4 byte information
        field will be placed if found.
    :type info_out: u64 \*

.. _`scsi_get_sense_info_fld.return-value`:

Return value
------------

     true if information field found, false if not found.

.. This file was automatic generated / don't edit.

