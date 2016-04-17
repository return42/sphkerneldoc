.. -*- coding: utf-8; mode: rst -*-

==========
mptscsih.c
==========


.. _`mptscsih_info_scsiio`:

mptscsih_info_scsiio
====================

.. c:function:: void mptscsih_info_scsiio (MPT_ADAPTER *ioc, struct scsi_cmnd *sc, SCSIIOReply_t *pScsiReply)

    debug print info on reply frame

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param struct scsi_cmnd \*sc:
        original scsi cmnd pointer

    :param SCSIIOReply_t \*pScsiReply:
        Pointer to MPT reply frame



.. _`mptscsih_info_scsiio.description`:

Description
-----------

MPT_DEBUG_REPLY needs to be enabled to obtain this info

Refer to lsi/mpi.h.



.. _`mptscsih_info`:

mptscsih_info
=============

.. c:function:: const char *mptscsih_info (struct Scsi_Host *SChost)

    Return information about MPT adapter

    :param struct Scsi_Host \*SChost:
        Pointer to Scsi_Host structure



.. _`mptscsih_info.description`:

Description
-----------

(linux scsi_host_template.info routine)

Returns pointer to buffer where information was written.



.. _`mptscsih_qcmd`:

mptscsih_qcmd
=============

.. c:function:: int mptscsih_qcmd (struct scsi_cmnd *SCpnt)

    Primary Fusion MPT SCSI initiator IO start routine.

    :param struct scsi_cmnd \*SCpnt:
        Pointer to scsi_cmnd structure



.. _`mptscsih_qcmd.description`:

Description
-----------

(linux scsi_host_template.queuecommand routine)
This is the primary SCSI IO start routine.  Create a MPI SCSIIORequest
from a linux scsi_cmnd request and send it to the IOC.

Returns 0. (rtn value discarded by linux scsi mid-layer)



.. _`mptscsih_issuetaskmgmt`:

mptscsih_IssueTaskMgmt
======================

.. c:function:: int mptscsih_IssueTaskMgmt (MPT_SCSI_HOST *hd, u8 type, u8 channel, u8 id, u64 lun, int ctx2abort, ulong timeout)

    Generic send Task Management function.

    :param MPT_SCSI_HOST \*hd:
        Pointer to MPT_SCSI_HOST structure

    :param u8 type:
        Task Management type

    :param u8 channel:
        channel number for task management

    :param u8 id:
        Logical Target ID for reset (if appropriate)

    :param u64 lun:
        Logical Unit for reset (if appropriate)

    :param int ctx2abort:
        Context for the task to be aborted (if appropriate)

    :param ulong timeout:
        timeout for task management control



.. _`mptscsih_issuetaskmgmt.remark`:

Remark
------

_HardResetHandler can be invoked from an interrupt thread (timer)
or a non-interrupt thread.  In the former, must not call :c:func:`schedule`.

Not all fields are meaningfull for all task types.

Returns 0 for SUCCESS, or FAILED.



.. _`mptscsih_abort`:

mptscsih_abort
==============

.. c:function:: int mptscsih_abort (struct scsi_cmnd *SCpnt)

    Abort linux scsi_cmnd routine, new_eh variant

    :param struct scsi_cmnd \*SCpnt:
        Pointer to scsi_cmnd structure, IO to be aborted



.. _`mptscsih_abort.description`:

Description
-----------

(linux scsi_host_template.eh_abort_handler routine)

Returns SUCCESS or FAILED.



.. _`mptscsih_dev_reset`:

mptscsih_dev_reset
==================

.. c:function:: int mptscsih_dev_reset (struct scsi_cmnd *SCpnt)

    Perform a SCSI TARGET_RESET! new_eh variant

    :param struct scsi_cmnd \*SCpnt:
        Pointer to scsi_cmnd structure, IO which reset is due to



.. _`mptscsih_dev_reset.description`:

Description
-----------

(linux scsi_host_template.eh_dev_reset_handler routine)

Returns SUCCESS or FAILED.



.. _`mptscsih_bus_reset`:

mptscsih_bus_reset
==================

.. c:function:: int mptscsih_bus_reset (struct scsi_cmnd *SCpnt)

    Perform a SCSI BUS_RESET! new_eh variant

    :param struct scsi_cmnd \*SCpnt:
        Pointer to scsi_cmnd structure, IO which reset is due to



.. _`mptscsih_bus_reset.description`:

Description
-----------

(linux scsi_host_template.eh_bus_reset_handler routine)

Returns SUCCESS or FAILED.



.. _`mptscsih_host_reset`:

mptscsih_host_reset
===================

.. c:function:: int mptscsih_host_reset (struct scsi_cmnd *SCpnt)

    Perform a SCSI host adapter RESET (new_eh variant)

    :param struct scsi_cmnd \*SCpnt:
        Pointer to scsi_cmnd structure, IO which reset is due to



.. _`mptscsih_host_reset.description`:

Description
-----------

(linux scsi_host_template.eh_host_reset_handler routine)

Returns SUCCESS or FAILED.



.. _`mptscsih_taskmgmt_complete`:

mptscsih_taskmgmt_complete
==========================

.. c:function:: int mptscsih_taskmgmt_complete (MPT_ADAPTER *ioc, MPT_FRAME_HDR *mf, MPT_FRAME_HDR *mr)

    Registered with Fusion MPT base driver

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param MPT_FRAME_HDR \*mf:
        Pointer to SCSI task mgmt request frame

    :param MPT_FRAME_HDR \*mr:
        Pointer to SCSI task mgmt reply frame



.. _`mptscsih_taskmgmt_complete.description`:

Description
-----------

This routine is called from mptbase.c:::c:func:`mpt_interrupt` at the completion
of any SCSI task management request.
This routine is registered with the MPT (base) driver at driver
load/init time via the :c:func:`mpt_register` API call.

Returns 1 indicating alloc'd request frame ptr should be freed.



.. _`mptscsih_get_scsi_lookup`:

mptscsih_get_scsi_lookup
========================

.. c:function:: struct scsi_cmnd *mptscsih_get_scsi_lookup (MPT_ADAPTER *ioc, int i)

    retrieves scmd entry

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int i:
        index into the array



.. _`mptscsih_get_scsi_lookup.description`:

Description
-----------

Returns the scsi_cmd pointer



.. _`mptscsih_getclear_scsi_lookup`:

mptscsih_getclear_scsi_lookup
=============================

.. c:function:: struct scsi_cmnd *mptscsih_getclear_scsi_lookup (MPT_ADAPTER *ioc, int i)

    retrieves and clears scmd entry from ScsiLookup[] array list

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int i:
        index into the array



.. _`mptscsih_getclear_scsi_lookup.description`:

Description
-----------

Returns the scsi_cmd pointer



.. _`mptscsih_set_scsi_lookup`:

mptscsih_set_scsi_lookup
========================

.. c:function:: void mptscsih_set_scsi_lookup (MPT_ADAPTER *ioc, int i, struct scsi_cmnd *scmd)

    write a scmd entry into the ScsiLookup[] array list

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int i:
        index into the array

    :param struct scsi_cmnd \*scmd:
        scsi_cmnd pointer



.. _`scpnt_to_lookup_idx`:

SCPNT_TO_LOOKUP_IDX
===================

.. c:function:: int SCPNT_TO_LOOKUP_IDX (MPT_ADAPTER *ioc, struct scsi_cmnd *sc)

    searches for a given scmd in the ScsiLookup[] array list

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param struct scsi_cmnd \*sc:
        scsi_cmnd pointer



.. _`mptscsih_get_completion_code`:

mptscsih_get_completion_code
============================

.. c:function:: int mptscsih_get_completion_code (MPT_ADAPTER *ioc, MPT_FRAME_HDR *req, MPT_FRAME_HDR *reply)

    get completion code from MPT request

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param MPT_FRAME_HDR \*req:
        Pointer to original MPT request frame

    :param MPT_FRAME_HDR \*reply:
        Pointer to MPT reply frame (NULL if TurboReply)



.. _`mptscsih_do_cmd`:

mptscsih_do_cmd
===============

.. c:function:: int mptscsih_do_cmd (MPT_SCSI_HOST *hd, INTERNAL_CMD *io)

    Do internal command.

    :param MPT_SCSI_HOST \*hd:
        MPT_SCSI_HOST pointer

    :param INTERNAL_CMD \*io:
        INTERNAL_CMD pointer.



.. _`mptscsih_do_cmd.description`:

Description
-----------

Issue the specified internally generated command and do command
specific cleanup. For bus scan / DV only.



.. _`mptscsih_do_cmd.notes`:

NOTES
-----

If command is Inquiry and status is good,
initialize a target structure, save the data



.. _`mptscsih_do_cmd.remark`:

Remark
------

Single threaded access only.



.. _`mptscsih_do_cmd.return`:

Return
------

< 0 if an illegal command or no resources

   0 if good

 > 0 if command complete but some type of completion error.



.. _`mptscsih_synchronize_cache`:

mptscsih_synchronize_cache
==========================

.. c:function:: void mptscsih_synchronize_cache (MPT_SCSI_HOST *hd, VirtDevice *vdevice)

    Send SYNCHRONIZE_CACHE to all disks.

    :param MPT_SCSI_HOST \*hd:
        Pointer to a SCSI HOST structure

    :param VirtDevice \*vdevice:
        virtual target device



.. _`mptscsih_synchronize_cache.description`:

Description
-----------

Uses the ISR, but with special processing.
MUST be single-threaded.

