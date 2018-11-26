.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/message/fusion/mptspi.c

.. _`mptspi_settargetnegoparms`:

mptspi_setTargetNegoParms
=========================

.. c:function:: void mptspi_setTargetNegoParms(MPT_SCSI_HOST *hd, VirtTarget *target, struct scsi_device *sdev)

    Update the target negotiation parameters

    :param hd:
        Pointer to a SCSI Host Structure
    :type hd: MPT_SCSI_HOST \*

    :param target:
        per target private data
    :type target: VirtTarget \*

    :param sdev:
        SCSI device
    :type sdev: struct scsi_device \*

.. _`mptspi_settargetnegoparms.description`:

Description
-----------

Update the target negotiation parameters based on the the Inquiry
data, adapter capabilities, and NVRAM settings.

.. _`mptspi_writeiocpage4`:

mptspi_writeIOCPage4
====================

.. c:function:: int mptspi_writeIOCPage4(MPT_SCSI_HOST *hd, u8 channel, u8 id)

    write IOC Page 4

    :param hd:
        Pointer to a SCSI Host Structure
    :type hd: MPT_SCSI_HOST \*

    :param channel:
        channel number
    :type channel: u8

    :param id:
        write IOC Page4 for this ID & Bus
    :type id: u8

.. _`mptspi_writeiocpage4.return`:

Return
------

-EAGAIN if unable to obtain a Message Frame
or 0 if success.

.. _`mptspi_writeiocpage4.remark`:

Remark
------

We do not wait for a return, write pages sequentially.

.. _`mptspi_inittarget`:

mptspi_initTarget
=================

.. c:function:: void mptspi_initTarget(MPT_SCSI_HOST *hd, VirtTarget *vtarget, struct scsi_device *sdev)

    Target, LUN alloc/free functionality.

    :param hd:
        Pointer to MPT_SCSI_HOST structure
    :type hd: MPT_SCSI_HOST \*

    :param vtarget:
        per target private data
    :type vtarget: VirtTarget \*

    :param sdev:
        SCSI device
    :type sdev: struct scsi_device \*

.. _`mptspi_inittarget.note`:

NOTE
----

It's only SAFE to call this routine if data points to
sane & valid STANDARD INQUIRY data!

Allocate and initialize memory for this target.
Save inquiry data.

.. _`mptspi_is_raid`:

mptspi_is_raid
==============

.. c:function:: int mptspi_is_raid(struct _MPT_SCSI_HOST *hd, u32 id)

    Determines whether target is belonging to volume

    :param hd:
        Pointer to a SCSI HOST structure
    :type hd: struct _MPT_SCSI_HOST \*

    :param id:
        target device id
    :type id: u32

.. _`mptspi_is_raid.return`:

Return
------

non-zero = true
zero = false

.. _`mptspi_print_write_nego`:

mptspi_print_write_nego
=======================

.. c:function:: void mptspi_print_write_nego(struct _MPT_SCSI_HOST *hd, struct scsi_target *starget, u32 ii)

    negotiation parameters debug info that is being sent

    :param hd:
        Pointer to a SCSI HOST structure
    :type hd: struct _MPT_SCSI_HOST \*

    :param starget:
        SCSI target
    :type starget: struct scsi_target \*

    :param ii:
        negotiation parameters
    :type ii: u32

.. _`mptspi_print_read_nego`:

mptspi_print_read_nego
======================

.. c:function:: void mptspi_print_read_nego(struct _MPT_SCSI_HOST *hd, struct scsi_target *starget, u32 ii)

    negotiation parameters debug info that is being read

    :param hd:
        Pointer to a SCSI HOST structure
    :type hd: struct _MPT_SCSI_HOST \*

    :param starget:
        SCSI target
    :type starget: struct scsi_target \*

    :param ii:
        negotiation parameters
    :type ii: u32

.. _`mptspi_init`:

mptspi_init
===========

.. c:function:: int mptspi_init( void)

    Register MPT adapter(s) as SCSI host(s) with SCSI mid-layer.

    :param void:
        no arguments
    :type void: 

.. _`mptspi_init.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mptspi_exit`:

mptspi_exit
===========

.. c:function:: void __exit mptspi_exit( void)

    Unregisters MPT adapter(s)

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

