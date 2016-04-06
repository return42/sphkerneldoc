
.. _API-scsi-change-queue-depth:

=======================
scsi_change_queue_depth
=======================

*man scsi_change_queue_depth(9)*

*4.6.0-rc1*

change a device's queue depth


Synopsis
========

.. c:function:: int scsi_change_queue_depth( struct scsi_device * sdev, int depth )

Arguments
=========

``sdev``
    SCSI Device in question

``depth``
    number of commands allowed to be queued to the driver


Description
===========

Sets the device queue depth and returns the new value.
