.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/mpt3sas/mpt3sas_warpdrive.c

.. _`_warpdrive_disable_ddio`:

\_warpdrive_disable_ddio
========================

.. c:function:: void _warpdrive_disable_ddio(struct MPT3SAS_ADAPTER *ioc)

    Disable direct I/O for all the volumes

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`mpt3sas_get_num_volumes`:

mpt3sas_get_num_volumes
=======================

.. c:function:: u8 mpt3sas_get_num_volumes(struct MPT3SAS_ADAPTER *ioc)

    Get number of volumes in the ioc

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`mpt3sas_init_warpdrive_properties`:

mpt3sas_init_warpdrive_properties
=================================

.. c:function:: void mpt3sas_init_warpdrive_properties(struct MPT3SAS_ADAPTER *ioc, struct _raid_device *raid_device)

    Set properties for warpdrive direct I/O.

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param raid_device:
        the raid_device object
    :type raid_device: struct _raid_device \*

.. _`mpt3sas_setup_direct_io`:

mpt3sas_setup_direct_io
=======================

.. c:function:: void mpt3sas_setup_direct_io(struct MPT3SAS_ADAPTER *ioc, struct scsi_cmnd *scmd, struct _raid_device *raid_device, Mpi25SCSIIORequest_t *mpi_request)

    setup MPI request for WARPDRIVE Direct I/O

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param scmd:
        pointer to scsi command object
    :type scmd: struct scsi_cmnd \*

    :param raid_device:
        pointer to raid device data structure
    :type raid_device: struct _raid_device \*

    :param mpi_request:
        pointer to the SCSI_IO reqest message frame
    :type mpi_request: Mpi25SCSIIORequest_t \*

.. This file was automatic generated / don't edit.

