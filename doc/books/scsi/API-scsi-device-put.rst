.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-device-put:

===============
scsi_device_put
===============

*man scsi_device_put(9)*

*4.6.0-rc5*

release a reference to a scsi_device


Synopsis
========

.. c:function:: void scsi_device_put( struct scsi_device * sdev )

Arguments
=========

``sdev``
    device to release a reference on.


Description
===========

Release a reference to the scsi_device and decrements the use count of
the underlying LLDD module. The device is freed once the last user
vanishes.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
