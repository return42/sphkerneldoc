
.. _API-ata-cable-80wire:

================
ata_cable_80wire
================

*man ata_cable_80wire(9)*

*4.6.0-rc1*

return 80 wire cable type


Synopsis
========

.. c:function:: int ata_cable_80wire( struct ata_port * ap )

Arguments
=========

``ap``
    port


Description
===========

Helper method for drivers which want to hardwire 80 wire cable detection.
