
.. _API-ata-dev-read-id:

===============
ata_dev_read_id
===============

*man ata_dev_read_id(9)*

*4.6.0-rc1*

Read ID data from the specified device


Synopsis
========

.. c:function:: int ata_dev_read_id( struct ata_device * dev, unsigned int * p_class, unsigned int flags, u16 * id )

Arguments
=========

``dev``
    target device

``p_class``
    pointer to class of the target device (may be changed)

``flags``
    ATA_READID_⋆ flags

``id``
    buffer to read IDENTIFY data into


Description
===========

Read ID data from the specified device. ATA_CMD_ID_ATA is performed on ATA devices and ATA_CMD_ID_ATAPI on ATAPI devices. This function also issues
ATA_CMD_INIT_DEV_PARAMS for pre-ATA4 drives.


FIXME
=====

ATA_CMD_ID_ATA is optional for early drives and right now we abort if we hit that case.


LOCKING
=======

Kernel thread context (may sleep)


RETURNS
=======

0 on success, -errno otherwise.
