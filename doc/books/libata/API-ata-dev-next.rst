
.. _API-ata-dev-next:

============
ata_dev_next
============

*man ata_dev_next(9)*

*4.6.0-rc1*

device iteration helper


Synopsis
========

.. c:function:: struct ata_device ⋆ ata_dev_next( struct ata_device * dev, struct ata_link * link, enum ata_dev_iter_mode mode )

Arguments
=========

``dev``
    the previous device, NULL to start

``link``
    ATA link containing devices to iterate

``mode``
    iteration mode, one of ATA_DITER_⋆


LOCKING
=======

Host lock or EH context.


RETURNS
=======

Pointer to the next device.
