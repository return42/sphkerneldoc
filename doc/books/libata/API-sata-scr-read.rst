.. -*- coding: utf-8; mode: rst -*-

.. _API-sata-scr-read:

=============
sata_scr_read
=============

*man sata_scr_read(9)*

*4.6.0-rc5*

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

Read SCR register ``reg`` of ``link`` into *\ ``val``. This function is
guaranteed to succeed if ``link`` is ap->link, the cable type of the
port is SATA and the port implements ->scr_read.


LOCKING
=======

None if ``link`` is ap->link. Kernel thread context otherwise.


RETURNS
=======

0 on success, negative errno on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
