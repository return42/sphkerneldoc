
.. _API-ata-cable-sata:

==============
ata_cable_sata
==============

*man ata_cable_sata(9)*

*4.6.0-rc1*

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
