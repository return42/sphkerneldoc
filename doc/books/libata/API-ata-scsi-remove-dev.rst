
.. _API-ata-scsi-remove-dev:

===================
ata_scsi_remove_dev
===================

*man ata_scsi_remove_dev(9)*

*4.6.0-rc1*

remove attached SCSI device


Synopsis
========

.. c:function:: void ata_scsi_remove_dev( struct ata_device * dev )

Arguments
=========

``dev``
    ATA device to remove attached SCSI device for


Description
===========

This function is called from ``ata_eh_scsi_hotplug`` and responsible for removing the SCSI device attached to ``dev``.


LOCKING
=======

Kernel thread context (may sleep).
