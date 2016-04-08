
.. _API-ata-scsi-slave-config:

=====================
ata_scsi_slave_config
=====================

*man ata_scsi_slave_config(9)*

*4.6.0-rc1*

Set SCSI device attributes


Synopsis
========

.. c:function:: int ata_scsi_slave_config( struct scsi_device * sdev )

Arguments
=========

``sdev``
    SCSI device to examine


Description
===========

This is called before we actually start reading and writing to the device, to configure certain SCSI mid-layer behaviors.


LOCKING
=======

Defined by SCSI layer. We don't really care.
