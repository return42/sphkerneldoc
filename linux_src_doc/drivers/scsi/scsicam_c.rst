.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/scsicam.c

.. _`scsi_bios_ptable`:

scsi_bios_ptable
================

.. c:function:: unsigned char *scsi_bios_ptable(struct block_device *dev)

    Read PC partition table out of first sector of device.

    :param struct block_device \*dev:
        from this device

.. _`scsi_bios_ptable.description`:

Description
-----------

Reads the first sector from the device and returns \ ``0x42``\  bytes
             starting at offset \ ``0x1be``\ .

.. _`scsi_bios_ptable.return`:

Return
------

partition table in kmalloc(GFP_KERNEL) memory, or NULL on error.

.. _`scsicam_bios_param`:

scsicam_bios_param
==================

.. c:function:: int scsicam_bios_param(struct block_device *bdev, sector_t capacity, int *ip)

    Determine geometry of a disk in cylinders/heads/sectors.

    :param struct block_device \*bdev:
        which device

    :param sector_t capacity:
        size of the disk in sectors

    :param int \*ip:
        return value: ip[0]=heads, ip[1]=sectors, ip[2]=cylinders

.. _`scsicam_bios_param.description`:

Description
-----------

Description : determine the BIOS mapping/geometry used for a drive in a
     SCSI-CAM system, storing the results in ip as required
     by the HDIO_GETGEO \ :c:func:`ioctl`\ .

Returns : -1 on failure, 0 on success.

.. _`scsi_partsize`:

scsi_partsize
=============

.. c:function:: int scsi_partsize(unsigned char *buf, unsigned long capacity, unsigned int *cyls, unsigned int *hds, unsigned int *secs)

    Parse cylinders/heads/sectors from PC partition table

    :param unsigned char \*buf:
        partition table, see \ :c:func:`scsi_bios_ptable`\ 

    :param unsigned long capacity:
        size of the disk in sectors

    :param unsigned int \*cyls:
        put cylinders here

    :param unsigned int \*hds:
        put heads here

    :param unsigned int \*secs:
        put sectors here

.. _`scsi_partsize.description`:

Description
-----------

Determine the BIOS mapping/geometry used to create the partition
table, storing the results in \ ``cyls``\ , \ ``hds``\ , and \ ``secs``\ 

.. _`scsi_partsize.return`:

Return
------

-1 on failure, 0 on success.

.. This file was automatic generated / don't edit.

