
.. _API-sata-scr-write-flush:

====================
sata_scr_write_flush
====================

*man sata_scr_write_flush(9)*

*4.6.0-rc1*

write SCR register of the specified port and flush


Synopsis
========

.. c:function:: int sata_scr_write_flush( struct ata_link * link, int reg, u32 val )

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

This function is identical to ``sata_scr_write`` except that this function performs flush after writing to the register.


LOCKING
=======

None if ``link`` is ap->link. Kernel thread context otherwise.


RETURNS
=======

0 on success, negative errno on failure.
