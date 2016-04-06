
.. _API-scsi-ioctl-reset:

================
scsi_ioctl_reset
================

*man scsi_ioctl_reset(9)*

*4.6.0-rc1*


Synopsis
========

.. c:function:: int scsi_ioctl_reset( struct scsi_device * dev, int __user * arg )

Arguments
=========

``dev``
    scsi_device to operate on

``arg``
    reset type (see sg.h)
