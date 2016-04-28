.. -*- coding: utf-8; mode: rst -*-

.. _API-sdev-evt-send:

=============
sdev_evt_send
=============

*man sdev_evt_send(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
