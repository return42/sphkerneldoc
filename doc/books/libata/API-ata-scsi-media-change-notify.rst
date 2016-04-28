.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsi-media-change-notify:

============================
ata_scsi_media_change_notify
============================

*man ata_scsi_media_change_notify(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
