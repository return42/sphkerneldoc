.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-ioctl:

==========
scsi_ioctl
==========

*man scsi_ioctl(9)*

*4.6.0-rc5*

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

The ``scsi_ioctl`` function differs from most ioctls in that it does not
take a major/minor number as the dev field. Rather, it takes a pointer
to a ``struct scsi_device``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
