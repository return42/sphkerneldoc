.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-is-40wire:

=============
ata_is_40wire
=============

*man ata_is_40wire(9)*

*4.6.0-rc5*

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

Perform drive side detection decoding, allowing for device vendors who
can't follow the documentation.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
