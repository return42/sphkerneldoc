
.. _API-ata-force-xfermask:

==================
ata_force_xfermask
==================

*man ata_force_xfermask(9)*

*4.6.0-rc1*

force xfermask according to libata.force


Synopsis
========

.. c:function:: void ata_force_xfermask( struct ata_device * dev )

Arguments
=========

``dev``
    ATA device of interest


Description
===========

Force xfer_mask according to libata.force and whine about it. For consistency with link selection, device number 15 selects the first device connected to the host link.


LOCKING
=======

EH context.
