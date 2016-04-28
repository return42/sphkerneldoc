.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-port-detach:

===============
ata_port_detach
===============

*man ata_port_detach(9)*

*4.6.0-rc5*

Detach ATA port in prepration of device removal


Synopsis
========

.. c:function:: void ata_port_detach( struct ata_port * ap )

Arguments
=========

``ap``
    ATA port to be detached


Description
===========

Detach all ATA devices and the associated SCSI devices of ``ap``; then,
remove the associated SCSI host. ``ap`` is guaranteed to be quiescent on
return from this function.


LOCKING
=======

Kernel thread context (may sleep).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
