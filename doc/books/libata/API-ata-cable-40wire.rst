
.. _API-ata-cable-40wire:

================
ata_cable_40wire
================

*man ata_cable_40wire(9)*

*4.6.0-rc1*

return 40 wire cable type


Synopsis
========

.. c:function:: int ata_cable_40wire( struct ata_port * ap )

Arguments
=========

``ap``
    port


Description
===========

Helper method for drivers which want to hardwire 40 wire cable detection.
