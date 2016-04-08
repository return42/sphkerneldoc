
.. _API-ata-sas-port-alloc:

==================
ata_sas_port_alloc
==================

*man ata_sas_port_alloc(9)*

*4.6.0-rc1*

Allocate port for a SAS attached SATA device


Synopsis
========

.. c:function:: struct ata_port ⋆ ata_sas_port_alloc( struct ata_host * host, struct ata_port_info * port_info, struct Scsi_Host * shost )

Arguments
=========

``host``
    ATA host container for all SAS ports

``port_info``
    Information from low-level host driver

``shost``
    SCSI host that the scsi device is attached to


LOCKING
=======

PCI/etc. bus probe sem.


RETURNS
=======

ata_port pointer on success / NULL on failure.
