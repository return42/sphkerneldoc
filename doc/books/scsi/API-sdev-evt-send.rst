
.. _API-sdev-evt-send:

=============
sdev_evt_send
=============

*man sdev_evt_send(9)*

*4.6.0-rc1*

send asserted event to uevent thread


Synopsis
========

.. c:function:: void sdev_evt_send( struct scsi_device * sdev, struct scsi_event * evt )

Arguments
=========

``sdev``
    scsi_device event occurred on

``evt``
    event to send


Description
===========

Assert scsi device event asynchronously.
