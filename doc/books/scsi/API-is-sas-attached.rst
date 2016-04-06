
.. _API-is-sas-attached:

===============
is_sas_attached
===============

*man is_sas_attached(9)*

*4.6.0-rc1*

check if device is SAS attached


Synopsis
========

.. c:function:: int is_sas_attached( struct scsi_device * sdev )

Arguments
=========

``sdev``
    scsi device to check


Description
===========

returns true if the device is SAS attached
