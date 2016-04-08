
.. _API-ata-scsi-offline-dev:

====================
ata_scsi_offline_dev
====================

*man ata_scsi_offline_dev(9)*

*4.6.0-rc1*

offline attached SCSI device


Synopsis
========

.. c:function:: int ata_scsi_offline_dev( struct ata_device * dev )

Arguments
=========

``dev``
    ATA device to offline attached SCSI device for


Description
===========

This function is called from ``ata_eh_hotplug`` and responsible for taking the SCSI device attached to ``dev`` offline. This function is called with host lock which protects
dev->sdev against clearing.


LOCKING
=======

spin_lock_irqsave(host lock)


RETURNS
=======

1 if attached SCSI device exists, 0 otherwise.
