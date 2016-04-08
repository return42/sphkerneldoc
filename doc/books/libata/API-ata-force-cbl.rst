
.. _API-ata-force-cbl:

=============
ata_force_cbl
=============

*man ata_force_cbl(9)*

*4.6.0-rc1*

force cable type according to libata.force


Synopsis
========

.. c:function:: void ata_force_cbl( struct ata_port * ap )

Arguments
=========

``ap``
    ATA port of interest


Description
===========

Force cable type according to libata.force and whine about it. The last entry which has matching port number is used, so it can be specified as part of device force parameters. For
example, both “a:40c,1.00:udma4” and “1.00:40c,udma4” have the same effect.


LOCKING
=======

EH context.
