
.. _API-ata-scsi-media-change-notify:

============================
ata_scsi_media_change_notify
============================

*man ata_scsi_media_change_notify(9)*

*4.6.0-rc1*

send media change event


Synopsis
========

.. c:function:: void ata_scsi_media_change_notify( struct ata_device * dev )

Arguments
=========

``dev``
    Pointer to the disk device with media change event


Description
===========

Tell the block layer to send a media change notification event.


LOCKING
=======

spin_lock_irqsave(host lock)
