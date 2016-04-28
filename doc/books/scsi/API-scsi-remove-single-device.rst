.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-remove-single-device:

=========================
scsi_remove_single_device
=========================

*man scsi_remove_single_device(9)*

*4.6.0-rc5*

Respond to user request to remove a device


Synopsis
========

.. c:function:: int scsi_remove_single_device( uint host, uint channel, uint id, uint lun )

Arguments
=========

``host``
    user-supplied decimal integer

``channel``
    user-supplied decimal integer

``id``
    user-supplied decimal integer

``lun``
    user-supplied decimal integer


Description
===========

called by writing “scsi remove-single-device” to /proc/scsi/scsi. Does a
``scsi_device_lookup`` and ``scsi_remove_device``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
