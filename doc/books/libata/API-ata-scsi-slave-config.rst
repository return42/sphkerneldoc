.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsi-slave-config:

=====================
ata_scsi_slave_config
=====================

*man ata_scsi_slave_config(9)*

*4.6.0-rc5*

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

This is called before we actually start reading and writing to the
device, to configure certain SCSI mid-layer behaviors.


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
