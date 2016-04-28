.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsi-hotplug:

================
ata_scsi_hotplug
================

*man ata_scsi_hotplug(9)*

*4.6.0-rc5*

SCSI part of hotplug


Synopsis
========

.. c:function:: void ata_scsi_hotplug( struct work_struct * work )

Arguments
=========

``work``
    Pointer to ATA port to perform SCSI hotplug on


Description
===========

Perform SCSI part of hotplug. It's executed from a separate workqueue
after EH completes. This is necessary because SCSI hot plugging requires
working EH and hot unplugging is synchronized with hot plugging with a
mutex.


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
