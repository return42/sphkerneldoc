.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-force-link-limits:

=====================
ata_force_link_limits
=====================

*man ata_force_link_limits(9)*

*4.6.0-rc5*

force link limits according to libata.force


Synopsis
========

.. c:function:: void ata_force_link_limits( struct ata_link * link )

Arguments
=========

``link``
    ATA link of interest


Description
===========

Force link flags and SATA spd limit according to libata.force and whine
about it. When only the port part is specified (e.g. 1:), the limit
applies to all links connected to both the host link and all fan-out
ports connected via PMP. If the device part is specified as 0 (e.g.
1.00:), it specifies the first fan-out link not the host link. Device
number 15 always points to the host link whether PMP is attached or not.
If the controller has slave link, device number 16 points to it.


LOCKING
=======

EH context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
