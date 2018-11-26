.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/scsicam.c

.. _`scsi_bios_ptable`:

scsi_bios_ptable
================

.. c:function:: unsigned char *scsi_bios_ptable(struct block_device *dev)

    Read PC partition table out of first sector of device.

    :param dev:
        from this device
    :type dev: struct block_device \*

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

    :param bdev:
        which device
    :type bdev: struct block_device \*

    :param capacity:
        size of the disk in sectors
    :type capacity: sector_t

    :param ip:
        return value: ip[0]=heads, ip[1]=sectors, ip[2]=cylinders
    :type ip: int \*

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

    :param buf:
        partition table, see \ :c:func:`scsi_bios_ptable`\ 
    :type buf: unsigned char \*

    :param capacity:
        size of the disk in sectors
    :type capacity: unsigned long

    :param cyls:
        put cylinders here
    :type cyls: unsigned int \*

    :param hds:
        put heads here
    :type hds: unsigned int \*

    :param secs:
        put sectors here
    :type secs: unsigned int \*

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

