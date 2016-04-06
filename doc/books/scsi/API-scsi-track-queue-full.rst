
.. _API-scsi-track-queue-full:

=====================
scsi_track_queue_full
=====================

*man scsi_track_queue_full(9)*

*4.6.0-rc1*

track QUEUE_FULL events to adjust queue depth


Synopsis
========

.. c:function:: int scsi_track_queue_full( struct scsi_device * sdev, int depth )

Arguments
=========

``sdev``
    SCSI Device in question

``depth``
    Current number of outstanding SCSI commands on this device, not counting the one returned as QUEUE_FULL.


Description
===========

This function will track successive QUEUE_FULL events on a specific SCSI device to determine if and when there is a need to adjust the queue depth on the device.


Returns
=======

0 - No change needed, >0 - Adjust queue depth to this new depth, -1 - Drop back to untagged operation using host->cmd_per_lun as the untagged command depth


Lock Status
===========

None held on entry


Notes
=====

Low level drivers may call this at any time and we will do “The Right Thing.” We are interrupt context safe.
