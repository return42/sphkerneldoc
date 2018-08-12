.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/scsi/zfcp_scsi.c

.. _`zfcp_scsi_task_mgmt_function`:

zfcp_scsi_task_mgmt_function
============================

.. c:function:: int zfcp_scsi_task_mgmt_function(struct scsi_device *sdev, u8 tm_flags)

    Send a task management function (sync).

    :param struct scsi_device \*sdev:
        Pointer to SCSI device to send the task management command to.

    :param u8 tm_flags:
        Task management flags,
        here we only handle \ ``FCP_TMF_TGT_RESET``\  or \ ``FCP_TMF_LUN_RESET``\ .

.. _`zfcp_scsi_sysfs_host_reset`:

zfcp_scsi_sysfs_host_reset
==========================

.. c:function:: int zfcp_scsi_sysfs_host_reset(struct Scsi_Host *shost, int reset_type)

    Support scsi_host sysfs attribute host_reset.

    :param struct Scsi_Host \*shost:
        Pointer to Scsi_Host to perform action on.

    :param int reset_type:
        We support \ ``SCSI_ADAPTER_RESET``\  but not \ ``SCSI_FIRMWARE_RESET``\ .

.. _`zfcp_scsi_sysfs_host_reset.return`:

Return
------

0 on \ ``SCSI_ADAPTER_RESET``\ , -%EOPNOTSUPP otherwise.

This is similar to \ :c:func:`zfcp_sysfs_adapter_failed_store`\ .

.. _`zfcp_scsi_adapter_register`:

zfcp_scsi_adapter_register
==========================

.. c:function:: int zfcp_scsi_adapter_register(struct zfcp_adapter *adapter)

    Register SCSI and FC host with SCSI midlayer

    :param struct zfcp_adapter \*adapter:
        The zfcp adapter to register with the SCSI midlayer

.. _`zfcp_scsi_adapter_unregister`:

zfcp_scsi_adapter_unregister
============================

.. c:function:: void zfcp_scsi_adapter_unregister(struct zfcp_adapter *adapter)

    Unregister SCSI and FC host from SCSI midlayer

    :param struct zfcp_adapter \*adapter:
        The zfcp adapter to unregister.

.. _`zfcp_scsi_terminate_rport_io`:

zfcp_scsi_terminate_rport_io
============================

.. c:function:: void zfcp_scsi_terminate_rport_io(struct fc_rport *rport)

    Terminate all I/O on a rport

    :param struct fc_rport \*rport:
        The FC rport where to teminate I/O

.. _`zfcp_scsi_terminate_rport_io.description`:

Description
-----------

Abort all pending SCSI commands for a port by closing the
port. Using a reopen avoids a conflict with a shutdown
overwriting a reopen. The "forced" ensures that a disappeared port
is not opened again as valid due to the cached plogi data in
non-NPIV mode.

.. _`zfcp_scsi_set_prot`:

zfcp_scsi_set_prot
==================

.. c:function:: void zfcp_scsi_set_prot(struct zfcp_adapter *adapter)

    Configure DIF/DIX support in scsi_host

    :param struct zfcp_adapter \*adapter:
        The adapter where to configure DIF/DIX for the SCSI host

.. _`zfcp_scsi_dif_sense_error`:

zfcp_scsi_dif_sense_error
=========================

.. c:function:: void zfcp_scsi_dif_sense_error(struct scsi_cmnd *scmd, int ascq)

    Report DIF/DIX error as driver sense error

    :param struct scsi_cmnd \*scmd:
        The SCSI command to report the error for

    :param int ascq:
        The ASCQ to put in the sense buffer

.. _`zfcp_scsi_dif_sense_error.description`:

Description
-----------

See the error handling in sd_done for the sense codes used here.
Set DID_SOFT_ERROR to retry the request, if possible.

.. This file was automatic generated / don't edit.

