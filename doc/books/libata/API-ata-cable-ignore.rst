
.. _API-ata-cable-ignore:

================
ata_cable_ignore
================

*man ata_cable_ignore(9)*

*4.6.0-rc1*

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

Helper method for drivers which don't use cable type to limit transfer mode.
