
.. _API-sdev-evt-alloc:

==============
sdev_evt_alloc
==============

*man sdev_evt_alloc(9)*

*4.6.0-rc1*

allocate a new scsi event


Synopsis
========

.. c:function:: struct scsi_event ⋆ sdev_evt_alloc( enum scsi_device_event evt_type, gfp_t gfpflags )

Arguments
=========

``evt_type``
    type of event to allocate

``gfpflags``
    GFP flags for allocation


Description
===========

Allocates and returns a new scsi_event.
