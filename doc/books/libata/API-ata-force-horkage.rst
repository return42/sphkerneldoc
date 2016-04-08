
.. _API-ata-force-horkage:

=================
ata_force_horkage
=================

*man ata_force_horkage(9)*

*4.6.0-rc1*

force horkage according to libata.force


Synopsis
========

.. c:function:: void ata_force_horkage( struct ata_device * dev )

Arguments
=========

``dev``
    ATA device of interest


Description
===========

Force horkage according to libata.force and whine about it. For consistency with link selection, device number 15 selects the first device connected to the host link.


LOCKING
=======

EH context.
