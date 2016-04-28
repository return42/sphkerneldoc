.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-get-device-flags:

=====================
scsi_get_device_flags
=====================

*man scsi_get_device_flags(9)*

*4.6.0-rc5*

get device specific flags from the dynamic device list.


Synopsis
========

.. c:function:: int scsi_get_device_flags( struct scsi_device * sdev, const unsigned char * vendor, const unsigned char * model )

Arguments
=========

``sdev``
    ``scsi_device`` to get flags for

``vendor``
    vendor name

``model``
    model name


Description
===========

Search the global scsi_dev_info_list (specified by list zero) for an
entry matching ``vendor`` and ``model``, if found, return the matching
flags value, else return the host or global default settings. Called
during scan time.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
