.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-change-queue-depth:

=======================
scsi_change_queue_depth
=======================

*man scsi_change_queue_depth(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
