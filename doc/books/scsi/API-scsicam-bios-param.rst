
.. _API-scsicam-bios-param:

==================
scsicam_bios_param
==================

*man scsicam_bios_param(9)*

*4.6.0-rc1*

Determine geometry of a disk in cylinders/heads/sectors.


Synopsis
========

.. c:function:: int scsicam_bios_param( struct block_device * bdev, sector_t capacity, int * ip )

Arguments
=========

``bdev``
    which device

``capacity``
    size of the disk in sectors

``ip``
    return value: ip[0]=heads, ip[1]=sectors, ip[2]=cylinders


Description
===========

determine the BIOS mapping/geometry used for a drive in a SCSI-CAM system, storing the results in ip as required by the HDIO_GETGEO ``ioctl``.


Returns
=======

-1 on failure, 0 on success.
