
.. _API-sata-scr-write:

==============
sata_scr_write
==============

*man sata_scr_write(9)*

*4.6.0-rc1*

write SCR register of the specified port


Synopsis
========

.. c:function:: int sata_scr_write( struct ata_link * link, int reg, u32 val )

Arguments
=========

``link``
    ATA link to write SCR for

``reg``
    SCR to write

``val``
    value to write


Description
===========

Write ``val`` to SCR register ``reg`` of ``link``. This function is guaranteed to succeed if ``link`` is ap->link, the cable type of the port is SATA and the port implements
->scr_read.


LOCKING
=======

None if ``link`` is ap->link. Kernel thread context otherwise.


RETURNS
=======

0 on success, negative errno on failure.
