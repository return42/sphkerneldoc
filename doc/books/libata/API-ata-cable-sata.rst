.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-cable-sata:

==============
ata_cable_sata
==============

*man ata_cable_sata(9)*

*4.6.0-rc5*

return SATA cable type


Synopsis
========

.. c:function:: int ata_cable_sata( struct ata_port * ap )

Arguments
=========

``ap``
    port


Description
===========

Helper method for drivers which have SATA cables


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
