.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-sas-slave-configure:

=======================
ata_sas_slave_configure
=======================

*man ata_sas_slave_configure(9)*

*4.6.0-rc5*

Default slave_config routine for libata devices


Synopsis
========

.. c:function:: int ata_sas_slave_configure( struct scsi_device * sdev, struct ata_port * ap )

Arguments
=========

``sdev``
    SCSI device to configure

``ap``
    ATA port to which SCSI device is attached


RETURNS
=======

Zero.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
