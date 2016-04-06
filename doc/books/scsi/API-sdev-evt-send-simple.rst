
.. _API-sdev-evt-send-simple:

====================
sdev_evt_send_simple
====================

*man sdev_evt_send_simple(9)*

*4.6.0-rc1*

send asserted event to uevent thread


Synopsis
========

.. c:function:: void sdev_evt_send_simple( struct scsi_device * sdev, enum scsi_device_event evt_type, gfp_t gfpflags )

Arguments
=========

``sdev``
    scsi_device event occurred on

``evt_type``
    type of event to send

``gfpflags``
    GFP flags for allocation


Description
===========

Assert scsi device event asynchronously, given an event type.
