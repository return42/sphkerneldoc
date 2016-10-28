.. -*- coding: utf-8; mode: rst -*-

.. _libataEH:

**************
Error handling
**************

This chapter describes how errors are handled under libata. Readers are
advised to read SCSI EH (Documentation/scsi/scsi_eh.txt) and ATA
exceptions doc first.


Origins of commands
===================

In libata, a command is represented with struct ata_queued_cmd or qc.
qc's are preallocated during port initialization and repetitively used
for command executions. Currently only one qc is allocated per port but
yet-to-be-merged NCQ branch allocates one for each tag and maps each qc
to NCQ tag 1-to-1.

libata commands can originate from two sources - libata itself and SCSI
midlayer. libata internal commands are used for initialization and error
handling. All normal blk requests and commands for SCSI emulation are
passed as SCSI commands through queuecommand callback of SCSI host
template.


How commands are issued
=======================

Internal commands
    First, qc is allocated and initialized using ata_qc_new_init().
    Although ata_qc_new_init() doesn't implement any wait or retry
    mechanism when qc is not available, internal commands are currently
    issued only during initialization and error recovery, so no other
    command is active and allocation is guaranteed to succeed.

    Once allocated qc's taskfile is initialized for the command to be
    executed. qc currently has two mechanisms to notify completion. One
    is via qc->complete_fn() callback and the other is completion
    qc->waiting. qc->complete_fn() callback is the asynchronous path
    used by normal SCSI translated commands and qc->waiting is the
    synchronous (issuer sleeps in process context) path used by internal
    commands.

    Once initialization is complete, host_set lock is acquired and the
    qc is issued.

SCSI commands
    All libata drivers use ata_scsi_queuecmd() as hostt->queuecommand
    callback. scmds can either be simulated or translated. No qc is
    involved in processing a simulated scmd. The result is computed
    right away and the scmd is completed.

    For a translated scmd, ata_qc_new_init() is invoked to allocate a
    qc and the scmd is translated into the qc. SCSI midlayer's
    completion notification function pointer is stored into
    qc->scsidone.

    qc->complete_fn() callback is used for completion notification. ATA
    commands use ata_scsi_qc_complete() while ATAPI commands use
    atapi_qc_complete(). Both functions end up calling qc->scsidone to
    notify upper layer when the qc is finished. After translation is
    completed, the qc is issued with ata_qc_issue().

    Note that SCSI midlayer invokes hostt->queuecommand while holding
    host_set lock, so all above occur while holding host_set lock.


How commands are processed
==========================

Depending on which protocol and which controller are used, commands are
processed differently. For the purpose of discussion, a controller which
uses taskfile interface and all standard callbacks is assumed.

Currently 6 ATA command protocols are used. They can be sorted into the
following four categories according to how they are processed.

ATA NO DATA or DMA
    ATA_PROT_NODATA and ATA_PROT_DMA fall into this category. These
    types of commands don't require any software intervention once
    issued. Device will raise interrupt on completion.

ATA PIO
    ATA_PROT_PIO is in this category. libata currently implements PIO
    with polling. ATA_NIEN bit is set to turn off interrupt and
    pio_task on ata_wq performs polling and IO.

ATAPI NODATA or DMA
    ATA_PROT_ATAPI_NODATA and ATA_PROT_ATAPI_DMA are in this
    category. packet_task is used to poll BSY bit after issuing PACKET
    command. Once BSY is turned off by the device, packet_task
    transfers CDB and hands off processing to interrupt handler.

ATAPI PIO
    ATA_PROT_ATAPI is in this category. ATA_NIEN bit is set and, as
    in ATAPI NODATA or DMA, packet_task submits cdb. However, after
    submitting cdb, further processing (data transfer) is handed off to
    pio_task.


How commands are completed
==========================

Once issued, all qc's are either completed with ata_qc_complete() or
time out. For commands which are handled by interrupts,
ata_host_intr() invokes ata_qc_complete(), and, for PIO tasks,
pio_task invokes ata_qc_complete(). In error cases, packet_task may
also complete commands.

ata_qc_complete() does the following.

1. DMA memory is unmapped.

2. ATA_QCFLAG_ACTIVE is cleared from qc->flags.

3. qc->complete_fn() callback is invoked. If the return value of the
   callback is not zero. Completion is short circuited and
   ata_qc_complete() returns.

4. __ata_qc_complete() is called, which does

   1. qc->flags is cleared to zero.

   2. ap->active_tag and qc->tag are poisoned.

   3. qc->waiting is cleared & completed (in that order).

   4. qc is deallocated by clearing appropriate bit in ap->qactive.

So, it basically notifies upper layer and deallocates qc. One exception
is short-circuit path in #3 which is used by atapi_qc_complete().

For all non-ATAPI commands, whether it fails or not, almost the same
code path is taken and very little error handling takes place. A qc is
completed with success status if it succeeded, with failed status
otherwise.

However, failed ATAPI commands require more handling as REQUEST SENSE is
needed to acquire sense data. If an ATAPI command fails,
ata_qc_complete() is invoked with error status, which in turn invokes
atapi_qc_complete() via qc->complete_fn() callback.

This makes atapi_qc_complete() set scmd->result to
SAM_STAT_CHECK_CONDITION, complete the scmd and return 1. As the
sense data is empty but scmd->result is CHECK CONDITION, SCSI midlayer
will invoke EH for the scmd, and returning 1 makes ata_qc_complete()
to return without deallocating the qc. This leads us to
ata_scsi_error() with partially completed qc.


ata_scsi_error()
================

ata_scsi_error() is the current transportt->eh_strategy_handler()
for libata. As discussed above, this will be entered in two cases -
timeout and ATAPI error completion. This function calls low level libata
driver's eng_timeout() callback, the standard callback for which is
ata_eng_timeout(). It checks if a qc is active and calls
ata_qc_timeout() on the qc if so. Actual error handling occurs in
ata_qc_timeout().

If EH is invoked for timeout, ata_qc_timeout() stops BMDMA and
completes the qc. Note that as we're currently in EH, we cannot call
scsi_done. As described in SCSI EH doc, a recovered scmd should be
either retried with scsi_queue_insert() or finished with
scsi_finish_command(). Here, we override qc->scsidone with
scsi_finish_command() and calls ata_qc_complete().

If EH is invoked due to a failed ATAPI qc, the qc here is completed but
not deallocated. The purpose of this half-completion is to use the qc as
place holder to make EH code reach this place. This is a bit hackish,
but it works.

Once control reaches here, the qc is deallocated by invoking
__ata_qc_complete() explicitly. Then, internal qc for REQUEST SENSE
is issued. Once sense data is acquired, scmd is finished by directly
invoking scsi_finish_command() on the scmd. Note that as we already
have completed and deallocated the qc which was associated with the
scmd, we don't need to/cannot call ata_qc_complete() again.


Problems with the current EH
============================

-  Error representation is too crude. Currently any and all error
   conditions are represented with ATA STATUS and ERROR registers.
   Errors which aren't ATA device errors are treated as ATA device
   errors by setting ATA_ERR bit. Better error descriptor which can
   properly represent ATA and other errors/exceptions is needed.

-  When handling timeouts, no action is taken to make device forget
   about the timed out command and ready for new commands.

-  EH handling via ata_scsi_error() is not properly protected from
   usual command processing. On EH entrance, the device is not in
   quiescent state. Timed out commands may succeed or fail any time.
   pio_task and atapi_task may still be running.

-  Too weak error recovery. Devices / controllers causing HSM mismatch
   errors and other errors quite often require reset to return to known
   state. Also, advanced error handling is necessary to support features
   like NCQ and hotplug.

-  ATA errors are directly handled in the interrupt handler and PIO
   errors in pio_task. This is problematic for advanced error handling
   for the following reasons.

   First, advanced error handling often requires context and internal qc
   execution.

   Second, even a simple failure (say, CRC error) needs information
   gathering and could trigger complex error handling (say, resetting &
   reconfiguring). Having multiple code paths to gather information,
   enter EH and trigger actions makes life painful.

   Third, scattered EH code makes implementing low level drivers
   difficult. Low level drivers override libata callbacks. If EH is
   scattered over several places, each affected callbacks should perform
   its part of error handling. This can be error prone and painful.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
