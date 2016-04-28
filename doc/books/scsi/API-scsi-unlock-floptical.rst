.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-unlock-floptical:

=====================
scsi_unlock_floptical
=====================

*man scsi_unlock_floptical(9)*

*4.6.0-rc5*

unlock device via a special MODE SENSE command


Synopsis
========

.. c:function:: void scsi_unlock_floptical( struct scsi_device * sdev, unsigned char * result )

Arguments
=========

``sdev``
    scsi device to send command to

``result``
    area to store the result of the MODE SENSE


Description
===========

Send a vendor specific MODE SENSE (not a MODE SELECT) command. Called
for BLIST_KEY devices.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
