.. -*- coding: utf-8; mode: rst -*-

.. _API-sdev-evt-alloc:

==============
sdev_evt_alloc
==============

*man sdev_evt_alloc(9)*

*4.6.0-rc5*

allocate a new scsi event


Synopsis
========

.. c:function:: struct scsi_event * sdev_evt_alloc( enum scsi_device_event evt_type, gfp_t gfpflags )

Arguments
=========

``evt_type``
    type of event to allocate

``gfpflags``
    GFP flags for allocation


Description
===========

Allocates and returns a new scsi_event.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
