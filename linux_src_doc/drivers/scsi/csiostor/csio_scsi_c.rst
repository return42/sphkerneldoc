.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/csiostor/csio_scsi.c

.. _`csio_queuecommand`:

csio_queuecommand
=================

.. c:function:: int csio_queuecommand(struct Scsi_Host *host, struct scsi_cmnd *cmnd)

    Entry point to kickstart an I/O request.

    :param struct Scsi_Host \*host:
        The scsi_host pointer.

    :param struct scsi_cmnd \*cmnd:
        The I/O request from ML.

.. _`csio_queuecommand.this-routine-does-the-following`:

This routine does the following
-------------------------------

- Checks for HW and Rnode module readiness.
- Gets a free ioreq structure (which is already initialized
to uninit during its allocation).
- Maps SG elements.
- Initializes ioreq members.
- Kicks off the SCSI state machine for this IO.
- Returns busy status on error.

.. _`csio_scsim_init`:

csio_scsim_init
===============

.. c:function:: int csio_scsim_init(struct csio_scsim *scm, struct csio_hw *hw)

    Initialize SCSI Module

    :param struct csio_scsim \*scm:
        SCSI Module

    :param struct csio_hw \*hw:
        HW module

.. _`csio_scsim_exit`:

csio_scsim_exit
===============

.. c:function:: void csio_scsim_exit(struct csio_scsim *scm)

    Uninitialize SCSI Module

    :param struct csio_scsim \*scm:
        SCSI Module

.. This file was automatic generated / don't edit.

