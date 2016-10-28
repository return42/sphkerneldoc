.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/scsi/zfcp_scsi.c

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

