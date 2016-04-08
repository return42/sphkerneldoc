
.. _API-ata-msense-caching:

==================
ata_msense_caching
==================

*man ata_msense_caching(9)*

*4.6.0-rc1*

Simulate MODE SENSE caching info page


Synopsis
========

.. c:function:: unsigned int ata_msense_caching( u16 * id, u8 * buf, bool changeable )

Arguments
=========

``id``
    device IDENTIFY data

``buf``
    output buffer

``changeable``
    whether changeable parameters are requested


Description
===========

Generate a caching info page, which conditionally indicates write caching to the SCSI layer, depending on device capabilities.


LOCKING
=======

None.
