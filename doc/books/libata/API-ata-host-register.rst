
.. _API-ata-host-register:

=================
ata_host_register
=================

*man ata_host_register(9)*

*4.6.0-rc1*

register initialized ATA host


Synopsis
========

.. c:function:: int ata_host_register( struct ata_host * host, struct scsi_host_template * sht )

Arguments
=========

``host``
    ATA host to register

``sht``
    template for SCSI host


Description
===========

Register initialized ATA host. ``host`` is allocated using ``ata_host_alloc`` and fully initialized by LLD. This function starts ports, registers ``host`` with ATA and SCSI layers
and probe registered devices.


LOCKING
=======

Inherited from calling layer (may sleep).


RETURNS
=======

0 on success, -errno otherwise.
