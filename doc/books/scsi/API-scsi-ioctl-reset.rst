.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-ioctl-reset:

================
scsi_ioctl_reset
================

*man scsi_ioctl_reset(9)*

*4.6.0-rc5*


Synopsis
========

.. c:function:: int scsi_ioctl_reset( struct scsi_device * dev, int __user * arg )

Arguments
=========

``dev``
    scsi_device to operate on

``arg``
    reset type (see sg.h)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
