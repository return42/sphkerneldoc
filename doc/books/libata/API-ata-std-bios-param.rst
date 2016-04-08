
.. _API-ata-std-bios-param:

==================
ata_std_bios_param
==================

*man ata_std_bios_param(9)*

*4.6.0-rc1*

generic bios head/sector/cylinder calculator used by sd.


Synopsis
========

.. c:function:: int ata_std_bios_param( struct scsi_device * sdev, struct block_device * bdev, sector_t capacity, int geom[] )

Arguments
=========

``sdev``
    SCSI device for which BIOS geometry is to be determined

``bdev``
    block device associated with ``sdev``

``capacity``
    capacity of SCSI device

``geom[]``
    location to which geometry will be output


Description
===========

Generic bios head/sector/cylinder calculator used by sd. Most BIOSes nowadays expect a XXX/255/16 (CHS) mapping. Some situations may arise where the disk is not bootable if this is
not used.


LOCKING
=======

Defined by the SCSI layer. We don't really care.


RETURNS
=======

Zero.
