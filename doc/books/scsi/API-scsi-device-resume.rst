.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-device-resume:

==================
scsi_device_resume
==================

*man scsi_device_resume(9)*

*4.6.0-rc5*

Restart user issued commands to a quiesced device.


Synopsis
========

.. c:function:: void scsi_device_resume( struct scsi_device * sdev )

Arguments
=========

``sdev``
    scsi device to resume.


Description
===========

Moves the device from quiesced back to running and restarts the queues.

Must be called with user context, may sleep.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
