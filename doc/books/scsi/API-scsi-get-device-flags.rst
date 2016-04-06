
.. _API-scsi-get-device-flags:

=====================
scsi_get_device_flags
=====================

*man scsi_get_device_flags(9)*

*4.6.0-rc1*

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

Search the global scsi_dev_info_list (specified by list zero) for an entry matching ``vendor`` and ``model``, if found, return the matching flags value, else return the host or
global default settings. Called during scan time.
