
.. _API-ata-cable-unknown:

=================
ata_cable_unknown
=================

*man ata_cable_unknown(9)*

*4.6.0-rc1*

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
