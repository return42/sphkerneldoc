
.. _API-scsi-ioctl:

==========
scsi_ioctl
==========

*man scsi_ioctl(9)*

*4.6.0-rc1*

Dispatch ioctl to scsi device


Synopsis
========

.. c:function:: int scsi_ioctl( struct scsi_device * sdev, int cmd, void __user * arg )

Arguments
=========

``sdev``
    scsi device receiving ioctl

``cmd``
    which ioctl is it

``arg``
    data associated with ioctl


Description
===========

The ``scsi_ioctl`` function differs from most ioctls in that it does not take a major/minor number as the dev field. Rather, it takes a pointer to a ``struct scsi_device``.
