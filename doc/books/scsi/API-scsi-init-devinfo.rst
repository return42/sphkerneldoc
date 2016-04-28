.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-init-devinfo:

=================
scsi_init_devinfo
=================

*man scsi_init_devinfo(9)*

*4.6.0-rc5*

set up the dynamic device list.


Synopsis
========

.. c:function:: int scsi_init_devinfo( void )

Arguments
=========

``void``
    no arguments


Description
===========

Add command line entries from scsi_dev_flags, then add
scsi_static_device_list entries to the scsi device info list.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
