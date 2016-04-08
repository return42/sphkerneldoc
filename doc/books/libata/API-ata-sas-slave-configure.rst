
.. _API-ata-sas-slave-configure:

=======================
ata_sas_slave_configure
=======================

*man ata_sas_slave_configure(9)*

*4.6.0-rc1*

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
