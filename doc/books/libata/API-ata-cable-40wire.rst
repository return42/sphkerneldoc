.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-cable-40wire:

================
ata_cable_40wire
================

*man ata_cable_40wire(9)*

*4.6.0-rc5*

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

Helper method for drivers which want to hardwire 40 wire cable
detection.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
