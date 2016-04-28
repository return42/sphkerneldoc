.. -*- coding: utf-8; mode: rst -*-

.. _API-shost-for-each-device:

=====================
shost_for_each_device
=====================

*man shost_for_each_device(9)*

*4.6.0-rc5*

iterate over all devices of a host


Synopsis
========

.. c:function:: shost_for_each_device( sdev, shost )

Arguments
=========

``sdev``
    the ``struct scsi_device`` to use as a cursor

``shost``
    the ``struct scsi_host`` to iterate over


Description
===========

Iterator that returns each device attached to ``shost``. This loop takes
a reference on each device and releases it at the end. If you break out
of the loop, you must call scsi_device_put(sdev).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
