.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/libata-eh.c

.. _`__ata_ehi_push_desc`:

__ata_ehi_push_desc
===================

.. c:function:: void __ata_ehi_push_desc(struct ata_eh_info *ehi, const char *fmt,  ...)

    push error description without adding separator

    :param struct ata_eh_info \*ehi:
        target EHI

    :param const char \*fmt:
        printf format string

    :param ... :
        variable arguments

.. _`__ata_ehi_push_desc.description`:

Description
-----------

     Format string according to \ ``fmt``\  and append it to \ ``ehi``\ ->desc.

.. _`__ata_ehi_push_desc.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_ehi_push_desc`:

ata_ehi_push_desc
=================

.. c:function:: void ata_ehi_push_desc(struct ata_eh_info *ehi, const char *fmt,  ...)

    push error description with separator

    :param struct ata_eh_info \*ehi:
        target EHI

    :param const char \*fmt:
        printf format string

    :param ... :
        variable arguments

.. _`ata_ehi_push_desc.description`:

Description
-----------

     Format string according to \ ``fmt``\  and append it to \ ``ehi``\ ->desc.
     If \ ``ehi``\ ->desc is not empty, ", " is added in-between.

.. _`ata_ehi_push_desc.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_ehi_clear_desc`:

ata_ehi_clear_desc
==================

.. c:function:: void ata_ehi_clear_desc(struct ata_eh_info *ehi)

    clean error description

    :param struct ata_eh_info \*ehi:
        target EHI

.. _`ata_ehi_clear_desc.description`:

Description
-----------

     Clear \ ``ehi``\ ->desc.

.. _`ata_ehi_clear_desc.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_port_desc`:

ata_port_desc
=============

.. c:function:: void ata_port_desc(struct ata_port *ap, const char *fmt,  ...)

    append port description

    :param struct ata_port \*ap:
        target ATA port

    :param const char \*fmt:
        printf format string

    :param ... :
        variable arguments

.. _`ata_port_desc.description`:

Description
-----------

     Format string according to \ ``fmt``\  and append it to port
     description.  If port description is not empty, " " is added
     in-between.  This function is to be used while initializing
     ata_host.  The description is printed on host registration.

.. _`ata_port_desc.locking`:

LOCKING
-------

     None.

.. _`ata_port_pbar_desc`:

ata_port_pbar_desc
==================

.. c:function:: void ata_port_pbar_desc(struct ata_port *ap, int bar, ssize_t offset, const char *name)

    append PCI BAR description

    :param struct ata_port \*ap:
        target ATA port

    :param int bar:
        target PCI BAR

    :param ssize_t offset:
        offset into PCI BAR

    :param const char \*name:
        name of the area

.. _`ata_port_pbar_desc.description`:

Description
-----------

     If \ ``offset``\  is negative, this function formats a string which
     contains the name, address, size and type of the BAR and
     appends it to the port description.  If \ ``offset``\  is zero or
     positive, only name and offsetted address is appended.

.. _`ata_port_pbar_desc.locking`:

LOCKING
-------

     None.

.. _`ata_internal_cmd_timeout`:

ata_internal_cmd_timeout
========================

.. c:function:: unsigned long ata_internal_cmd_timeout(struct ata_device *dev, u8 cmd)

    determine timeout for an internal command

    :param struct ata_device \*dev:
        target device

    :param u8 cmd:
        internal command to be issued

.. _`ata_internal_cmd_timeout.description`:

Description
-----------

     Determine timeout for internal command \ ``cmd``\  for \ ``dev``\ .

.. _`ata_internal_cmd_timeout.locking`:

LOCKING
-------

     EH context.

.. _`ata_internal_cmd_timeout.return`:

Return
------

     Determined timeout.

.. _`ata_internal_cmd_timed_out`:

ata_internal_cmd_timed_out
==========================

.. c:function:: void ata_internal_cmd_timed_out(struct ata_device *dev, u8 cmd)

    notification for internal command timeout

    :param struct ata_device \*dev:
        target device

    :param u8 cmd:
        internal command which timed out

.. _`ata_internal_cmd_timed_out.description`:

Description
-----------

     Notify EH that internal command \ ``cmd``\  for \ ``dev``\  timed out.  This
     function should be called only for commands whose timeouts are
     determined using \ :c:func:`ata_internal_cmd_timeout`\ .

.. _`ata_internal_cmd_timed_out.locking`:

LOCKING
-------

     EH context.

.. _`ata_eh_acquire`:

ata_eh_acquire
==============

.. c:function:: void ata_eh_acquire(struct ata_port *ap)

    acquire EH ownership

    :param struct ata_port \*ap:
        ATA port to acquire EH ownership for

.. _`ata_eh_acquire.description`:

Description
-----------

     Acquire EH ownership for \ ``ap``\ .  This is the basic exclusion
     mechanism for ports sharing a host.  Only one port hanging off
     the same host can claim the ownership of EH.

.. _`ata_eh_acquire.locking`:

LOCKING
-------

     EH context.

.. _`ata_eh_release`:

ata_eh_release
==============

.. c:function:: void ata_eh_release(struct ata_port *ap)

    release EH ownership

    :param struct ata_port \*ap:
        ATA port to release EH ownership for

.. _`ata_eh_release.description`:

Description
-----------

     Release EH ownership for \ ``ap``\  if the caller.  The caller must
     have acquired EH ownership using \ :c:func:`ata_eh_acquire`\  previously.

.. _`ata_eh_release.locking`:

LOCKING
-------

     EH context.

.. _`ata_scsi_timed_out`:

ata_scsi_timed_out
==================

.. c:function:: enum blk_eh_timer_return ata_scsi_timed_out(struct scsi_cmnd *cmd)

    SCSI layer time out callback

    :param struct scsi_cmnd \*cmd:
        timed out SCSI command

.. _`ata_scsi_timed_out.description`:

Description
-----------

     Handles SCSI layer timeout.  We race with normal completion of
     the qc for \ ``cmd``\ .  If the qc is already gone, we lose and let
     the scsi command finish (EH_HANDLED).  Otherwise, the qc has
     timed out and EH should be invoked.  Prevent \ :c:func:`ata_qc_complete`\ 
     from finishing it by setting EH_SCHEDULED and return
     EH_NOT_HANDLED.

     TODO: kill this function once old EH is gone.

.. _`ata_scsi_timed_out.locking`:

LOCKING
-------

     Called from timer context

.. _`ata_scsi_timed_out.return`:

Return
------

     EH_HANDLED or EH_NOT_HANDLED

.. _`ata_scsi_error`:

ata_scsi_error
==============

.. c:function:: void ata_scsi_error(struct Scsi_Host *host)

    SCSI layer error handler callback

    :param struct Scsi_Host \*host:
        SCSI host on which error occurred

.. _`ata_scsi_error.description`:

Description
-----------

     Handles SCSI-layer-thrown error events.

.. _`ata_scsi_error.locking`:

LOCKING
-------

     Inherited from SCSI layer (none, can sleep)

.. _`ata_scsi_error.return`:

Return
------

     Zero.

.. _`ata_scsi_cmd_error_handler`:

ata_scsi_cmd_error_handler
==========================

.. c:function:: void ata_scsi_cmd_error_handler(struct Scsi_Host *host, struct ata_port *ap, struct list_head *eh_work_q)

    error callback for a list of commands

    :param struct Scsi_Host \*host:
        scsi host containing the port

    :param struct ata_port \*ap:
        ATA port within the host

    :param struct list_head \*eh_work_q:
        list of commands to process

.. _`ata_scsi_cmd_error_handler.description`:

Description
-----------

process the given list of commands and return those finished to the
ap->eh_done_q.  This function is the first part of the libata error
handler which processes a given list of failed commands.

.. _`ata_scsi_port_error_handler`:

ata_scsi_port_error_handler
===========================

.. c:function:: void ata_scsi_port_error_handler(struct Scsi_Host *host, struct ata_port *ap)

    recover the port after the commands

    :param struct Scsi_Host \*host:
        SCSI host containing the port

    :param struct ata_port \*ap:
        the ATA port

.. _`ata_scsi_port_error_handler.description`:

Description
-----------

Handle the recovery of the port \ ``ap``\  after all the commands
have been recovered.

.. _`ata_port_wait_eh`:

ata_port_wait_eh
================

.. c:function:: void ata_port_wait_eh(struct ata_port *ap)

    Wait for the currently pending EH to complete

    :param struct ata_port \*ap:
        Port to wait EH for

.. _`ata_port_wait_eh.description`:

Description
-----------

     Wait until the currently pending EH is complete.

.. _`ata_port_wait_eh.locking`:

LOCKING
-------

     Kernel thread context (may sleep).

.. _`ata_eh_set_pending`:

ata_eh_set_pending
==================

.. c:function:: void ata_eh_set_pending(struct ata_port *ap, int fastdrain)

    set ATA_PFLAG_EH_PENDING and activate fast drain

    :param struct ata_port \*ap:
        target ATA port

    :param int fastdrain:
        activate fast drain

.. _`ata_eh_set_pending.description`:

Description
-----------

     Set ATA_PFLAG_EH_PENDING and activate fast drain if \ ``fastdrain``\ 
     is non-zero and EH wasn't pending before.  Fast drain ensures
     that EH kicks in in timely manner.

.. _`ata_eh_set_pending.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_qc_schedule_eh`:

ata_qc_schedule_eh
==================

.. c:function:: void ata_qc_schedule_eh(struct ata_queued_cmd *qc)

    schedule qc for error handling

    :param struct ata_queued_cmd \*qc:
        command to schedule error handling for

.. _`ata_qc_schedule_eh.description`:

Description
-----------

     Schedule error handling for \ ``qc``\ .  EH will kick in as soon as
     other commands are drained.

.. _`ata_qc_schedule_eh.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_std_sched_eh`:

ata_std_sched_eh
================

.. c:function:: void ata_std_sched_eh(struct ata_port *ap)

    non-libsas ata_ports issue eh with this common routine

    :param struct ata_port \*ap:
        ATA port to schedule EH for

.. _`ata_std_sched_eh.description`:

Description
-----------

     LOCKING: inherited from ata_port_schedule_eh
     spin_lock_irqsave(host lock)

.. _`ata_std_end_eh`:

ata_std_end_eh
==============

.. c:function:: void ata_std_end_eh(struct ata_port *ap)

    non-libsas ata_ports complete eh with this common routine

    :param struct ata_port \*ap:
        ATA port to end EH for

.. _`ata_std_end_eh.description`:

Description
-----------

In the libata object model there is a 1:1 mapping of ata_port to
shost, so host fields can be directly manipulated under ap->lock, in
the libsas case we need to hold a lock at the ha->level to coordinate
these events.

.. _`ata_std_end_eh.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_port_schedule_eh`:

ata_port_schedule_eh
====================

.. c:function:: void ata_port_schedule_eh(struct ata_port *ap)

    schedule error handling without a qc

    :param struct ata_port \*ap:
        ATA port to schedule EH for

.. _`ata_port_schedule_eh.description`:

Description
-----------

     Schedule error handling for \ ``ap``\ .  EH will kick in as soon as
     all commands are drained.

.. _`ata_port_schedule_eh.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_link_abort`:

ata_link_abort
==============

.. c:function:: int ata_link_abort(struct ata_link *link)

    abort all qc's on the link

    :param struct ata_link \*link:
        ATA link to abort qc's for

.. _`ata_link_abort.description`:

Description
-----------

     Abort all active qc's active on \ ``link``\  and schedule EH.

.. _`ata_link_abort.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_link_abort.return`:

Return
------

     Number of aborted qc's.

.. _`ata_port_abort`:

ata_port_abort
==============

.. c:function:: int ata_port_abort(struct ata_port *ap)

    abort all qc's on the port

    :param struct ata_port \*ap:
        ATA port to abort qc's for

.. _`ata_port_abort.description`:

Description
-----------

     Abort all active qc's of \ ``ap``\  and schedule EH.

.. _`ata_port_abort.locking`:

LOCKING
-------

     spin_lock_irqsave(host_set lock)

.. _`ata_port_abort.return`:

Return
------

     Number of aborted qc's.

.. _`__ata_port_freeze`:

__ata_port_freeze
=================

.. c:function:: void __ata_port_freeze(struct ata_port *ap)

    freeze port

    :param struct ata_port \*ap:
        ATA port to freeze

.. _`__ata_port_freeze.description`:

Description
-----------

     This function is called when HSM violation or some other
     condition disrupts normal operation of the port.  Frozen port
     is not allowed to perform any operation until the port is
     thawed, which usually follows a successful reset.

     ap->ops->freeze() callback can be used for freezing the port
     hardware-wise (e.g. mask interrupt and stop DMA engine).  If a
     port cannot be frozen hardware-wise, the interrupt handler
     must ack and clear interrupts unconditionally while the port
     is frozen.

.. _`__ata_port_freeze.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_port_freeze`:

ata_port_freeze
===============

.. c:function:: int ata_port_freeze(struct ata_port *ap)

    abort & freeze port

    :param struct ata_port \*ap:
        ATA port to freeze

.. _`ata_port_freeze.description`:

Description
-----------

     Abort and freeze \ ``ap``\ .  The freeze operation must be called
     first, because some hardware requires special operations
     before the taskfile registers are accessible.

.. _`ata_port_freeze.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_port_freeze.return`:

Return
------

     Number of aborted commands.

.. _`sata_async_notification`:

sata_async_notification
=======================

.. c:function:: int sata_async_notification(struct ata_port *ap)

    SATA async notification handler

    :param struct ata_port \*ap:
        ATA port where async notification is received

.. _`sata_async_notification.description`:

Description
-----------

     Handler to be called when async notification via SDB FIS is
     received.  This function schedules EH if necessary.

.. _`sata_async_notification.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`sata_async_notification.return`:

Return
------

     1 if EH is scheduled, 0 otherwise.

.. _`ata_eh_freeze_port`:

ata_eh_freeze_port
==================

.. c:function:: void ata_eh_freeze_port(struct ata_port *ap)

    EH helper to freeze port

    :param struct ata_port \*ap:
        ATA port to freeze

.. _`ata_eh_freeze_port.description`:

Description
-----------

     Freeze \ ``ap``\ .

.. _`ata_eh_freeze_port.locking`:

LOCKING
-------

     None.

.. _`ata_eh_thaw_port`:

ata_eh_thaw_port
================

.. c:function:: void ata_eh_thaw_port(struct ata_port *ap)

    EH helper to thaw port

    :param struct ata_port \*ap:
        ATA port to thaw

.. _`ata_eh_thaw_port.description`:

Description
-----------

     Thaw frozen port \ ``ap``\ .

.. _`ata_eh_thaw_port.locking`:

LOCKING
-------

     None.

.. _`ata_eh_qc_complete`:

ata_eh_qc_complete
==================

.. c:function:: void ata_eh_qc_complete(struct ata_queued_cmd *qc)

    Complete an active ATA command from EH

    :param struct ata_queued_cmd \*qc:
        Command to complete

.. _`ata_eh_qc_complete.description`:

Description
-----------

     Indicate to the mid and upper layers that an ATA command has
     completed.  To be used from EH.

.. _`ata_eh_qc_retry`:

ata_eh_qc_retry
===============

.. c:function:: void ata_eh_qc_retry(struct ata_queued_cmd *qc)

    Tell midlayer to retry an ATA command after EH

    :param struct ata_queued_cmd \*qc:
        Command to retry

.. _`ata_eh_qc_retry.description`:

Description
-----------

     Indicate to the mid and upper layers that an ATA command
     should be retried.  To be used from EH.

     SCSI midlayer limits the number of retries to scmd->allowed.
     scmd->allowed is incremented for commands which get retried
     due to unrelated failures (qc->err_mask is zero).

.. _`ata_dev_disable`:

ata_dev_disable
===============

.. c:function:: void ata_dev_disable(struct ata_device *dev)

    disable ATA device

    :param struct ata_device \*dev:
        ATA device to disable

.. _`ata_dev_disable.description`:

Description
-----------

     Disable \ ``dev``\ .

.. _`ata_dev_disable.locking`:

Locking
-------

     EH context.

.. _`ata_eh_detach_dev`:

ata_eh_detach_dev
=================

.. c:function:: void ata_eh_detach_dev(struct ata_device *dev)

    detach ATA device

    :param struct ata_device \*dev:
        ATA device to detach

.. _`ata_eh_detach_dev.description`:

Description
-----------

     Detach \ ``dev``\ .

.. _`ata_eh_detach_dev.locking`:

LOCKING
-------

     None.

.. _`ata_eh_about_to_do`:

ata_eh_about_to_do
==================

.. c:function:: void ata_eh_about_to_do(struct ata_link *link, struct ata_device *dev, unsigned int action)

    about to perform eh_action

    :param struct ata_link \*link:
        target ATA link

    :param struct ata_device \*dev:
        target ATA dev for per-dev action (can be NULL)

    :param unsigned int action:
        action about to be performed

.. _`ata_eh_about_to_do.description`:

Description
-----------

     Called just before performing EH actions to clear related bits
     in \ ``link``\ ->eh_info such that eh actions are not unnecessarily
     repeated.

.. _`ata_eh_about_to_do.locking`:

LOCKING
-------

     None.

.. _`ata_eh_done`:

ata_eh_done
===========

.. c:function:: void ata_eh_done(struct ata_link *link, struct ata_device *dev, unsigned int action)

    EH action complete

    :param struct ata_link \*link:
        *undescribed*

    :param struct ata_device \*dev:
        target ATA dev for per-dev action (can be NULL)

    :param unsigned int action:
        action just completed

.. _`ata_eh_done.description`:

Description
-----------

     Called right after performing EH actions to clear related bits
     in \ ``link``\ ->eh_context.

.. _`ata_eh_done.locking`:

LOCKING
-------

     None.

.. _`ata_err_string`:

ata_err_string
==============

.. c:function:: const char *ata_err_string(unsigned int err_mask)

    convert err_mask to descriptive string

    :param unsigned int err_mask:
        error mask to convert to string

.. _`ata_err_string.description`:

Description
-----------

     Convert \ ``err_mask``\  to descriptive string.  Errors are
     prioritized according to severity and only the most severe
     error is reported.

.. _`ata_err_string.locking`:

LOCKING
-------

     None.

.. _`ata_err_string.return`:

Return
------

     Descriptive string for \ ``err_mask``\ 

.. _`ata_read_log_page`:

ata_read_log_page
=================

.. c:function:: unsigned int ata_read_log_page(struct ata_device *dev, u8 log, u8 page, void *buf, unsigned int sectors)

    read a specific log page

    :param struct ata_device \*dev:
        target device

    :param u8 log:
        log to read

    :param u8 page:
        page to read

    :param void \*buf:
        buffer to store read page

    :param unsigned int sectors:
        number of sectors to read

.. _`ata_read_log_page.description`:

Description
-----------

     Read log page using READ_LOG_EXT command.

.. _`ata_read_log_page.locking`:

LOCKING
-------

     Kernel thread context (may sleep).

.. _`ata_read_log_page.return`:

Return
------

     0 on success, AC_ERR_* mask otherwise.

.. _`ata_eh_read_log_10h`:

ata_eh_read_log_10h
===================

.. c:function:: int ata_eh_read_log_10h(struct ata_device *dev, int *tag, struct ata_taskfile *tf)

    Read log page 10h for NCQ error details

    :param struct ata_device \*dev:
        Device to read log page 10h from

    :param int \*tag:
        Resulting tag of the failed command

    :param struct ata_taskfile \*tf:
        Resulting taskfile registers of the failed command

.. _`ata_eh_read_log_10h.description`:

Description
-----------

     Read log page 10h to obtain NCQ error details and clear error
     condition.

.. _`ata_eh_read_log_10h.locking`:

LOCKING
-------

     Kernel thread context (may sleep).

.. _`ata_eh_read_log_10h.return`:

Return
------

     0 on success, -errno otherwise.

.. _`atapi_eh_tur`:

atapi_eh_tur
============

.. c:function:: unsigned int atapi_eh_tur(struct ata_device *dev, u8 *r_sense_key)

    perform ATAPI TEST_UNIT_READY

    :param struct ata_device \*dev:
        target ATAPI device

    :param u8 \*r_sense_key:
        out parameter for sense_key

.. _`atapi_eh_tur.description`:

Description
-----------

     Perform ATAPI TEST_UNIT_READY.

.. _`atapi_eh_tur.locking`:

LOCKING
-------

     EH context (may sleep).

.. _`atapi_eh_tur.return`:

Return
------

     0 on success, AC_ERR_* mask on failure.

.. _`ata_eh_request_sense`:

ata_eh_request_sense
====================

.. c:function:: void ata_eh_request_sense(struct ata_queued_cmd *qc, struct scsi_cmnd *cmd)

    perform REQUEST_SENSE_DATA_EXT

    :param struct ata_queued_cmd \*qc:
        *undescribed*

    :param struct scsi_cmnd \*cmd:
        scsi command for which the sense code should be set

.. _`ata_eh_request_sense.description`:

Description
-----------

     Perform REQUEST_SENSE_DATA_EXT after the device reported CHECK
     SENSE.  This function is an EH helper.

.. _`ata_eh_request_sense.locking`:

LOCKING
-------

     Kernel thread context (may sleep).

.. _`atapi_eh_request_sense`:

atapi_eh_request_sense
======================

.. c:function:: unsigned int atapi_eh_request_sense(struct ata_device *dev, u8 *sense_buf, u8 dfl_sense_key)

    perform ATAPI REQUEST_SENSE

    :param struct ata_device \*dev:
        device to perform REQUEST_SENSE to

    :param u8 \*sense_buf:
        result sense data buffer (SCSI_SENSE_BUFFERSIZE bytes long)

    :param u8 dfl_sense_key:
        default sense key to use

.. _`atapi_eh_request_sense.description`:

Description
-----------

     Perform ATAPI REQUEST_SENSE after the device reported CHECK
     SENSE.  This function is EH helper.

.. _`atapi_eh_request_sense.locking`:

LOCKING
-------

     Kernel thread context (may sleep).

.. _`atapi_eh_request_sense.return`:

Return
------

     0 on success, AC_ERR_* mask on failure

.. _`ata_eh_analyze_serror`:

ata_eh_analyze_serror
=====================

.. c:function:: void ata_eh_analyze_serror(struct ata_link *link)

    analyze SError for a failed port

    :param struct ata_link \*link:
        ATA link to analyze SError for

.. _`ata_eh_analyze_serror.description`:

Description
-----------

     Analyze SError if available and further determine cause of
     failure.

.. _`ata_eh_analyze_serror.locking`:

LOCKING
-------

     None.

.. _`ata_eh_analyze_ncq_error`:

ata_eh_analyze_ncq_error
========================

.. c:function:: void ata_eh_analyze_ncq_error(struct ata_link *link)

    analyze NCQ error

    :param struct ata_link \*link:
        ATA link to analyze NCQ error for

.. _`ata_eh_analyze_ncq_error.description`:

Description
-----------

     Read log page 10h, determine the offending qc and acquire
     error status TF.  For NCQ device errors, all LLDDs have to do
     is setting AC_ERR_DEV in ehi->err_mask.  This function takes
     care of the rest.

.. _`ata_eh_analyze_ncq_error.locking`:

LOCKING
-------

     Kernel thread context (may sleep).

.. _`ata_eh_analyze_tf`:

ata_eh_analyze_tf
=================

.. c:function:: unsigned int ata_eh_analyze_tf(struct ata_queued_cmd *qc, const struct ata_taskfile *tf)

    analyze taskfile of a failed qc

    :param struct ata_queued_cmd \*qc:
        qc to analyze

    :param const struct ata_taskfile \*tf:
        Taskfile registers to analyze

.. _`ata_eh_analyze_tf.description`:

Description
-----------

     Analyze taskfile of \ ``qc``\  and further determine cause of
     failure.  This function also requests ATAPI sense data if
     available.

.. _`ata_eh_analyze_tf.locking`:

LOCKING
-------

     Kernel thread context (may sleep).

.. _`ata_eh_analyze_tf.return`:

Return
------

     Determined recovery action

.. _`ata_eh_speed_down_verdict`:

ata_eh_speed_down_verdict
=========================

.. c:function:: unsigned int ata_eh_speed_down_verdict(struct ata_device *dev)

    Determine speed down verdict

    :param struct ata_device \*dev:
        Device of interest

.. _`ata_eh_speed_down_verdict.description`:

Description
-----------

     This function examines error ring of \ ``dev``\  and determines
     whether NCQ needs to be turned off, transfer speed should be
     stepped down, or falling back to PIO is necessary.

     ECAT_ATA_BUS    : ATA_BUS error for any command

     ECAT_TOUT_HSM   : TIMEOUT for any command or HSM violation for
                       IO commands

     ECAT_UNK_DEV    : Unknown DEV error for IO commands

     ECAT_DUBIOUS_*  : Identical to above three but occurred while
                       data transfer hasn't been verified.

     Verdicts are

     NCQ_OFF         : Turn off NCQ.

     SPEED_DOWN      : Speed down transfer speed but don't fall back
                       to PIO.

     FALLBACK_TO_PIO : Fall back to PIO.

     Even if multiple verdicts are returned, only one action is
     taken per error.  An action triggered by non-DUBIOUS errors
     clears ering, while one triggered by DUBIOUS_* errors doesn't.
     This is to expedite speed down decisions right after device is
     initially configured.

     The following are speed down rules.  #1 and #2 deal with
     DUBIOUS errors.

     1. If more than one DUBIOUS_ATA_BUS or DUBIOUS_TOUT_HSM errors
        occurred during last 5 mins, SPEED_DOWN and FALLBACK_TO_PIO.

     2. If more than one DUBIOUS_TOUT_HSM or DUBIOUS_UNK_DEV errors
        occurred during last 5 mins, NCQ_OFF.

     3. If more than 8 ATA_BUS, TOUT_HSM or UNK_DEV errors
        occurred during last 5 mins, FALLBACK_TO_PIO

     4. If more than 3 TOUT_HSM or UNK_DEV errors occurred
        during last 10 mins, NCQ_OFF.

     5. If more than 3 ATA_BUS or TOUT_HSM errors, or more than 6
        UNK_DEV errors occurred during last 10 mins, SPEED_DOWN.

.. _`ata_eh_speed_down_verdict.locking`:

LOCKING
-------

     Inherited from caller.

.. _`ata_eh_speed_down_verdict.return`:

Return
------

     OR of ATA_EH_SPDN_* flags.

.. _`ata_eh_speed_down`:

ata_eh_speed_down
=================

.. c:function:: unsigned int ata_eh_speed_down(struct ata_device *dev, unsigned int eflags, unsigned int err_mask)

    record error and speed down if necessary

    :param struct ata_device \*dev:
        Failed device

    :param unsigned int eflags:
        mask of ATA_EFLAG_* flags

    :param unsigned int err_mask:
        err_mask of the error

.. _`ata_eh_speed_down.description`:

Description
-----------

     Record error and examine error history to determine whether
     adjusting transmission speed is necessary.  It also sets
     transmission limits appropriately if such adjustment is
     necessary.

.. _`ata_eh_speed_down.locking`:

LOCKING
-------

     Kernel thread context (may sleep).

.. _`ata_eh_speed_down.return`:

Return
------

     Determined recovery action.

.. _`ata_eh_worth_retry`:

ata_eh_worth_retry
==================

.. c:function:: int ata_eh_worth_retry(struct ata_queued_cmd *qc)

    analyze error and decide whether to retry

    :param struct ata_queued_cmd \*qc:
        qc to possibly retry

.. _`ata_eh_worth_retry.description`:

Description
-----------

     Look at the cause of the error and decide if a retry
     might be useful or not.  We don't want to retry media errors
     because the drive itself has probably already taken 10-30 seconds
     doing its own internal retries before reporting the failure.

.. _`ata_eh_link_autopsy`:

ata_eh_link_autopsy
===================

.. c:function:: void ata_eh_link_autopsy(struct ata_link *link)

    analyze error and determine recovery action

    :param struct ata_link \*link:
        host link to perform autopsy on

.. _`ata_eh_link_autopsy.description`:

Description
-----------

     Analyze why \ ``link``\  failed and determine which recovery actions
     are needed.  This function also sets more detailed AC_ERR_*
     values and fills sense data for ATAPI CHECK SENSE.

.. _`ata_eh_link_autopsy.locking`:

LOCKING
-------

     Kernel thread context (may sleep).

.. _`ata_eh_autopsy`:

ata_eh_autopsy
==============

.. c:function:: void ata_eh_autopsy(struct ata_port *ap)

    analyze error and determine recovery action

    :param struct ata_port \*ap:
        host port to perform autopsy on

.. _`ata_eh_autopsy.description`:

Description
-----------

     Analyze all links of \ ``ap``\  and determine why they failed and
     which recovery actions are needed.

.. _`ata_eh_autopsy.locking`:

LOCKING
-------

     Kernel thread context (may sleep).

.. _`ata_get_cmd_descript`:

ata_get_cmd_descript
====================

.. c:function:: const char *ata_get_cmd_descript(u8 command)

    get description for ATA command

    :param u8 command:
        ATA command code to get description for

.. _`ata_get_cmd_descript.description`:

Description
-----------

     Return a textual description of the given command, or NULL if the
     command is not known.

.. _`ata_get_cmd_descript.locking`:

LOCKING
-------

     None

.. _`ata_eh_link_report`:

ata_eh_link_report
==================

.. c:function:: void ata_eh_link_report(struct ata_link *link)

    report error handling to user

    :param struct ata_link \*link:
        ATA link EH is going on

.. _`ata_eh_link_report.description`:

Description
-----------

     Report EH to user.

.. _`ata_eh_link_report.locking`:

LOCKING
-------

     None.

.. _`ata_eh_report`:

ata_eh_report
=============

.. c:function:: void ata_eh_report(struct ata_port *ap)

    report error handling to user

    :param struct ata_port \*ap:
        ATA port to report EH about

.. _`ata_eh_report.description`:

Description
-----------

     Report EH to user.

.. _`ata_eh_report.locking`:

LOCKING
-------

     None.

.. _`ata_set_mode`:

ata_set_mode
============

.. c:function:: int ata_set_mode(struct ata_link *link, struct ata_device **r_failed_dev)

    Program timings and issue SET FEATURES - XFER

    :param struct ata_link \*link:
        link on which timings will be programmed

    :param struct ata_device \*\*r_failed_dev:
        out parameter for failed device

.. _`ata_set_mode.description`:

Description
-----------

     Set ATA device disk transfer mode (PIO3, UDMA6, etc.).  If
     \ :c:func:`ata_set_mode`\  fails, pointer to the failing device is
     returned in \ ``r_failed_dev``\ .

.. _`ata_set_mode.locking`:

LOCKING
-------

     PCI/etc. bus probe sem.

.. _`ata_set_mode.return`:

Return
------

     0 on success, negative errno otherwise

.. _`atapi_eh_clear_ua`:

atapi_eh_clear_ua
=================

.. c:function:: int atapi_eh_clear_ua(struct ata_device *dev)

    Clear ATAPI UNIT ATTENTION after reset

    :param struct ata_device \*dev:
        ATAPI device to clear UA for

.. _`atapi_eh_clear_ua.description`:

Description
-----------

     Resets and other operations can make an ATAPI device raise
     UNIT ATTENTION which causes the next operation to fail.  This
     function clears UA.

.. _`atapi_eh_clear_ua.locking`:

LOCKING
-------

     EH context (may sleep).

.. _`atapi_eh_clear_ua.return`:

Return
------

     0 on success, -errno on failure.

.. _`ata_eh_maybe_retry_flush`:

ata_eh_maybe_retry_flush
========================

.. c:function:: int ata_eh_maybe_retry_flush(struct ata_device *dev)

    Retry FLUSH if necessary

    :param struct ata_device \*dev:
        ATA device which may need FLUSH retry

.. _`ata_eh_maybe_retry_flush.description`:

Description
-----------

     If \ ``dev``\  failed FLUSH, it needs to be reported upper layer
     immediately as it means that \ ``dev``\  failed to remap and already
     lost at least a sector and further FLUSH retrials won't make
     any difference to the lost sector.  However, if FLUSH failed
     for other reasons, for example transmission error, FLUSH needs
     to be retried.

     This function determines whether FLUSH failure retry is
     necessary and performs it if so.

.. _`ata_eh_maybe_retry_flush.return`:

Return
------

     0 if EH can continue, -errno if EH needs to be repeated.

.. _`ata_eh_set_lpm`:

ata_eh_set_lpm
==============

.. c:function:: int ata_eh_set_lpm(struct ata_link *link, enum ata_lpm_policy policy, struct ata_device **r_failed_dev)

    configure SATA interface power management

    :param struct ata_link \*link:
        link to configure power management

    :param enum ata_lpm_policy policy:
        the link power management policy

    :param struct ata_device \*\*r_failed_dev:
        out parameter for failed device

.. _`ata_eh_set_lpm.description`:

Description
-----------

     Enable SATA Interface power management.  This will enable
     Device Interface Power Management (DIPM) for min_power
     policy, and then call driver specific callbacks for
     enabling Host Initiated Power management.

.. _`ata_eh_set_lpm.locking`:

LOCKING
-------

     EH context.

.. _`ata_eh_set_lpm.return`:

Return
------

     0 on success, -errno on failure.

.. _`ata_eh_recover`:

ata_eh_recover
==============

.. c:function:: int ata_eh_recover(struct ata_port *ap, ata_prereset_fn_t prereset, ata_reset_fn_t softreset, ata_reset_fn_t hardreset, ata_postreset_fn_t postreset, struct ata_link **r_failed_link)

    recover host port after error

    :param struct ata_port \*ap:
        host port to recover

    :param ata_prereset_fn_t prereset:
        prereset method (can be NULL)

    :param ata_reset_fn_t softreset:
        softreset method (can be NULL)

    :param ata_reset_fn_t hardreset:
        hardreset method (can be NULL)

    :param ata_postreset_fn_t postreset:
        postreset method (can be NULL)

    :param struct ata_link \*\*r_failed_link:
        out parameter for failed link

.. _`ata_eh_recover.description`:

Description
-----------

     This is the alpha and omega, eum and yang, heart and soul of
     libata exception handling.  On entry, actions required to
     recover each link and hotplug requests are recorded in the
     link's eh_context.  This function executes all the operations
     with appropriate retrials and fallbacks to resurrect failed
     devices, detach goners and greet newcomers.

.. _`ata_eh_recover.locking`:

LOCKING
-------

     Kernel thread context (may sleep).

.. _`ata_eh_recover.return`:

Return
------

     0 on success, -errno on failure.

.. _`ata_eh_finish`:

ata_eh_finish
=============

.. c:function:: void ata_eh_finish(struct ata_port *ap)

    finish up EH

    :param struct ata_port \*ap:
        host port to finish EH for

.. _`ata_eh_finish.description`:

Description
-----------

     Recovery is complete.  Clean up EH states and retry or finish
     failed qcs.

.. _`ata_eh_finish.locking`:

LOCKING
-------

     None.

.. _`ata_do_eh`:

ata_do_eh
=========

.. c:function:: void ata_do_eh(struct ata_port *ap, ata_prereset_fn_t prereset, ata_reset_fn_t softreset, ata_reset_fn_t hardreset, ata_postreset_fn_t postreset)

    do standard error handling

    :param struct ata_port \*ap:
        host port to handle error for

    :param ata_prereset_fn_t prereset:
        prereset method (can be NULL)

    :param ata_reset_fn_t softreset:
        softreset method (can be NULL)

    :param ata_reset_fn_t hardreset:
        hardreset method (can be NULL)

    :param ata_postreset_fn_t postreset:
        postreset method (can be NULL)

.. _`ata_do_eh.description`:

Description
-----------

     Perform standard error handling sequence.

.. _`ata_do_eh.locking`:

LOCKING
-------

     Kernel thread context (may sleep).

.. _`ata_std_error_handler`:

ata_std_error_handler
=====================

.. c:function:: void ata_std_error_handler(struct ata_port *ap)

    standard error handler

    :param struct ata_port \*ap:
        host port to handle error for

.. _`ata_std_error_handler.description`:

Description
-----------

     Standard error handler

.. _`ata_std_error_handler.locking`:

LOCKING
-------

     Kernel thread context (may sleep).

.. _`ata_eh_handle_port_suspend`:

ata_eh_handle_port_suspend
==========================

.. c:function:: void ata_eh_handle_port_suspend(struct ata_port *ap)

    perform port suspend operation

    :param struct ata_port \*ap:
        port to suspend

.. _`ata_eh_handle_port_suspend.description`:

Description
-----------

     Suspend \ ``ap``\ .

.. _`ata_eh_handle_port_suspend.locking`:

LOCKING
-------

     Kernel thread context (may sleep).

.. _`ata_eh_handle_port_resume`:

ata_eh_handle_port_resume
=========================

.. c:function:: void ata_eh_handle_port_resume(struct ata_port *ap)

    perform port resume operation

    :param struct ata_port \*ap:
        port to resume

.. _`ata_eh_handle_port_resume.description`:

Description
-----------

     Resume \ ``ap``\ .

.. _`ata_eh_handle_port_resume.locking`:

LOCKING
-------

     Kernel thread context (may sleep).

.. This file was automatic generated / don't edit.

