.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/bnx2fc/bnx2fc_io.c

.. _`bnx2fc_eh_target_reset`:

bnx2fc_eh_target_reset
======================

.. c:function:: int bnx2fc_eh_target_reset(struct scsi_cmnd *sc_cmd)

    Reset a target

    :param struct scsi_cmnd \*sc_cmd:
        SCSI command

.. _`bnx2fc_eh_target_reset.description`:

Description
-----------

Set from SCSI host template to send task mgmt command to the target
and wait for the response

.. _`bnx2fc_eh_device_reset`:

bnx2fc_eh_device_reset
======================

.. c:function:: int bnx2fc_eh_device_reset(struct scsi_cmnd *sc_cmd)

    Reset a single LUN

    :param struct scsi_cmnd \*sc_cmd:
        SCSI command

.. _`bnx2fc_eh_device_reset.description`:

Description
-----------

Set from SCSI host template to send task mgmt command to the target
and wait for the response

.. _`bnx2fc_eh_abort`:

bnx2fc_eh_abort
===============

.. c:function:: int bnx2fc_eh_abort(struct scsi_cmnd *sc_cmd)

    eh_abort_handler api to abort an outstanding SCSI command

    :param struct scsi_cmnd \*sc_cmd:
        SCSI_ML command pointer

.. _`bnx2fc_eh_abort.description`:

Description
-----------

SCSI abort request handler

.. _`bnx2fc_queuecommand`:

bnx2fc_queuecommand
===================

.. c:function:: int bnx2fc_queuecommand(struct Scsi_Host *host, struct scsi_cmnd *sc_cmd)

    Queuecommand function of the scsi template

    :param struct Scsi_Host \*host:
        The Scsi_Host the command was issued to

    :param struct scsi_cmnd \*sc_cmd:
        struct scsi_cmnd to be executed

.. _`bnx2fc_queuecommand.description`:

Description
-----------

This is the IO strategy routine, called by SCSI-ML

.. This file was automatic generated / don't edit.

