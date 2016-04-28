.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-cable-ignore:

================
ata_cable_ignore
================

*man ata_cable_ignore(9)*

*4.6.0-rc5*

return ignored PATA cable.


Synopsis
========

.. c:function:: int ata_cable_ignore( struct ata_port * ap )

Arguments
=========

``ap``
    port


Description
===========

Helper method for drivers which don't use cable type to limit transfer
mode.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
