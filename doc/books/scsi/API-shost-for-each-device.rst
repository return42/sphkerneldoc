
.. _API-shost-for-each-device:

=====================
shost_for_each_device
=====================

*man shost_for_each_device(9)*

*4.6.0-rc1*

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

Iterator that returns each device attached to ``shost``. This loop takes a reference on each device and releases it at the end. If you break out of the loop, you must call
scsi_device_put(sdev).
