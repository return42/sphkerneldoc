
.. _API-ata-is-40wire:

=============
ata_is_40wire
=============

*man ata_is_40wire(9)*

*4.6.0-rc1*

check drive side detection


Synopsis
========

.. c:function:: int ata_is_40wire( struct ata_device * dev )

Arguments
=========

``dev``
    device


Description
===========

Perform drive side detection decoding, allowing for device vendors who can't follow the documentation.
