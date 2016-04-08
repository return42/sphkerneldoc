
.. _API-ata-mselect-caching:

===================
ata_mselect_caching
===================

*man ata_mselect_caching(9)*

*4.6.0-rc1*

Simulate MODE SELECT for caching info page


Synopsis
========

.. c:function:: int ata_mselect_caching( struct ata_queued_cmd * qc, const u8 * buf, int len )

Arguments
=========

``qc``
    Storage for translated ATA taskfile

``buf``
    input buffer

``len``
    number of valid bytes in the input buffer


Description
===========

Prepare a taskfile to modify caching information for the device.


LOCKING
=======

None.
