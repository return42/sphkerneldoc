.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-cable-unknown:

=================
ata_cable_unknown
=================

*man ata_cable_unknown(9)*

*4.6.0-rc5*

return unknown PATA cable.


Synopsis
========

.. c:function:: int ata_cable_unknown( struct ata_port * ap )

Arguments
=========

``ap``
    port


Description
===========

Helper method for drivers which have no PATA cable detection.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
