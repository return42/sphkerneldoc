.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsi-slave-destroy:

======================
ata_scsi_slave_destroy
======================

*man ata_scsi_slave_destroy(9)*

*4.6.0-rc5*

SCSI device is about to be destroyed


Synopsis
========

.. c:function:: void ata_scsi_slave_destroy( struct scsi_device * sdev )

Arguments
=========

``sdev``
    SCSI device to be destroyed


Description
===========

``sdev`` is about to be destroyed for hot/warm unplugging. If this
unplugging was initiated by libata as indicated by NULL dev->sdev, this
function doesn't have to do anything. Otherwise, SCSI layer initiated
warm-unplug is in progress. Clear dev->sdev, schedule the device for ATA
detach and invoke EH.


LOCKING
=======

Defined by SCSI layer. We don't really care.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
