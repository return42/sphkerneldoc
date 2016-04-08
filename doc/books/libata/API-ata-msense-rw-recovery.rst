
.. _API-ata-msense-rw-recovery:

======================
ata_msense_rw_recovery
======================

*man ata_msense_rw_recovery(9)*

*4.6.0-rc1*

Simulate MODE SENSE r/w error recovery page


Synopsis
========

.. c:function:: unsigned int ata_msense_rw_recovery( u8 * buf, bool changeable )

Arguments
=========

``buf``
    output buffer

``changeable``
    whether changeable parameters are requested


Description
===========

Generate a generic MODE SENSE r/w error recovery page.


LOCKING
=======

None.
