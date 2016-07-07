.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/mpt3sas/mpt3sas_warpdrive.c

.. _`_warpdrive_disable_ddio`:

_warpdrive_disable_ddio
=======================

.. c:function:: void _warpdrive_disable_ddio(struct MPT3SAS_ADAPTER *ioc)

    Disable direct I/O for all the volumes

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`mpt3sas_get_num_volumes`:

mpt3sas_get_num_volumes
=======================

.. c:function:: u8 mpt3sas_get_num_volumes(struct MPT3SAS_ADAPTER *ioc)

    Get number of volumes in the ioc

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`mpt3sas_init_warpdrive_properties`:

mpt3sas_init_warpdrive_properties
=================================

.. c:function:: void mpt3sas_init_warpdrive_properties(struct MPT3SAS_ADAPTER *ioc, struct _raid_device *raid_device)

    Set properties for warpdrive direct I/O.

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct _raid_device \*raid_device:
        the raid_device object

.. _`mpt3sas_scsi_direct_io_get`:

mpt3sas_scsi_direct_io_get
==========================

.. c:function:: u8 mpt3sas_scsi_direct_io_get(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    returns direct io flag

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

.. _`mpt3sas_scsi_direct_io_get.description`:

Description
-----------

Returns the smid stored scmd pointer.

.. _`mpt3sas_scsi_direct_io_set`:

mpt3sas_scsi_direct_io_set
==========================

.. c:function:: void mpt3sas_scsi_direct_io_set(struct MPT3SAS_ADAPTER *ioc, u16 smid, u8 direct_io)

    sets direct io flag

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param u8 direct_io:
        Zero or non-zero value to set in the direct_io flag

.. _`mpt3sas_scsi_direct_io_set.description`:

Description
-----------

Returns Nothing.

.. _`mpt3sas_setup_direct_io`:

mpt3sas_setup_direct_io
=======================

.. c:function:: void mpt3sas_setup_direct_io(struct MPT3SAS_ADAPTER *ioc, struct scsi_cmnd *scmd, struct _raid_device *raid_device, Mpi2SCSIIORequest_t *mpi_request, u16 smid)

    setup MPI request for WARPDRIVE Direct I/O

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct scsi_cmnd \*scmd:
        pointer to scsi command object

    :param struct _raid_device \*raid_device:
        pointer to raid device data structure

    :param Mpi2SCSIIORequest_t \*mpi_request:
        pointer to the SCSI_IO reqest message frame

    :param u16 smid:
        system request message index

.. _`mpt3sas_setup_direct_io.description`:

Description
-----------

Returns nothing

.. This file was automatic generated / don't edit.

