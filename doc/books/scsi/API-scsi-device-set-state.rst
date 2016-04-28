.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-device-set-state:

=====================
scsi_device_set_state
=====================

*man scsi_device_set_state(9)*

*4.6.0-rc5*

Take the given device through the device state model.


Synopsis
========

.. c:function:: int scsi_device_set_state( struct scsi_device * sdev, enum scsi_device_state state )

Arguments
=========

``sdev``
    scsi device to change the state of.

``state``
    state to change to.


Description
===========

Returns zero if unsuccessful or an error if the requested transition is
illegal.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
