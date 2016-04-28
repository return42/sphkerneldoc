.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-rwcmd-protocol:

==================
ata_rwcmd_protocol
==================

*man ata_rwcmd_protocol(9)*

*4.6.0-rc5*

set taskfile r/w commands and protocol


Synopsis
========

.. c:function:: int ata_rwcmd_protocol( struct ata_taskfile * tf, struct ata_device * dev )

Arguments
=========

``tf``
    command to examine and configure

``dev``
    device tf belongs to


Description
===========

Examine the device configuration and tf->flags to calculate the proper
read/write commands and protocol to use.


LOCKING
=======

caller.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
