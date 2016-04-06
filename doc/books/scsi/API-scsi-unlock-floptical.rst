
.. _API-scsi-unlock-floptical:

=====================
scsi_unlock_floptical
=====================

*man scsi_unlock_floptical(9)*

*4.6.0-rc1*

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

Send a vendor specific MODE SENSE (not a MODE SELECT) command. Called for BLIST_KEY devices.
