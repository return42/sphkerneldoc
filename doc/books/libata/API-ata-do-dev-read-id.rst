
.. _API-ata-do-dev-read-id:

==================
ata_do_dev_read_id
==================

*man ata_do_dev_read_id(9)*

*4.6.0-rc1*

default ID read method


Synopsis
========

.. c:function:: unsigned int ata_do_dev_read_id( struct ata_device * dev, struct ata_taskfile * tf, u16 * id )

Arguments
=========

``dev``
    device

``tf``
    proposed taskfile

``id``
    data buffer


Description
===========

Issue the identify taskfile and hand back the buffer containing identify data. For some RAID controllers and for pre ATA devices this function is wrapped or replaced by the driver
