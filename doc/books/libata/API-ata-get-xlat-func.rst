
.. _API-ata-get-xlat-func:

=================
ata_get_xlat_func
=================

*man ata_get_xlat_func(9)*

*4.6.0-rc1*

check if SCSI to ATA translation is possible


Synopsis
========

.. c:function:: ata_xlat_func_t ata_get_xlat_func( struct ata_device * dev, u8 cmd )

Arguments
=========

``dev``
    ATA device

``cmd``
    SCSI command opcode to consider


Description
===========

Look up the SCSI command given, and determine whether the SCSI command is to be translated or simulated.


RETURNS
=======

Pointer to translation function if possible, ``NULL`` if not.
