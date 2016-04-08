
.. _API-sata-scr-read:

=============
sata_scr_read
=============

*man sata_scr_read(9)*

*4.6.0-rc1*

read SCR register of the specified port


Synopsis
========

.. c:function:: int sata_scr_read( struct ata_link * link, int reg, u32 * val )

Arguments
=========

``link``
    ATA link to read SCR for

``reg``
    SCR to read

``val``
    Place to store read value


Description
===========

Read SCR register ``reg`` of ``link`` into ⋆\ ``val``. This function is guaranteed to succeed if ``link`` is ap->link, the cable type of the port is SATA and the port implements
->scr_read.


LOCKING
=======

None if ``link`` is ap->link. Kernel thread context otherwise.


RETURNS
=======

0 on success, negative errno on failure.
